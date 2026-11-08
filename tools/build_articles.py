#!/usr/bin/env python3
"""Build the article pages of hamou.de.

There is no server, database or dashboard: every article is a plain HTML file
in the repository, and GitHub Pages serves it as it is. This script only
writes those files, so that every article gets the same layout, metadata and
links without anyone copying HTML by hand.

Source: content/articles/<slug>/
  meta.json   shared facts (dates, colors, icon, product, video)
  en.md       English text (required), de.md German, ar.md Arabic

Output, for every language (English has no prefix, German /de, Arabic /ar):
  <prefix>/articles/<slug>/index.html   the article page
  <prefix>/articles/<slug>/index.md     a clean Markdown copy for AI assistants
  <prefix>/articles/index.html          the list of all articles
  <prefix>/articles/feed.xml            an Atom feed
and also: the article cards on the home page (index.html, between the
"articles:start/end" markers), sitemap.xml, the article block of llms.txt,
and llms-full.txt.

Usage:
  python3 tools/build_articles.py            write the pages
  python3 tools/build_articles.py --images   also render the share images
                                             (og.jpg) and video posters
                                             (poster.jpg); needs Node and
                                             Playwright

Only the Python standard library is used. See content/articles/README.md.
"""

import datetime as dt
import hashlib
import html
import json
import math
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content', 'articles')
SITE = 'https://hamou.de'
WEBSITE_ID = SITE + '/#website'
PERSON_ID = SITE + '/#person'
ORG_ID = SITE + '/#alhamou'
ORG_NAME = {'en': 'Alhamou', 'de': 'Alhamou', 'ar': 'شركة الحمو'}
SAME_AS = ['https://github.com/Alhamou', 'https://www.youtube.com/@emadalhamo']

OG_W, OG_H = 1200, 630
POSTER_W, POSTER_H = 1280, 720
FALLBACK_OG = ('/og.png', 1731, 909)

CSP = ("default-src 'self'; script-src 'self' https://www.youtube.com https://s.ytimg.com; "
       "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; "
       "frame-src https://www.youtube-nocookie.com; connect-src 'self'; "
       "manifest-src 'self'; object-src 'none'; base-uri 'self'; "
       "form-action 'self'; upgrade-insecure-requests")
FONTS = ('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700'
         '&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700'
         '&family=Manrope:wght@400;500;600;700&display=swap')

LANGS = ['en', 'de', 'ar']   # the first one is the x-default
DEFAULT = 'en'
HOME_ORDER = ['ar', 'en', 'de']   # the home page's source language comes first

LANG = {
    'en': {'prefix': '', 'dir': 'ltr', 'locale': 'en_US', 'name': 'English', 'wpm': 220},
    'de': {'prefix': '/de', 'dir': 'ltr', 'locale': 'de_DE', 'name': 'Deutsch', 'wpm': 200},
    'ar': {'prefix': '/ar', 'dir': 'rtl', 'locale': 'ar_AR', 'name': 'العربية', 'wpm': 180},
}

MONTHS = {
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December'],
    'de': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli',
           'August', 'September', 'Oktober', 'November', 'Dezember'],
    'ar': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو',
           'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
}

UI = {
    'en': {
        'home': 'Home', 'articles': 'Articles', 'nav': 'Main navigation',
        'crumbs': 'Breadcrumb', 'skip': 'Skip to content', 'lets_talk': "Let's talk",
        'author': 'Emad Alhamou', 'role': 'Founder & Product Builder',
        'published': 'Published', 'updated': 'Updated', 'toc': 'On this page',
        'also_in': 'Also in', 'play': 'Play video', 'watch_yt': 'Watch on YouTube',
        'yt_notice': 'The video loads from YouTube (Google) only when you press play.',
        'visit': 'Visit {}', 'since': 'since', 'more': 'More articles', 'lang': 'Language',
        'product': 'About the product', 'feed': 'Atom feed',
        'articles_title': 'Articles by Emad Alhamou: products, tools and how they are built',
        'articles_h1': 'Articles',
        'articles_intro': 'Stories behind the products and tools I build: what they do, '
                          'why they exist, and how they work.',
        'articles_desc': 'Articles by Emad Alhamou about the products and tools he builds: '
                         'what they do, why they exist, and how they work.',
        'empty': 'No articles in this language yet.',
    },
    'de': {
        'home': 'Startseite', 'articles': 'Artikel', 'nav': 'Hauptnavigation',
        'crumbs': 'Brotkrümelnavigation', 'skip': 'Zum Inhalt springen', 'lets_talk': 'Kontakt',
        'author': 'Emad Alhamou', 'role': 'Gründer & Produktentwickler',
        'published': 'Veröffentlicht am', 'updated': 'Aktualisiert am', 'toc': 'Auf dieser Seite',
        'also_in': 'Auch auf', 'play': 'Video abspielen', 'watch_yt': 'Auf YouTube ansehen',
        'yt_notice': 'Das Video wird erst beim Abspielen von YouTube (Google) geladen.',
        'visit': '{} besuchen', 'since': 'seit', 'more': 'Weitere Artikel', 'lang': 'Sprache',
        'product': 'Zum Produkt', 'feed': 'Atom-Feed',
        'articles_title': 'Artikel von Emad Alhamou: Produkte, Tools und wie sie entstehen',
        'articles_h1': 'Artikel',
        'articles_intro': 'Geschichten hinter den Produkten und Tools, die ich baue: was sie können, '
                          'warum es sie gibt und wie sie funktionieren.',
        'articles_desc': 'Artikel von Emad Alhamou über die Produkte und Tools, die er baut: '
                         'was sie können, warum es sie gibt und wie sie funktionieren.',
        'empty': 'In dieser Sprache gibt es noch keine Artikel.',
    },
    'ar': {
        'home': 'الرئيسية', 'articles': 'مقالات', 'nav': 'التنقل الرئيسي',
        'crumbs': 'مسار التنقل', 'skip': 'تخطَّ إلى المحتوى', 'lets_talk': 'لنتواصل',
        'author': 'عماد الحمو', 'role': 'مؤسس وصانع منتجات',
        'published': 'نُشر في', 'updated': 'حُدّث في', 'toc': 'في هذه الصفحة',
        'also_in': 'بلغات أخرى', 'play': 'تشغيل الفيديو', 'watch_yt': 'شاهد على يوتيوب',
        'yt_notice': 'لا يُحمَّل الفيديو من يوتيوب (Google) إلا عند الضغط على تشغيل.',
        'visit': 'زيارة {}', 'since': 'منذ', 'more': 'مقالات أخرى', 'lang': 'اللغة',
        'product': 'عن المنتج', 'feed': 'خلاصة Atom',
        'articles_title': 'مقالات عماد الحمو: المنتجات والأدوات وكيف تُبنى',
        'articles_h1': 'مقالات',
        'articles_intro': 'قصص المنتجات والأدوات التي أبنيها: ماذا تفعل، ولماذا وُجدت، وكيف تعمل.',
        'articles_desc': 'مقالات عماد الحمو عن المنتجات والأدوات التي يبنيها: ماذا تفعل، '
                         'ولماذا وُجدت، وكيف تعمل.',
        'empty': 'لا توجد مقالات بهذه اللغة بعد.',
    },
}

ARR_EXT = ('<svg class="icon-arr" viewBox="0 0 12 12" width="11" height="11" aria-hidden="true">'
           '<path d="M3.5 8.5L8.5 3.5M8.5 3.5H4.5M8.5 3.5V7.5" fill="none" stroke="currentColor" '
           'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARR_FWD = ('<svg class="icon-arr fwd" viewBox="0 0 12 12" width="11" height="11" aria-hidden="true">'
           '<path d="M8.5 6H3.5M3.5 6L6 3.5M3.5 6L6 8.5" fill="none" stroke="currentColor" '
           'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
PLAY = ('<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true">'
        '<path d="M8 5.5v13a1 1 0 0 0 1.52.85l10.4-6.5a1 1 0 0 0 0-1.7L9.52 4.65A1 1 0 0 0 8 5.5z" '
        'fill="currentColor"/></svg>')
GLOBE = ('<svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><g fill="none" '
         'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
         '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 3.8 5.6 3.8 9s'
         '-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></g></svg>')
CHEV = ('<svg class="chev" viewBox="0 0 10 10" width="10" height="10" aria-hidden="true">'
        '<path d="M2.5 4l2.5 2.5L7.5 4" fill="none" stroke="currentColor" stroke-width="1.5" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')


# ---------------------------------------------------------------- helpers

def esc(s):
    return html.escape(str(s), quote=True)


def path_for(lang, rest):
    return LANG[lang]['prefix'] + rest


def abs_url(path):
    return SITE + path


def art_path(a, lang):
    return path_for(lang, '/articles/%s/' % a['slug'])


def index_path(lang):
    return path_for(lang, '/articles/')


def feed_path(lang):
    return path_for(lang, '/articles/feed.xml')


def og_rel(a, lang):
    return art_path(a, lang) + 'og.jpg'


def video_for(a, lang):
    """The video shown in one language: the article's video, with the fields
    of video.by_lang[lang] on top (usually a video recorded in that language).
    'owner' is the language the video belongs to: it names the video in the
    structured data and decides where its poster lives."""
    v = a.get('video')
    if not v:
        return None
    out = {k: x for k, x in v.items() if k != 'by_lang'}
    own = (v.get('by_lang') or {}).get(lang) if lang != DEFAULT else None
    out.update(own or {})
    out['owner'] = lang if own else DEFAULT
    return out


def video_ld_id(a, v):
    return abs_url(art_path(a, v['owner'])) + '#video'


def poster_rel(a, owner=DEFAULT):
    # /articles/<slug>/poster.jpg for the main video, /ar/articles/<slug>/...
    # for a language with its own video.
    return art_path(a, owner) + 'poster.jpg'


def exists(rel):
    return os.path.isfile(os.path.join(ROOT, rel.lstrip('/')))


def og_for(a, lang):
    rel = og_rel(a, lang)
    return (rel, OG_W, OG_H) if exists(rel) else FALLBACK_OG


def poster_for(a, lang):
    v = video_for(a, lang)
    if not v:
        return None
    rel = poster_rel(a, v['owner'])
    return rel if exists(rel) else None


def ver(rel):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def fmt_date(iso, lang):
    y, m, d = (int(x) for x in iso.split('-'))
    month = MONTHS[lang][m - 1]
    return ('%d. %s %d' if lang == 'de' else '%d %s %d') % (d, month, y)


def fmt_month(ym, lang):
    y, m = (int(x) for x in ym.split('-')[:2])
    return '%s %d' % (MONTHS[lang][m - 1], y)


def minutes_label(n, lang):
    if lang == 'en':
        return '%d min read' % n
    if lang == 'de':
        return '%d Min. Lesezeit' % n
    if n == 1:
        return 'قراءة دقيقة واحدة'
    if n == 2:
        return 'قراءة دقيقتين'
    if n <= 10:
        return 'قراءة %d دقائق' % n
    return 'قراءة %d دقيقة' % n


def ld_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2).replace('</', '<\\/')


def theme_style(a):
    t = a.get('theme') or {}
    return '--art-bg:%s;--art-accent:%s;--art-fg:%s' % (
        t.get('bg', '#191a16'), t.get('accent', '#c7ff34'), t.get('fg', '#f4f2ea'))


def write(rel, content):
    path = os.path.join(ROOT, rel.lstrip('/'))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            if f.read() == content:
                return
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print('wrote', rel.lstrip('/'))


def git_date(rel):
    try:
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', rel], cwd=ROOT,
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


# ---------------------------------------------------------------- markdown

BOLD = re.compile(r'\*\*(.+?)\*\*')
LINK = re.compile(r'\[([^\]]+)\]\(([^)\s]+)\)')


def inline_html(text):
    out = []
    for part in re.split(r'(`[^`]+`)', text):
        if len(part) > 1 and part.startswith('`') and part.endswith('`'):
            out.append('<code>%s</code>' % esc(part[1:-1]))
            continue
        s = html.escape(part, quote=False)
        s = BOLD.sub(r'<strong>\1</strong>', s)
        s = LINK.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2).replace('"', '%22'), m.group(1)), s)
        out.append(s)
    return ''.join(out)


def plain(text):
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = BOLD.sub(r'\1', text)
    return LINK.sub(lambda m: m.group(1) if m.group(1) in m.group(2) else
                    '%s (%s)' % (m.group(1), m.group(2)), text)


def slugify(text, used):
    s = text.lower()
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        s = s.replace(a, b)
    s = re.sub(r'[^\w]+', '-', s).strip('-_') or 'section'
    base, n = s, 2
    while s in used:
        s = '%s-%d' % (base, n)
        n += 1
    used.add(s)
    return s


def parse_front_matter(text, where):
    if not text.startswith('---\n') or '\n---\n' not in text[3:]:
        raise SystemExit('%s: the file must start with a --- front matter block' % where)
    end = text.index('\n---\n', 3)
    fm = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, sep, value = line.partition(':')
        if not sep:
            raise SystemExit('%s: front matter line without "key: value": %s' % (where, line))
        fm[key.strip()] = value.strip()
    return fm, text[end + 5:]


def parse_body(md, where):
    blocks, para, items = [], [], []

    def flush():
        if para:
            blocks.append(('p', ' '.join(para)))
            para.clear()
        if items:
            blocks.append(('ul', list(items)))
            items.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.strip() == '<!-- faq -->':
            flush()
            blocks.append(('faq', None))
            continue
        m = re.match(r'^(#{2,3})\s+(.+)$', line)
        if m:
            flush()
            blocks.append(('h%d' % len(m.group(1)), m.group(2).strip()))
            continue
        if re.match(r'^[-*]\s+', line):
            if para:
                flush()
            items.append(re.sub(r'^[-*]\s+', '', line))
            continue
        if not line.strip():
            flush()
            continue
        if items and raw.startswith('  '):
            items[-1] += ' ' + line.strip()
            continue
        if items:
            flush()
        para.append(line.strip())
    flush()

    if ('faq', None) in blocks:
        i = blocks.index(('faq', None))
        main, rest = blocks[:i], blocks[i + 1:]
    else:
        main, rest = blocks, []
    faq = None
    if rest:
        if rest[0][0] != 'h2':
            raise SystemExit('%s: the FAQ must start with a ## heading' % where)
        faq = {'heading': rest[0][1], 'items': []}
        for kind, payload in rest[1:]:
            if kind == 'h3':
                faq['items'].append({'q': payload, 'a': []})
            elif kind in ('p', 'ul') and faq['items']:
                faq['items'][-1]['a'].append((kind, payload))
            else:
                raise SystemExit('%s: the FAQ takes ### questions, each followed by its answer' % where)
    return main, faq


def render_blocks(blocks, used, toc):
    out = []
    for kind, payload in blocks:
        if kind == 'h2':
            sid = slugify(plain(payload), used)
            toc.append((sid, plain(payload)))
            out.append('<h2 id="%s">%s</h2>' % (sid, inline_html(payload)))
        elif kind == 'h3':
            out.append('<h3>%s</h3>' % inline_html(payload))
        elif kind == 'p':
            out.append('<p>%s</p>' % inline_html(payload))
        elif kind == 'ul':
            out.append('<ul>\n%s\n</ul>' % '\n'.join('<li>%s</li>' % inline_html(i) for i in payload))
    return '\n'.join(out)


def render_faq(faq, used, toc):
    sid = slugify(plain(faq['heading']), used)
    toc.append((sid, plain(faq['heading'])))
    out = ['<section class="artFaq" aria-labelledby="%s">' % sid,
           '<h2 id="%s">%s</h2>' % (sid, inline_html(faq['heading']))]
    for item in faq['items']:
        out.append('<div class="artQ">\n<h3>%s</h3>\n%s\n</div>'
                   % (inline_html(item['q']), render_blocks(item['a'], used, [])))
    out.append('</section>')
    return '\n'.join(out)


def answer_text(answer):
    parts = []
    for kind, payload in answer:
        parts.append(plain(payload) if kind == 'p' else '; '.join(plain(i) for i in payload))
    return ' '.join(parts)


# ---------------------------------------------------------------- content

REQUIRED = ('title', 'description', 'dek', 'kicker')


def load_articles():
    articles = []
    if not os.path.isdir(CONTENT):
        return articles
    for slug in sorted(os.listdir(CONTENT)):
        folder = os.path.join(CONTENT, slug)
        meta_path = os.path.join(folder, 'meta.json')
        if not os.path.isfile(meta_path):
            continue
        with open(meta_path, encoding='utf-8') as f:
            meta = json.load(f)
        if meta.get('draft'):
            continue
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug):
            raise SystemExit('%s: the folder name is the URL, use lowercase letters, digits and -' % folder)
        meta['slug'] = slug
        for key in ('date_published', 'date_modified'):
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', meta.get(key, '')):
                raise SystemExit('%s: "%s" must look like 2026-11-07' % (meta_path, key))
        langs = {}
        for lang in LANGS:
            p = os.path.join(folder, lang + '.md')
            if not os.path.isfile(p):
                continue
            with open(p, encoding='utf-8') as f:
                fm, body = parse_front_matter(f.read(), p)
            for key in REQUIRED:
                if not fm.get(key):
                    raise SystemExit('%s: front matter needs "%s"' % (p, key))
            fm.setdefault('short_title', fm['title'])
            fm.setdefault('seo_title', '%s | %s' % (fm['title'], UI[lang]['author']))
            main, faq = parse_body(body, p)
            used, toc = set(), []
            body_html = render_blocks(main, used, toc)
            faq_html = render_faq(faq, used, toc) if faq else ''
            text = '\n'.join(l for l in body.splitlines() if l.strip() != '<!-- faq -->')
            words = len(re.findall(r'\S+', plain(text)))
            langs[lang] = {
                'fm': fm, 'md': text.strip() + '\n', 'body_html': body_html, 'faq': faq,
                'faq_html': faq_html, 'toc': toc, 'words': words,
                'minutes': max(1, math.ceil(words / LANG[lang]['wpm'])),
            }
        if DEFAULT not in langs:
            raise SystemExit('%s: %s.md is required' % (folder, DEFAULT))
        meta['langs'] = langs
        articles.append(meta)
    articles.sort(key=lambda a: (a['date_published'], a['slug']), reverse=True)
    return articles


# ---------------------------------------------------------------- page parts

def page_head(lang, *, title, og_title, description, canonical, alternates, og_image,
              og_type, extra='', jsonld=None, keywords='', md_alt=None):
    canonical_url = abs_url(canonical)
    alt = ''
    if len(alternates) > 1:
        alt = ''.join('\n  <link rel="alternate" hreflang="%s" href="%s">' % (l, esc(abs_url(p)))
                      for l, p in alternates)
        default = dict(alternates).get(DEFAULT, alternates[0][1])
        alt += '\n  <link rel="alternate" hreflang="x-default" href="%s">' % esc(abs_url(default))
    locales = ''.join('\n  <meta property="og:locale:alternate" content="%s">' % LANG[l]['locale']
                      for l, _ in alternates if l != lang)
    img, w, h = og_image
    lines = [
        '<!DOCTYPE html>',
        '<html lang="%s" dir="%s">' % (lang, LANG[lang]['dir']),
        '<head>',
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        '  <meta http-equiv="Content-Security-Policy" content="%s">' % CSP,
        '  <meta name="referrer" content="strict-origin-when-cross-origin">',
        '  <title>%s</title>' % esc(title),
        '  <meta name="description" content="%s">' % esc(description),
        '  <meta name="author" content="%s">' % esc(UI[lang]['author']),
    ]
    if keywords:
        lines.append('  <meta name="keywords" content="%s">' % esc(keywords))
    lines += [
        '  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
        '  <meta name="theme-color" content="#12130f">',
        '  <link rel="canonical" href="%s">%s' % (esc(canonical_url), alt),
    ]
    if md_alt:
        lines.append('  <link rel="alternate" type="text/markdown" href="%s" title="Markdown">' % esc(md_alt))
    lines += [
        '  <link rel="alternate" type="application/atom+xml" href="%s" title="%s">'
        % (esc(feed_path(lang)), esc(UI[lang]['feed'])),
        '  <meta property="og:site_name" content="Emad Alhamou">',
        '  <meta property="og:type" content="%s">' % og_type,
        '  <meta property="og:locale" content="%s">%s' % (LANG[lang]['locale'], locales),
        '  <meta property="og:url" content="%s">' % esc(canonical_url),
        '  <meta property="og:title" content="%s">' % esc(og_title),
        '  <meta property="og:description" content="%s">' % esc(description),
        '  <meta property="og:image" content="%s">' % esc(abs_url(img)),
        '  <meta property="og:image:width" content="%d">' % w,
        '  <meta property="og:image:height" content="%d">' % h,
        '  <meta property="og:image:alt" content="%s">' % esc(og_title),
    ]
    if extra:
        lines.append(extra)
    lines += [
        '  <meta name="twitter:card" content="summary_large_image">',
        '  <meta name="twitter:title" content="%s">' % esc(og_title),
        '  <meta name="twitter:description" content="%s">' % esc(description),
        '  <meta name="twitter:image" content="%s">' % esc(abs_url(img)),
        '  <link rel="icon" type="image/svg+xml" href="/favicon.svg">',
        '  <link rel="icon" type="image/x-icon" href="/favicon.ico">',
        '  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">',
        '  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">',
        '  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">',
        '  <link rel="manifest" href="/site.webmanifest">',
        '  <link rel="preconnect" href="https://fonts.googleapis.com">',
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '  <link href="%s" rel="stylesheet">' % FONTS,
        '  <link rel="stylesheet" href="/styles.css?v=%s">' % ver('styles.css'),
        '  <link rel="stylesheet" href="/articles/article.css?v=%s">' % ver('articles/article.css'),
    ]
    if jsonld:
        lines.append('  <script type="application/ld+json">\n%s\n  </script>' % ld_json(jsonld))
    lines.append('</head>')
    return '\n'.join(lines)


def page_nav(lang, current):
    ui = UI[lang]
    cur = ' aria-current="page"' if current == 'index' else ''
    return '\n'.join([
        '  <a class="skipLink" href="#main">%s</a>' % esc(ui['skip']),
        '  <header>',
        '    <nav class="nav container" aria-label="%s">' % esc(ui['nav']),
        '      <a class="brand" href="/?lang=%s" aria-label="%s"><span>EA</span> Emad Alhamou</a>'
        % (lang, esc(ui['home'])),
        '      <div class="links">',
        '        <a href="/?lang=%s">%s</a>' % (lang, esc(ui['home'])),
        '        <a href="%s"%s>%s</a>' % (index_path(lang), cur, esc(ui['articles'])),
        '      </div>',
        '      <a class="navCta" href="/?lang=%s#contact">%s</a>' % (lang, esc(ui['lets_talk'])),
        '    </nav>',
        '  </header>',
    ])


def page_footer(lang, alternates):
    picker = ''
    if len(alternates) > 1:
        options = ''.join('<option value="%s" lang="%s"%s>%s</option>'
                          % (esc(p), l, ' selected' if l == lang else '', LANG[l]['name'])
                          for l, p in alternates)
        picker = ('\n    <label class="langPick">%s<select id="langSelect" aria-label="%s" data-nav>'
                  '%s</select>%s</label>' % (GLOBE, esc(UI[lang]['lang']), options, CHEV))
    return '\n'.join([
        '  <footer class="container">',
        '    <a class="brand" href="/?lang=%s"><span>EA</span> Emad Alhamou</a>' % lang,
        '    <p>Founder &amp; Product Builder</p>%s' % picker,
        '    <p>© %d</p>' % dt.date.today().year,
        '  </footer>',
        '  <script src="/video.js?v=%s"></script>' % ver('video.js'),
        '  <script src="/articles/article.js?v=%s"></script>' % ver('articles/article.js'),
        '</body>',
        '</html>',
        '',
    ])


def crumbs_html(lang, last=None):
    ui = UI[lang]
    items = ['<li><a href="/?lang=%s">%s</a></li>' % (lang, esc(ui['home']))]
    if last is None:
        items.append('<li aria-current="page">%s</li>' % esc(ui['articles']))
    else:
        items.append('<li><a href="%s">%s</a></li>' % (index_path(lang), esc(ui['articles'])))
        items.append('<li aria-current="page">%s</li>' % esc(last))
    return '<nav class="crumbs" aria-label="%s"><ol>%s</ol></nav>' % (esc(ui['crumbs']), ''.join(items))


def card_html(a, lang, heading='h2'):
    t = a['langs'][lang]
    fm = t['fm']
    return '\n'.join([
        '<a class="artCard" href="%s" style="%s">' % (art_path(a, lang), theme_style(a)),
        '  <span class="artCardTop"><img src="/%s" width="56" height="56" alt="" loading="lazy">'
        '<span>%s</span></span>' % (esc(a['icon']), esc(fm['kicker'])),
        '  <span class="artCardBody">',
        '    <%s class="artCardTitle">%s</%s>' % (heading, esc(fm['title']), heading),
        '    <span class="artCardDek">%s</span>' % esc(fm['dek']),
        '    <span class="artCardMeta"><time datetime="%s">%s</time> · %s</span>'
        % (a['date_published'], fmt_date(a['date_published'], lang), minutes_label(t['minutes'], lang)),
        '  </span>',
        '</a>',
    ])


# ---------------------------------------------------------------- structured data

def ld_base():
    return [
        {'@type': 'WebSite', '@id': WEBSITE_ID, 'url': SITE + '/', 'name': 'Emad Alhamou',
         'inLanguage': ['ar', 'en', 'de'], 'publisher': {'@id': PERSON_ID}},
        {'@type': 'Person', '@id': PERSON_ID, 'name': 'Emad Alhamou', 'alternateName': 'عماد الحمو',
         'url': SITE + '/', 'jobTitle': 'Founder & Product Builder',
         'knowsLanguage': ['ar', 'de', 'en'], 'sameAs': SAME_AS},
        {'@type': 'Organization', '@id': ORG_ID, 'name': 'Alhamou', 'alternateName': 'شركة الحمو',
         'url': SITE + '/', 'logo': {'@type': 'ImageObject', 'url': SITE + '/android-chrome-512x512.png',
                                     'width': 512, 'height': 512}},
    ]


def ld_breadcrumbs(url, crumbs):
    return {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u}
                                for i, (n, u) in enumerate(crumbs)]}


def ld_article(a, lang):
    t = a['langs'][lang]
    fm = t['fm']
    url = abs_url(art_path(a, lang))
    base_url = abs_url(art_path(a, DEFAULT))
    og_path, w, h = og_for(a, lang)
    images = [abs_url(og_path)]
    v = video_for(a, lang)
    poster = poster_for(a, lang)
    if poster:
        images.append(abs_url(poster))
    graph = ld_base()
    graph.append(ld_breadcrumbs(url, [(UI[lang]['home'], SITE + '/'),
                                      (UI[lang]['articles'], abs_url(index_path(lang))),
                                      (fm['short_title'], url)]))
    graph.append({'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': fm['seo_title'],
                  'description': fm['description'], 'inLanguage': lang, 'isPartOf': {'@id': WEBSITE_ID},
                  'breadcrumb': {'@id': url + '#breadcrumb'}, 'primaryImageOfPage': {'@id': url + '#primaryimage'},
                  'datePublished': a['date_published'], 'dateModified': a['date_modified']})
    graph.append({'@type': 'ImageObject', '@id': url + '#primaryimage', 'url': abs_url(og_path),
                  'contentUrl': abs_url(og_path), 'width': w, 'height': h, 'caption': fm['title']})
    article = {
        '@type': 'Article', '@id': url + '#article', 'headline': fm['title'][:110],
        'description': fm['description'], 'abstract': fm['dek'], 'inLanguage': lang,
        'datePublished': a['date_published'], 'dateModified': a['date_modified'],
        'author': {'@id': PERSON_ID}, 'publisher': {'@id': ORG_ID},
        'copyrightHolder': {'@id': PERSON_ID}, 'mainEntityOfPage': {'@id': url + '#webpage'},
        'image': images, 'articleSection': fm['kicker'], 'wordCount': t['words'],
        'isAccessibleForFree': True,
    }
    if fm.get('keywords'):
        article['keywords'] = [k.strip() for k in fm['keywords'].split(',') if k.strip()]
    if a.get('product'):
        article['about'] = {'@id': base_url + '#software'}
    if v:
        article['video'] = {'@id': video_ld_id(a, v)}
    others = [l for l in LANGS if l in a['langs'] and l != lang]
    if lang == DEFAULT and others:
        article['workTranslation'] = [{'@id': abs_url(art_path(a, l)) + '#article'} for l in others]
    elif lang != DEFAULT:
        article['translationOfWork'] = {'@id': base_url + '#article'}
    graph.append(article)

    p = a.get('product')
    if p:
        sw = {'@type': 'SoftwareApplication', '@id': base_url + '#software', 'name': p['name'],
              'url': p.get('url', {}).get(lang) or p.get('url', {}).get(DEFAULT),
              'applicationCategory': p.get('category', 'UtilitiesApplication'),
              'image': abs_url('/' + a['icon'])}
        if p.get('publisher', 'org') != 'none':
            # "publisher": "none" in meta.json leaves the maker out, for a product Alhamou did not publish
            sw['publisher'] = {'@id': ORG_ID}
            sw['author'] = {'@id': ORG_ID}
        for src, dst in (('alternate_name', 'alternateName'), ('operating_system', 'operatingSystem'),
                         ('requirements', 'softwareRequirements'), ('languages', 'inLanguage')):
            if p.get(src):
                sw[dst] = p[src]
        if fm.get('product_line'):
            sw['description'] = fm['product_line']
        if fm.get('status'):
            sw['creativeWorkStatus'] = fm['status']
        graph.append(sw)

    if v:
        yid = v['youtube_id']
        thumbs = ([abs_url(poster)] if poster else []) + ['https://i.ytimg.com/vi/%s/hqdefault.jpg' % yid]
        video = {'@type': 'VideoObject', '@id': video_ld_id(a, v), 'name': v['title'],
                 'description': v['description'], 'thumbnailUrl': thumbs, 'uploadDate': v['upload_date'],
                 'embedUrl': 'https://www.youtube.com/embed/%s' % yid,
                 'url': 'https://www.youtube.com/watch?v=%s' % yid,
                 'inLanguage': v.get('language', DEFAULT),
                 'author': {'@id': PERSON_ID}, 'publisher': {'@id': ORG_ID}}
        if v.get('duration'):
            video['duration'] = v['duration']
        graph.append(video)

    if t['faq']:
        graph.append({'@type': 'FAQPage', '@id': url + '#faq', 'inLanguage': lang,
                      'isPartOf': {'@id': url + '#webpage'},
                      'mainEntity': [{'@type': 'Question', 'name': plain(i['q']),
                                      'acceptedAnswer': {'@type': 'Answer', 'text': answer_text(i['a'])}}
                                     for i in t['faq']['items']]})
    return {'@context': 'https://schema.org', '@graph': graph}


# ---------------------------------------------------------------- pages

def article_page(a, lang, articles):
    t = a['langs'][lang]
    fm = t['fm']
    ui = UI[lang]
    alternates = [(l, art_path(a, l)) for l in LANGS if l in a['langs']]
    canonical = art_path(a, lang)
    og = og_for(a, lang)
    extra = ['  <meta property="article:published_time" content="%s">' % a['date_published'],
             '  <meta property="article:modified_time" content="%s">' % a['date_modified'],
             '  <meta property="article:author" content="%s/">' % SITE,
             '  <meta property="article:section" content="%s">' % esc(fm['kicker'])]
    for k in [k.strip() for k in fm.get('keywords', '').split(',') if k.strip()][:6]:
        extra.append('  <meta property="article:tag" content="%s">' % esc(k))
    head = page_head(lang, title=fm['seo_title'], og_title=fm['title'], description=fm['description'],
                     canonical=canonical, alternates=alternates, og_image=og, og_type='article',
                     extra='\n'.join(extra), jsonld=ld_article(a, lang), keywords=fm.get('keywords', ''),
                     md_alt=canonical + 'index.md')

    v = video_for(a, lang)
    status = fm.get('status')
    pill = ' <span class="artStatus"><i></i>%s</span>' % esc(status) if status else ''
    meta = ['<span class="artAuthor"><span class="mono" aria-hidden="true">EA</span>'
            '<span><b>%s</b><small>%s</small></span></span>' % (esc(ui['author']), esc(ui['role'])),
            '<span>%s <time datetime="%s">%s</time></span>'
            % (esc(ui['published']), a['date_published'], fmt_date(a['date_published'], lang))]
    if a['date_modified'] != a['date_published']:
        meta.append('<span>%s <time datetime="%s">%s</time></span>'
                    % (esc(ui['updated']), a['date_modified'], fmt_date(a['date_modified'], lang)))
    meta.append('<span>%s</span>' % minutes_label(t['minutes'], lang))
    if len(alternates) > 1:
        meta.append('<span class="artLangs">%s: %s</span>' % (esc(ui['also_in']), ' · '.join(
            '<a href="%s" hreflang="%s" lang="%s">%s</a>' % (p, l, l, LANG[l]['name'])
            for l, p in alternates if l != lang)))

    body = [
        page_nav(lang, 'article'),
        '  <main id="main">',
        '  <article class="art" style="%s">' % theme_style(a),
        '    <header class="artHero%s" data-mark="%s">' % ('' if v else ' noVideo', esc(a.get('mark', ''))),
        '      <div class="container artHeroIn">',
        '        ' + crumbs_html(lang, fm['short_title']),
        '        <p class="artKicker"><img src="/%s" width="40" height="40" alt="">%s%s</p>'
        % (esc(a['icon']), esc(fm['kicker']), pill),
        '        <h1>%s</h1>' % esc(fm['title']),
        '        <p class="artDek">%s</p>' % esc(fm['dek']),
        '        <div class="artMeta">%s</div>' % ''.join(meta),
        '      </div>',
        '    </header>',
    ]
    if v:
        yid = v['youtube_id']
        watch = 'https://www.youtube.com/watch?v=%s' % yid
        poster = poster_for(a, lang)
        img = ('<img src="%s" width="%d" height="%d" alt="" fetchpriority="high" decoding="async">'
               % (poster, POSTER_W, POSTER_H)) if poster else \
              ('<span class="ytFallback"><img src="/%s" width="96" height="96" alt=""></span>' % esc(a['icon']))
        body += [
            '    <figure class="container artVideo">',
            '      <a class="yt" href="%s" data-yt="%s" data-title="%s" aria-label="%s: %s">%s'
            '<span class="ytPlay" aria-hidden="true">%s</span></a>'
            % (watch, yid, esc(v['title']), esc(ui['play']), esc(v['title']), img, PLAY),
            '      <figcaption><span>%s</span><a href="%s" target="_blank" rel="noopener">%s <b>%s</b></a>'
            '<small>%s</small></figcaption>'
            % (esc(fm.get('video_caption', v['title'])), watch, esc(ui['watch_yt']), ARR_EXT, esc(ui['yt_notice'])),
            '    </figure>',
        ]
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (sid, esc(text)) for sid, text in t['toc'])
    body += [
        '    <div class="container artGrid">',
        '      <aside class="artToc" aria-labelledby="toc-title"><p class="label" id="toc-title">%s</p>'
        '<ol>%s</ol></aside>' % (esc(ui['toc']), toc),
        '      <div class="artBody">',
        t['body_html'],
        t['faq_html'],
    ]
    p = a.get('product')
    if p:
        url = p.get('url', {}).get(lang) or p.get('url', {}).get(DEFAULT)
        domain = re.sub(r'^https?://', '', url).strip('/').split('/')[0]
        facts = []
        if status:
            facts.append('%s · %s %s' % (status, ui['since'], fmt_month(p['since'], lang)) if p.get('since') else status)
        if fm.get('requirements'):
            facts.append(fm['requirements'])
        actions = ['<a class="artBtn" href="%s">%s <b>%s</b></a>' % (esc(url), esc(ui['visit'].format(domain)), ARR_EXT)]
        if v:
            actions.append('<a class="artBtn ghost" href="https://www.youtube.com/watch?v=%s" target="_blank" '
                           'rel="noopener">%s <b>%s</b></a>' % (v['youtube_id'], esc(ui['watch_yt']), ARR_EXT))
        body += [
            '      <aside class="artProduct" aria-labelledby="product-title">',
            '        <img src="/%s" width="72" height="72" alt="" loading="lazy">' % esc(a['icon']),
            '        <div>',
            '          <p class="label">%s</p>' % esc(ui['product']),
            '          <p class="artProductName" id="product-title">%s</p>' % esc(p['name']),
            '          <p>%s</p>' % esc(fm.get('product_line', '')),
            '          <ul class="artFacts">%s</ul>' % ''.join('<li>%s</li>' % esc(f) for f in facts),
            '          <p class="artActions">%s</p>' % ''.join(actions),
            '        </div>',
            '      </aside>',
        ]
    body += ['      </div>', '    </div>', '  </article>']
    more = [o for o in articles if o is not a and lang in o['langs']][:3]
    if more:
        body += ['  <section class="container artMore" aria-labelledby="more-title">',
                 '    <p class="label" id="more-title">%s</p>' % esc(ui['more']),
                 '    <div class="artList">', '\n'.join(card_html(o, lang, 'h3') for o in more),
                 '    </div>', '  </section>']
    body.append('  </main>')
    return head + '\n<body>\n' + '\n'.join(body) + '\n' + page_footer(lang, alternates)


def index_page(lang, articles):
    ui = UI[lang]
    items = [a for a in articles if lang in a['langs']]
    url = abs_url(index_path(lang))
    alternates = [(l, index_path(l)) for l in LANGS]
    graph = ld_base()
    graph.append(ld_breadcrumbs(url, [(ui['home'], SITE + '/'), (ui['articles'], url)]))
    graph.append({'@type': 'CollectionPage', '@id': url + '#webpage', 'url': url, 'name': ui['articles_title'],
                  'description': ui['articles_desc'], 'inLanguage': lang, 'isPartOf': {'@id': WEBSITE_ID},
                  'breadcrumb': {'@id': url + '#breadcrumb'},
                  'mainEntity': {'@type': 'ItemList', 'itemListElement': [
                      {'@type': 'ListItem', 'position': i + 1, 'url': abs_url(art_path(a, lang)),
                       'name': a['langs'][lang]['fm']['title']} for i, a in enumerate(items)]}})
    head = page_head(lang, title=ui['articles_title'], og_title=ui['articles_title'],
                     description=ui['articles_desc'], canonical=index_path(lang), alternates=alternates,
                     og_image=FALLBACK_OG, og_type='website',
                     jsonld={'@context': 'https://schema.org', '@graph': graph})
    cards = '\n'.join(card_html(a, lang) for a in items) or '<p class="artEmpty">%s</p>' % esc(ui['empty'])
    body = [
        page_nav(lang, 'index'),
        '  <main id="main" class="art">',
        '    <header class="artHero noVideo" data-mark="ARTICLES">',
        '      <div class="container artHeroIn">',
        '        ' + crumbs_html(lang),
        '        <h1>%s</h1>' % esc(ui['articles_h1']),
        '        <p class="artDek">%s</p>' % esc(ui['articles_intro']),
        '        <p class="artFeed"><a href="%s">%s</a></p>' % (feed_path(lang), esc(ui['feed'])),
        '      </div>',
        '    </header>',
        '    <section class="container artList artListMain" aria-label="%s">' % esc(ui['articles']),
        cards,
        '    </section>',
        '  </main>',
    ]
    return head + '\n<body>\n' + '\n'.join(body) + '\n' + page_footer(lang, alternates)


def article_md(a, lang):
    t = a['langs'][lang]
    fm = t['fm']
    ui = UI[lang]
    lines = ['# %s' % fm['title'], '', '> %s' % fm['dek'], '',
             '- Author: [Emad Alhamou](%s/), %s' % (SITE, UI['en']['role']),
             '- Published: %s (updated %s)' % (a['date_published'], a['date_modified']),
             '- Language: %s' % LANG[lang]['name'],
             '- Web page: %s' % abs_url(art_path(a, lang))]
    others = [l for l in LANGS if l in a['langs'] and l != lang]
    if others:
        lines.append('- Other languages: ' + ', '.join(
            '[%s](%s)' % (LANG[l]['name'], abs_url(art_path(a, l)) + 'index.md') for l in others))
    v = video_for(a, lang)
    if v:
        lines.append('- Video: [%s](https://www.youtube.com/watch?v=%s)' % (v['title'], v['youtube_id']))
    p = a.get('product')
    if p:
        url = p.get('url', {}).get(lang) or p.get('url', {}).get(DEFAULT)
        facts = [x for x in (fm.get('status'), fm.get('requirements')) if x]
        lines.append('- Product: [%s](%s)%s' % (p['name'], url, ''.join(' · ' + f for f in facts)))
    lines += ['', t['md'].strip(), '']
    return '\n'.join(lines)


def atom_feed(lang, articles):
    ui = UI[lang]
    items = [a for a in articles if lang in a['langs']]
    updated = max([a['date_modified'] for a in items] or [dt.date.today().isoformat()])
    out = ['<?xml version="1.0" encoding="utf-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="%s">' % lang,
           '  <title>%s · Emad Alhamou</title>' % esc(ui['articles_h1']),
           '  <subtitle>%s</subtitle>' % esc(ui['articles_intro']),
           '  <link rel="self" type="application/atom+xml" href="%s"/>' % abs_url(feed_path(lang)),
           '  <link rel="alternate" type="text/html" href="%s"/>' % abs_url(index_path(lang)),
           '  <id>%s</id>' % abs_url(index_path(lang)),
           '  <updated>%sT00:00:00Z</updated>' % updated,
           '  <author><name>Emad Alhamou</name><uri>%s/</uri></author>' % SITE,
           '  <icon>%s/favicon-32x32.png</icon>' % SITE]
    for a in items:
        t = a['langs'][lang]
        url = abs_url(art_path(a, lang))
        out += ['  <entry>',
                '    <title>%s</title>' % esc(t['fm']['title']),
                '    <link rel="alternate" type="text/html" href="%s"/>' % url,
                '    <id>%s</id>' % url,
                '    <published>%sT00:00:00Z</published>' % a['date_published'],
                '    <updated>%sT00:00:00Z</updated>' % a['date_modified'],
                '    <summary>%s</summary>' % esc(t['fm']['dek']),
                '    <content type="html">%s</content>' % esc(t['body_html'] + '\n' + t['faq_html']),
                '  </entry>']
    out += ['</feed>', '']
    return '\n'.join(out)


def home_cards(articles):
    cards = []
    for a in articles[:6]:
        def pick(l):
            return l if l in a['langs'] else DEFAULT

        def ml(fn):
            return ''.join('<span data-l="%s" lang="%s">%s</span>' % (l, pick(l), fn(pick(l))) for l in HOME_ORDER)

        base = art_path(a, pick('ar'))
        cards.append('\n'.join([
            '<a class="homeArt" href="%s" data-href-en="%s" data-href-de="%s" style="%s">'
            % (base, art_path(a, pick('en')), art_path(a, pick('de')), theme_style(a)),
            '  <span class="homeArtTop"><img src="/%s" width="56" height="56" alt="" loading="lazy">'
            '<span class="ml">%s</span></span>' % (esc(a['icon']), ml(lambda l: esc(a['langs'][l]['fm']['kicker']))),
            '  <span class="homeArtBody">',
            '    <h3 class="ml">%s</h3>' % ml(lambda l: esc(a['langs'][l]['fm']['title'])),
            '    <span class="homeArtDek ml">%s</span>' % ml(lambda l: esc(a['langs'][l]['fm']['dek'])),
            '    <span class="homeArtMeta ml">%s</span>' % ml(lambda l: '<time datetime="%s">%s</time> · %s' % (
                a['date_published'], fmt_date(a['date_published'], l),
                minutes_label(a['langs'][l]['minutes'], l))),
            '  </span>',
            '</a>',
        ]))
    return '\n'.join(cards)


def replace_block(text, block, where, indent=''):
    start, end = '<!-- articles:start -->', '<!-- articles:end -->'
    if start not in text or end not in text:
        print('note: %s has no %s ... %s markers, skipped' % (where, start, end))
        return text
    i = text.index(start) + len(start)
    j = text.index(end)
    inner = '\n'.join((indent + l) if l.strip() else l for l in block.splitlines())
    return text[:i] + '\n' + inner + '\n' + indent + text[j:]


def sitemap(articles):
    home_lastmod = max([d for d in [git_date('index.html')] if d] +
                       [a['date_modified'] for a in articles] or [dt.date.today().isoformat()])
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
           '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"',
           '        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">',
           '  <url>', '    <loc>%s/</loc>' % SITE, '    <lastmod>%s</lastmod>' % home_lastmod,
           '    <changefreq>monthly</changefreq>', '    <priority>1.0</priority>', '  </url>']

    def entry(path, lastmod, alts, extra=()):
        lines = ['  <url>', '    <loc>%s</loc>' % esc(abs_url(path)), '    <lastmod>%s</lastmod>' % lastmod]
        if len(alts) > 1:
            lines += ['    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (l, esc(abs_url(p)))
                      for l, p in alts]
            lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                         % esc(abs_url(dict(alts).get(DEFAULT, alts[0][1]))))
        return lines + list(extra) + ['  </url>']

    if articles:
        idx_alts = [(l, index_path(l)) for l in LANGS]
        idx_lastmod = max(a['date_modified'] for a in articles)
        for l, p in idx_alts:
            out += entry(p, idx_lastmod, idx_alts)
    for a in articles:
        alts = [(l, art_path(a, l)) for l in LANGS if l in a['langs']]
        for l, p in alts:
            extra = []
            poster = poster_for(a, l)
            og_path = og_for(a, l)[0]
            for img in [og_path] + ([poster] if poster else []):
                extra += ['    <image:image>', '      <image:loc>%s</image:loc>' % esc(abs_url(img)),
                          '    </image:image>']
            v = video_for(a, l)
            if v:
                thumb = abs_url(poster) if poster else 'https://i.ytimg.com/vi/%s/hqdefault.jpg' % v['youtube_id']
                extra += ['    <video:video>',
                          '      <video:thumbnail_loc>%s</video:thumbnail_loc>' % esc(thumb),
                          '      <video:title>%s</video:title>' % esc(v['title']),
                          '      <video:description>%s</video:description>' % esc(v['description']),
                          '      <video:player_loc>https://www.youtube.com/embed/%s</video:player_loc>' % v['youtube_id'],
                          '      <video:publication_date>%s</video:publication_date>' % v['upload_date']]
                if v.get('duration_seconds'):
                    extra.append('      <video:duration>%d</video:duration>' % int(v['duration_seconds']))
                extra.append('    </video:video>')
            out += entry(p, a['date_modified'], alts, extra)
    out += ['</urlset>', '']
    return '\n'.join(out)


def llms_block(articles):
    lines = ['## Articles', '',
             'Articles are static pages in English, German and Arabic (where a translation exists). Add index.md to an article URL '
             'for a plain Markdown copy. All English articles in one file: [llms-full.txt](%s/llms-full.txt).' % SITE,
             '']
    for a in articles:
        t = a['langs'][DEFAULT]
        others = [l for l in LANGS if l in a['langs'] and l != DEFAULT]
        tail = ''
        if others:
            tail = ' Also in ' + ' and '.join('[%s](%s)' % (LANG[l]['name'], abs_url(art_path(a, l)) + 'index.md')
                                              for l in others) + '.'
        lines.append('- [%s](%s): %s%s' % (t['fm']['title'], abs_url(art_path(a, DEFAULT)) + 'index.md',
                                            t['fm']['description'], tail))
    return '\n'.join(lines)


def llms_full(articles):
    out = ['# Emad Alhamou: articles in full', '',
           '> The full text of every article on hamou.de, in English, for AI assistants and language models. '
           'Index of the site: %s/llms.txt' % SITE, '']
    for a in articles:
        out += ['---', '', article_md(a, DEFAULT).strip(), '']
    return '\n'.join(out)


# ---------------------------------------------------------------- images

def image_jobs(articles):
    jobs = []
    for a in articles:
        icon = os.path.join(ROOT, a['icon'])
        theme = a.get('theme') or {}
        for lang, t in a['langs'].items():
            fm = t['fm']
            jobs.append({'kind': 'og', 'out': os.path.join(ROOT, og_rel(a, lang).lstrip('/')),
                         'width': OG_W, 'height': OG_H, 'lang': lang, 'dir': LANG[lang]['dir'],
                         'title': fm['title'], 'kicker': fm['kicker'], 'status': fm.get('status', ''),
                         'author': UI[lang]['author'], 'section': UI[lang]['articles'],
                         'url': ('hamou.de' + art_path(a, lang)).rstrip('/'), 'icon': icon,
                         'theme': theme, 'mark': a.get('mark', '')})
        if a.get('video'):
            # One poster per video: the main one, and one for every language
            # that has its own video (video.by_lang).
            owners = [DEFAULT] + [l for l in a['video'].get('by_lang') or {} if l != DEFAULT and l in a['langs']]
            for owner in owners:
                v = video_for(a, owner)
                vlang = owner  # the poster text follows the page language, not the spoken language
                jobs.append({'kind': 'poster', 'out': os.path.join(ROOT, poster_rel(a, owner).lstrip('/')),
                             'width': POSTER_W, 'height': POSTER_H, 'lang': vlang, 'dir': LANG[vlang]['dir'],
                             'title': v.get('poster_title') or a['langs'][owner]['fm']['short_title'],
                             'subtitle': v.get('poster_subtitle', ''), 'kicker': v.get('poster_kicker', ''),
                             'brand': ORG_NAME[vlang], 'icon': icon, 'theme': theme, 'mark': a.get('mark', '')})
    return jobs


def render_images(articles):
    jobs = image_jobs(articles)
    if not jobs:
        return
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False)
        jobs_path = f.name
    try:
        for job in jobs:
            os.makedirs(os.path.dirname(job['out']), exist_ok=True)
        subprocess.run(['node', os.path.join(ROOT, 'tools', 'render_images.js'), jobs_path], check=True)
    finally:
        os.unlink(jobs_path)


# ---------------------------------------------------------------- main

def main():
    articles = load_articles()
    if '--images' in sys.argv[1:]:
        render_images(articles)
    for a in articles:
        for lang in a['langs']:
            write(art_path(a, lang) + 'index.html', article_page(a, lang, articles))
            write(art_path(a, lang) + 'index.md', article_md(a, lang))
    for lang in LANGS:
        write(index_path(lang) + 'index.html', index_page(lang, articles))
        write(feed_path(lang), atom_feed(lang, articles))
    home = os.path.join(ROOT, 'index.html')
    with open(home, encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'\n([ \t]*)<!-- articles:start -->', text)
    write('index.html', replace_block(text, home_cards(articles), 'index.html', m.group(1) if m else ''))
    write('sitemap.xml', sitemap(articles))
    llms = os.path.join(ROOT, 'llms.txt')
    with open(llms, encoding='utf-8') as f:
        write('llms.txt', replace_block(f.read(), llms_block(articles), 'llms.txt'))
    write('llms-full.txt', llms_full(articles))
    print('%d article(s), %d page(s)' % (len(articles), sum(len(a['langs']) for a in articles)))


if __name__ == '__main__':
    main()
