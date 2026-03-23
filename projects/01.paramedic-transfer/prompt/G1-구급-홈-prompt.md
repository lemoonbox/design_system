# Figma 실행 프롬프트 — G1 구급 홈

## 사전 확인
- 문서: `context/figma-target.json`의 `fileKey`(프로젝트에 파일이 없으면 생성·기입 후 사용)
- 페이지: Figma 문서 내 **G1 작업용 페이지명**을 확인한 뒤 동일 이름으로 `set_current_page`
- 화면 frame 이름: `G1-구급 홈`
- 디바이스 기준: **390×844** 모바일(명령 템플릿 기준)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| PAT-001 동기화 칩 (동기화됨) | icon.baseicon.tokens.cloud | 2:647 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (오프라인) | icon.baseicon.tokens.cloudOff | 2:638 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (동기화 중) | icon.baseicon.tokens.refreshCw | 2:1058 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-004 CTA 버튼 (음성·구급일지) | icon.baseicon.tokens.mic | 2:938 | 20×20 | text-on-primary color.white (#ffffff) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 케이스·동기화 헤더 | 화면 최상단(앱 바) | 64:4585 |
| PAT-002 | 동기화·네트워크 배너 | 헤더 바로 아래(오프라인·대기·실패 시만) | 65:4595 |
| PAT-003 | 업무 단계 스텝퍼 | 본문 상단~중앙(3단계 진행) | 65:4597 |
| PAT-004 | 하단 고정 주요 CTA 바 | 화면 하단(단일 주요 행동) | 65:4618 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-005 | G1은 풀스크린 허브·요약 화면이며, 확인 모달은 M1~M4·L2→L4 경고 등 별도 레이어에서만 사용 |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{작업 페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: `G1-구급 홈`
  - x: 0, y: 0, width: **390**, height: **844**
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **0**, paddingBottom: **0**, paddingLeft: **0**, paddingRight: **0**
  - itemSpacing: **0**
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

### 3. 헤더 영역 (PAT-001)
- `get_node_info` → PAT-001 노드 확인(높이·자식 구조 파악)
- `clone_node` → PAT-001 복사
- `insert_child` → 화면 frame의 **첫 번째** 자식으로 삽입
- `set_text_content` 등으로 다음 데이터 반영:
  - **케이스 식별자** 가독 라벨(예: 「오늘 14:32 출동」) — **body** `text md` · regular **16px** / line **24px** / weight **400**, **text-primary** `color.gray.900` (**#181d27**)
  - **출동·시각** — **caption** `text sm` · regular **14px** / line **20px** / weight **400**, **text-secondary** `color.gray.500` (**#717680**)
  - **동기화 상태** — 배지·아이콘 영역에 **success** `color.success.600` (**#039855**) / **warning** `color.warning.500` (**#f79009**) / 오프라인은 **text-secondary** 또는 **error** `color.error.600` (**#d92d20**) 중 상태에 맞게 적용(색만으로 구분하지 말고 아이콘·문구 병행)

### 3b. 동기화 배너 (PAT-002, 조건부)
- 오프라인·전송 대기·실패 시에만: PAT-002 `clone` → 헤더(PAT-001) **바로 아래**에 삽입
- `get_node_info`로 배너 내 텍스트·버튼 자리 확인 후 **한 줄 요약**·**재시도/자세히(M2)** 라벨을 스펙 문구로 치환
- 배너 배경은 스펙·패턴 정의를 따르되, 본 프로젝트 토큤 범위에서는 **error-subtle** `color.error.50` (**#fef3f2**) 또는 **surface** `color.gray.50` (**#fafafa**) + **border-default** **1px** `color.gray.300` (**#d5d7da**) 조합이 자연스러움

### 4. 주요 콘텐츠 영역 (`main-content`)

- `create_frame`
  - name: `main-content`
  - parentId: 화면 frame ID
  - width: **390**
  - height: **FILL**(남은 세로 공간; PAT-001·002·004 높이에 따라 자동)
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)(또는 패턴과 동일 톤 유지)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.3xl** (**24px**), paddingBottom: **spacing.3xl** (**24px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.3xl** (**24px**)
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

#### 4a. 요약 카드 (`summary-card`) — 직접 구현
- `create_frame`
  - name: `summary-card`
  - parentId: `main-content` ID
  - width: **FILL**(좌우 패딩 **16px** 안쪽 전폭)
  - height: **HUG**
  - fillColor: **surface** `color.gray.50` (**#fafafa**)
  - stroke: **border.width.default** (**1px**), stroke 색 **border-default** `color.gray.300` (**#d5d7da**)
  - cornerRadius: **radius.xl** (**12px**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.xl** (**16px**), paddingBottom: **spacing.xl** (**16px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
- `create_text` — **subheading** `text xl` · semibold **20px** / line **30px** / weight **600`, **text-primary** (**#181d27**), text: `진행 요약`
- `create_text`(또는 가로 행) — **일지 요약 한 줄**(있을 때): **body** **16px** regular, **text-primary**
- `create_frame` — **pre-KTAS** 행(name: `row-ktas`): HORIZONTAL, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
  - 칩: `create_frame` cornerRadius **radius.md** (**8px**), fill **primary-subtle** `color.brand.50` (**#f9f5ff**), padding **spacing.lg** (**12px**) 좌우·상하, stroke **1px** **border-focus** `color.brand.600` (**#7f56d9**)(선택)
  - 칩 내부 `create_text`: **label** `text sm` · medium **14px** / line **20px** / weight **500**, **text-primary**
  - 옆 `create_text`: **caption** **14px** regular, **text-secondary** — pre-KTAS 한글 라벨
- `create_text` — **이송 상태 한 줄**(있을 때): **body** **16px** regular, **text-primary**; 거리·보조 링크가 필요하면 해당 토큰만 **accent** `color.blue.600` (**#1570ef**)로 강조

#### 4b. 단계 스텝퍼 (PAT-003)
- `get_node_info` → PAT-003 확인
- `clone_node` → `main-content`의 **요약 카드 아래**에 삽입
- 단계 라벨·마커 아이콘을 스펙 필드에 맞게 치환(마커 안 **1·2·3 숫자 금지**):
  - 고정 아이콘: **음성·구급일지** → Base **`mic`**, **증상·pre-KTAS** → **`activity`**, **이송 병원·조율** → **`truck`** (`icon-tokens.json` `figmaId`로 `clone_node`·틴트는 완료/현재/미시작 변형)
  - 각 단계 **미시작·진행중·완료**(이송은 **신청중·이송중** 등 세분화 가능)
- **보조 진입(L2/L4)**: 스텝퍼 옆 또는 스텝 행에 **caption** **14px** regular, **accent** (**#1570ef**) 링크 스타일 텍스트로 「증상·pre-KTAS」「이송 병원·조율」 진입(주요 CTA와 동일 시각적 무게 금지 — 스펙: 하단 단일 CTA만 L1)

#### 4c. 로딩·빈 상태·오류(디자인 시안용)
- **로딩**: `summary-card` 내부에 **text-secondary** (**#717680**) **caption** **14px** 자리표시 「불러오는 중…」 또는 스켈레톤 프레임(회색 **surface** + **border-subtle** **#f5f5f5**)
- **빈 상태**: `main-content`에 **body** **16px** **text-primary** 「진행 중 출동이 없습니다」+ **caption** **14px** **text-secondary** L1 진입 안내
- **오류**: **body** **16px** **error** (**#d92d20**) 메시지 + 보조 **text** **button** 스타일 **primary** (**#7f56d9**) 「다시 시도」

### 5. 하단 고정 영역 (PAT-004)
- `get_node_info` → PAT-004 확인
- `clone_node` → 화면 frame **마지막** 자식으로 삽입(헤더·본문·배너 위에 고정되도록 순서 유지)
- 주요 버튼 라벨: **「음성·구급 일지」** → L1 이동(스펙상 **유일한 주요 CTA**)
- 버튼 스타일이 패턴에 없으면 직접 보정:
  - fill **primary** `color.brand.600` (**#7f56d9**)
  - 텍스트 **button** `text md` · semibold **16px** / line **24px** / weight **600**, **text-on-primary** `color.white` (**#ffffff**)
  - cornerRadius **radius.md** (**8px**)
  - 가로 **FILL**, 상하 패딩 최소 **spacing.lg** (**12px**)~**spacing.xl** (**16px**)(터치 타깃 확보)

### 6. 검증
- `get_node_info` → 최상위 `G1-구급 홈` frame: 자식 순서 **PAT-001 → (PAT-002) → main-content → PAT-004**, 너비 **390**
- `export_node_as_image` → 시각적 확인(선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상(팔레트 키 / Hex) |
|--------|----------|----------|------------------------|
| 케이스 식별자 | PAT-001 헤더 | `text md` 16px regular | text-primary / **#181d27** |
| 출동·케이스 시작 시각 | PAT-001 헤더 | `text sm` 14px regular | text-secondary / **#717680** |
| 동기화 상태 | PAT-001 + (PAT-002) | 아이콘·배지·한 줄 | success **#039855** · warning **#f79009** · 오류 시 error **#d92d20** 등 |
| 단계: 음성·구급일지 | PAT-003 | 마커 **`mic`** + 라벨 | 완료: 마커 success + 아이콘 흰색; 라벨 gray.600 |
| 단계: 증상·pre-KTAS | PAT-003 | 마커 **`activity`** + 라벨 | 현재: 마커 brand 스트로크 + 아이콘 brand; 라벨 gray.900 medium |
| 단계: 이송 병원·조율 | PAT-003 | 마커 **`truck`** + 라벨 | 미시작: 마커 테두리만 + 아이콘 gray.500(이송중 등 세분은 라벨·상태 문구) |
| 일지 요약 한 줄 | summary-card | `text md` 16px | text-primary / **#181d27** |
| pre-KTAS 요약 | summary-card | 칩+텍스트 | 칩 배경 primary-subtle **#f9f5ff**, 테두리 선택 시 border-focus **#7f56d9** |
| 이송 상태 한 줄 | summary-card | `text md` 16px | text-primary; 보조 링크만 accent **#1570ef** |
| 음성·구급일지(주요 액션) | PAT-004 | 단일 CTA | primary **#7f56d9**, 라벨 text-on-primary **#ffffff** |
