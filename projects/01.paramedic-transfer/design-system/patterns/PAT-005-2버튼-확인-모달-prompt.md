# PAT-005 — 2버튼 확인 모달

## 메타
- 등장 화면: M1, M2, M3, M4, L2→L4 경고
- 구조: **제목·본문** 아래 **취소(보조) + 확인(주요)** 2버튼이 모달 패널에서 반복된다.

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| (기본 텍스트 모달) | 없음 | — | — | 파괴적 확인은 **변형**에서 error 톤만 적용 |

> 경고 제목 옆 아이콘이 필요하면 `alertTriangle`(2:472) 또는 `alertCircle`(2:467)을 제목 행에 추가하는 변형으로 명시(구조 동일).

---

## Figma 실행 지시

### 외부 frame (모달 패널)

```
create_frame
  name: "PAT-005-2버튼-확인-모달"
  parentId: 42-4415
  x: 0
  y: 0
  width: 311
  height: 260
  fillColor: surface — color.gray.50 #fafafa (r:0.98 g:0.98 b:0.98 a:1)
```

```
set_auto_layout
  nodeId: {외부 frame nodeId}
  layoutMode: VERTICAL
  paddingTop: 24
  paddingBottom: 24
  paddingLeft: 24
  paddingRight: 24
  itemSpacing: 16
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
```

```
set_corner_radius → nodeId: {외부 frame nodeId}, radius: 16
```

**elevation — effect.shadow.lg**

```
set_effects
  nodeId: {외부 frame nodeId}
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.031}, offset:{x:0,y:4}, radius:6, spread:-2, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.078}, offset:{x:0,y:12}, radius:16, spread:-4, visible:true }
  ]
```

> 테두리 없음 — `visual-direction` (그림자만).

---

### 제목 `modal-title`

```
create_text
  name: "modal-title"
  parentId: {외부 frame nodeId}
  text: "이송 출발 확인"
  fontSize: 20
  fontWeight: 600
  fontColor: text-primary — color.gray.900 #181d27 (r:0.094 g:0.114 b:0.153 a:1)
```

```
set_font_name → nodeId: {modal-title nodeId}, fontFamily: Inter, style: SemiBold
set_line_height → lineHeight: 30, unit: PIXELS
set_letter_spacing → letterSpacing: -0.2, unit: PIXELS
```

```
resize_node → nodeId: {modal-title nodeId}, width: 263, height: 30
```

> 가용폭: 311 − 48 = **263**

---

### 본문 `modal-body`

```
create_text
  name: "modal-body"
  parentId: {외부 frame nodeId}
  text: "선택한 병원으로 출발을 확정합니다. 다른 병원에 대한 신청은 자동으로 취소됩니다."
  fontSize: 16
  fontWeight: 400
  fontColor: text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

```
resize_node → nodeId: {modal-body nodeId}, width: 263, height: 72
```

---

### 버튼 행 `modal-actions`

```
create_frame
  name: "modal-actions"
  parentId: {외부 frame nodeId}
  width: 263
  height: 48
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {modal-actions nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 12
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
```

> 각 버튼 폭: (263 − 12) / 2 = **125** (반올림).

---

### 보조 버튼 `btn-cancel`

```
create_frame
  name: "btn-cancel"
  parentId: {modal-actions nodeId}
  width: 125
  height: 48
  fillColor: surface-raised — color.white #ffffff (r:1 g:1 b:1 a:1)
```

```
set_corner_radius → nodeId: {btn-cancel nodeId}, radius: 8
```

```
set_stroke_color
  nodeId: {btn-cancel nodeId}
  r: 0.835
  g: 0.843
  b: 0.855
  a: 1
  strokeWeight: 1
```

```
set_auto_layout
  nodeId: {btn-cancel nodeId}
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 16
  paddingRight: 16
```

```
create_text
  name: "label-cancel"
  parentId: {btn-cancel nodeId}
  text: "취소"
  fontSize: 16
  fontWeight: 600
  fontColor: text-primary — color.gray.900 #181d27 (r:0.094 g:0.114 b:0.153 a:1)
```

```
set_font_name → fontFamily: Inter, style: SemiBold
set_line_height → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

### 주요 버튼 `btn-confirm` (기본: primary)

```
create_frame
  name: "btn-confirm"
  parentId: {modal-actions nodeId}
  width: 126
  height: 48
  fillColor: primary — color.brand.600 #7f56d9 (r:0.498 g:0.337 b:0.851 a:1)
```

```
set_corner_radius → nodeId: {btn-confirm nodeId}, radius: 8
```

```
set_auto_layout
  nodeId: {btn-confirm nodeId}
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 16
  paddingRight: 16
```

```
create_text
  name: "label-confirm"
  parentId: {btn-confirm nodeId}
  text: "출발 확정"
  fontSize: 16
  fontWeight: 600
  fontColor: text-on-primary — color.white #ffffff (r:1 g:1 b:1 a:1)
```

```
set_font_name → fontFamily: Inter, style: SemiBold
set_line_height → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 파괴적 확인(M3 등) | btn-confirm fill + (선택) 아이콘 | fill error #d92d20 (r:0.851 g:0.176 b:0.125 a:1) · 제목 행에 alertTriangle(2:472) |
| 동기화 오류(M2) | 카피·주요 라벨 | "다시 시도" / "닫기" 등 문자열만 치환 · 주요 버튼은 primary 유지 가능 |
| pressed(주요) | fillColor | primary-pressed #6941c6 (r:0.412 g:0.255 b:0.776 a:1) |

---

## Visual Recipe (정보 검증 — MCP 명령 없음)

### Elevation 처리
- 적용 여부: ✅ — 모달 패널 → **effect.shadow.lg**
- 적용된 shadow 토큰: effect.shadow.lg
- → MCP는 "외부 frame"에 포함됨

### Surface Depth 검증
- 이 패턴 fill: surface gray.50 (#fafafa)
- 화면 배경 예상 fill(딤 뒤): background gray.25 (#fdfdfd) + 오버레이(별도 레이어)
- 대비 평가: 패널 vs 페이지 **충분**; 딤은 별도 frame으로 처리(본 패턴 범위 아님).

### 강조 처리
- focal point: 주요 확인 버튼(`btn-confirm`)
- 처리 방식: primary(또는 파괴적 시 error) fill + SemiBold 라벨
- 근거: `visual-direction.mdc` 강조 방식

### 밀도 검증
- 터치 타겟 최소: 44px
- 이 패턴에서 터치 가능 요소: 각 버튼 **48px** 높이
- 충족 여부: ✅

## 주의
- `create_component` 금지
- 실제 화면에서는 **딤 배경**을 패턴 외부에서 별도 frame으로 깔고, 본 패널을 중앙에 배치한다.
- 생성 후 반환된 nodeId를 `_index.md`에 기입
