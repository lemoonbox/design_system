# PAT-002 — 동기화·네트워크 배너

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 본문 상단 또는 리스트 위에 **경고/오류 톤 한 블록**으로, 요약 문구와 **재시도·자세히(M2)** 액션이 반복된다.

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| 상태 표시 | alertTriangle (`icon.feedback.tokens.alertTriangle`) | 2:472 | 24×24 | error — color.error.600 #d92d20 (r:0.851 g:0.176 b:0.125 a:1) |
| 재시도(선택 시각 보조) | refreshCw (`icon.baseicon.tokens.refreshCw`) | 2:1058 | 20×20 | accent — color.blue.600 #1570ef (r:0.082 g:0.439 b:0.937 a:1) |
| 자세히 진입 | chevronRight (`icon.baseicon.tokens.chevronRight`) | 2:602 | 16×16 | accent — color.blue.600 #1570ef (r:0.082 g:0.439 b:0.937 a:1) |

---

## Figma 실행 지시

### 외부 frame

```
create_frame
  name: "PAT-002-동기화-네트워크-배너"
  parentId: 42-4415
  x: 0
  y: 0
  width: 343
  height: 72
  fillColor: error-subtle — color.error.50 #fef3f2 (r:0.996 g:0.953 b:0.949 a:1)
```

```
set_auto_layout
  nodeId: {외부 frame nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 16
  paddingBottom: 16
  paddingLeft: 16
  paddingRight: 16
  itemSpacing: 12
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: CENTER
```

```
set_corner_radius → nodeId: {외부 frame nodeId}, radius: 12
```

> elevation: 카드형 인라인 배너이므로 **적용** — `effect.shadow.sm` (테두리 없음, 그림자만).

```
set_effects
  nodeId: {외부 frame nodeId}
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.059}, offset:{x:0,y:1}, radius:2, spread:0, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.102}, offset:{x:0,y:1}, radius:3, spread:0, visible:true }
  ]
```

---

### 아이콘 `alertTriangle`

```
create_frame
  name: "icon-wrap-alert"
  parentId: {외부 frame nodeId}
  width: 24
  height: 24
  fillColor: (r:0 g:0 b:0 a:0)
```

```
아이콘명: alertTriangle
figmaId: 2:472
크기: 24×24
색상: error color.error.600 (r:0.851 g:0.176 b:0.125 a:1)
컨테이너: {icon-wrap-alert nodeId}
```

---

### 텍스트 블록 `banner-copy`

```
create_frame
  name: "banner-copy"
  parentId: {외부 frame nodeId}
  x: 0
  y: 0
  width: 179
  height: 40
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {banner-copy nodeId}
  layoutMode: VERTICAL
  itemSpacing: 4
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
```

```
create_text
  name: "banner-title"
  parentId: {banner-copy nodeId}
  text: "일지를 전송하지 못했습니다"
  fontSize: 16
  fontWeight: 400
  fontColor: text-primary — color.gray.900 #181d27 (r:0.094 g:0.114 b:0.153 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

```
create_text
  name: "banner-sub"
  parentId: {banner-copy nodeId}
  text: "네트워크 연결을 확인해 주세요"
  fontSize: 14
  fontWeight: 400
  fontColor: text-secondary — color.gray.500 #717680 (r:0.443 g:0.463 b:0.502 a:1)
```

```
set_font_name → fontFamily: Inter, style: Regular
set_line_height → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

> 가용폭: (343 − 32 padding) − 24(icon) − 12(gap) − 96(actions) ≈ **179** — 액션 폭에 따라 `resize_node`로 `banner-copy` width 조정.

---

### 액션 영역 `banner-actions`

```
create_frame
  name: "banner-actions"
  parentId: {외부 frame nodeId}
  width: 96
  height: 44
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {banner-actions nodeId}
  layoutMode: VERTICAL
  itemSpacing: 8
  primaryAxisAlignItems: MAX
  counterAxisAlignItems: MAX
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 0
  paddingRight: 0
```

```
create_text
  name: "action-retry"
  parentId: {banner-actions nodeId}
  text: "재시도"
  fontSize: 14
  fontWeight: 500
  fontColor: accent — color.blue.600 #1570ef (r:0.082 g:0.439 b:0.937 a:1)
```

```
set_font_name → fontFamily: Inter, style: Medium
set_line_height → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

```
create_frame
  name: "detail-row"
  parentId: {banner-actions nodeId}
  width: 96
  height: 20
  fillColor: (r:0 g:0 b:0 a:0)
```

```
set_auto_layout
  nodeId: {detail-row nodeId}
  layoutMode: HORIZONTAL
  itemSpacing: 4
  primaryAxisAlignItems: MAX
  counterAxisAlignItems: CENTER
```

```
create_text
  name: "action-detail"
  parentId: {detail-row nodeId}
  text: "자세히"
  fontSize: 14
  fontWeight: 500
  fontColor: accent — color.blue.600 #1570ef (r:0.082 g:0.439 b:0.937 a:1)
```

```
set_font_name → fontFamily: Inter, style: Medium
set_line_height → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

**아이콘 chevronRight** (자세히 옆):

```
아이콘명: chevronRight
figmaId: 2:602
크기: 16×16
색상: accent color.blue.600 (r:0.082 g:0.439 b:0.937 a:1)
컨테이너: {detail-row nodeId}
```

(선택) 재시도 행에 **refreshCw** 20×20을 텍스트 왼쪽에 두는 변형은 동일 시퀀스로 추가 가능.

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 전송 실패(기본) | fill + 아이콘 | error-subtle + alertTriangle + error 색 |
| 경고(대기 큐) | fill + 아이콘 + 텍스트 | surface gray.50 #fafafa (r:0.98 g:0.98 b:0.98 a:1) + alertCircle(2:467) + warning 아이콘색 #f79009 (r:0.969 g:0.565 b:0.035 a:1) |
| 오프라인 강조 | 본문 카피만 | 사용자 메시지 치환(M2 스펙) |

---

## Visual Recipe (정보 검증 — MCP 명령 없음)

### Elevation 처리
- 적용 여부: ✅ — 근거: 인라인 카드형 배너 → `visual-direction` 카드·입력 필드급 → **effect.shadow.sm**
- 적용된 shadow 토큰: effect.shadow.sm
- → MCP는 위 "외부 frame" 블록에 포함됨

### Surface Depth 검증
- 이 패턴 fill: error-subtle (#fef3f2)
- 화면 배경 예상 fill: background gray.25 (#fdfdfd)
- 대비 평가: **충분**
- → 별도 stroke 불필요(그림자만 사용).

### 강조 처리
- focal point: 첫 줄 본문(`banner-title`) + 상태 아이콘
- 처리 방식: 색상만이 아니라 **삼각형 아이콘 + 문구** 병행
- 근거: `visual-direction.mdc` 상태 표시 원칙

### 밀도 검증
- 터치 타겟 최소: 44px
- 이 패턴에서 터치 가능 요소: "재시도"·"자세히" — 행 높이·패딩으로 **44px 이상** 확보 권장(현재 액션 프레임 44h)
- 충족 여부: ✅ (빌드 시 실제 탭 영역 검증)

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
