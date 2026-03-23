# 패턴 실행 프롬프트 — 구급 이송 조율 모바일 앱

## 사전 확인

- 문서: `context/figma-target.json`의 **fileKey** (파일이 없으면 사용자 제공 후 기입)
- 대상 페이지: **"Patterns"**

---

## PAT-001 — 케이스·동기화 헤더

### 등장 화면

G1, L1, L2, L4

### 구조 설명

진행 중 케이스의 **가독 라벨·시각**과 **동기화 상태**를 한 줄(또는 좌·우 그룹)로 반복 표시한다.

### 시각적 위계 (품질)

- **포컬**: 케이스 라벨(`body-strong`) → 보조 시각(`caption`) → 우측은 **스캔용** 동기화 칩(아이콘+캡션).
- **색 계층**: 루트 `background`(gray.25) 위에서 텍스트 그룹도 **동일 배경**으로 두어 “한 블록”으로 읽히게 하고, 유일한 `surface`(gray.50)는 **동기화 칩**에만 둔다(인접 면이 같은 fill로 뭉개이지 않게).
- **칩 가독성**: 칩은 `border-default`(1px, gray.300) 스트로크 권장 — 그림자와 동시 사용 금지.
- **아이콘**: 빈 `create_frame` 슬롯만 두지 말고, 문서에 이미 올라온 Base icon **컴포넌트 인스턴스**를 `clone_node`로 복사해 칩 **첫 번째 자식**으로 넣는다(`icon-tokens.json`의 `figmaId`). 새 컴포넌트 생성(`create_component_*`)은 금지.

### Figma 실행 지시

- `create_frame`
  - name: `PAT-001-케이스-동기화-헤더`
  - x: `0`, y: `0`
  - width: `390`, height: `84` — **두 줄**(라벨+보조) 기준 권장; 한 줄만 쓰면 `64`로 줄여도 됨
  - fillColor: 투명 또는 `background` — `color.gray.25` (`#fdfdfd`) (상위 화면과 동일하게 맞출 경우)
- `set_auto_layout`
  - layoutMode: `HORIZONTAL`
  - primaryAxisAlignItems: `SPACE_BETWEEN` (또는 START + 중간 스페이서)
  - paddingTop: `spacing.xl` (`16px`), paddingBottom: `spacing.xl` (`16px`)
  - paddingLeft: `spacing.xl` (`16px`), paddingRight: `spacing.xl` (`16px`)
  - itemSpacing: `spacing.lg` (`12px`)
  - counterAxisAlignItems: `CENTER` (좌·우 블록 수직 중앙 정렬)
- 내부 (왼쪽 그룹 — `create_frame` + `set_auto_layout` VERTICAL)
  - name: `헤더-텍스트-그룹`
  - 생성 후 `set_fill_color`: 루트와 동일 `color.gray.25` (`#fdfdfd`) — 기본 프레임 흰색이 남으면 라벨 블록이 떠 보임
  - itemSpacing: `spacing.xs` (`4px`) — 제목·보조를 **한 덩어리**로 읽히게; 한 줄만 쓸 경우 텍스트 1개만 두고 보조 시각은 생략 가능
  - `create_text`: 케이스 라벨 예시 `오늘 14:32 출동` — 역할 **body-strong** · `text lg` medium · `18px` / line `28px` · `color.gray.900` (`#181d27`)
  - `create_text`: 보조 시각(선택) — 역할 **caption** · `text sm` regular · `14px` / line `20px` · `color.gray.500` (`#717680`) · 예: `케이스 · 응급 이송 조율`
- 내부 (오른쪽 — 상태 그룹 `create_frame` HORIZONTAL)
  - name: `동기화-상태`
  - fillColor: `surface` — `color.gray.50` (`#fafafa`) (상태 영역 **칩**처럼 스캔되게)
  - `set_stroke_color`: `border.width.default` (`1px`) · `color.gray.300` (`#d5d7da`) — 배경과의 미세 대비(현장 조도)
  - `set_corner_radius`: `radius.md` (`8px`)
  - `set_auto_layout`: HORIZONTAL, itemSpacing `spacing.md` (`8px`), paddingTop/Bottom `spacing.sm` (`6px`), paddingLeft `spacing.md` (`8px`), paddingRight `spacing.md+2` 권장 (`10px`, 터치·광학 밸런스)
  - **동기화 아이콘 (기본 동기 완료)**: `clone_node` → 소스 nodeId는 `icon-tokens.json` Base **`cloud`**의 `figmaId` (예: `2:647`) → `insert_child`로 `동기화-상태` 프레임의 **index 0**(캡션 텍스트 앞) → `resize_node` **`20×20`**(또는 칩에 맞게 `24×24`) → `set_fill_color` **`color.gray.500`** (`#717680`, 캡션과 톤 맞춤). 상세·상태별 교체는 `PAT-001-케이스-동기화-헤더-prompt.md` 참고.
  - `create_text`: 배지 캡션 예시 `동기화됨` — **caption** · `text sm` **medium** (`500`) · `color.gray.500` (`#717680`) (상태에 따라 아래 변형 표 참고)

### 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 동기 완료 | 아이콘 인스턴스 | `cloud` (`figmaId` 토큰 참고), fill/틴트 `color.gray.500` (`#717680`), 캡션 동일 톤 |
| 동기 대기 | 캡션 색·문구·(선택) 아이콘 | `color.warning.500` (`#f79009`), 예: `동기화 대기`; 아이콘은 `refreshCw` 등 토큰에서 선택 |
| 오프라인 | 캡션 색·문구·아이콘 | `color.error.600` (`#d92d20`), 예: `오프라인`; 아이콘 `cloudOff` 토큰 `figmaId`로 인스턴스 교체 |

### 주의

- `create_component` 금지. `create_frame`만 사용한다.
- 생성 후 반환된 **nodeId**를 `_index.md`의 Figma 노드 ID에 기입한다(`/build-patterns` 이후).

---

## PAT-002 — 동기화·네트워크 배너

### 등장 화면

G1, L1, L2, L4

### 구조 설명

오프라인·전송 실패·대기 등 **한 줄 요약**과 **재시도 / 자세히(M2)** 진입을 반복 제공한다.

### Figma 실행 지시

- `create_frame`
  - name: `PAT-002-동기화-네트워크-배너`
  - x: `0`, y: `0`
  - width: `390`, height: `52`
  - fillColor: 기본 `error-subtle` — `color.error.50` (`#fef3f2`) (경고 변형은 아래 표)
- `set_auto_layout`
  - layoutMode: `HORIZONTAL`
  - paddingTop: `spacing.lg` (`12px`), paddingBottom: `spacing.lg` (`12px`)
  - paddingLeft: `spacing.xl` (`16px`), paddingRight: `spacing.xl` (`16px`)
  - itemSpacing: `spacing.lg` (`12px`)
  - counterAxisAlignItems: `CENTER`
- `create_frame` — `icon-slot` `20×20` (피드백 아이콘 `alertCircle` 등 배치용)
- `create_text` — 본문 한 줄 — 역할 **caption** · `text sm` regular · `14px` / `20px` · `color.gray.900` (`#181d27`) · 텍스트 예: `일부 기록이 아직 전송되지 않았습니다.`
- `create_text` — 액션 링크 — 역할 **label** · `text sm` medium · `14px` / `20px` · `color.brand.600` (`#7f56d9`) · 텍스트 예: `자세히` 또는 `재시도`

### 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 경고(대기) | fillColor | `primary-subtle` — `color.brand.50` (`#f9f5ff`) |
| 오류·오프라인 | fillColor | `error-subtle` — `color.error.50` (`#fef3f2`) |
| 정보(중립) | fillColor | `surface` — `color.gray.50` (`#fafafa`), 본문 `color.gray.900` 유지 |

### 주의

- `create_component` 금지. `create_frame`만 사용한다.
- 생성 후 반환된 nodeId를 기록한다.

---

## PAT-003 — 업무 단계 스텝퍼

### 등장 화면

G1, L2, L4 (L2·L4는 상단 축약 재사용)

### 구조 설명

**음성·구급일지 → 증상·pre-KTAS → 이송** 3단계 진행을 동일 구조로 표시한다.

### 시각적 위계 (품질)

- **포컬**: **현재 단계** 라벨 — `text sm` **medium** (`500`) · `color.gray.900` (`#181d27`). 완료 단계 라벨은 `color.gray.600` (`#535862`), 미시작은 `color.gray.500` (`#717680`)로 한 단계 낮춘다.
- **마커 안에는 1·2·3 숫자를 쓰지 않는다.** 단계 의미에 맞는 Base 아이콘을 `icon-tokens.json`의 `figmaId`로 `clone_node`해 마커 중앙에 둔다(약 `18×18`). PAT-001과 동일하게 **인스턴스 복제**만 사용한다.
  - 1단계(음성·구급일지): **`mic`**
  - 2단계(증상·pre-KTAS): **`activity`**
  - 3단계(이송·조율): **`truck`**
- 틴트: 완료 마커 안 아이콘은 `text-on-primary` (`#ffffff`), 현재는 `brand.600`, 미시작은 `gray.500`.

### Figma 실행 지시

- `create_frame`
  - name: `PAT-003-업무-단계-스텝퍼`
  - x: `0`, y: `0`
  - width: `390`, height: `72`
  - fillColor: 투명 또는 `background` — `color.gray.25` (`#fdfdfd`)
- `set_auto_layout`
  - layoutMode: `HORIZONTAL`
  - paddingLeft: `spacing.xl` (`16px`), paddingRight: `spacing.xl` (`16px`)
  - paddingTop: `spacing.lg` (`12px`), paddingBottom: `spacing.lg` (`12px`)
  - itemSpacing: `spacing.3xl` (`24px`)
  - primaryAxisAlignItems: `SPACE_BETWEEN` (3등분에 가깝게)
- 단계 1개당 `create_frame` (name: `step-1` … `step-3`) + `set_auto_layout` VERTICAL, itemSpacing `spacing.lg` (`12px`), horizontalAlign: `CENTER`
  - 자식 `create_frame` — 단계 마커 `32×32`, cornerRadius `16` (원형) — stroke `border.width.default` (`1px`) `color.gray.300` (`#d5d7da`), fill `surface-raised` (`#ffffff`); `set_auto_layout` HORIZONTAL, 축 정렬 CENTER
  - 마커 안: 위 3단계별 아이콘 `clone_node` → `insert_child`(index 0) → `resize_node` `18×18` → 상태에 맞는 `set_fill_color` (완료 단계는 마커 `success` + 아이콘 흰색)
  - 자식 `create_text` — 단계 라벨 — **caption** `text sm` `14px` / `20px`: 완료 `gray.600`, **현재** `gray.900` + **medium (`500`)**, 미시작 `gray.500` regular
  - 라벨 예: `음성·구급일지`, `증상·pre-KTAS`, `이송·조율`

### 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 완료 | 마커 fill / 내부 | fill `success` — `color.success.600` (`#039855`); 내부는 해당 단계 의미 아이콘(예: 1단계 **`mic`**) `clone_node` 약 `18×18`, 틴트 `text-on-primary` (`#ffffff`) |
| 완료 | 라벨 | `color.gray.600` (`#535862`), regular |
| 현재 | 마커 stroke / 안 아이콘 | stroke `border-focus` — `color.brand.600` (`#7f56d9`), `2px`; 아이콘 틴트 동일 브랜드색 |
| 현재 | 라벨 | `color.gray.900` (`#181d27`), medium (`500`) |
| 미시작 | 마커 / 안 아이콘 | fill `surface-raised` (`#ffffff`), stroke `border-default` (`#d5d7da`); 아이콘 틴트 `gray.500` |
| 미시작 | 라벨 | `color.gray.500` (`#717680`), regular |

### 주의

- 레이아웃을 바꾼 축약형(예: 가로 스크롤 3탭)은 **새 PAT**로 분리한다.
- `create_component` 금지.

---

## PAT-004 — 하단 고정 주요 CTA 바

### 등장 화면

G1, L1, L2, L4

### 구조 설명

화면 하단에 **단일 주요 행동** 버튼을 고정하고, 좌우 안전 영역을 둔다.

### Figma 실행 지시

- `create_frame`
  - name: `PAT-004-하단-고정-주요-CTA-바`
  - x: `0`, y: `0`
  - width: `390`, height: `96` (홈 인디케이터 여유 포함; 플랫폼별로 높이 조정 가능)
  - fillColor: `surface-raised` (`#ffffff`) + 상단 구분선: `create_rectangle` 또는 상단 stroke — `border-subtle` — `color.gray.100` (`#f5f5f5`), 높이 `1px` full width
- `set_auto_layout`
  - layoutMode: `VERTICAL`
  - paddingTop: `spacing.xl` (`16px`), paddingBottom: `spacing.3xl` (`24px`) (또는 안전영역 더함)
  - paddingLeft: `spacing.xl` (`16px`), paddingRight: `spacing.xl` (`16px`)
  - itemSpacing: `0`
- `create_frame` (버튼 컨테이너, HORIZONTAL, width `fill`)
  - name: `primary-cta`
  - height: `48` (최소 터치 타깃)
  - fillColor: `primary` — `color.brand.600` (`#7f56d9`)
  - cornerRadius: `radius.md` (`8px`)
  - 내부 `create_text`: 예 `음성·구급 일지` — 역할 **button** · `text md` semibold · `16px` / `24px` · `color.white` (`#ffffff`)

### 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| pressed(시각) | fillColor | `primary-pressed` — `color.brand.700` (`#6941c6`) |
| 비활성 | fillColor | `color.gray.300` (`#d5d7da`), 텍스트 `text-disabled` 동일 hex, **opacity 40%** 적용 가능 |

### 주의

- `create_component` 금지. 버튼은 `create_frame` + 텍스트로만 구성한다.

---

## PAT-005 — 2버튼 확인 모달

### 등장 화면

M1, M2, M3, M4, L2

### 구조 설명

제목·본문 아래 **취소(보조)** 와 **주요 확인** 두 버튼을 동일 배치로 반복한다(바텀시트·센터 다이얼로그 공통 뼈대).

### Figma 실행 지시

- `create_frame` (루트 패턴 프레임 — 스크린샷·배치용)
  - name: `PAT-005-2버튼-확인-모달`
  - x: `0`, y: `0`
  - width: `390`, height: `420`
  - fillColor: 투명 (딤은 별도 화면에서 `color.gray.900` 40% 오버레이로 처리하지만 **본 PAT 프레임은 패널만** 포함해도 됨)
- `create_frame` (모달 패널)
  - name: `modal-panel`
  - width: `358` (좌우 `16px` 마진 상당: 390−32), height: `auto` by layout
  - fillColor: `surface` — `color.gray.50` (`#fafafa`) 또는 `surface-raised` (`#ffffff`) — **권장** `surface-raised` (`#ffffff`)
  - cornerRadius: `radius.2xl` (`16px`)
  - stroke: `border.width.default` (`1px`) `border-default` (`#d5d7da`) (선택)
- 패널에 `set_auto_layout` VERTICAL
  - paddingTop: `spacing.xl` (`16px`), paddingBottom: `spacing.xl` (`16px`)
  - paddingLeft: `spacing.xl` (`16px`), paddingRight: `spacing.xl` (`16px`)
  - itemSpacing: `spacing.3xl` (`24px`)
- `create_text` — 제목 — **subheading** · `text xl` semibold · `20px` / `30px` · `color.gray.900` (`#181d27`) · 예: `이송 출발 확인`
- `create_text` — 본문 — **body** · `text md` regular · `16px` / `24px` · `color.gray.900` (`#181d27`) · 예시 2~3줄 플레이스홀더
- 버튼 행 `create_frame` + `set_auto_layout` HORIZONTAL, itemSpacing `spacing.lg` (`12px`), width `fill`
  - 보조 `create_frame` name: `btn-cancel` — height `48`, cornerRadius `radius.md` (`8px`), fill `surface-raised` (`#ffffff`), stroke `1px` `border-default` (`#d5d7da`), horizontal layout `fill` 균등 권장
    - 내부 `create_text`: `취소` — **button** 스타일 · `color.gray.900` (`#181d27`)
  - 주요 `create_frame` name: `btn-primary` — 동일 높이·반경, fill `primary` (`#7f56d9`)
    - 내부 `create_text`: `출발 확정` — **button** · `color.white` (`#ffffff`)

### 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 파괴적 확인 | 주요 버튼 fillColor | `error` — `color.error.600` (`#d92d20`), 텍스트 `text-on-primary` (`#ffffff`) |
| 로딩(표시용) | 주요 버튼 | 텍스트 opacity 60%, 보조 버튼 비활성과 동일 처리(구조 변경 없음) |

### 주의

- `create_component` 금지.
- 패널과 딤을 한 프레임에 묶지 않아도 되며, **패턴 간 독립 실행**을 우선한다.

---

## 공통

- 색·타이포·간격·반경은 모두 `design-system.md`와 동일; 팔레트 키와 Hex를 함께 유지한다.
- 아이콘은 `icon-tokens.json`의 Base/feedback 자산을 Figma에 배치한다(프롬프트의 `icon-slot` 프레임에 맞춤).
- 각 PAT 빌드 후 `get_node_info`로 검증한다(프로젝트 Figma 규칙).
