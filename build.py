#!/usr/bin/env python3
"""Static site generator for brodski.name.

Single source of truth: data/*.yaml (projects, skills, talks, education, site)
and pages/*.md (per-direction narrative). Every direction page is a filtered
view of the same data, so a visitor looking for one technology only sees the
work relevant to it.

Usage: python build.py  ->  _site/
"""
from __future__ import annotations

import datetime as _dt
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
DATA, PAGES, TEMPLATES, STATIC, OUT = (
    ROOT / "data", ROOT / "pages", ROOT / "templates", ROOT / "static", ROOT / "_site")
YEAR_NOW = _dt.date.today().year
TIMELINE_START = 1997

# --------------------------------------------------------------------------- load


def load_yaml(name: str):
    with open(DATA / f"{name}.yaml", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


FRONT = re.compile(r"^---[ \t]*\n(.*?)^---[ \t]*\n", re.S | re.M)


def load_page(slug: str) -> dict:
    """pages/<slug>.md: optional YAML front matter (may be empty) + markdown body."""
    path = PAGES / f"{slug}.md"
    if not path.exists():
        return {"body": ""}
    text = path.read_text(encoding="utf-8")
    m = FRONT.match(text)
    meta, body = (yaml.safe_load(m.group(1)) or {}, text[m.end():]) if m else ({}, text)
    meta["body"] = md(body)
    return meta


MD = markdown.Markdown(extensions=["smarty", "sane_lists", "attr_list"])


def md(text: str) -> str:
    MD.reset()
    return MD.convert(text or "")


# ------------------------------------------------------------------ derived views


def projects_for(projects: list[dict], slug: str) -> list[dict]:
    """Projects tagged with a direction, ranked, with the direction's blurb applied."""
    rows = []
    for p in projects:
        tag = (p.get("directions") or {}).get(slug)
        if tag is None:
            continue
        tag = tag or {}
        q = dict(p)
        q["rank"] = tag.get("rank", 9)
        q["blurb"] = tag.get("blurb") or p.get("summary", "")
        q["highlights"] = tag.get("highlights") or p.get("highlights") or []
        rows.append(q)
    rows.sort(key=lambda r: (r["rank"], -r.get("start", 0)))
    return rows


def skills_for(groups: list[dict], slug: str | None) -> list[dict]:
    out = []
    for g in groups:
        items = [s for s in g["skills"] if slug is None or slug in (s.get("directions") or [])]
        if items:
            out.append({"name": g["name"], "skills": items})
    return out


def talks_for(talks: list[dict], slug: str | None) -> list[dict]:
    return [t for t in talks if slug is None or slug in (t.get("directions") or [])]


# --------------------------------------------------------------------- timeline


def timeline_svg(groups: list[dict], limit: int = 28) -> str:
    """Gantt-style SVG of skills over time. Colours come from CSS classes so the
    chart follows the page theme."""
    skills = [s for g in groups for s in g["skills"]]
    skills.sort(key=lambda s: (-(s.get("level", 3)), s["start"]))
    skills = sorted(skills[:limit], key=lambda s: (s["start"], -(s.get("level", 3))))
    if not skills:
        return ""
    label_w, row_h, pad_top, pad_right = 230, 22, 28, 12
    plot_w = 660
    width = label_w + plot_w + pad_right
    height = pad_top + row_h * len(skills) + 8
    span = YEAR_NOW + 1 - TIMELINE_START

    def x(year: float) -> float:
        return label_w + (year - TIMELINE_START) / span * plot_w

    parts = [f'<svg class="timeline" viewBox="0 0 {width} {height}" role="img" '
             f'aria-label="Skills timeline {TIMELINE_START}–{YEAR_NOW}">']
    for y in range(2000, YEAR_NOW + 1, 5):
        parts.append(f'<line class="tl-grid" x1="{x(y):.1f}" y1="{pad_top - 6}" '
                     f'x2="{x(y):.1f}" y2="{height - 6}"/>')
        parts.append(f'<text class="tl-year" x="{x(y):.1f}" y="{pad_top - 10}" '
                     f'text-anchor="middle">{y}</text>')
    for i, s in enumerate(skills):
        y0 = pad_top + i * row_h
        end = s.get("end") or (YEAR_NOW + 1)
        x0, x1 = x(s["start"]), x(end)
        lvl = s.get("level", 3)
        label = s.get("short") or s["name"]
        if len(label) > 34:
            label = label[:33].rstrip(" ,:;") + "…"
        parts.append(f'<text class="tl-label" x="{label_w - 8}" y="{y0 + 15}" '
                     f'text-anchor="end">{esc(label)}</text>')
        parts.append(f'<rect class="tl-bar lvl-{lvl}" x="{x0:.1f}" y="{y0 + 4}" '
                     f'width="{max(x1 - x0, 6):.1f}" height="{row_h - 8}" rx="4">'
                     f'<title>{esc(s["name"])}: {s["start"]}–{s.get("end") or "now"}</title></rect>')
    parts.append("</svg>")
    return "\n".join(parts)


def esc(t: str) -> str:
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# -------------------------------------------------------------------------- build


def main() -> int:
    site = load_yaml("site")
    projects = load_yaml("projects")
    skills = load_yaml("skills")
    talks = load_yaml("talks")
    education = load_yaml("education")

    env = Environment(loader=FileSystemLoader(TEMPLATES),
                      autoescape=select_autoescape(["html"]), trim_blocks=True,
                      lstrip_blocks=True)
    env.filters["md"] = md

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    (OUT / "CNAME").write_text(site["domain"] + "\n")

    cv_dir = STATIC / "cv"
    cv_de = next((f.name for f in cv_dir.glob("*-de.pdf")), None) if cv_dir.exists() else None

    base = dict(site=site, year=YEAR_NOW, cv_de=cv_de)
    urls = []

    def render(template: str, out: Path, **ctx):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(env.get_template(template).render(**base, **ctx), encoding="utf-8")
        rel = out.relative_to(OUT).as_posix().replace("index.html", "")
        urls.append(f"https://{site['domain']}/{rel}")

    # directions
    for d in site["directions"]:
        slug = d["slug"]
        page = load_page(slug)
        cv_pdf = f"cv/boris-brodski-{slug}.pdf"
        groups = skills_for(skills, slug)
        render("direction.html", OUT / slug / "index.html", direction=d, page=page,
               projects=projects_for(projects, slug), skills=groups,
               timeline=timeline_svg(groups, limit=18), talks=talks_for(talks, slug),
               cv_pdf=cv_pdf if (STATIC / cv_pdf).exists() else None,
               related=[o for o in site["directions"] if o["slug"] in (d.get("related") or [])])

    # hub
    featured = [p for p in projects if p.get("featured")]
    featured.sort(key=lambda p: p.get("featured_rank", 9))
    render("index.html", OUT / "index.html", page=load_page("index"), featured=featured)

    # full CV
    chrono = sorted(projects, key=lambda p: (-p.get("start", 0), -(p.get("end") or 9999)))
    cv_pdfs = [(d, f"cv/boris-brodski-{d['slug']}.pdf") for d in site["directions"]
               if (STATIC / f"cv/boris-brodski-{d['slug']}.pdf").exists()]
    render("cv.html", OUT / "cv" / "index.html", page=load_page("cv"), projects=chrono,
           skills=skills_for(skills, None), timeline=timeline_svg(skills_for(skills, None), 40),
           talks=talks_for(talks, None), education=education, cv_pdfs=cv_pdfs)

    render("404.html", OUT / "404.html")
    urls.pop()  # 404 is not a sitemap entry

    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: https://{site['domain']}/sitemap.xml\n")
    print(f"built {len(urls)} pages -> {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
