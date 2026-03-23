# /screen-prompt {screen-id}

## 목적
단일 화면의 Figma 실행 프롬프트 파일을 생성한다.
실행 전 계획 문서이므로 Figma는 건드리지 않는다.

## 실행 전 읽기 (이 순서로)
1. `projects/{nn}.{project-name}/design-system/design-system.md` — 색상·타이포·간격·**이펙트 토큰(shadow)**·**타이포 세밀값(행간/자간)**·테두리 전체
2. `projects/{nn}.{project-name}/context/screen-specs/{screen-id}-*.md` — 이 화면의 기능명세
3. `projects/{nn}.{project-name}/design-system/patterns/_index.md` — 적용 가능한 패턴 및 노드 ID 확인
   (`/build-patterns` 실행 전이라면 노드 ID는 비어있음. 플레이스홀더로 남겨둔다)
4. `projects/{nn}.{project-name}/context/foundation/icon-tokens.json` — **아이콘 figmaId 조회**
   화면에 필요한 아이콘을 이 파일에서 찾아 figmaId를 프롬프트에 명시한다

읽기 후 Figma는 실행하지 않는다. 프롬프트 파일만 작성한다.

---

## 작성 원칙

**구체적으로 작성한다.** 추상적 지시 금지.
- ❌ "헤더를 만든다"
- ✅ "헤더 frame: width 390, height 56, fillColor gray.900(#1d2939), auto-layout HORIZONTAL, paddingLeft 16, paddingRight 16, counterAxisAlignItems CENTER"

**모든 수치는 design-system.md에서 가져온다.**
임의의 숫자 사용 금지. 팔레트 키와 hex를 함께 표기한다.

**elevation 적용 필수:**
카드·입력창·모달·플로팅 요소는 반드시 design-system의 shadow 토큰을 `set_effects`로 적용한다.
shadow와 stroke를 동시에 쓰지 않는다 — 둘 중 하나 선택.

**타이포 세밀값 필수:**
모든 텍스트 노드에 `set_line_height`와 `set_letter_spacing`을 적용한다.
design-system의 "타이포그래피 세밀값" 표 값을 사용한다. 생략 금지.

**아이콘 사용 원칙:**
- 아이콘 슬롯을 빈 placeholder frame으로 두지 않는다
- `icon-tokens.json`의 `icon.baseicon.tokens` 또는 `icon.feedback.tokens`에서 맥락에 맞는 아이콘을 찾아 `figmaId`를 확인한다
- 프롬프트에 아이콘 이름과 figmaId를 명시하고, 실행 지시는 아래 시퀀스로 작성한다:
  ```
  clone_node → nodeId: "{figmaId}"    ← icon-tokens.json의 figmaId
  insert_child → parentId: {아이콘 컨테이너 nodeId}
  resize_node → width: {size}, height: {size}   ← 20 또는 24
  set_fill_color → 아이콘 색상 (맥락에 맞는 색상 토큰)
  ```
- 적합한 아이콘이 없을 때만 빈 frame으로 남기고 이유를 명시한다

**패턴 사용 판단:**
- 자연스럽게 맞으면 사용 → 패턴 노드 ID와 함께 명시
- 화면 의도를 해치면 미사용 → 이유 명시하고 직접 구조 작성

---

## 출력: prompt/{id}-{name}-prompt.md

```markdown
# Figma 실행 프롬프트 — {ID} {화면명}

## 사전 확인
- 문서: (figma-target.json의 fileKey)
- 페이지: (작업할 페이지명)
- 화면 frame 이름: "{ID}-{화면명}"
- 디바이스 기준: (예: 390×844 모바일)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| 헤더 뒤로가기 | chevronLeft | 2:XXX | 24×24 | text-primary |
| 동기화 상태 | cloudOff | 2:XXX | 20×20 | error |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | row-data-item | 목록 각 행 | (노드ID) |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-003 | 이 화면은 단일 항목 뷰어라 행 구조 불필요 |

---

## 실행 순서

### 1. 문서 준비
- get_document_info

### 2. 화면 외부 frame
- create_frame
  - name: "{ID}-{화면명}"
  - parentId: {부모 프레임 nodeId — 08-build-screen 설정값}
  - x: {nextX — 08 Step 1에서 계산}, y: 0
  - width: 390, height: 844
  - fillColor: background(#ffffff)
- set_auto_layout
  - layoutMode: VERTICAL
  - paddingTop: 0, paddingBottom: 0, paddingLeft: 0, paddingRight: 0
  - itemSpacing: 0

### 3. 헤더 영역
- create_frame
  - name: "header"
  - parentId: {화면 frame ID}
  - width: 390, height: 56
  - fillColor: {팔레트키}(#{hex})
- set_auto_layout
  - layoutMode: HORIZONTAL
  - paddingLeft: 16, paddingRight: 16
  - counterAxisAlignItems: CENTER
  - primaryAxisAlignItems: SPACE_BETWEEN
- create_text
  - name: "header-title"
  - parentId: header frame ID
  - text: "{화면 제목}"
  - fontSize: {heading 크기}px
  - fontWeight: {heading 굵기}
  - fontColor: text-primary(#{hex})
- set_line_height → {heading line-height값}, unit: PIXELS
- set_letter_spacing → {heading letter-spacing값}, unit: PIXELS

(헤더에 아이콘이 있는 경우 — "사용 아이콘" 표 참조)
- clone_node → nodeId: "{figmaId}"        ← icon-tokens.json figmaId
- insert_child → parentId: header frame ID
- resize_node → width: 24, height: 24
- set_fill_color → {맥락 색상 r/g/b/a}

### 4. {주요 콘텐츠 영역명}
(screen-spec의 레이아웃 구조와 데이터 필드 기준으로 작성)

- create_frame
  - name: "content"
  - parentId: 화면 frame ID
  - width: 390, height: {가변 or 고정값}
  - fillColor: surface(#{hex})
- set_auto_layout
  - layoutMode: VERTICAL
  - paddingTop: {spacing값}, paddingBottom: {spacing값}
  - paddingLeft: {spacing값}, paddingRight: {spacing값}
  - itemSpacing: {spacing값}
- set_effects → shadow-sm (카드인 경우: design-system 이펙트 토큰 값 사용)
- set_corner_radius → {카드 radius값}

#### 패턴 적용 (PAT-001 사용 시)
- get_node_info → PAT-001 노드 확인
- clone_node → PAT-001 복사
- insert_child → content frame에 삽입
- set_text_content → 실제 데이터로 텍스트 교체

#### 직접 구현 (패턴 미사용 시)
(구조를 단계별로 작성)

### 5. 하단 고정 영역 (있는 경우)
- create_frame
  - name: "bottom-bar"
  - parentId: 화면 frame ID
  - width: 390, height: {height}
  - fillColor: surface(#{hex})
- (버튼, 탭 등 내부 요소 구체적으로 기술)

### 6. 검증
- get_node_info → 최상위 frame 확인
- export_node_as_image → 시각적 확인 (선택)

---

## 데이터 매핑
(screen-spec의 데이터 필드가 이 화면 어디에 어떻게 표시되는지)
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| 환자명 | 헤더 제목 | text-xl, text-primary | #{hex} |
| 상태 | 헤더 우측 | 배지, success 배경 | #{hex} |
```

저장 위치: `projects/{nn}.{project-name}/prompt/{id}-{name}-prompt.md`
