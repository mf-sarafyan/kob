from __future__ import annotations
import json
import re
from typing import Any


def _quote(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def _needs_quote(s: str) -> bool:
    return bool(re.search(r"[:\n\r\t\[\]{}#,>&*!|\"'%@`]", s)) or s.strip() != s


def dump_yaml(frontmatter: dict[str, Any]) -> str:
    try:
        import yaml  # type: ignore
        return yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    except Exception:
        lines: list[str] = []
        for k, v in frontmatter.items():
            if v is None:
                lines.append(f"{k}:")
            elif isinstance(v, bool):
                lines.append(f"{k}: {'true' if v else 'false'}")
            elif isinstance(v, (int, float)):
                lines.append(f"{k}: {v}")
            elif isinstance(v, str):
                lines.append(f"{k}: {_quote(v) if _needs_quote(v) else v}")
            elif isinstance(v, list):
                items = []
                for it in v:
                    if isinstance(it, str):
                        items.append(_quote(it) if _needs_quote(it) else it)
                    else:
                        items.append(str(it))
                lines.append(f"{k}: [{', '.join(items)}]")
            else:
                lines.append(f"{k}: {_quote(str(v))}")
        return "\n".join(lines).strip()


def wrap_frontmatter(frontmatter: dict[str, Any]) -> str:
    return f"---\n{dump_yaml(frontmatter)}\n---"

