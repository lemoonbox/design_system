# Figma 실행 프롬프트 — L4 이송 병원 추천·조율

## 사전 확인
- 문서: `context/figma-target.json`의 `fileKey`(프로젝트에 파일이 없으면 생성·기입 후 사용)
- 페이지: Figma 문서 내 **L4 작업용 페이지명**을 확인한 뒤 동일 이름으로 `set_current_page`
- 화면 frame 이름: `L4-이송-병원-추천-조율`
- 디바이스 기준: **390×844** 모바일(명령 템플릿 기준)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| app-nav 뒤로 버튼 | icon.baseicon.tokens.chevronLeft | 2:599 | 20×20 | text-primary color.gray.900 (#181d27) |
| PAT-001 동기화 칩 (동기화됨) | icon.baseicon.tokens.cloud | 2:647 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (오프라인) | icon.baseicon.tokens.cloudOff | 2:638 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (동기화 중) | icon.baseicon.tokens.refreshCw | 2:1058 | 20×20 | text-secondary color.gray.500 (#717680) |
| row-distance 거리 아이콘 | icon.baseicon.tokens.mapPin | 2:911 | 20×20 | accent color.blue.600 (#1570ef) |
| badge-transfer-status 승인 | icon.feedback.tokens.checkCircle | 2:588 | 20×20 | success color.success.600 (#039855) |
| badge-transfer-status 신청중 | icon.baseicon.tokens.clock | 2:629 | 20×20 | warning color.warning.500 (#f79009) |
| badge-transfer-status 거절·무응답 | icon.feedback.tokens.alertCircle | 2:467 | 20×20 | error color.error.600 (#d92d20) |
| btn-depart 출발 확인 버튼 | icon.baseicon.tokens.arrowRight | 2:516 | 20×20 | text-on-primary color.white (#ffffff) |
| PAT-004 CTA 버튼 (병원 도착, 이송 중 모드) | icon.baseicon.tokens.checkSquare | 2:590 | 20×20 | text-on-primary color.white (#ffffff) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 케이스·동기화 헤더 | `mode-header` 아래(케이스·시각·동기화·오프라인) | 64:4585 |
| PAT-002 | 동기화·네트워크 배너 | PAT-001 바로 아래(오프라인·전송 대기·실패 시만) | 65:4595 |
| PAT-003 | 업무 단계 스텝퍼 | 배너(있으면) 아래 — L4는 **상단 축약**(G1·L2와 동일 3단계 축) | 65:4597 |
| PAT-004 | 하단 고정 주요 CTA 바 | 화면 하단 — **이송 중** 모드에서만 **「병원 도착」**(M4 트리거). **추천·신청** 모드에서는 클론 후 높이 **HUG**·내부 비우거나 시안용 안내 **caption** 한 줄만(카드 액션이 주행동) | 65:4618 |
| PAT-005 | 2버튼 확인 모달 | **별도 오버레이 프레임** ×2 — **M1**(출발 최종 확인), **M4**(케이스 완료 확인) | 65:4624 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| — | 인덱스의 PAT-001~005는 L4에서 모두 사용한다. **병원 카드**는 `design-system.md` 공통 목록의 **L4 전용**으로 패턴 인덱스에 노드 ID 없음 → 본 프롬프트 **직접 구현**으로 복제 프레임 만든다. PAT-005는 기본 화면과 **분리된 모달 프레임**으로만 구현한다. |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{작업 페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: `L4-이송-병원-추천-조율`
  - x: 0, y: 0, width: **390**, height: **844**
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **0**, paddingBottom: **0**, paddingLeft: **0**, paddingRight: **0**
  - itemSpacing: **0**
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

### 3. 앱 네비게이션 (`app-nav`) — 직접 구현
- `create_frame`
  - name: `app-nav`
  - parentId: 화면 frame ID
  - width: **390**, height: **56**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
  - stroke: 하단만 **border.width.default** (**1px**), stroke 색 **border-subtle** `color.gray.100` (**#f5f5f5**)(도구가 전면만 지원 시 **1px** **border-default** `color.gray.300` (**#d5d7da**)로 대체)
- `set_auto_layout`
  - layoutMode: **HORIZONTAL**
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - counterAxisAlignItems: **CENTER**, primaryAxisAlignItems: **MIN**
- 아이콘 슬롯: **뒤로** — `icon.baseicon` · **navigation** · `chevronLeft`, 크기 **sm**(`icon-tokens.json`의 sm 수치)
- `create_text`
  - name: `nav-title`
  - parentId: `app-nav` ID
  - text: `이송·병원`
  - fontFamily: **Inter**
  - fontSize: **30px**, lineHeight: **38px**, fontWeight: **600** — **heading** `display sm` · semibold
  - fontColor: **text-primary** `color.gray.900` (**#181d27**)

### 4. 모드·맥락 헤더 (`mode-header`) — 직접 구현
- `create_frame`
  - name: `mode-header`
  - parentId: 화면 frame ID
  - width: **390**, height: **HUG**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
- `set_auto_layout`
  - layoutMode: **HORIZONTAL**
  - paddingTop: **spacing.lg** (**12px**), paddingBottom: **spacing.lg** (**12px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - counterAxisAlignItems: **CENTER**, primaryAxisAlignItems: **SPACE_BETWEEN**
- 좌측 `create_frame` name: `badge-mode`, cornerRadius: **radius.md** (**8px**), fill: **primary-subtle** `color.brand.50` (**#f9f5ff**), stroke: **border.width.default** (**1px**) **border-focus** `color.brand.600` (**#7f56d9**), 내부 HORIZONTAL padding **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
  - `create_text` — **label** `text sm` · medium **14px** / line **20px** / weight **500**, **text-primary** (**#181d27**), 시안 텍스트: `추천·신청`(또는 `이송 중` 변형 프레임 병행)
- 우측(이송 중 시안): `create_text` name: `departure-hospital-summary` — **caption** `text sm` · regular **14px** / line **20px** / weight **400**, **text-secondary** `color.gray.500` (**#717680**), text: `출발: ○○병원`(플레이스홀더; **선택된 출발 병원** 필드)

### 5. 케이스·동기화 (PAT-001)
- `get_node_info` → PAT-001 노드 확인
- `clone_node` → PAT-001 복사
- `insert_child` → `mode-header` **아래**에 삽입
- `set_text_content` 등으로 케이스 라벨·시각·동기화 배지 반영 — 타이포·색은 L2 프롬프트 PAT-001 절과 동일(**body** `text md` · regular **16px** / **24px** / **400** **text-primary**, **caption** **14px** **text-secondary**, 상태 **success** **#039855** / **warning** **#f79009** / **error** **#d92d20** + 아이콘·문구 병행)

### 5b. 동기화 배너 (PAT-002, 조건부)
- 오프라인·전송 대기·실패 시에만: PAT-002 `clone` → PAT-001 **바로 아래** 삽입
- 배경·테두리: L2 프롬프트 5b·G1과 동일(**error-subtle** `color.error.50` **#fef3f2** 또는 **surface** `color.gray.50` **#fafafa** + **border-default** **1px** **#d5d7da**)

### 5c. L2 필수 미충족 경고 띠(조건부) — 직접 구현
- L2 미충족 진입 시만: `create_frame` name: `banner-l2-warning`, width **FILL**, height **HUG**, fill **surface** `color.gray.50` (**#fafafa**), stroke **border.width.medium** (**2px**) 좌측만 시각적 강조 가능 시 stroke 색 **warning** `color.warning.500` (**#f79009**)(전면 스트로크 불가 시 상단 **1px** **border-default**로 대체하고 본문에 **icon.feedback** · `alertTriangle` **sm** 병행)
- padding: **spacing.xl** (**16px**), auto-layout VERTICAL, itemSpacing **spacing.lg** (**12px**)
- `create_text` — **body** **16px** regular **text-primary**, 한 줄 요약 + `create_text` 링크 스타일 **accent** `color.blue.600` (**#1570ef**) **text md** semibold `L2에서 보완`(스펙 동작 반영)

### 6. 업무 단계 스텝퍼 축약 (PAT-003)
- `get_node_info` → PAT-003 확인 후 `clone_node` → (PAT-002 또는 `banner-l2-warning` 유무에 따라 그 아래, 없으면 PAT-001 아래) 삽입
- 단계 라벨: **음성·구급일지** / **증상·pre-KTAS** / **이송 병원·조율**(현재 단계 강조)
- 현재 단계: **primary** **#7f56d9** 또는 **border-focus** 링; 완료 단계는 **success** **#039855** 아이콘+문구(색만 구분 금지)
- L4는 디자인 시스템 **상단 축약** 지침으로 높이·라벨 길이 압축

### 7. 주요 콘텐츠 영역 (`main-content`)

- `create_frame`
  - name: `main-content`
  - parentId: 화면 frame ID
  - width: **390**
  - height: **FILL**
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.3xl** (**24px**), paddingBottom: **spacing.3xl** (**24px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

#### 7a. 목록 메타(선택)
- `create_text` name: `list-meta` — **meta** `text xs` · regular **12px** / line **18px** / weight **400**, **text-secondary** (**#717680**), text: `목록 갱신 · 14:32`( **추천 목록 버전·타임스탬프** 필드)

#### 7b. 병원 카드 (`hospital-card`) — 직접 구현(복제용 원본 1개 후 duplicate)
- `create_frame`
  - name: `hospital-card`
  - parentId: `list-stack` 또는 직접 `main-content`(아래 `list-stack` 권장)
  - width: **FILL** (부모 폭 **358** = **390** − **16**×2)
  - height: **HUG**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
  - stroke: **border.width.default** (**1px**), stroke 색 **border-default** `color.gray.300` (**#d5d7da**)
  - cornerRadius: **radius.xl** (**12px**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.xl** (**16px**), paddingBottom: **spacing.xl** (**16px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

**카드 상단 행 (`card-top-row`)** — HORIZONTAL, width **FILL**, primaryAxisAlignItems **SPACE_BETWEEN**, counterAxisAlignItems **CENTER**, itemSpacing **spacing.lg** (**12px**)
- `create_text` name: `hospital-name` — **body-strong** `text lg` · medium **18px** / line **28px** / weight **500**, **text-primary** (**#181d27**), text: `○○대학교병원`
- `create_frame` name: `badge-transfer-status`, cornerRadius **radius.md** (**8px**), padding **spacing.lg** (**12px**) HORIZONTAL, counterAxisAlignItems **CENTER**, fill·stroke는 상태별:
  - **승인**: fill **success** 배경 대신 가독성 위해 **surface** **#fafafa** + stroke **1px** **success** **#039855**, 글자 **success** **#039855** + **icon.feedback** `checkCircle` **sm**
  - **신청중**: fill **warning** 과한 면적 피하고 **surface** **#fafafa** + **caption** **warning** **#f79009** + `clock` **sm**
  - **거절·무응답**: **error** **#d92d20** 문구 + `alertCircle` **sm**, 배경 **error-subtle** **#fef3f2** 선택
  - **미신청**: stroke **1px** **border-default**, fill **surface-raised**, **caption** **text-secondary**
- 내부 텍스트: **caption** **14px** regular 또는 **label** **14px** medium — 상태명 `승인` 등(색+아이콘+문구 병행)

**여유 병상 (`row-beds`)**
- `create_frame` HORIZONTAL, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
- `create_text` — **label** **14px** medium **text-primary**, `여유 병상`
- `create_frame` name: `badge-beds`, **radius.md** (**8px**), padding **spacing.lg** (**12px**), fill **primary-subtle** **#f9f5ff**, stroke **1px** **border-default**, `create_text` — **body** **16px** regular **text-primary**, text: `ICU 2병상`(또는 `가용`/`부족` 배지 카피)

**거리 (`row-distance`)**
- HORIZONTAL, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
- 아이콘: `mapPin` 또는 `navigation` 계열 **sm**(**icon-tokens.json**), 색 **accent** **#1570ef**
- `create_text` — **body** **16px** regular, **accent** **#1570ef** 강조: `12.4 km · 약 18분`( **거리** 필드)

**처치 가능 의료과 (`row-specialties`)**
- `create_frame` layoutMode **HORIZONTAL**, wrap 시 Figma에서 별도 행 분할 또는 세로 스택에 칩 나열; itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
- 칩: cornerRadius **radius.md** (**8px**), fill **surface** **#fafafa**, stroke **1px** **border-default** **#d5d7da**, padding HORIZONTAL·VERTICAL **spacing.lg** (**12px**), 텍스트 **label** **14px** medium **text-primary** — 예: `신경외과`, `흉부외과`, `소아과`

**추천 사유(선택) (`row-reason`)**
- `create_text` — **caption** **14px** regular **text-secondary** (**#717680**), text: `권역 내 신경외과 가용·거리 우선`( **추천 사유 한 줄**)

**승인 시각·메시지(선택) (`row-approval-meta`)**
- `create_text` — **meta** **12px** regular **text-secondary**, text: `승인 14:05 · 수용 가능`( **승인 시각·메시지**)

**카드 액션 행 (`card-actions`)** — HORIZONTAL, width **FILL**, itemSpacing **spacing.lg** (**12px**), primaryAxisAlignItems **MIN**, counterAxisAlignItems **CENTER**
- **이송 신청** 버튼(`btn-request`): 노출 조건 시만 — height 최소 터치 목표, cornerRadius **radius.md** (**8px**), fill **primary** **#7f56d9**, 텍스트 **button** `text md` · semibold **16px** / **24px** / **600**, **text-on-primary** **#ffffff**, padding 좌우 **spacing.xl** (**16px**) 이상
- **재신청** 버튼: 동일 크기, fill **surface-raised**, stroke **1px** **border-default**, 텍스트 **button** **16px** semibold **text-primary**(거절·무응답 시)
- **출발** 버튼(`btn-depart`): **승인** 카드만 — fill **primary** **#7f56d9**, 텍스트 동일 토큰 **text-on-primary**; 비승인 카드에서는 **미생성** 또는 숨김(스펙: 비승인 출발 숨김·비활성)

**이송 중 모드 변형(타 카드)**
- 동일 카드 프레임에 opacity 낮추거나 fill **surface** **#fafafa**, 상단 `create_text` **caption** **text-secondary** `신청 취소됨`(또는 **text-disabled** **#d5d7da** 메타) — **전체 이송 모드** = 이송 중일 때 표현

#### 7c. 목록 컨테이너 (`list-stack`)
- `create_frame` name: `list-stack`, parentId `main-content`, width **FILL**, height **HUG**, fill transparent, auto-layout VERTICAL, itemSpacing **spacing.lg** (**12px**)
- `hospital-card`를 자식으로 두고 **duplicate**로 2~3장 시안

#### 7d. 로딩·빈·오류 상태(시안 변형)
- **로딩**: `skeleton-card` × 2~3 — width **FILL**, fill **surface** `color.gray.50` (**#fafafa**), cornerRadius **radius.xl** (**12px**), padding **spacing.xl** (**16px**), auto-layout VERTICAL itemSpacing **spacing.lg** (**12px**); 자식 막대 **3**개 각 height **spacing.3xl** (**24px**), width **FILL**, fill **border-subtle** `color.gray.100` (**#f5f5f5**); 목록 상단 **caption** **14px** **text-secondary** `불러오는 중…`
- **빈 추천**: `main-content` 중앙 세로 스택 itemSpacing **spacing.3xl** (**24px**) — **subheading** **20px** semibold **text-primary** `추천 병원이 없습니다`, **body** **16px** **text-secondary** `증상·pre-KTAS를 보완하면 목록이 달라질 수 있습니다`, 텍스트 버튼 **accent** **#1570ef** **16px** semibold `L2로 이동`
- **오류**: **body** **16px** **error** **#d92d20** + **primary** **16px** semibold 링크 스타일 `다시 시도`

### 8. 하단 고정 영역 (PAT-004)
- `get_node_info` → PAT-004 확인
- `clone_node` → 화면 frame **마지막** 자식으로 삽입
- **이송 중** 시안: 단일 주요 버튼 **「병원 도착」** — fill **primary** **#7f56d9**, **button** **16px** semibold **600**, **text-on-primary** **#ffffff**, cornerRadius **radius.md** (**8px**), 패딩·하단 안전영역은 PAT-004 정의 준수; 없으면 paddingBottom **spacing.xl** (**16px**)
- **추천·신청** 시안: 바 내부를 비우고 높이 **HUG** + **caption** **14px** **text-secondary** `카드에서 이송 신청·출발`(선택) 또는 PAT-004 레이어 가시성 off

### 9. 모달 오버레이 — M1 출발 확인 (PAT-005)
- `create_frame` name: `L4-M1-departure-modal`, width **390**, height **844**, fill **text-primary** `color.gray.900` (**#181d27**) **50%** 투명(미지원 시 별도 반투명 사각)
- 중앙 `modal-card`: width **358**, fill **surface-raised** **#ffffff**, cornerRadius **radius.2xl** (**16px**), stroke **1px** **border-default** **#d5d7da**, padding **spacing.3xl** (**24px**)
- `get_node_info` → PAT-005 `clone` 후 제목·본문·버튼 배치
- 제목: **subheading** `text xl` · semibold **20px** / **30px** / **600** **text-primary**
- 본문: **body** **16px** regular **text-primary** — 예: `선택한 병원으로 출발합니다. 다른 병원 신청은 취소됩니다.`
- 버튼 행 HORIZONTAL, itemSpacing **spacing.lg** (**12px**):
  - **취소**: stroke **1px** **border-default**, fill **surface-raised**, **button** **16px** semibold **text-primary**
  - **출발 확인**: fill **primary** **#7f56d9**, **button** **16px** semibold **text-on-primary** **#ffffff**, cornerRadius **radius.md** (**8px**)

### 10. 모달 오버레이 — M4 케이스 완료 (PAT-005)
- `create_frame` name: `L4-M4-complete-modal`, 동일 오버레이·`modal-card` 토큰
- PAT-005 `clone` 후 카피만 교체
- 제목·본문: **subheading** **20px** semibold / **body** **16px** regular **text-primary** — 예: `케이스를 완료할까요?` / `병원 도착을 확인했습니다. 이번 케이스를 종료합니다.`
- 버튼: **취소**(보조, 위와 동일) / **완료**(주요 — fill **primary** **#7f56d9**, 텍스트 **text-on-primary**)

### 11. 검증
- `get_node_info` → 최상위 `L4-이송-병원-추천-조율`: 자식 순서 **app-nav → mode-header → PAT-001 → (PAT-002) → (banner-l2-warning) → PAT-003 → main-content → PAT-004**, 너비 **390**
- 모달 프레임(M1/M4)은 가시성 끄거나 별도 페이지 배치
- `export_node_as_image` → 시각적 확인(선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| (네비 제목) | `nav-title` | **heading** 30px semibold | **text-primary** **#181d27** |
| 전체 이송 모드 | `badge-mode` 등 | 칩 라벨 `추천·신청` / `이송 중` | 배경 **primary-subtle** **#f9f5ff**, 테두리 **border-focus** **#7f56d9**, 글자 **text-primary** |
| 선택된 출발 병원 ID | `departure-hospital-summary` | **caption** 14px | **text-secondary** **#717680** |
| 케이스·시각·동기화 | PAT-001 | 텍스트·배지·아이콘 | **text-primary** / **text-secondary** / **success·warning·error** |
| 동기화·오류 | PAT-002 | 한 줄+액션 | **error-subtle** 또는 **surface** + **border-default** |
| L2 미충족 경고 | `banner-l2-warning` | 본문+링크 | 본문 **text-primary**, 링크 **accent** **#1570ef** |
| 업무 단계 | PAT-003 | 3단계 축약 — 마커 **`mic`·`activity`·`truck`**(숫자 없음) | 현재 **primary** **#7f56d9**, 완료 **success** **#039855**+해당 아이콘 흰색 |
| 추천 목록 타임스탬프 | `list-meta` | **meta** 12px | **text-secondary** **#717680** |
| 병원명 | `hospital-name` | **body-strong** 18px medium | **text-primary** **#181d27** |
| 여유 병상 | `badge-beds` | 배지+수치/가용 | **primary-subtle** 또는 **surface**+테두리, 글자 **text-primary** |
| 거리 | `row-distance` | 아이콘+문구 | **accent** **#1570ef** |
| 처치 가능 의료과 | `row-specialties` 칩들 | **label** 14px medium | 칩 **surface** **#fafafa**, **border-default** |
| 추천 사유 | `row-reason` | **caption** 14px | **text-secondary** **#717680** |
| 이송 신청 상태 | `badge-transfer-status` | 배지+아이콘+문구 | 상태색 **success** / **warning** / **error** + 형태 병행 |
| 승인 시각·메시지 | `row-approval-meta` | **meta** 12px | **text-secondary** |
| 이송 신청 / 재신청 | `btn-request` 등 | 주요 또는 테두리 버튼 | **primary** **#7f56d9**+**text-on-primary** 또는 **surface-raised**+**border-default** |
| 출발 | `btn-depart` | 주요 버튼 | **primary** **#7f56d9**, **text-on-primary** **#ffffff** |
| 병원 도착 | PAT-004 | 하단 고정 CTA | **primary** **#7f56d9**, **text-on-primary** |
| M1 / M4 카피 | 각 모달 `modal-card` | 제목·본문·2버튼 | 본문 **text-primary**, 주요 버튼 **primary** |
