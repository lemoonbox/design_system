# PAT-003 — 업무 단계 스텝퍼

## 메타
- 등장 화면: G1, L2, L4 (L2·L4는 상단 축약 재사용)
- 구조: 음성·구급일지 → 증상·pre-KTAS → 이송 **3단계 진행**을 동일 구조로 표시

---

## Figma 실행 지시

### 외부 frame
```
create_frame
  name: "PAT-003-업무-단계-스텝퍼"
  parentId: {부모 프레임 nodeId}
  x: {nextX}, y: 0
  width: 390, height: 72
  fillColor: background — color.gray.25 (r:0.992 g:0.992 b:0.992 a:1)
```
```
set_auto_layout
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: SPACE_BETWEEN
  counterAxisAlignItems: CENTER
  paddingTop: 12, paddingBottom: 12
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 24
```
> 루트는 `itemSpacing: 24` + `SPACE_BETWEEN`으로 3등분 리듬 유지. shadow 없음.

---

### 단계 1개 반복 (step-1 / step-2 / step-3)

**단계 컨테이너**
```
create_frame
  name: "step-1"   (step-2, step-3 동일 반복)
  parentId: PAT-003 frame nodeId
set_auto_layout
  layoutMode: VERTICAL
  counterAxisAlignItems: CENTER
  itemSpacing: 12
```

**마커 원 (32×32)** — `resize_node`로 가로·세로 **32** 고정(오토레이아웃 붕괴 방지).

**단계별 마커 아이콘 (숫자·체크 금지 — 단계 의미 고정)**

| 단계 | 라벨 | Base 키 | `icon-tokens.json` `figmaId` |
|------|------|---------|------------------------------|
| step-1 | 음성·구급일지 | `mic` | **2:938** |
| step-2 | 증상·pre-KTAS | `activity` | **2:461** |
| step-3 | 이송·조율 | `truck` | **2:1208** |

**step-1 (완료)**
```
set_fill_color (마커) → success color.success.600 (r:0.012 g:0.596 b:0.333 a:1)
set_stroke_color → strokeWeight: 0
set_auto_layout (마커) → HORIZONTAL, primary/counter CENTER
clone_node → nodeId: **2:938** (mic)
insert_child → parentId: step-1-marker, index: 0
resize_node → width: 18, height: 18
set_fill_color (인스턴스) → white text-on-primary (r:1 g:1 b:1 a:1)
```
**step-2 (현재)** — 마커 흰 채움 + `set_stroke_color` brand.600, **strokeWeight: 2**. 마커 안 `clone_node` **2:461** (activity) → `insert_child` index 0 → `resize_node` 18×18 → `set_fill_color` brand.600.

**step-3 (미시작)** — 마커 흰 채움 + stroke gray.300 weight 1. 마커 안 `clone_node` **2:1208** (truck) → `insert_child` index 0 → `resize_node` 18×18 → `set_fill_color` gray.500.

**단계 라벨 (caption)**
```
create_text
  parentId: step-1 nodeId
  text: "음성·구급일지"
  fontSize: 14, fontWeight: 400
  fontColor: color.gray.600 (r:0.325 g:0.345 b:0.384 a:1)   ← 완료 단계
set_line_height → 20 PIXELS
```
```
create_text (step-2 라벨)
  fontColor: color.gray.900 (r:0.094 g:0.114 b:0.153 a:1)
  fontWeight: 500
```
```
create_text (step-3 라벨)
  fontColor: color.gray.500 (r:0.443 g:0.463 b:0.502 a:1)
  fontWeight: 400
```

> 다른 단계가 **현재/완료/미시작**으로 바뀔 때는 **같은 단계의 고정 아이콘**을 유지하고, 마커 채움·스트로크·아이콘 틴트만 변형 표대로 바꾼다.

---

### 연결선 (비권장)
루트가 `HORIZONTAL` + 단계 컬럼(마커+라벨) **세로 스택**이면, 형제로 넣은 가로 막대는 마커 행이 아니라 프레임 **세로 중앙**에 붙어 어색해진다. 연결선이 필요하면 **마커만 담은 별도 행** 프레임을 두는 식으로 레이아웃을 나눈다(새 구조 = 스펙 협의 후).

---

## 변형 상태

| 상태 | 대상 | 변경 항목 | 값 |
|------|------|----------|-----|
| 완료 | 마커 fill | fillColor | color.success.600 (r:0.012 g:0.596 b:0.333 a:1) |
| 완료 | 마커 내부 아이콘 | 해당 단계 고정 아이콘(`mic` / `activity` / `truck`) → `clone_node` → `insert_child`(마커 index 0) → `resize_node` **18×18** → 완료 시 `set_fill_color` white | 위 표 `figmaId` |
| 완료 | 라벨 | fontColor · weight | color.gray.600 (#535862), regular 400 |
| 현재 | 마커 stroke / 아이콘 | strokeColor brand.600, strokeWeight: 2; 아이콘 틴트 brand.600 |
| 현재 | 라벨 색 | fontColor | text-primary color.gray.900 (#181d27), fontWeight: 500 |
| 미시작 | 마커 | fill white, stroke border-default gray.300 | (기본값) |
| 미시작 | 라벨 | fontColor · weight | color.gray.500 (#717680), regular 400 |

---

## 주의
- `create_component` 금지
- 레이아웃이 다른 축약형(가로 스크롤 탭 등)은 새 PAT ID로 분리
- 생성 후 반환된 nodeId를 `_index.md`에 기입
