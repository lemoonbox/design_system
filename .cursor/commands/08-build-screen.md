# /build-screen {screen-id}

## 목적
화면 **디자인 명세서**(`prompt/{screen-id}-*-prompt.md`)를 읽고 Figma에 화면을 생성한다.
**명세서에는 MCP 명령이 없다.** agent가 디자인 의도를 해석하고 `figma-tools.md`를 참조하여 실행 계획을 수립한다.

프롬프트 파일이 없으면 먼저 `/screen-prompt {screen-id}`를 실행한다.

## 실행 전 읽기
0. `.cursor/context/figma-project-config.md` — 프로젝트 설정 확인 (채널명, 부모 프레임 nodeId)
1. `{프로젝트}/prompt/{screen-id}-*-prompt.md` — **디자인 명세** (핵심 입력)
2. `{프로젝트}/design-system/design-system.md` — 이펙트 토큰(shadow) 구체 값, 타이포 세밀값 확인
3. `{프로젝트}/design-system/visual-direction.mdc` — 시각적 판단 기준
4. `.cursor/context/figma-tools.md` — **MCP 도구, 파라미터, 제약 사항, 실행 패턴**

---

## 핵심 원칙: 디자인 명세 → 빌드 계획

화면 디자인 명세는 **디자인 의도와 토큰 값**으로 작성되어 있다. MCP 명령은 없다.
agent는 다음 순서로 실행 계획을 수립한다:

### 1단계: 시각적 의도 파악
명세의 "시각적 의도" 섹션을 읽고 **완성된 화면의 모습**을 머릿속에 그린다.
- 전체 분위기는 어떤가?
- 사용자의 시선이 먼저 가는 곳은?
- 이 화면을 "잘 디자인했다"고 느끼게 할 포인트는?

### 2단계: 레이아웃 분석
명세의 "레이아웃 구조" 섹션과 ASCII 다이어그램에서 frame 계층을 도출한다:
- 화면 최상위 frame → 영역 frame → 하위 frame → 요소 순서로 트리 구성
- 각 영역 표의 속성을 MCP 파라미터로 변환:
  - "수직 스택" → layoutMode: VERTICAL
  - "수평 스택" → layoutMode: HORIZONTAL
  - "양끝 정렬" → primaryAxisAlignItems: SPACE_BETWEEN
  - "중앙 정렬" → CENTER, "시작 정렬" → MIN, "끝 정렬" → MAX

### 3단계: 토큰 매핑
각 요소의 색상·타이포·간격·깊이를 design-system.md에서 구체 값으로 확인한다:
- shadow 토큰명 → `design-system.md` 이펙트 토큰 표에서 `set_effects` 파라미터 구성
- 타이포 역할명 → `design-system.md` 타이포 세밀값 표에서 정확한 수치 확인

### 4단계: MCP 도구 선택
`figma-tools.md`에서 도구를 매칭한다. 반드시 확인할 섹션:
- **생성·수정·텍스트 스타일** — 파라미터 정확한 형식 확인
- **MCP 미지원 항목** — STRETCH/fill/hug/transparent 대체 방법
- **실행 계획 패턴** — 카드 레이아웃, 아이콘 복제 등 시퀀스 참고

---

## 실행 흐름

### Step 1. 사전 확인

```
join_channel → channel: "{rvecoa2p}"
get_node_info → nodeId: "{65:4639}"
```

- 프레임 존재 확인
- nextX 계산: `max(child.x + child.width) + 40` (없으면 0)
- 오류 시 즉시 중단, nodeId 재확인 요청
- 동일 화면 frame이 이미 존재 시 → 사용자에게 "덮어쓸까요, 새로 만들까요?" 확인

### Step 2. 빌드 계획 수립

디자인 명세를 해석하고 **실행 전에** 계획을 정리한다:

```
빌드 계획 — {screen-id} {화면명}

Phase 1: 구조
1. 화면 frame — 390×844, {배경}, 수직 스택
2. 헤더 영역 — {크기}, {배경}, {배치}
3. 콘텐츠 영역 — {크기}, {배경}, {배치}
4. 하단 CTA — {크기}, {배경}, {배치}

Phase 2: 콘텐츠
5. 헤더 텍스트·아이콘
6. 패턴 적용: PAT-{ID} clone → insert → 텍스트 교체
7. 직접 구현 요소: {목록}

Phase 3: 시각 품질
8. elevation 적용 — {대상별 shadow 토큰}
9. 타이포 세밀값 확인 — 모든 텍스트에 font_name + line_height + letter_spacing
10. surface depth 확인 — 인접 요소 fill 대비

Phase 4: 검증
11. export_node_as_image → 시각 확인
```

### Step 3. 실행

빌드 계획의 Phase 순서대로 실행한다.

#### Phase 1: 구조 (Structure)
명세의 레이아웃 구조를 따라 frame 트리를 생성한다.
- 화면 최상위 frame → 영역 frame → 하위 frame 순서
- 각 frame에 auto-layout + padding + spacing 설정
- fill color 적용 (투명은 `{r:0, g:0, b:0, a:0}` + **무조건** `set_fill_color a:0` 재적용, 확인 생략)

#### Phase 2: 콘텐츠 (Content)
구조 위에 텍스트·아이콘·패턴을 배치한다.

**텍스트 생성 (모든 텍스트 노드에 필수)**:
1. `create_text` — fontSize, fontWeight, fontColor
2. `set_font_name` — fontFamily + style (400→Regular, 500→Medium, 600→SemiBold)
3. `set_line_height` — 행간 (unit: PIXELS)
4. `set_letter_spacing` — 자간 (unit: PIXELS)

**아이콘 배치** (`figma-tools.md` "아이콘 복제 후 컨테이너 삽입" 참조):
1. `get_node_info` → figmaId 원본 구조 확인
2. `clone_node` → 복제
3. `insert_child` → 컨테이너 삽입
4. `move_node` → (0,0) 재배치 (**필수**)
5. `resize_node` → 크기 적용
6. 색상 — 원본 구조에 따라:
   - 단일 VECTOR: `set_fill_color` 직접
   - GROUP/FRAME: children 탐색 → 각 path에 개별 적용
   - 실패 시: `flatten_node` → 재시도, 또는 원본 유지 + 보고
7. `get_node_info` → 검증

**패턴 적용** (명세의 "사용 패턴" 표 참조):
1. `get_node_info` → 패턴 노드 존재 확인
2. `clone_node` → 복사
3. `insert_child` → 대상 frame에 삽입
4. `move_node` → 위치 조정
5. 텍스트 교체: `scan_text_nodes` → 대상 텍스트 nodeId 확인 → `set_text_content` / `set_multiple_text_contents`
6. 필요 시 색상·아이콘 교체

> 패턴 노드 ID가 비어있으면 `/build-patterns`가 먼저 필요. 사용자에게 알리고 중단.

#### Phase 3: 시각 품질 (Visual Polish)
디자인 명세의 "Visual Recipe" 섹션을 기준으로 보정한다.
Phase 2에서 이미 적용한 항목은 재검사하지 않는다.

**Elevation** (Phase 2에서 미적용된 경우만):
- 명세의 "Elevation" 표에 shadow 토큰이 명시된 요소 중 Phase 2에서 누락된 것만 `set_effects` 적용
- shadow와 stroke가 동시에 적용된 요소가 있으면 stroke 제거

**Surface Depth** (명세에서 "부족" 판정된 경우만):
- 명세의 "Surface Depth" 표에서 "부족" 판정된 요소만 fill color 보정 또는 border-subtle 적용

### Step 4. 검증 (선별적)

#### 4-a. 구조 검증 [선택]
조건: 복잡한 다중 영역 또는 새로운 레이아웃 구조
실행: export_node_as_image → 전체 프레임 배치, 영역 분리 확인
체크:
- [ ] 전체 레이아웃이 명세 다이어그램과 일치?
- [ ] 각 영역 배치 순서가 맞는가?
- [ ] 여백 리듬이 일관되는가?

#### 4-b. 스타일 검증 [선택]
조건: 색상/shadow 여러 개 또는 복잡한 surface depth
실행: export_node_as_image → 색상 톤, 깊이감 확인
체크:
- [ ] 색상 계층이 명확한가 (배경 → 카드 → 요소 → 텍스트)?
- [ ] 카드·모달에 shadow가 적용되어 깊이감이 있는가?
- [ ] 색상 톤이 설계된 분위기와 일치?

#### 4-c. 최종 검증 [필수]
조건: 모든 경우
실행: export_node_as_image → 전체 시각 확인
체크:
- [ ] 전체 분위기가 "시각적 의도"와 일치?
- [ ] focal point가 명확하게 눈에 들어오는가?
- [ ] 아이콘이 정상 렌더되는가 (단색 블록 아님)?
- [ ] 텍스트 위계가 명확한가 (제목 > 본문 > 보조)?
- [ ] 완성되었다는 느낌이 드는가?

## 검증 생략 규칙

다음 경우 구조/스타일 검증 스킵 가능:
- 단일 영역 또는 극도로 단순한 화면
- 이미 검증된 패턴만 적용
- 명세가 매우 상세한 경우 (레이아웃 동일)

최종 검증은 항상 필수. 결과 이미지를 검토하고 사용자에게 보고한다.

---

## 실행 규칙
- `create_component` 절대 금지
- x, y는 부모 프레임 내부 좌표 기준
- 디자인 명세에 없는 시각적 선택이 필요하면 사용자에게 확인
- MCP 미지원 값은 `figma-tools.md` 대체 방법 적용

---

## 완료 보고
```
완료: {screen-id} — {화면명}
frame nodeId: {id}
사용 패턴: {PAT 목록 또는 "없음"}
시각 검증: {통과 / 수정 사항}
이슈: {있다면 구체적으로}
```

## 실패 시
- 오류 내용을 그대로 보고한다
- 부분 완료된 노드 ID를 명시한다
- 재시도는 1회. 동일 오류 반복 시 중단하고 보고한다
- 롤백(delete_node) 필요 시 사용자 확인 후 실행한다
