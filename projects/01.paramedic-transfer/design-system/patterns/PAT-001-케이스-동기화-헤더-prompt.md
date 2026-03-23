# PAT-001 — 케이스·동기화 헤더

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 화면 상단·케이스 맥락에서 **케이스 라벨 + 시각 + 동기화 상태 배지**가 한 행(또는 좌·우 그룹)으로 반복된다.

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| 시각 앞 | clock (`icon.baseicon.tokens.clock`) | 2:629 | 20×20 | text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1) |
| 동기 완료 배지 | checkCircle (`icon.feedback.tokens.checkCircle`) | 2:588 | 20×20 | success — color.success.600 #039855 (r:0.012 g:0.596 b:0.333 a:1) |
| 오프라인(변형) | cloudOff (`icon.baseicon.tokens.cloudOff`) | 2:638 | 20×20 | warning — color.warning.500 #f79009 (r:0.969 g:0.565 b:0.035 a:1) |
| 동기 대기(변형) | loader (`icon.baseicon.tokens.loader`) | 2:896 | 20×20 | text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1) |

---

## Figma 실행 지시

### 외부 frame

```
create_frame
  name: "PAT-001-케이스-동기화-헤더"
  parentId: 42-4415
  x: 0
  y: 0
  width: 343
  height: 64
  fillColor: 투명 — (r:0 g:0 b:0 a:0)
```

> `07-build-patterns`의 `nextX`로 `x`를 조정한다. 첫 패턴이 아니면 `x: nextX` 사용.  
> 생성 직후 `get_node_info`로 fill이 `#ffffff`면 `set_fill_color`로 `a:0` 재적용.

```
set_auto_layout
  nodeId: {외부 frame nodeId}
  layoutMode: VERTICAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 8
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
```

> elevation·그림자 없음(헤더 스트립). 테두리 없음.

---

### 행 컨테이너 `header-row`

```
create_frame
  name: "header-row"
  parentId: {외부 frame nodeId}
  x: 0
  y: 0
  width: 343
  height: 48
  fillColor: 투명 — (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {header-row nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 12
  primaryAxisAlignItems: SPACE_BETWEEN
  counterAxisAlignItems: CENTER
```

---

### 좌측 `case-block` (케이스·시각)

```
create_frame
  name: "case-block"
  parentId: {header-row nodeId}
  x: 0
  y: 0
  width: 215
  height: 44
  fillColor: 투명 — (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {case-block nodeId}
  layoutMode: VERTICAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 4
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
```

```
create_text
  name: "case-title"
  parentId: {case-block nodeId}
  x: 0
  y: 0
  width: 215
  height: 28
  text: "오늘 14:32 출동"
  fontSize: 18
  fontWeight: 500
  fontColor: text-primary — color.gray.900 #181d27 (r:0.094 g:0.114 b:0.153 a:1)
```

```
set_font_name → nodeId: {case-title nodeId}, fontFamily: Inter, style: Medium
set_line_height → nodeId: {case-title nodeId}, lineHeight: 28, unit: PIXELS
set_letter_spacing → nodeId: {case-title nodeId}, letterSpacing: 0, unit: PIXELS
```

```
create_frame
  name: "time-row"
  parentId: {case-block nodeId}
  x: 0
  y: 0
  width: 215
  height: 20
  fillColor: 투명 — (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {time-row nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 6
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
```

**아이콘 clock** — `07-build-patterns` 아이콘 슬롯 표준 시퀀스:

```
아이콘명: clock
figmaId: 2:629
크기: 20×20
색상: text-secondary color.gray.500 (r:0.443 g:0.463 b:0.502 a:1)
컨테이너: {time-row nodeId} (먼저 20×20 `icon-slot` frame 생성 후 그 안에 삽입 권장)
```

```
create_frame
  name: "icon-slot-clock"
  parentId: {time-row nodeId}
  width: 20
  height: 20
  fillColor: (r:0 g:0 b:0 a:0)
```
→ `clone_node` / `insert_child` / `move_node` / `resize_node` / `set_fill_color` 순서 적용.

```
create_text
  name: "time-meta"
  parentId: {time-row nodeId}
  text: "14:32 기준"
  fontSize: 14
  fontWeight: 400
  fontColor: text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1)
```

```
set_font_name → nodeId: {time-meta nodeId}, fontFamily: Inter, style: Regular
set_line_height → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

### 우측 `sync-badge`

```
create_frame
  name: "sync-badge"
  parentId: {header-row nodeId}
  x: 0
  y: 0
  width: 116
  height: 36
  fillColor: primary-subtle — color.brand.50 #f9f5ff (r:0.976 g:0.961 b:1 a:1)
```

```
set_auto_layout
  nodeId: {sync-badge nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 8
  paddingBottom: 8
  paddingLeft: 12
  paddingRight: 12
  itemSpacing: 8
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
```

```
set_corner_radius → nodeId: {sync-badge nodeId}, radius: 8
```

**아이콘 checkCircle** (기본 상태):

```
아이콘명: checkCircle
figmaId: 2:588
크기: 20×20
색상: success color.success.600 (r:0.012 g:0.596 b:0.333 a:1)
컨테이너: {sync-badge nodeId}
```

```
create_text
  name: "sync-label"
  parentId: {sync-badge nodeId}
  text: "동기 완료"
  fontSize: 14
  fontWeight: 400
  fontColor: text-primary — color.gray.900 #181d27 (r:0.094 g:0.114 b:0.153 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 동기 완료(기본) | 배지 아이콘 + 라벨 | checkCircle(2:588) + "동기 완료" |
| 오프라인 | 아이콘·라벨·배지 fill | cloudOff(2:638) + "오프라인" · fill error-subtle #fef3f2 (r:0.996 g:0.953 b:0.949 a:1) · 아이콘색 warning |
| 동기 대기 | 아이콘·라벨 | loader(2:896) + "동기 대기" · 아이콘색 text-secondary |

---

## Visual Recipe (정보 검증 — MCP 명령 없음)

### Elevation 처리
- 적용 여부: ❌ — 근거: `visual-direction.mdc` 헤더 스트립은 평면 배치, 카드급 깊이 불필요.
- 적용된 shadow 토큰: 없음

### Surface Depth 검증
- 이 패턴 루트 fill: 투명 (페이지 배경 위)
- 화면 배경 예상 fill: background — color.gray.25 #fdfdfd
- 대비 평가: 본문·배지는 **충분** (배지는 brand.50으로 배경과 구분)
- → Surface 보정 MCP는 외부 frame에 포함하지 않음(투명 유지).

### 강조 처리
- focal point: 케이스 제목 한 줄(`case-title`)
- 처리 방식: `body-strong` 스케일 + text-primary
- 근거: `visual-direction.mdc` > 강조 방식 (크기 + 컬러, 상태에는 아이콘+문구 병행)

### 밀도 검증
- 터치 타겟 최소: 44px (`visual-direction.mdc`)
- 이 패턴에서 터치 가능 요소: 동기 배지(높이 36px) — **배지 탭 시 44px 미만**
- 충족 여부: ❌ — 스펙상 배지가 탭 가능하면 세로 패딩을 늘려 **최소 44px**로 조정하거나, 탭 영역을 행 전체로 확장하는 것을 권장(구현 시 확인).

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
