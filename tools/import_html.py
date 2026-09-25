#!/usr/bin/env python3
"""Import a standalone XRIML guide (.html) into the archive.

    python3 tools/import_html.py ~/Downloads/my-guide.html \
        --slug quest3-mr-meta-sdk \
        --category "Quick Start Guides" \
        --tags "Unity, Meta Quest 3, Mixed Reality"

What it does:
  * pulls embedded base64 images out into docs/documents/<slug>/images/
  * drops the <head>/<style> (the shared look lives in stylesheets/guide.css)
  * gives every heading an id so search results jump straight to the step
  * turns the cover-page index ("- Page 4") into clickable links
  * writes docs/documents/<slug>/index.md with front matter the library reads

Re-running on the same slug overwrites that document. Only the standard
library is used, so no extra installs are needed.
"""

import argparse
import base64
import hashlib
import html
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "documents"

DATA_IMG = re.compile(r'data:image/(png|jpe?g|gif|webp|svg\+xml);base64,([A-Za-z0-9+/=\s]+)')
HEADING = re.compile(r'<(h[1-4])\b([^>]*)>(.*?)</\1>', re.S)


def slugify(text):
    text = re.sub(r'<[^>]+>', '', html.unescape(text)).lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-') or 'section'


def plain(fragment):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', fragment))).strip()


def first(pattern, text):
    m = re.search(pattern, text, re.S)
    return plain(m.group(1)) if m else ''


def yaml_str(value):
    return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"') + '"'


def extract_images(body, img_dir):
    img_dir.mkdir(parents=True, exist_ok=True)
    for old in img_dir.iterdir():
        old.unlink()
    seen = {}

    def save(m):
        kind, data = m.group(1), re.sub(r'\s+', '', m.group(2))
        raw = base64.b64decode(data)
        digest = hashlib.sha1(raw).hexdigest()
        if digest not in seen:
            ext = {'jpeg': 'jpg', 'svg+xml': 'svg'}.get(kind, kind)
            name = f'img-{len(seen) + 1:03d}.{ext}'
            (img_dir / name).write_bytes(raw)
            seen[digest] = name
        return 'images/' + seen[digest]

    return DATA_IMG.sub(save, body), len(seen)


def add_heading_ids(body):
    used = set()

    def unique(base):
        slug, n = base, 2
        while slug in used:
            slug, n = f'{base}-{n}', n + 1
        used.add(slug)
        return slug

    # Numbered steps: <div class="bignum">12</div><h3>... -> id="step-12"
    def step(m):
        return f'{m.group(1)}<h3 id="{unique("step-" + m.group(2))}"'
    body = re.sub(r'(<div class="bignum[^"]*">\s*(\d+)\s*</div>\s*)<h3(?![^>]*\bid=)', step, body)

    def other(m):
        tag, attrs, inner = m.groups()
        if re.search(r'\bid=', attrs):
            used.add(re.search(r'\bid="([^"]+)"', attrs).group(1))
            return m.group(0)
        return f'<{tag} id="{unique(slugify(inner))}"{attrs}>{inner}</{tag}>'
    return HEADING.sub(other, body)


def link_index(body):
    # <div class="t1">...<span class="pg">- Page 4</span></div> -> <a class="t1" href="#p4">
    return re.sub(
        r'<div class="t1">(.*?)<span class="pg">(.*?Page\s*(\d+).*?)</span>\s*</div>',
        r'<a class="t1" href="#p\3">\1<span class="pg">\2</span></a>',
        body, flags=re.S)


def parse_date(text):
    for fmt in ('%m/%d/%Y', '%m-%d-%Y', '%Y-%m-%d'):
        try:
            return datetime.strptime(text.strip(), fmt).date().isoformat()
        except ValueError:
            pass
    return ''


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('source', type=Path)
    ap.add_argument('--slug', required=True, help='folder/URL name, e.g. quest3-mr-meta-sdk')
    ap.add_argument('--category', default='Quick Start Guides')
    ap.add_argument('--tags', default='', help='comma-separated')
    ap.add_argument('--title', help='defaults to the <title> of the HTML file')
    ap.add_argument('--description', help='defaults to the cover page "Additional Notes"')
    args = ap.parse_args()

    src = args.source.expanduser().read_text(encoding='utf-8')
    out_dir = DOCS / args.slug

    cover = re.search(r'<h1 class="cover-title">(.*?)</h1>', src, re.S)
    cover = plain(re.sub(r'<br\s*/?>', ' — ', cover.group(1))) if cover else ''
    title = args.title or cover or first(r'<title>(.*?)</title>', src) or args.slug
    title = re.sub(r'\s*[-–|]\s*XRIML Guide\s*$', '', title)
    description = args.description or first(
        r'Additional Notes:\s*</div>\s*<div class="val">(.*?)</div>', src)
    software = first(r'<span class="uver">(.*?)</span>', src)
    version = first(r'XRIML Versioning:\s*</div>\s*<div class="val">(.*?)</div>', src)
    updated = parse_date(version) if version else ''

    body = re.sub(r'<!DOCTYPE[^>]*>|</?(html|head|body)\b[^>]*>|<meta\b[^>]*>|<link\b[^>]*>', '', src, flags=re.I)
    body = re.sub(r'<(title|style|script)\b.*?</\1>', '', body, flags=re.S | re.I)
    body, n_images = extract_images(body, out_dir / 'images')
    body = add_heading_ids(body)
    body = link_index(body)
    body = body.strip()
    pages = len(re.findall(r'<section class="page"', body))

    tags = [t.strip() for t in args.tags.split(',') if t.strip()]
    fm = ['---', f'title: {yaml_str(title)}', f'description: {yaml_str(description)}',
          'template: document.html', f'category: {yaml_str(args.category)}']
    if software:
        fm.append(f'software: {yaml_str(software)}')
    if version:
        fm.append(f'version: {yaml_str(version)}')
    if updated:
        fm.append(f'updated: {updated}')
    fm.append(f'pages: {pages}')
    fm.append(f'source: {yaml_str(args.source.name)}')
    fm.append('tags:' + ('' if tags else ' []'))
    fm += [f'  - {yaml_str(t)}' for t in tags]
    fm += ['hide:', '  - navigation', '  - toc', '---', '']

    (out_dir / 'index.md').write_text('\n'.join(fm) + body + '\n', encoding='utf-8')
    print(f'Wrote {out_dir.relative_to(ROOT)}/index.md  ({pages} pages, {n_images} images)')
    used = {c for attr in re.findall(r'class="([^"]+)"', body) for c in attr.split()}
    unknown = sorted(used - known_classes())
    if unknown:
        print('Note: these classes are not styled in guide.css yet:', ', '.join(unknown), file=sys.stderr)


def known_classes():
    css = (ROOT / 'docs' / 'stylesheets' / 'guide.css').read_text(encoding='utf-8')
    return set(re.findall(r'\.([a-zA-Z][\w-]*)', css))


if __name__ == '__main__':
    main()
