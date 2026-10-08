"""Genera simulator/index.html a partir de los simulacros en Markdown.

Uso: python simulator/build.py
Lee practice-questions/mock-exam-*.md, extrae preguntas, opciones y clave de
respuestas, y las inserta en simulator/template.html.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMS = [
    ("sim01", "Simulacro 01", ROOT / "practice-questions" / "mock-exam-01.md"),
    ("sim02", "Simulacro 02", ROOT / "practice-questions" / "mock-exam-02.md"),
]
QUESTION_RE = re.compile(r"^\*\*(\d+)\.\*\*\s+(.*)$")
OPTION_RE = re.compile(r"^- ([A-E])\. (.*)$")
KEY_RE = re.compile(r"^\| (\d+) \| ([A-E](?:, [A-E])*) \| (D\d)( 🆕)? \| (.*) \|$")


def inline(text: str) -> str:
    """Escapa HTML y convierte **negrita** y `código` de Markdown."""
    text = html.escape(text.replace("🆕", "").strip(), quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", text)


def parse(exam_id: str, path: Path) -> list:
    questions, keys, current = {}, {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if m := QUESTION_RE.match(line):
            current = int(m.group(1))
            questions[current] = {"text": inline(m.group(2)), "options": []}
        elif (m := OPTION_RE.match(line)) and current is not None:
            questions[current]["options"].append({"id": m.group(1), "text": inline(m.group(2))})
        elif m := KEY_RE.match(line):
            keys[int(m.group(1))] = {
                "answer": m.group(2).split(", "),
                "domain": m.group(3),
                "new": bool(m.group(4)),
                "why": inline(m.group(5)),
            }
    if sorted(questions) != sorted(keys) or not questions:
        sys.exit(f"{path.name}: preguntas {len(questions)} y clave {len(keys)} no coinciden")
    out = []
    for n in sorted(questions):
        q = {**questions[n], **keys[n], "id": f"{exam_id}-{n}", "n": n}
        if not set(q["answer"]) <= {o["id"] for o in q["options"]}:
            sys.exit(f"{path.name} Q{n}: la respuesta no está entre las opciones")
        out.append(q)
    return out


def main() -> int:
    data = {
        "exams": [
            {"id": exam_id, "name": name, "questions": parse(exam_id, path)}
            for exam_id, name, path in EXAMS
        ]
    }
    template = (ROOT / "simulator" / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    output = template.replace("/*__DATA__*/null", payload)
    (ROOT / "simulator" / "index.html").write_text(output, encoding="utf-8")
    total = sum(len(e["questions"]) for e in data["exams"])
    print(f"simulator/index.html generado con {total} preguntas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
