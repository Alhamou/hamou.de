# Articles

Every article on hamou.de is a plain, static HTML file. There is no server,
database or dashboard. This folder holds the text; `tools/build_articles.py`
turns it into the HTML files that GitHub Pages serves.

## Add an article

1. Copy the `nadhif` folder and rename it. The folder name becomes the URL:
   `content/articles/my-tool/` is published at `hamou.de/articles/my-tool/`,
   `hamou.de/de/articles/my-tool/` and `hamou.de/ar/articles/my-tool/`.
2. Edit `meta.json`: dates, colors, icon, and the `product` and `video`
   blocks (delete a block the article does not need).
3. Write the text in `en.md` (required), `de.md` and `ar.md`. A missing
   language is simply not published.
4. Run, from the repository root:

   ```
   python3 tools/build_articles.py --images
   ```

   `--images` also draws the share image (`og.jpg`) for every language and
   the video poster (`poster.jpg`). It needs Node and Playwright; leave it out
   to rebuild only the HTML.
5. Commit everything the script wrote and push to `main`.

The script also updates the article cards on the home page, `sitemap.xml`
(with language alternates, images and videos), the article lists in
`llms.txt`, `llms-full.txt`, and the Atom feeds. Edit the files here, never
the generated HTML: the next build overwrites it.

## Products and open-source tools

An article belongs to one of two groups, set by `group` in `meta.json`:

- **`product`** (the default): a product of the Alhamou team (Nadhif, TakeCar,
  Arab Solutions) or one Emad Alhamou helped build (Shfli). These appear on
  the home page in the Articles section.
- **`tool`**: a personal open-source tool (OpenBlock, RemoteDesk, pinFiy,
  closeAll, SafeShare, TopMovies, moveMouse, Haki). It is linked from its own
  card in the home page's open-source section ("Read the article"), not from
  the Articles section.

The article lists (`/articles/`, in each language) show two headings,
Products and Open source tools. Inside a group, articles are sorted by
publication date (newest first), then by `order` (a lower number comes first).
A page's "More articles" links start with its own group.

To add a tool:

1. Copy a folder from a tool such as `movemouse` and set `"group": "tool"` and
   an `order`.
2. In `product`, set `publisher` to `"person"` (Emad is credited as author, not
   the Alhamou team), `repo` (the GitHub URL, used for the main button and for
   the `SoftwareSourceCode` data), `license` (`name` and `url`) and `language`
   (the programming languages). `url.en` is the repository too.
3. Write from the project's own README and source, in the third person. Say
   what is verified ("according to the README") and keep the honest caveats
   (what is unencrypted, what loses data, what leaves the Mac). Do not quote
   version numbers or prices, which go stale.
4. Add an `a.ossArticle` link to the tool's card in `index.html` (copy one of
   the existing links) and, for a new tool, its `oss.article` text is already
   in `i18n.js`.

`llms.txt` has two generated blocks, `<!-- articles:start -->` for products and
`<!-- tools:start -->` for tools. Keep both pairs of markers.

## meta.json

| Key | Meaning |
|---|---|
| `date_published`, `date_modified` | `YYYY-MM-DD`. Change `date_modified` when you update the text. |
| `theme` | `bg`, `accent`, `fg` colors of the article's hero band and cards. |
| `mark` | Large faint word in the hero background, e.g. `NADHIF`. |
| `icon` | Path of a square icon in the repository, e.g. `oss/nadhif.png`. Use the product's real icon from its own app or website repository (never a redrawn letter box): a 256 px PNG with rounded corners (about 22%), which is what the home page, the article hero, the cards and the share images draw. |
| `group`, `order` | Optional. `product` (default) or `tool`, and the sort position inside a group. See "Products and open-source tools". |
| `product` | Optional. The product the article is about; becomes the product card and `SoftwareApplication` data. `since` is `YYYY-MM`. The maker is credited as Alhamou by default; set `"publisher": "person"` for a personal tool (Emad as author) or `"none"` for a product Alhamou did not publish (Shfli). A tool also sets `repo`, `license` (`name`, `url`) and `language`, which add the repository button, the license and `SoftwareSourceCode` data. |
| `video` | Optional. `youtube_id`, title, description, `upload_date` (`YYYY-MM-DD`), optional `duration` (ISO 8601, e.g. `PT1M45S`) and `duration_seconds`, `language`, and the poster texts. |
| `video.by_lang` | Optional. A video recorded in another language, e.g. `"ar": {...}` with its own `youtube_id`, title, description, `upload_date`, `language` and poster texts. That language's page shows it, with its own poster in `/ar/articles/<slug>/poster.jpg`; languages without an entry show the main video. An entry can also reuse the same `youtube_id` and only translate `title`, `description` and the poster texts (TakeCar does this: one Arabic video, shown with English, German and Arabic text). The poster is always written in the page's language; `language` is the language spoken in the video. |
| `draft` | Set to `true` to keep the article out of the build. |

## The Markdown files

Each file starts with front matter:

```
---
title: Shown as the H1 and in search results
short_title: Short name for breadcrumbs
seo_title: The <title>, ideally under 65 characters
description: Meta description, about 150 characters
kicker: Small label above the title, e.g. Product story
status: Optional status pill, e.g. In development
dek: One or two sentences under the title
keywords: comma, separated, search, terms
video_caption: Text under the video
product_line: One line for the product card
requirements: Shown on the product card
---
```

The body supports `## headings` (they form the table of contents),
`### subheadings`, paragraphs, `- lists`, `**bold**`, `` `code` `` and
`[links](https://...)`. Fenced code blocks and numbered lists are not
supported (write steps as sentences). Identifiers such as `GPL-3.0` are kept
on one line automatically. Put `<!-- faq -->` on its own line before a final
`## Questions` section whose `### questions` are each followed by their
answer: they become the FAQ and its structured data.
