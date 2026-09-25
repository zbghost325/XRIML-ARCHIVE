"""Builds the document library from front matter.

Every page under docs/documents/ is collected; any page containing
<!-- archive:library --> gets the filterable card grid in its place.
Add a document folder and it shows up here - no nav edits needed.
"""

import datetime
from html import escape

from mkdocs.utils import get_relative_url
from mkdocs.utils.meta import get_data

MARKER = "<!-- archive:library -->"
_docs = []


def on_files(files, config):
    _docs.clear()
    for f in files.documentation_pages():
        if not f.src_uri.startswith("documents/"):
            continue
        with open(f.abs_src_path, encoding="utf-8") as fh:
            _, meta = get_data(fh.read())
        _docs.append({**meta, "url": f.url})
    _docs.sort(key=lambda d: str(d.get("updated", "")), reverse=True)


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown
    return markdown.replace(MARKER, _render(page))


def _fmt_date(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.strftime("%m-%d-%Y"), value.isoformat()
    return str(value or ""), str(value or "")


def _render(page):
    categories = sorted({d.get("category", "Other") for d in _docs})
    tags = sorted({t for d in _docs for t in d.get("tags") or []}, key=str.lower)
    total_pages = sum(int(d.get("pages") or 0) for d in _docs)

    chips = ['<button type="button" class="xa-chip is-on" data-cat="">All</button>']
    chips += [f'<button type="button" class="xa-chip" data-cat="{escape(c)}">{escape(c)}</button>'
              for c in categories]
    tag_chips = [f'<button type="button" class="xa-tag" data-tag="{escape(t)}">{escape(t)}</button>'
                 for t in tags]

    cards = []
    for d in _docs:
        title = d.get("title", "Untitled")
        cat = d.get("category", "Other")
        dtags = d.get("tags") or []
        shown, iso = _fmt_date(d.get("updated"))
        haystack = " ".join([title, cat, d.get("description", ""), d.get("software", ""), *dtags]).lower()
        href = get_relative_url(d["url"], page.url)
        meta = [f"<span>Updated {escape(shown)}</span>"] if shown else []
        if d.get("pages"):
            n = int(d["pages"])
            meta.append(f"<span>{n} page{'s' if n != 1 else ''}</span>")
        cards.append(f"""
<a class="xa-card" href="{escape(href)}" data-cat="{escape(cat)}" data-tags="{escape('|'.join(dtags))}"
   data-text="{escape(haystack)}" data-title="{escape(title.lower())}" data-updated="{escape(iso)}">
  <span class="xa-card__band">{escape(d.get("software", "") or cat)}</span>
  <span class="xa-card__body">
    <span class="xa-card__cat">{escape(cat)}</span>
    <span class="xa-card__title">{escape(title)}</span>
    <span class="xa-card__rule"></span>
    <span class="xa-card__desc">{escape(d.get("description", ""))}</span>
    <span class="xa-card__tags">{"".join(f"<span>{escape(t)}</span>" for t in dtags)}</span>
  </span>
  <span class="xa-card__foot">{"".join(meta)}</span>
</a>""")

    return f"""
<div class="xa-library" markdown="0">
  <div class="xa-stats">
    <span><b>{len(_docs)}</b> document{"s" if len(_docs) != 1 else ""}</span>
    <span><b>{total_pages}</b> pages</span>
    <span><b>{len(categories)}</b> collection{"s" if len(categories) != 1 else ""}</span>
  </div>
  <div class="xa-controls">
    <div class="xa-filter">
      <input type="search" data-xa-filter placeholder="Filter documents by title, tag, or software…" aria-label="Filter documents">
      <select data-xa-sort aria-label="Sort documents">
        <option value="updated">Recently updated</option>
        <option value="title">Title A–Z</option>
      </select>
    </div>
    <div class="xa-chips" role="group" aria-label="Collections">{"".join(chips)}</div>
    <div class="xa-tags" role="group" aria-label="Tags">{"".join(tag_chips)}</div>
  </div>
  <p class="xa-count" data-xa-count></p>
  <div class="xa-grid" data-xa-grid>{"".join(cards)}</div>
  <p class="xa-empty" data-xa-empty hidden>No documents match. Try the full-text search above — it searches inside every page.</p>
</div>
"""
