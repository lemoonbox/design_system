# PAT-003 — 업무 단계 스텝퍼

## 메타
- 등장 화면: G1, (L2/L4 상단 축약)
- 구조: **음성·구급일지 → 증상·pre-KTAS → 이송** 3단계가 가로로 나열되고, 완료/진행/대기 상태가 반복된다.

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| 완료 단계 | checkCircle (`icon.feedback.tokens.checkCircle`) | 2:588 | 24×24 | success — color.success.600 #039855 (r:0.012 g:0.596 b:0.333 a:1) |
| 단계 사이 구분 | chevronRight (`icon.baseicon.tokens.chevronRight`) | 2:602 | 16×16 | text-disabled — color.gray.300 #d5d7da (r:0.835 g:0.843 b:0.855 a:1) |

> 진행 중·대기 **원형 마커**는 플레이스홀더 대신 `create_ellipse`로 단색 처리(아래 참조).

---

## Figma 실행 지시

### 외부 frame

```
create_frame
  name: "PAT-003-업무-단계-스텝퍼"
  parentId: 42-4415
  x: 0
  y: 0
  width: 343
  height: 88
  fillColor: 투명 — (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {외부 frame nodeId}
  layoutMode: VERTICAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 0
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
```

> elevation 없음.

---

### 단계 행 `stepper-track`

```
create_frame
  name: "stepper-track"
  parentId: {외부 frame nodeId}
  width: 343
  height: 88
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {stepper-track nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
  itemSpacing: 8
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
```

---

### `step-1` 열 (완료 예시)

```
create_frame
  name: "step-1"
  parentId: {stepper-track nodeId}
  width: 100
  height: 88
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {step-1 nodeId}
  layoutMode: VERTICAL
  itemSpacing: 8
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
```

**아이콘 checkCircle**

```
create_frame
  name: "icon-slot-s1"
  parentId: {step-1 nodeId}
  width: 24
  height: 24
  fillColor: (r:0 g:0 b:0 a:0)
```

```
아이콘명: checkCircle
figmaId: 2:588
크기: 24×24
색상: success (r:0.012 g:0.596 b:0.333 a:1)
컨테이너: {icon-slot-s1 nodeId}
```

```
create_text
  name: "label-s1"
  parentId: {step-1 nodeId}
  text: "음성·일지"
  fontSize: 12
  fontWeight: 400
  fontColor: text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 18, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

### 구분 chevron A

```
create_frame
  name: "chev-a-wrap"
  parentId: {stepper-track nodeId}
  width: 16
  height: 24
  fillColor: (r:0 g:0 b:0 a:0)
```

```
아이콘명: chevronRight
figmaId: 2:602
크기: 16×16
색상: text-disabled gray.300 (r:0.835 g:0.843 b:0.855 a:1)
컨테이너: {chev-a-wrap nodeId}
```

---

### `step-2` 열 (진행 중 — 타원 마커)

```
create_frame
  name: "step-2"
  parentId: {stepper-track nodeId}
  width: 100
  height: 88
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {step-2 nodeId}
  layoutMode: VERTICAL
  itemSpacing: 8
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
```

```
create_ellipse
  name: "dot-current"
  parentId: {step-2 nodeId}
  width: 24
  height: 24
  fillColor: primary — color.brand.600 #7f56d9 (r:0.498 g:0.337 b:0.851 a:1)
```

```
create_text
  name: "label-s2"
  parentId: {step-2 nodeId}
  text: "증상·KTAS"
  fontSize: 12
  fontWeight: 500
  fontColor: primary — color.brand.600 #7f56d9 (r:0.498 g:0.337 b:0.851 a:1)
```

```
set_font_name → fontFamily: Inter, style: Medium
set_line_height → lineHeight: 18, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

### 구분 chevron B

동일 `chevronRight` 2:602, 16×16, gray.300 — 컨테이너 `chev-b-wrap`.

---

### `step-3` 열 (대기 — 링 마커)

```
create_frame
  name: "step-3"
  parentId: {stepper-track nodeId}
  width: 100
  height: 88
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {step-3 nodeId}
  layoutMode: VERTICAL
  itemSpacing: 8
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
```

```
create_ellipse
  name: "dot-pending"
  parentId: {step-3 nodeId}
  width: 24
  height: 24
  fillColor: surface-raised — color.white #ffffff (r:1 g:1 b:1 a:1)
```

```
set_stroke_color
  nodeId: {dot-pending nodeId}
  r: 0.835
  g: 0.843
  b: 0.855
  a: 1
  strokeWeight: 2
```

```
create_text
  name: "label-s3"
  parentId: {step-3 nodeId}
  text: "이송"
  fontSize: 12
  fontWeight: 400
  fontColor: text-disabled — color.gray.300 #d5d7da (r:0.835 g:0.843 b:0.855 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 18, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

> 가로 합계: 100+16+100+16+100 = 332 — 부모 343이면 `resize_node`로 `stepper-track` 자식 간격을 조정하거나 좌우 패딩 5.5씩 외부 frame에 추가. 빌드 시 **343 맞춤**으로 `step-1/2/3` width를 각 102로 조정 가능(102×3+16×2=334 → 패딩 4).

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 1단계 진행 중 | step-1 마커 | checkCircle → `create_ellipse` 24px primary-subtle fill #f9f5ff (r:0.976 g:0.961 b:1 a:1) + 라벨 Medium primary |
| 2·3단계 완료 | 해당 열 마커 | checkCircle(2:588) success + 라벨 caption text-secondary |
| L2/L4 축약 | 높이·캡션 | 라벨 `meta` 12/18로 축소 시 `fontSize: 12`, `lineHeight: 18`, `letterSpacing: 0.1` 유지 |

---

## Visual Recipe (정보 검증 — MCP 명령 없음)

### Elevation 처리
- 적용 여부: ❌ — 스텝퍼는 본문 플로우 안내용 평면 조합.
- 적용된 shadow 토큰: 없음

### Surface Depth 검증
- 이 패턴 루트 fill: 투명
- 화면 배경 예상 fill: background gray.25 (#fdfdfd)
- 대비 평가: **충분** (마커·라벨 색으로 단계 구분)

### 강조 처리
- focal point: **현재 단계** 라벨 + 채워진 마커(brand.600)
- 처리 방식: 크기 동일 유지, **색상( primary ) + 굵기(Medium)** 으로 현재 단계만 강조
- 근거: `visual-direction.mdc` 강조 방식

### 밀도 검증
- 터치 타겟: 스텝 자체는 정보 위주 — 탭 가능하면 44px 확보(현재 설계는 표시 위주)
- 충족 여부: 스텝이 버튼이 아니면 ✅ / 버튼이면 각 열 높이·폭 재검증

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
