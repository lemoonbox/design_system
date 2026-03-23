# PAT-001 — 케이스·동기화 헤더

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 진행 중 케이스의 **가독 라벨·시각**과 **동기화 상태 칩**을 좌우 배치로 반복 표시

---

## Figma 실행 지시

### 외부 frame
```
create_frame
  name: "PAT-001-케이스-동기화-헤더"
  parentId: {부모 프레임 nodeId}
  x: {nextX}, y: 0
  width: 390, height: 84
  fillColor: background — color.gray.25 (r:0.992 g:0.992 b:0.992 a:1)
```
> 한 줄만 쓰는 화면은 높이 `64`로 줄여도 됨 (`patterns-prompt.md`와 동일).

```
set_auto_layout
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: SPACE_BETWEEN
  counterAxisAlignItems: CENTER
  paddingTop: 16, paddingBottom: 16
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 12
```
> shadow 없음 — 전체 폭 헤더는 배경색(gray.25 vs gray.50 surface)으로 구역 구분

---

### 왼쪽 텍스트 그룹
```
create_frame
  name: "헤더-텍스트-그룹"
  parentId: PAT-001 frame nodeId
  fillColor: transparent (a:0)  ← 부모 gray.25와 이중 배경 방지
set_auto_layout
  layoutMode: VERTICAL
  itemSpacing: 4
  counterAxisAlignItems: MIN
```

**케이스 라벨 (body-strong)**
```
create_text
  name: "케이스-라벨"
  parentId: 헤더-텍스트-그룹 nodeId
  text: "오늘 14:32 출동"
  fontSize: 18, fontWeight: 500
  fontColor: text-primary — color.gray.900 (r:0.094 g:0.114 b:0.153 a:1)
set_line_height    → lineHeight: 28, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

**보조 캡션 (caption)**
```
create_text
  name: "케이스-보조"
  parentId: 헤더-텍스트-그룹 nodeId
  text: "케이스 · 응급 이송 조율"
  fontSize: 14, fontWeight: 400
  fontColor: text-secondary — color.gray.500 (r:0.443 g:0.463 b:0.502 a:1)
set_line_height    → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

### 오른쪽 동기화 상태 칩
```
create_frame
  name: "동기화-상태"
  parentId: PAT-001 frame nodeId
  fillColor: surface — color.gray.50 (r:0.980 g:0.980 b:0.980 a:1)
set_corner_radius → radius: 8
set_auto_layout
  layoutMode: HORIZONTAL
  counterAxisAlignItems: CENTER
  paddingTop: 6, paddingBottom: 6
  paddingLeft: 8, paddingRight: 10
  itemSpacing: 8
set_stroke_color
  r:0.835 g:0.843 b:0.855 a:1   ← border-default color.gray.300
  strokeWeight: 1
```

**동기화 아이콘 (기본: cloud)**
```
clone_node   → nodeId: "2:647"          ← icon.baseicon.tokens.cloud
insert_child → parentId: 동기화-상태 nodeId
resize_node  → width: 20, height: 20
set_fill_color → r:0.443 g:0.463 b:0.502 a:1   ← text-secondary color.gray.500
```
> 상태별 아이콘 교체: cloudOff(2:638) → 오프라인, refreshCw(2:1058) → 동기화 중

**배지 캡션 (caption medium)**
```
create_text
  name: "동기화-텍스트"
  parentId: 동기화-상태 nodeId
  text: "동기화됨"
  fontSize: 14, fontWeight: 500
  fontColor: text-secondary — color.gray.500 (r:0.443 g:0.463 b:0.502 a:1)
set_line_height    → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

## 변형 상태

| 상태 | 변경 항목 | 값 |
|------|----------|-----|
| 동기 완료 | 배지 텍스트·아이콘 | 텍스트 `동기화됨`, color.gray.500 |
| 동기 대기 | 배지 텍스트 색 | color.warning.500 (r:0.969 g:0.565 b:0.035 a:1), 텍스트 `동기화 대기` |
| 오프라인 | 배지 텍스트 색 | color.error.600 (r:0.851 g:0.173 b:0.125 a:1), 텍스트 `오프라인` |

---

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
