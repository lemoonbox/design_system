# PAT-004 — 하단 고정 주요 CTA 바

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 화면 하단에 **단일 주요 행동** 버튼 고정. 안전 영역(홈 인디케이터) 여유 포함

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| CTA 버튼 왼쪽 (화면별 선택) | mic | 2:938 | 20×20 | white (r:1 g:1 b:1 a:1) |
| CTA 버튼 왼쪽 — L4 이송 확정 | arrowRight | 2:516 | 20×20 | white (r:1 g:1 b:1 a:1) |
| CTA 버튼 왼쪽 — L2 완료 | checkSquare | 2:590 | 20×20 | white (r:1 g:1 b:1 a:1) |

> 아이콘은 화면 맥락에 따라 선택. 텍스트만 쓸 경우 아이콘 생략 가능.

---

## Figma 실행 지시

### 외부 frame
```
create_frame
  name: "PAT-004-하단-고정-CTA-바"
  parentId: {부모 프레임 nodeId}
  x: {nextX}, y: 0
  width: 390, height: 96
  fillColor: surface-raised — white (r:1 g:1 b:1 a:1)
```
```
set_auto_layout
  layoutMode: VERTICAL
  paddingTop: 16, paddingBottom: 24
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 0
  counterAxisAlignItems: STRETCH
```

**elevation — effect.shadow.md (상단에서 올라오는 느낌)**
```
set_effects
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.059}, offset:{x:0,y:-2}, radius:4, spread:-2, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.102}, offset:{x:0,y:-4}, radius:8, spread:-2, visible:true }
  ]
```
> offset y를 음수(-2, -4)로 설정해 위쪽으로 그림자가 올라오는 효과

---

### 버튼 컨테이너 (primary CTA)
```
create_frame
  name: "primary-cta"
  parentId: PAT-004 frame nodeId
  height: 48
  fillColor: primary — color.brand.600 (r:0.498 g:0.337 b:0.851 a:1)
set_corner_radius → radius: 8
set_auto_layout
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0, paddingBottom: 0
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 8
```

**버튼 아이콘 (화면별 선택 — "사용 아이콘" 표 참조)**
```
clone_node   → nodeId: "2:938"          ← icon.baseicon.tokens.mic (G1·L1 기본)
insert_child → parentId: primary-cta nodeId
resize_node  → width: 20, height: 20
set_fill_color → r:1 g:1 b:1 a:1        ← white
```

**버튼 텍스트 (button)**
```
create_text
  name: "cta-label"
  parentId: primary-cta nodeId
  text: "음성·구급 일지"
  fontSize: 16, fontWeight: 600
  fontColor: text-on-primary — white (r:1 g:1 b:1 a:1)
set_line_height    → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

## 변형 상태

| 상태 | 대상 | 변경 항목 | 값 |
|------|------|----------|-----|
| pressed | 버튼 fill | fillColor | primary-pressed color.brand.700 (r:0.412 g:0.255 b:0.776 a:1) |
| 비활성 | 버튼 fill | fillColor | color.gray.300 (r:0.835 g:0.843 b:0.855 a:1) |
| 비활성 | 버튼 텍스트 색 | fontColor | text-disabled color.gray.300 동일 hex, opacity 0.4 적용 |

---

## 주의
- `create_component` 금지. 버튼은 `create_frame` + 텍스트 구조
- 화면마다 버튼 라벨만 다름 → `set_text_content`로 교체
- 생성 후 반환된 nodeId를 `_index.md`에 기입
