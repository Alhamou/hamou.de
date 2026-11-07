#!/usr/bin/env node
/* Renders article share images (og.jpg, 1200x630) and video posters
   (poster.jpg, 1280x720). tools/build_articles.py --images writes the job
   list and calls this script; it needs Node and Playwright. */
const fs = require('fs');
const path = require('path');

let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  console.error('Playwright is missing. Install it with: npm install --no-save playwright && npx playwright install chromium');
  process.exit(1);
}

const root = path.resolve(__dirname, '..');
const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const dataUri = (file, type) => 'data:' + type + ';base64,' + fs.readFileSync(file).toString('base64');
const guesswhat = dataUri(path.join(root, 'fonts', 'Guesswhat-Exceptional.otf'), 'font/otf');
const esc = (s) => String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const FONTS = 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Instrument+Serif&family=Inter:wght@500;600;700&display=block';

function base(job, css, body) {
  const t = job.theme || {};
  // The page itself is always left-to-right so the absolute layout stays put;
  // text blocks carry their own dir attribute.
  return `<!doctype html><html lang="${esc(job.lang)}" dir="ltr"><head><meta charset="utf-8">
<link rel="stylesheet" href="${FONTS}">
<style>
@font-face{font-family:'Guesswhat';src:url(${guesswhat}) format('opentype');font-display:block}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${job.width}px;height:${job.height}px}
body{--bg:${t.bg || '#191a16'};--accent:${t.accent || '#c7ff34'};--fg:${t.fg || '#f4f2ea'};
  background:var(--bg);color:var(--fg);position:relative;overflow:hidden;
  font-family:${job.dir === 'rtl' ? "'IBM Plex Sans Arabic'" : "'Inter'"},sans-serif;-webkit-font-smoothing:antialiased}
.glow{position:absolute;border-radius:50%;pointer-events:none}
.mark{position:absolute;font:700 300px/1 'Inter',sans-serif;letter-spacing:-18px;color:#ffffff0a;white-space:nowrap}
.mono{background:#c7ff34;color:#12130f;display:grid;place-items:center;font:700 16px 'Inter',sans-serif}
${css}
</style></head><body>${body}</body></html>`;
}

function og(job) {
  const side = job.dir === 'rtl' ? 'left' : 'right';
  const display = job.dir === 'rtl' ? "'Guesswhat','IBM Plex Sans Arabic',sans-serif" : "'Instrument Serif',Georgia,serif";
  return base(job, `
.glow{width:820px;height:820px;top:-330px;${side}:-240px;background:radial-gradient(circle,color-mix(in srgb,var(--accent) 30%,transparent),transparent 64%)}
.mark{bottom:-64px;${side}:-24px}
.top{position:absolute;top:58px;left:72px;right:72px;display:flex;align-items:center;gap:14px;font-size:22px;font-weight:600}
.top .mono{width:46px;height:46px}
.top .sep{opacity:.4}
.main{position:absolute;left:72px;right:72px;bottom:132px}
.kick{display:flex;align-items:center;gap:18px;color:var(--accent);font-size:25px;font-weight:600;margin-bottom:22px}
.kick img{width:72px;height:72px;filter:drop-shadow(0 12px 20px #0008)}
.kick .pill{color:var(--fg);border:1.5px solid #ffffff33;border-radius:50px;padding:6px 16px;font-size:18px;font-weight:500}
h1{font-family:${display};font-weight:400;font-size:${job.dir === 'rtl' ? 74 : 86}px;line-height:${job.dir === 'rtl' ? 1.25 : 1.02};letter-spacing:${job.dir === 'rtl' ? 0 : '-0.01em'};max-width:1040px}
.foot{position:absolute;left:72px;right:72px;bottom:50px;display:flex;justify-content:space-between;align-items:center;font:500 20px 'Inter',sans-serif;opacity:.72;direction:ltr}
.bar{position:absolute;left:0;right:0;bottom:0;height:10px;background:var(--accent)}
`, `<div class="glow"></div><div class="mark">${esc(job.mark)}</div>
<div class="top" dir="${esc(job.dir)}"><span class="mono">EA</span><span>${esc(job.author)}</span><span class="sep">·</span><span>${esc(job.section)}</span></div>
<div class="main" dir="${esc(job.dir)}"><div class="kick"><img src="${dataUri(job.icon, 'image/png')}" alt="">${esc(job.kicker)}${job.status ? `<span class="pill">${esc(job.status)}</span>` : ''}</div><h1 id="t">${esc(job.title)}</h1></div>
<div class="foot"><span>${esc(job.url)}</span><span>hamou.de</span></div><div class="bar"></div>`);
}

function poster(job) {
  return base(job, `
body{background:radial-gradient(120% 90% at 85% 0%,color-mix(in srgb,var(--accent) 22%,var(--bg)) 0%,var(--bg) 55%,color-mix(in srgb,var(--bg) 80%,#000) 100%)}
.mark{bottom:-70px;right:-30px;font-size:330px}
.icon{position:absolute;top:70px;left:80px;width:150px;height:150px;filter:drop-shadow(0 22px 34px #0009)}
.brand{position:absolute;top:92px;right:80px;display:flex;align-items:center;gap:14px;font:600 22px 'Inter',sans-serif;opacity:.85}
.brand .mono{width:44px;height:44px}
.copy{position:absolute;left:80px;bottom:78px;max-width:900px}
.kick{color:var(--accent);font:700 18px 'Inter',sans-serif;letter-spacing:4px;text-transform:uppercase}
h1{font:400 132px/1 'Instrument Serif',Georgia,serif;letter-spacing:-0.01em;margin:16px 0 14px}
p{font:500 31px/1.35 'Inter',sans-serif;opacity:.85}
`, `<div class="mark">${esc(job.mark)}</div>
<img class="icon" src="${dataUri(job.icon, 'image/png')}" alt="">
<div class="brand"><span class="mono">EA</span><span>${esc(job.author)}</span></div>
<div class="copy"><div class="kick">${esc(job.kicker)}</div><h1>${esc(job.title)}</h1><p>${esc(job.subtitle)}</p></div>`);
}

(async () => {
  const browser = await chromium.launch();
  try {
    for (const job of jobs) {
      const page = await browser.newPage({ viewport: { width: job.width, height: job.height }, deviceScaleFactor: 1 });
      await page.setContent(job.kind === 'poster' ? poster(job) : og(job), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      if (job.kind === 'og') {
        // Shrink long titles until they fit in three lines.
        await page.evaluate(() => {
          const h1 = document.getElementById('t');
          let size = parseFloat(getComputedStyle(h1).fontSize);
          const line = parseFloat(getComputedStyle(h1).lineHeight) / size;
          while (h1.scrollHeight > size * line * 3 + 4 && size > 40) {
            size -= 2;
            h1.style.fontSize = size + 'px';
          }
        });
      }
      fs.mkdirSync(path.dirname(job.out), { recursive: true });
      await page.screenshot({ path: job.out, type: 'jpeg', quality: 88 });
      await page.close();
      console.log('wrote', path.relative(root, job.out));
    }
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
