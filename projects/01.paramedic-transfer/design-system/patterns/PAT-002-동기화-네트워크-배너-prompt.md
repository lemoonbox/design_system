# PAT-002 — 동기화·네트워크 배너

## 메타
- 등장 화면: G1, L1, L2, L4
- 구조: 오프라인·전송 실패·대기 등 **한 줄 요약**과 **재시도 / 자세히(M2)** 진입을 반복 제공

---

## Figma 실행 지시

### 외부 frame
```
create_frame
  name: "PAT-002-동기화-네트워크-배너"
  parentId: {부모 프레임 nodeId}
  x: {nextX}, y: 0
  width: 390, height: 48
  fillColor: error-subtle — color.error.50 (r:0.996 g:0.953 b:0.949 a:1)
```
```
set_auto_layout
  layoutMode: HORIZONTAL
  counterAxisAlignItems: CENTER
  primaryAxisAlignItems: MIN
  paddingTop: 12, paddingBottom: 12
  paddingLeft: 16, paddingRight: 16
  itemSpacing: 8
```
> shadow 없음 — 배너는 배경색으로 상태 전달. stroke 하단 1px로 섹션 구분 가능
```
set_stroke_color
  r:0.973 g:0.784 b:0.776 a:1   ← color.error.200 (서브틀 경계)
  strokeWeight: 1
```

---

### 피드백 아이콘 (기본: alertCircle — 오류·오프라인 상태)
```
clone_node   → nodeId: "2:467"          ← icon.feedback.tokens.alertCircle
insert_child → parentId: PAT-002 frame nodeId
resize_node  → width: 20, height: 20
set_fill_color → r:0.851 g:0.173 b:0.125 a:1   ← error color.error.600
```
> 상태별 아이콘 교체:
> - 경고·대기: alertTriangle(2:472) → color.warning.500 (r:0.969 g:0.565 b:0.035)
> - 정보·중립: alertCircle(2:467) → text-secondary (r:0.443 g:0.463 b:0.502)

---

### 본문 텍스트 (caption)
```
create_text
  name: "배너-본문"
  parentId: PAT-002 frame nodeId
  text: "일부 기록이 아직 전송되지 않았습니다."
  fontSize: 14, fontWeight: 400
  fontColor: text-primary — color.gray.900 (r:0.094 g:0.114 b:0.153 a:1)
set_line_height    → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

### 액션 링크 (label — brand)
```
create_text
  name: "배너-액션"
  parentId: PAT-002 frame nodeId
  text: "자세히"
  fontSize: 14, fontWeight: 500
  fontColor: primary — color.brand.600 (r:0.498 g:0.337 b:0.851 a:1)
set_line_height    → lineHeight: 20, unit: PIXELS
set_letter_spacing → letterSpacing: 0, unit: PIXELS
```

---

## 변형 상태

| 상태 | fillColor | strokeColor | 용도 |
|------|----------|-------------|------|
| 오류·오프라인 | error-subtle color.error.50 (#fef3f2) | color.error.200 | 기본값 |
| 경고·대기 | primary-subtle color.brand.50 (#f9f5ff) | color.brand.200 (#e9d7fe) | 동기화 대기 |
| 정보·중립 | surface color.gray.50 (#fafafa) | border-subtle color.gray.100 (#f5f5f5) | 일반 안내 |

---

## 주의
- `create_component` 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
