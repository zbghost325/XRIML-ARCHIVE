"""Writes a self-contained .html copy of every archive document.

The copy has guide.css inlined and images embedded as base64, so it opens
offline exactly like the original standalone guide. It is generated at
build time, so the repo only stores the images once.
"""

import base64
import mimetypes
import os
import re
from html import escape

_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
html{{scroll-behavior:smooth}}
body{{margin:0}}
</style>
</head>
<body class="{body_class}">
{body}
</body>
</html>
"""


def on_page_content(html, page, config, files):
    if page.meta.get("template") != "document.html":
        return html
    name = page.meta.get("source") or os.path.basename(os.path.dirname(page.file.src_uri)) + ".html"
    page.meta["download"] = name

    src_dir = os.path.dirname(page.file.abs_src_path)

    def inline(m):
        path = os.path.join(src_dir, m.group(2))
        if not os.path.isfile(path):
            return m.group(0)
        mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
        with open(path, "rb") as fh:
            data = base64.b64encode(fh.read()).decode("ascii")
        return f'{m.group(1)}data:{mime};base64,{data}"'

    body = re.sub(r'(<img\b[^>]*?\bsrc=")(images/[^"]+)"', inline, html)
    own = page.meta.get("stylesheet")
    css_path = os.path.join(src_dir, own) if own else os.path.join(config["docs_dir"], "stylesheets", "guide.css")
    with open(css_path, encoding="utf-8") as fh:
        css = fh.read()

    out = os.path.join(os.path.dirname(page.file.abs_dest_path), name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(_TEMPLATE.format(
            title=escape(page.title or name), css=css, body=body,
            body_class="xg-doc" if own else "xg-doc xg-guide"))
    return html
