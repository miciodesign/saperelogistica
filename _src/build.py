#!/usr/bin/env python3
"""Generatore del sito saperelogistica.it.

Legge i file Markdown in _src/content, applica i template in _src/templates
e scrive l'HTML statico nella radice del repository (che Hostinger pubblica).

Contenuti:
  _src/content/glossario/<slug>.md   voci del glossario (una per file)
  _src/content/rassegna/AAAA-MM-GG-<slug>.md   uscite della rassegna settimanale
  _src/content/corso/NN-<slug>.md   moduli del corso di aggiornamento
  _src/content/pagine/<slug>.md     pagine fisse (chi siamo, metodo, sponsor, correzioni...)

Uso:  python3 _src/build.py
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
CONTENT = SRC / "content"
TEMPLATES = SRC / "templates"
STATIC = SRC / "static"

CONFIG = json.loads((SRC / "config.json").read_text(encoding="utf-8"))
SITE_URL = CONFIG["site_url"].rstrip("/")
SITE_HOST = re.sub(r"^https?://", "", SITE_URL)

MD = markdown.Markdown(
    extensions=["tables", "toc", "attr_list", "sane_lists", "md_in_html"],
    extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}},
    output_format="html5",
)

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

ERRORS: list[str] = []


# ---------------------------------------------------------------- utilities
def parse_front_matter(text: str) -> tuple[dict, str]:
    """Front matter minimale: righe `chiave: valore` fra due `---`.
    Le liste si scrivono fra parentesi quadre: related: [slug-a, slug-b];
    un elemento che contiene virgole va fra doppi apici: lezioni: ["a, b", c]."""
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    meta: dict = {}
    for line in fm.strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            # elementi separati da virgola; un elemento che contiene virgole va fra doppi apici
            value = [(q or v).strip() for q, v in re.findall(r'"([^"]*)"|([^,]+)', value[1:-1]) if (q or v).strip()]
        meta[key.strip()] = value
    return meta, body.lstrip("\n")


def render_markdown(body: str) -> tuple[str, str]:
    MD.reset()
    html_out = MD.convert(body)
    toc = MD.toc if getattr(MD, "toc_tokens", None) else ""
    return html_out, toc


def mark_external_links(html_out: str) -> str:
    """I link esterni si aprono in una nuova scheda. Nessun rel="sponsored":
    il sito non usa link di affiliazione. I contenuti sponsorizzati, se mai ci
    saranno, vanno marcati a mano nel testo con l'attributo {: rel="sponsored"}."""
    return re.sub(
        r'<a href="(https?://(?!' + re.escape(SITE_HOST) + r')[^"]+)"(?![^>]*\brel=)',
        r'<a href="\1" rel="noopener" target="_blank"',
        html_out,
    )


def reading_time(body: str) -> int:
    words = len(re.findall(r"\w+", body))
    return max(1, round(words / 200))


def iso(d: str) -> str:
    return dt.date.fromisoformat(d).isoformat()


MONTHS = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
          "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def human_date(d: str) -> str:
    date = dt.date.fromisoformat(d)
    return f"{date.day} {MONTHS[date.month - 1]} {date.year}"


def sort_key(term: str) -> str:
    """Ordinamento alfabetico senza accenti e senza articoli iniziali."""
    t = term.lower()
    for ch, plain in (("à", "a"), ("è", "e"), ("é", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u")):
        t = t.replace(ch, plain)
    return t


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def clean_output() -> None:
    """Rimuove l'HTML generato in precedenza, lasciando sorgenti e git."""
    keep = {"_src", ".git", ".gitignore", "README.md", ".htaccess", "CNAME"}
    for item in ROOT.iterdir():
        if item.name in keep:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


# ---------------------------------------------------------------- content
def load_terms(areas: list[dict]) -> list[dict]:
    terms = []
    area_slugs = {a["slug"] for a in areas}
    for path in sorted((CONTENT / "glossario").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if meta.get("draft") == "true":
            continue
        for key in ("term", "slug", "area", "description"):
            if not meta.get(key):
                ERRORS.append(f"{path.name}: manca '{key}' nel front matter")
        if meta.get("area") not in area_slugs:
            ERRORS.append(f"{path.name}: area '{meta.get('area')}' non esiste in config.json")
        if meta.get("slug") != path.stem:
            ERRORS.append(f"{path.name}: lo slug nel front matter deve coincidere col nome del file")
        if 'class="fonte"' not in body:
            ERRORS.append(f"{path.name}: manca il blocco <div class=\"fonte\"> in fondo alla voce; "
                          "una voce senza fonte non si pubblica")
        html_body, _ = render_markdown(body)
        html_body = mark_external_links(html_body)
        term = {
            **meta,
            "body": html_body,
            "url": f"/glossario/{meta.get('slug')}/",
            "related": meta.get("related", []) if isinstance(meta.get("related"), list) else [],
            "updated_iso": iso(meta["updated"]) if meta.get("updated") else None,
            "updated_human": human_date(meta["updated"]) if meta.get("updated") else None,
            "letter": sort_key(meta.get("term", "?"))[0].upper(),
        }
        terms.append(term)
    terms.sort(key=lambda t: sort_key(t["term"]))
    by_slug = {t["slug"]: t for t in terms}
    for t in terms:
        resolved = []
        for r in t["related"]:
            if r in by_slug:
                resolved.append(by_slug[r])
            else:
                ERRORS.append(f"glossario/{t['slug']}.md: voce collegata '{r}' inesistente")
        t["related_obj"] = resolved
    return terms


def load_rassegna() -> list[dict]:
    items = []
    for path in sorted((CONTENT / "rassegna").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if meta.get("draft") == "true":
            continue
        html_body, toc = render_markdown(body)
        items.append({
            **meta,
            "body": mark_external_links(html_body),
            "toc": toc,
            "url": f"/rassegna/{meta['slug']}/",
            "date_iso": iso(meta["date"]),
            "date_human": human_date(meta["date"]),
            "updated_iso": iso(meta.get("updated", meta["date"])),
            "updated_human": human_date(meta.get("updated", meta["date"])),
            "minutes": reading_time(body),
        })
    items.sort(key=lambda a: a["date_iso"], reverse=True)
    return items


def load_corso() -> list[dict]:
    mods = []
    for path in sorted((CONTENT / "corso").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        html_body, toc = render_markdown(body)
        mods.append({
            **meta,
            "body": mark_external_links(html_body),
            "toc": toc,
            "url": f"/corso/{meta['slug']}/",
            "order": int(meta.get("order", 0)),
            "lezioni": meta.get("lezioni", []) if isinstance(meta.get("lezioni"), list) else [],
        })
    mods.sort(key=lambda m: m["order"])
    return mods


def load_pages() -> list[dict]:
    pages = []
    for path in sorted((CONTENT / "pagine").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        html_body, toc = render_markdown(body)
        pages.append({**meta, "body": mark_external_links(html_body), "toc": toc,
                      "url": f"/{meta['slug']}/",
                      "updated_human": human_date(meta["updated"]) if meta.get("updated") else None})
    return pages


# ---------------------------------------------------------------- build
def check_internal_links() -> None:
    """Ogni link interno deve puntare a una pagina generata."""
    generated = set()
    for p in ROOT.rglob("index.html"):
        if "_src" in p.parts or ".git" in p.parts:
            continue
        rel = p.relative_to(ROOT).parent.as_posix()
        generated.add("/" if rel == "." else f"/{rel}/")
    for p in ROOT.rglob("*"):
        if p.is_file() and "_src" not in p.parts and ".git" not in p.parts:
            generated.add("/" + p.relative_to(ROOT).as_posix())
    for p in ROOT.rglob("*.html"):
        if "_src" in p.parts or ".git" in p.parts:
            continue
        for m in re.finditer(r'href="(/[^"#?]*)', p.read_text(encoding="utf-8")):
            target = m.group(1)
            if target not in generated:
                ERRORS.append(f"{p.relative_to(ROOT)}: link interno rotto -> {target}")


def build() -> None:
    clean_output()
    areas = [{**a, "url": f"/glossario/{a['slug']}/"} for a in CONFIG["aree"]]
    terms = load_terms(areas)
    for a in areas:
        a["terms"] = [t for t in terms if t["area"] == a["slug"]]
        for t in a["terms"]:
            t["area_obj"] = a
    rassegna = load_rassegna()
    corso = load_corso()
    pages = load_pages()
    letters = sorted({t["letter"] for t in terms})

    base_ctx = {
        "site": CONFIG,
        "site_url": SITE_URL,
        "areas": areas,
        "corso_cfg": CONFIG["corso"],
        "rassegna_cfg": CONFIG["rassegna"],
        "n_terms": len(terms),
        "year": dt.date.today().year,
        "build_date": dt.date.today().isoformat(),
    }

    # assets
    shutil.copytree(STATIC, ROOT / "assets")
    for v in STATIC.glob("google*.html"):
        shutil.copy(v, ROOT / v.name)

    # home
    write(ROOT / "index.html", env.get_template("home.html").render(
        **base_ctx, terms=terms, rassegna=rassegna, corso=corso, page_url="/",
        title=CONFIG["title"], description=CONFIG["description"]))

    # glossario
    write(ROOT / "glossario" / "index.html", env.get_template("glossario.html").render(
        **base_ctx, terms=terms, letters=letters, page_url="/glossario/",
        title=f"Glossario della logistica · {CONFIG['name']}",
        description=f"{len(terms)} termini della logistica spiegati in italiano, per area e in ordine alfabetico, con la fonte ufficiale accanto a ogni definizione."))
    for a in areas:
        write(ROOT / "glossario" / a["slug"] / "index.html", env.get_template("area.html").render(
            **base_ctx, area=a, page_url=a["url"],
            title=f"Glossario: {a['name']} · {CONFIG['name']}", description=a["intro"]))
    for t in terms:
        write(ROOT / "glossario" / t["slug"] / "index.html", env.get_template("term.html").render(
            **base_ctx, t=t, page_url=t["url"],
            title=f"{t['term']}: cos'è e come si usa · {CONFIG['name']}", description=t["description"]))

    # rassegna
    write(ROOT / "rassegna" / "index.html", env.get_template("rassegna.html").render(
        **base_ctx, rassegna=rassegna, page_url="/rassegna/",
        title=f"Rassegna settimanale · {CONFIG['name']}", description=CONFIG["rassegna"]["short"] + "."))
    for i, a in enumerate(rassegna):
        write(ROOT / "rassegna" / a["slug"] / "index.html", env.get_template("rassegna-uscita.html").render(
            **base_ctx, a=a, prev=rassegna[i + 1] if i + 1 < len(rassegna) else None,
            nxt=rassegna[i - 1] if i > 0 else None, page_url=a["url"],
            title=f"{a['title']} · {CONFIG['name']}", description=a["description"]))

    # corso
    write(ROOT / "corso" / "index.html", env.get_template("corso.html").render(
        **base_ctx, corso=corso, page_url="/corso/",
        title=f"{CONFIG['corso']['name']} · {CONFIG['name']}",
        description="Corso di aggiornamento, non di certificazione: dodici moduli su regole, strumenti e indicatori della logistica, con fonti ufficiali e esercizi su casi reali."))
    for i, m in enumerate(corso):
        write(ROOT / "corso" / m["slug"] / "index.html", env.get_template("modulo.html").render(
            **base_ctx, m=m, corso=corso, prev=corso[i - 1] if i > 0 else None,
            nxt=corso[i + 1] if i + 1 < len(corso) else None, page_url=m["url"],
            title=f"Modulo {m['order']}: {m['title']} · {CONFIG['name']}", description=m["description"]))

    # pagine fisse
    for p in pages:
        write(ROOT / p["slug"] / "index.html", env.get_template("page.html").render(
            **base_ctx, p=p, page_url=p["url"],
            title=f"{p['title']} · {CONFIG['name']}", description=p.get("description", "")))

    # 404
    write(ROOT / "404.html", env.get_template("404.html").render(
        **base_ctx, page_url="/404.html", title=f"Pagina non trovata · {CONFIG['name']}", description=""))

    # sitemap, robots, feed
    urls = ["/", "/glossario/", "/rassegna/", "/corso/"]
    urls += [a["url"] for a in areas] + [t["url"] for t in terms] + [a["url"] for a in rassegna]
    urls += [m["url"] for m in corso] + [p["url"] for p in pages]
    lastmod = {t["url"]: t["updated_iso"] for t in terms if t["updated_iso"]}
    lastmod.update({a["url"]: a["updated_iso"] for a in rassegna})
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{SITE_URL}{u}</loc><lastmod>{lastmod.get(u, base_ctx['build_date'])}</lastmod></url>")
    sitemap.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(sitemap))
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_src/\nSitemap: {SITE_URL}/sitemap.xml\n")

    feed = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<rss version="2.0"><channel>',
            f"<title>{html.escape(CONFIG['name'])} · Rassegna settimanale</title>",
            f"<link>{SITE_URL}/rassegna/</link>",
            f"<description>{html.escape(CONFIG['rassegna']['short'])}</description>",
            "<language>it-it</language>"]
    for a in rassegna[:20]:
        feed.append("<item>"
                    f"<title>{html.escape(a['title'])}</title>"
                    f"<link>{SITE_URL}{a['url']}</link>"
                    f"<guid>{SITE_URL}{a['url']}</guid>"
                    f"<pubDate>{dt.datetime.fromisoformat(a['date_iso']).strftime('%a, %d %b %Y 08:00:00 +0100')}</pubDate>"
                    f"<description>{html.escape(a['description'])}</description>"
                    "</item>")
    feed.append("</channel></rss>")
    write(ROOT / "feed.xml", "\n".join(feed))

    write(ROOT / ".htaccess", "\n".join([
        "RedirectMatch 404 ^/_src/",
        "ErrorDocument 404 /404.html",
        "AddDefaultCharset UTF-8",
        "<IfModule mod_deflate.c>",
        "  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/xml",
        "</IfModule>",
        "<IfModule mod_expires.c>",
        "  ExpiresActive On",
        "  ExpiresByType text/css \"access plus 7 days\"",
        "  ExpiresByType image/svg+xml \"access plus 30 days\"",
        "  ExpiresByType image/png \"access plus 30 days\"",
        "  ExpiresByType image/webp \"access plus 30 days\"",
        "</IfModule>",
        "",
    ]))

    check_internal_links()
    if ERRORS:
        print("ERRORI:", file=sys.stderr)
        for e in ERRORS:
            print(" -", e, file=sys.stderr)
        sys.exit(1)
    print(f"Sito generato: {len(terms)} voci di glossario, {len(rassegna)} uscite della rassegna, "
          f"{len(corso)} moduli del corso, {len(pages)} pagine.")


if __name__ == "__main__":
    build()
