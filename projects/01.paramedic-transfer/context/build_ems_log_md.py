# -*- coding: utf-8 -*-
"""ems_log_source.tsv → ems-log-field-hierarchy.md (key → value → subvalue, 중복 병합)"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


def parse_line(line: str) -> tuple[str, str, str | None]:
    line = line.strip("\ufeff\n\r")
    if not line.strip():
        return ("", "", None)
    parts = re.split(r"\t+", line)
    if len(parts) >= 3:
        k, v, s = parts[0].strip(), parts[1].strip(), parts[2].strip()
        return (k, v, s or None)
    if len(parts) == 2:
        k, v = parts[0].strip(), parts[1].strip()
        return (k, v, None)
    if len(parts) == 1:
        return (parts[0].strip(), "", None)
    return ("", "", None)


KEY_ORDER = [
    "출동정보",
    "구급출동",
    "신고자",
    "환자인적사항",
    "보호자등",
    "환자발생위치",
    "환자발생장소",
    "환자증상",
    "환자발생유형",
    "환자평가",
    "응급처치",
    "의료지도",
    "의료지도기관",
    "의료지도의사",
    "의료지도내용",
    "환자이송",
    "공동대응",
    "환자희망이송병원",
    "미이송",
    "출동인원",
    "장애요인",
    "일련번호",
    "재난번호",
    "연계번호",
    "추가사항(ETYPE)",
]


def _key_sort(k: str) -> tuple[int, str]:
    if k in KEY_ORDER:
        return (KEY_ORDER.index(k), k)
    return (len(KEY_ORDER), k)


def main() -> None:
    base = Path(__file__).resolve().parent
    src = base / "ems_log_source.tsv"
    out = base / "ems-log-field-hierarchy.md"

    raw = src.read_text(encoding="utf-8")
    tree: dict[str, dict[str, set[str | None]]] = defaultdict(lambda: defaultdict(set))
    empty_root_marked: set[str] = set()

    for line in raw.splitlines():
        k, v, s = parse_line(line)
        if not k and not v:
            continue
        if not v and not s:
            empty_root_marked.add(k)
            continue
        tree[k][v].add(s)

    # key만 있고 하위 행이 전혀 없을 때만「직접 입력」플레이스홀더
    for k in empty_root_marked:
        if not tree[k]:
            tree[k]["_(직접 입력)_"].add(None)

    lines: list[str] = [
        "# 구급일지 필드 계층 (Key → Value → Subvalue)",
        "",
        "소방·구급 활동일지 등에 쓰이는 **3단계 필드 경로** 참조용이다. "
        "`subvalue`가 비면 **자유 입력·시각·수치** 등 값 타입은 스펙·구현에서 정의한다.",
        "원본 나열(TSV)은 `ems_log_source.tsv`에 두고, 본 문서는 **동일 key·value·subvalue 조합을 병합**했다.",
        "제공해 주신 목록의 **완전 중복 행**(동일 key·value·subvalue 반복)은 TSV 정리 시 제거했다.",
        "",
        "---",
        "",
    ]

    for key in sorted(tree.keys(), key=_key_sort):
        if not key:
            continue
        lines.append(f"## `{key}`")
        lines.append("")
        def _val_sort(x: str) -> tuple[int, str]:
            if x == "_(직접 입력)_":
                return (1, x)
            return (0, x)

        for val in sorted(tree[key].keys(), key=_val_sort):
            if val == "_(직접 입력)_":
                lines.append("- **(직접 입력)** — 원본 스키마에서 **key만** 있고 value/subvalue가 비어 있음")
                lines.append("")
                continue
            raw_subs = tree[key][val]
            has_free = None in raw_subs
            subs = {x for x in raw_subs if x}
            if subs:
                lines.append(f"### `{val}`" if val else "### _(값 없음)_")
                lines.append("")
                if has_free:
                    lines.append("- _(직접 값·시간·수치 등)_")
                for sub in sorted(subs, key=str):
                    lines.append(f"- `{sub}`")
                lines.append("")
            elif val:
                lines.append(f"- **`{val}`** — 직접 값(또는 시각/거리 등) 또는 플래그")
                lines.append("")
            elif has_free:
                lines.append("- _(하위 항목만 또는 자유값)_")
                lines.append("")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", out, "keys:", len(tree))


if __name__ == "__main__":
    main()
