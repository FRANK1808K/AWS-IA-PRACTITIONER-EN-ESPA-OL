"""Valida los enlaces relativos y las anclas de los archivos Markdown del repositorio.

Uso: python .github/scripts/check_links.py
Sale con código 1 si encuentra enlaces a archivos inexistentes o anclas que no
corresponden a ningún encabezado (según el algoritmo de slugs de GitHub).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def github_slug(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)          # quitar code spans
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # quitar enlaces
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)               # conservar letras (incl. acentos), dígitos, _, - y espacios
    return text.replace(" ", "-")


def strip_fences(lines):
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield line


def anchors_for(path: Path) -> set:
    seen, anchors = {}, set()
    for line in strip_fences(path.read_text(encoding="utf-8").splitlines()):
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = github_slug(match.group(2))
        count = seen.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1
    return anchors


def main() -> int:
    errors = []
    for md in sorted(ROOT.rglob("*.md")):
        if "node_modules" in md.parts:
            continue
        body = "\n".join(strip_fences(md.read_text(encoding="utf-8").splitlines()))
        body = re.sub(r"`[^`\n]*`", "", body)  # ignorar enlaces dentro de code spans
        for target in LINK_RE.findall(body):
            if re.match(r"^[a-z]+:", target):  # http:, https:, mailto:
                continue
            file_part, _, anchor = target.partition("#")
            dest = (md.parent / file_part).resolve() if file_part else md
            rel = md.relative_to(ROOT)
            if not dest.exists():
                errors.append(f"{rel}: archivo inexistente -> {target}")
                continue
            if anchor and dest.is_file() and dest.suffix == ".md" and anchor not in anchors_for(dest):
                errors.append(f"{rel}: ancla inexistente -> {target}")

    for error in errors:
        print(error)
    print(f"{len(errors)} error(es) de enlaces." if errors else "Todos los enlaces relativos son válidos.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
