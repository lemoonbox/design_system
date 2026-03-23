# PAT-005 — 2버튼 확인 모달

## 메타
- 등장 화면: M1, M2, M3, M4, L2
- 구조: 제목·본문 아래 **취소(보조)** + **주요 확인** 두 버튼 고정 배치 (바텀시트·센터 다이얼로그 공통 뼈대)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 | 화면 |
|------|---------|---------|------|------|------|
| 제목 왼쪽 (상태 강조) | checkCircle | 2:588 | 24×24 | success (r:0.012 g:0.596 b:0.333) | M1, M4 완료 확인 |
| 제목 왼쪽 (경고) | alertTriangle | 2:472 | 24×24 | warning (r:0.969 g:0.565 b:0.035) | M3 출동 종료 경고 |
| 제목 왼쪽 (오류) | alertCircle | 2:467 | 24×24 | error (r:0.851 g:0.173 b:0.125) | M2 동기화 오류 |

---

## Figma 실행 지시

### 루트 래퍼 frame (배치·스크린샷용)
```
create_frame
  name: "PAT-005-2버튼-확인-모달"
  parentId: {부모 프레임 nodeId}
  x: {nextX}, y: 0
  width: 390, height: 280
  fillColor: transparent (a:0)
```
```
set_auto_layout
  layoutMode: VERTICAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0, paddingBottom: 0
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 0
```

---

### 모달 패널
```
create_frame
  name: "modal-panel"
  parentId: PAT-005 래퍼 nodeId
  width: 358, height: 248
  fillColor: surface-raised — white (r:1 g:1 b:1 a:1)
set_corner_radius → radius: 16
```

**elevation — effect.shadow.lg (강한 부상감)**
```
set_effects
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.031}, offset:{x:0,y:4}, radius:6, spread:-2, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.078}, offset:{x:0,y:12}, radius:16, spread:-4, visible:true }
  ]
```

```
set_auto_layout
  layoutMode: VERTICAL
  paddingTop: 24, paddingBottom: 24
  paddingLeft: 24, paddingRight: 24
  itemSpacing: 20
  counterAxisAlignItems: STRETCH
```

---

### 텍스트 영역
```
create_frame
  name: "modal-text"
  parentId: modal-panel nodeId
set_auto_layout
  layoutMode: VERTICAL
  itemSpacing: 8
  counterAxisAlignItems: STRETCH
```

**제목 영역 아이콘 ("사용 아이콘" 표 참조 — 화면 맥락에 따라 선택)**
```
clone_node   → nodeId: "2:588"          ← icon.feedback.tokens.checkCircle (M1·M4 기본)
insert_child → parentId: modal-text nodeId   ← 텍스트보다 앞(index 0)에 삽입
resize_node  → width: 24, height: 24
set_fill_color → r:0.012 g:0.596 b:0.333 a:1  ← success color.success.600
```
> 경고(M3): alertTriangle(2:472) → warning / 오류(M2): alertCircle(2:467) → error

**제목 (subheading)**
```
create_text
  name: "modal-title"
  parentId: modal-text nodeId
  text: "이송 출발 확인"
  fontSize: 20, fontWeight: 600
  fontColor: text-primary — color.gray.900 (r:0.094 g:0.114 b:0.153 a:1)
set_line_height    → lineHeight: 30, unit: PIXELS
set_letter_spacing → letterSpacing: -0.2, unit: PIXELS
```

**본문 (body)**
```
create_text
  name: "modal-body"
  parentId: modal-text nodeId
  text: "환자를 이송 출발하겠습니까?\n출발 후에는 취소할 수 없습니다."
  fontSize: 16, fontWeight: 400
  fontColor: text-secondary — color.gray.500 (r:0.443 g:0.463 b:0.502 a:1)
set_line_height    → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

### 버튼 행
```
create_frame
  name: "modal-buttons"
  parentId: modal-panel nodeId
set_auto_layout
  layoutMode: HORIZONTAL
  counterAxisAlignItems: STRETCH
  itemSpacing: 12
  primaryAxisAlignItems: SPACE_BETWEEN
```

**취소 버튼 (보조)**
```
create_frame
  name: "btn-cancel"
  parentId: modal-buttons nodeId
  height: 48
  fillColor: surface-raised — white (r:1 g:1 b:1 a:1)
set_corner_radius → radius: 8
set_stroke_color
  r:0.835 g:0.843 b:0.855 a:1   ← border-default color.gray.300
  strokeWeight: 1
set_auto_layout
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0, paddingBottom: 0
  paddingLeft: 16, paddingRight: 16
```
```
create_text
  name: "cancel-label"
  parentId: btn-cancel nodeId
  text: "취소"
  fontSize: 16, fontWeight: 600
  fontColor: text-primary — color.gray.900 (r:0.094 g:0.114 b:0.153 a:1)
set_line_height    → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

**주요 확인 버튼**
```
create_frame
  name: "btn-primary"
  parentId: modal-buttons nodeId
  height: 48
  fillColor: primary — color.brand.600 (r:0.498 g:0.337 b:0.851 a:1)
set_corner_radius → radius: 8
set_auto_layout
  layoutMode: HORIZONTAL
  primaryAxisAlignItems: CENTER
  counterAxisAlignItems: CENTER
  paddingTop: 0, paddingBottom: 0
  paddingLeft: 16, paddingRight: 16
```
```
create_text
  name: "primary-label"
  parentId: btn-primary nodeId
  text: "출발 확정"
  fontSize: 16, fontWeight: 600
  fontColor: text-on-primary — white (r:1 g:1 b:1 a:1)
set_line_height    → lineHeight: 24, unit: PIXELS
set_letter_spacing → letterSpacing: 0.1, unit: PIXELS
```

---

## 변형 상태

| 상태 | 대상 | 변경 항목 | 값 |
|------|------|----------|-----|
| 파괴적 확인 | btn-primary fill | fillColor | error color.error.600 (r:0.851 g:0.173 b:0.125 a:1) |
| 파괴적 확인 | primary-label 색 | fontColor | white — 유지 |
| 로딩(표시용) | primary-label | opacity | 0.6 (구조 변경 없음) |

---

## 주의
- `create_component` 금지
- 패널과 딤(오버레이)을 한 프레임에 묶지 않아도 됨 — 패턴 간 독립 실행 우선
- 생성 후 반환된 nodeId를 `_index.md`에 기입
