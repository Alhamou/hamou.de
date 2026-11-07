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
(with language alternates, images and videos), the article list in
`llms.txt`, `llms-full.txt`, and the Atom feeds. Edit the files here, never
the generated HTML: the next build overwrites it.

## meta.json

| Key | Meaning |
|---|---|
| `date_published`, `date_modified` | `YYYY-MM-DD`. Change `date_modified` when you update the text. |
| `theme` | `bg`, `accent`, `fg` colors of the article's hero band and cards. |
| `mark` | Large faint word in the hero background, e.g. `NADHIF`. |
| `icon` | Path of a square icon in the repository, e.g. `oss/nadhif.png`. |
| `product` | Optional. The product the article is about; becomes the product card and `SoftwareApplication` data. `since` is `YYYY-MM`. |
| `video` | Optional. `youtube_id`, title, description, `upload_date` (`YYYY-MM-DD`), optional `duration` (ISO 8601, e.g. `PT1M45S`) and `duration_seconds`, `language`, and the poster texts. |
| `video.by_lang` | Optional. A video recorded in another language, e.g. `"ar": {...}` with its own `youtube_id`, title, description, `upload_date`, `language` and poster texts. That language's page shows it, with its own poster in `/ar/articles/<slug>/poster.jpg`; languages without an entry show the main video. |
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
`[links](https://...)`. Put `<!-- faq -->` on its own line before a final
`## Questions` section whose `### questions` are each followed by their
answer: they become the FAQ and its structured data.
