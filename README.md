# XRIML Archive

A searchable archive of XR Immersive Media Lab guides, built with the same
MkDocs Material theme as the [XRIML Wiki](https://zbghost325.github.io/XRIML-WIKI/).
Includes a copy of the Wiki's Resource Guide.

- **Full-text search** covers every page and step of every document. Results
  jump straight to the matching step (`#step-18`) and highlight the search term.
- **Library** (home page): filter by collection, tag, or text; sort by date or title.
- **Documents** keep their original print-style look (paper pages, red step
  timeline, callouts) and still print or save to PDF page by page.

## Adding a document

Export the guide as a single standalone `.html` file (images embedded), then:

```bash
python3 tools/import_html.py ~/Downloads/my-guide.html --slug my-guide --category "Quick Start Guides" --tags "Unity, Meta Quest 3"
```

This creates `docs/documents/my-guide/` and the document shows up in the
library and in search automatically. No nav edits needed. Run it again with the
same slug to replace a document with a newer version.

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Pushing to `main` deploys to GitHub Pages via `.github/workflows/deploy.yml`.

## Document format

Each document is one folder: `docs/documents/<slug>/index.md` plus `images/`.
This is also the format a future in-browser editor would read and write.

**Front matter** (read by the library and the page header):

| Field         | Example                              |
|---------------|--------------------------------------|
| `title`       | `Meta XR SDK + Unity 6 + Quest 3 ...` |
| `description` | shown on the library card            |
| `template`    | always `document.html`               |
| `category`    | `Quick Start Guides` (library collection) |
| `software`    | `Unity 6000.3.23f1` (top band)       |
| `version`     | `8/26/2026` (XRIML versioning)       |
| `updated`     | `2026-08-26` (sorting + "Last Updated") |
| `pages`       | `34`                                 |
| `tags`        | list; also feeds the Tags page       |

**Body**: the guide's HTML, styled by `docs/stylesheets/guide.css`. The building blocks:

| Block | Markup |
|-------|--------|
| Page | `<section class="page" id="pN">` with `.band.top` / `.band.bottom` |
| Page title | `<h2 class="ptitle">` + `<div class="rule">` |
| Step timeline | `.pbody` > `.rail` + `.step` > `.bignum` + `<h3>` |
| Sub-step | `.sub` > `.subnum` + `<h4>` |
| Callouts | `.box` (red outline), `.box.crit .hl` (yellow highlight), `.note` (red bar) |
| Troubleshooting | `.tbtag.prob` / `.tbtag.fix`, `.fixbox` |
| Figures | `.fig` (+ size class) > `<img>`, caption `.cap` |
| Inline | `.path` (menu paths/files), `.kbd`, `code.m` |
| Checklist | `.cl` > `<label><input type="checkbox"><span>` |

## Layout

```
docs/documents/<slug>/   one folder per document (index.md + images/)
docs/resource-guide/     equipment pages copied from the XRIML Wiki
docs/stylesheets/        extra.css (Wiki theme), guide.css (document look), archive.css (library UI)
hooks/library.py         builds the library cards from front matter
overrides/document.html  page layout for documents
tools/import_html.py     standalone HTML -> archive document
```
