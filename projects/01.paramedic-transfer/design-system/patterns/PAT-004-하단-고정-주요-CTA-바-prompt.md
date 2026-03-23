# PAT-004 — 하단 고정 주요 CTA 바

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 화면 **하단 고정**에 **단일 주요 버튼**과 **하단 안전 영역**이 반복된다.

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| (이 패턴 기본안) | 없음 | — | — | 주요 행동은 라벨 텍스트만 |

> 화면별로 아이콘+CTA가 필요하면 동일 바 안에 `icon.baseicon` 슬롯을 추가하는 **변형**으로 처리(레이아웃 구조 변경 시 새 PAT).

---

## Figma 실행 지시

### 외부 frame

```
create_frame
  name: "PAT-004-하단-고정-주요-CTA-바"
  parentId: 42-4415
  x: 0
  y: 0
  width: 375
  height: 120
  fillColor: surface-raised — color.white #ffffff (r:1 g:1 b:1 a:1)
```

```
set_auto_layout
  nodeId: {외부 frame nodeId}
  layoutMode: VERTICAL
  paddingTop: 16
  paddingBottom: 32
  paddingLeft: 16
  paddingRight: 16
  itemSpacing: 0
  primaryAxisAlignItems: MIN
  counterAxisAlignItems: MIN
```

```
set_corner_radius → nodeId: {외부 frame nodeId}, radius: 0
```

**elevation — effect.shadow.md** (`design-system.md`):

```
set_effects
  nodeId: {외부 frame nodeId}
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.059}, offset:{x:0,y:2}, radius:4, spread:-2, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.102}, offset:{x:0,y:4}, radius:8, spread:-2, visible:true }
  ]
```

> 상단 구분은 **그림자만** — stroke 없음(`visual-direction`).

---

### 주요 버튼 `primary-cta`

```
create_frame
  name: "primary-cta"
  parentId: {외부 frame nodeId}
  width: 343
  height: 48
  fillColor: primary — color.brand.600 #7f56d9 (r:0.498 g:0.337 b:0.851 a:1)
```

```
set_auto_layout
  nodeId: {primary-cta nodeId}
  layoutMode: HORIZONTAL
  paddingTop: 0
  paddingBottom: 0
  paddingLeft: 24
  paddingRight: 24
  itemSpacing: 0
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
```

```
set_corner_radius → nodeId: {primary-cta nodeId}, radius: 8
```

```
create_text
  name: "cta-label"
  parentId: {primary-cta nodeId}
  text: "음성·구급 일지로"
  fontSize: 16
  fontWeight: 600
  fontColor: text-on-primary — color.white #ffffff (r:1 g:1 b:1 a:1)
```

```
set_font_name → nodeId: {cta-label nodeId}, fontFamily: Inter, style: SemiBold
set_line_height → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

> `resize_node`로 `primary-cta` width를 부모 가용폭 **343**(375−32)에 고정.

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| pressed | fillColor | primary-pressed — color.brand.700 #6941c6 (r:0.412 g:0.255 b:0.776 a:1) |
| disabled | fillColor + 텍스트 | fill gray.300 #d5d7da (r:0.835 g:0.843 b:0.855 a:1) · fontColor text-disabled 동일 톤 |
| 보조 화면 카피 | `cta-label` 문자열만 | 예: "증상·pre-KTAS로", "다음" 등 화면별 치환 |

---

## Visual Recipe (정보 검증 — MCP 명령 없음)

### Elevation 처리
- 적용 여부: ✅ — 하단 고정 바 → `visual-direction` **effect.shadow.md**
- 적용된 shadow 토큰: effect.shadow.md
- → MCP는 "외부 frame"에 포함됨

### Surface Depth 검증
- 이 패턴 fill: surface-raised white (#ffffff)
- 화면 배경 예상 fill: background gray.25 (#fdfdfd)
- 대비 평가: **충분**
- → stroke 불필요

### 강조 처리
- focal point: `primary-cta` 단일 버튼
- 처리 방식: primary fill + text-on-primary + 전역에서 **하나만** 주요 CTA
- 근거: `visual-direction.mdc` 하단 CTA 패턴

### 밀도 검증
- 터치 타겟 최소: 44px
- 이 패턴에서 터치 가능 요소: 버튼 높이 **48px**
- 충족 여부: ✅

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
