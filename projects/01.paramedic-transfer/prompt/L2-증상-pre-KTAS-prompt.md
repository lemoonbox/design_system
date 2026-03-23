# Figma 실행 프롬프트 — L2 증상·pre-KTAS

## 사전 확인
- 문서: `context/figma-target.json`의 `fileKey`(프로젝트에 파일이 없으면 생성·기입 후 사용)
- 페이지: Figma 문서 내 **L2 작업용 페이지명**을 확인한 뒤 동일 이름으로 `set_current_page`
- 화면 frame 이름: `L2-증상·pre-KTAS`
- 디바이스 기준: **390×844** 모바일(명령 템플릿 기준)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| app-nav 뒤로 버튼 | icon.baseicon.tokens.chevronLeft | 2:599 | 20×20 | text-primary color.gray.900 (#181d27) |
| PAT-001 동기화 칩 (동기화됨) | icon.baseicon.tokens.cloud | 2:647 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (오프라인) | icon.baseicon.tokens.cloudOff | 2:638 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (동기화 중) | icon.baseicon.tokens.refreshCw | 2:1058 | 20×20 | text-secondary color.gray.500 (#717680) |
| section-symptom 필수 항목 확인 | icon.feedback.tokens.checkCircle | 2:588 | 20×20 | success color.success.600 (#039855) |
| section-symptom 필수 항목 미충족 | icon.feedback.tokens.alertCircle | 2:467 | 20×20 | warning color.warning.500 (#f79009) |
| PAT-004 CTA 버튼 (병원 추천·이송) | icon.baseicon.tokens.checkSquare | 2:590 | 20×20 | text-on-primary color.white (#ffffff) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 케이스·동기화 헤더 | 앱 네비·pre-KTAS 상태 행 아래(케이스 맥락·동기화) | 64:4585 |
| PAT-002 | 동기화·네트워크 배너 | PAT-001 바로 아래(오프라인·대기·실패 시만) | 65:4595 |
| PAT-003 | 업무 단계 스텝퍼 | 본문 상단(디자인 시스템: L2는 **상단 축약** 변형) | 65:4597 |
| PAT-004 | 하단 고정 주요 CTA 바 | 화면 하단 — 주행동 **「병원 추천·이송」** | 65:4618 |
| PAT-005 | 2버튼 확인 모달 | **별도 오버레이 프레임**(필수 미충족 + CTA 시) | 65:4624 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| — | 인덱스의 PAT-001~005는 L2 플로우에서 모두 사용한다. PAT-005는 기본 화면과 **분리된 모달 프레임**으로만 구현한다. |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{작업 페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: `L2-증상·pre-KTAS`
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
  - stroke: 하단만 **border.width.default** (**1px**), stroke 색 **border-subtle** `color.gray.100` (**#f5f5f5**)(전면 스트로크 대신 하단 구분선만 권장; 도구가 전면 스트로크만 지원하면 **1px** **border-default** `color.gray.300` (**#d5d7da**)로 대체)
- `set_auto_layout`
  - layoutMode: **HORIZONTAL**
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - counterAxisAlignItems: **CENTER**, primaryAxisAlignItems: **MIN**
- 아이콘 슬롯: **뒤로** — `icon.baseicon` · **navigation** · `chevronLeft`, 크기 **sm**(foundation `icon-tokens.json`의 sm 수치 적용)
- `create_text`
  - name: `nav-title`
  - parentId: `app-nav` ID
  - text: `증상·pre-KTAS`
  - fontFamily: **Inter**
  - fontSize: **30px**, lineHeight: **38px**, fontWeight: **600** — **heading** `display sm` · semibold
  - fontColor: **text-primary** `color.gray.900` (**#181d27**)

### 4. pre-KTAS 상태 헤더 (`prektas-header`) — 직접 구현
- `create_frame`
  - name: `prektas-header`
  - parentId: 화면 frame ID
  - width: **390**, height: **HUG**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
- `set_auto_layout`
  - layoutMode: **HORIZONTAL**
  - paddingTop: **spacing.lg** (**12px**), paddingBottom: **spacing.lg** (**12px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
  - counterAxisAlignItems: **CENTER**, primaryAxisAlignItems: **MIN**
- `create_text` — **caption** `text sm` · regular **14px** / line **20px** / weight **400**, **text-secondary** `color.gray.500` (**#717680**), text: `선택 등급`
- `create_frame` — name: `badge-prektas-selected`
  - cornerRadius: **radius.md** (**8px**)
  - fillColor: **primary-subtle** `color.brand.50` (**#f9f5ff**)
  - stroke: **border.width.medium** (**2px**), stroke 색 **border-focus** `color.brand.600` (**#7f56d9**)
  - 내부 auto-layout HORIZONTAL, padding 좌우·상하 **spacing.lg** (**12px**), itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
  - `create_text` — **body-strong** `text lg` · medium **18px** / line **28px** / weight **500**, **text-primary** (**#181d27**), text: `3 · 응급`(시안용; 실제 등급·명칭은 스펙 표준 명칭으로 치환)
  - (선택) `create_text` — **caption** **14px** regular, **text-secondary**, 스펙 요약 한 줄(카드·툴팁용 문구 중 짧은 버전)

### 5. 케이스·동기화 (PAT-001)
- `get_node_info` → PAT-001 노드 확인
- `clone_node` → PAT-001 복사
- `insert_child` → `prektas-header` **아래**에 삽입
- `set_text_content` 등으로 케이스 라벨·시각·동기화 배지를 L2 데이터에 맞게 반영 — 타이포·색은 G1 프롬프트 PAT-001 절과 동일 토큰(**body** **16px** **text-primary**, **caption** **14px** **text-secondary**, 상태색 **success** **#039855** / **warning** **#f79009** / **error** **#d92d20** 등)

### 5b. 동기화 배너 (PAT-002, 조건부)
- 오프라인·전송 대기·실패 시에만: PAT-002 `clone` → PAT-001 **바로 아래** 삽입
- 배너 배경·테두리: G1 프롬프트 3b와 동일(**error-subtle** **#fef3f2** 또는 **surface** **#fafafa** + **border-default** **1px** **#d5d7da**)

### 6. 업무 단계 스텝퍼 축약 (PAT-003)
- `get_node_info` → PAT-003 확인 후 `clone_node` → (PAT-002가 있으면 그 아래, 없으면 PAT-001 아래) 삽입
- 단계 라벨: **음성·구급일지** / **증상·pre-KTAS**(현재 단계 강조) / **이송 병원·조율** — 마커 안은 **`mic` / `activity` / `truck`** 고정 아이콘(숫자 없음, `icon-tokens.json` `clone_node`)
- L2 시안에서는 **증상·pre-KTAS** 단계에 **primary** **#7f56d9** 또는 **border-focus** 링, 완료 단계는 **success** 마커 + 해당 아이콘 흰색·라벨 톤 병행(색만으로 구분 금지)
- 디자인 시스템의 **L2 상단 축약** 지침에 맞게 세로 높이·라벨 길이를 G1 대비 압축

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
  - itemSpacing: **spacing.3xl** (**24px**)
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

#### 7a. 섹션 래퍼 공통
- 각 섹션: `create_frame` name `section-{이름}`, width **FILL**, height **HUG**, fill **transparent**
- auto-layout VERTICAL, itemSpacing **spacing.lg** (**12px**), primaryAxisAlignItems **MIN**, counterAxisAlignItems **STRETCH**
- 섹션 제목: `create_text` — **subheading** `text xl` · semibold **20px** / line **30px** / weight **600**, **text-primary** (**#181d27**)

#### 7b. 섹션 `필수 증상` (`section-symptom`)
- 제목 텍스트: `필수 증상`
- 필드 그룹(스펙 필드명 기준, 각 그룹 VERTICAL, 그룹 간 itemSpacing **spacing.lg** **12px**):
  - **주호소·주증상**: `create_text` 레이블 — **label** `text sm` · medium **14px** / line **20px** / weight **500**, **text-primary** (**#181d27**), text: `주호소·주증상` + 필수 표시는 **error** **#d92d20** `*`(접근성 병행 문구는 시안 생략 가능)
  - 입력 컨테이너 `input-field`: fill **surface-raised** **#ffffff**, stroke **1px** **border-default** **#d5d7da**, cornerRadius **radius.md** (**8px**), padding **spacing.xl** (**16px**), minHeight 터치 목표 이상
  - 플레이스홀더/값: **body** `text md` · regular **16px** / line **24px** / weight **400**, **text-primary** 또는 빈 상태 **text-secondary** **#717680**
  - **증상 발생 시각 또는 경과**: 동일 레이블/필드 스타일, 플레이스홀더 예: `약 30분 전` (**caption** 톤으로 보조 가능)
  - **동반 증상·특이징후**(선택): 가로 **칩** 행 — 칩 fill **surface** **#fafafa** 또는 **primary-subtle**, stroke **1px** **border-default**, cornerRadius **radius.md** (**8px**), 패딩 **spacing.lg** (**12px**), 라벨 **label** **14px** medium **text-primary**
  - **통증**: 행 HORIZONTAL — 토글/셀렉트 + 숫자 필드(통증 있을 때 NRS 필수). 숫자 필드는 위 `input-field`와 동일 토큰
  - **의식 수준**: 셀렉트(단일 스키마 가정) — 드롭다운 시각은 동일 **input-field** 프레임 + **caption** **14px** **text-secondary** 보조 설명

#### 7c. 섹션 `필수 바이탈` (`section-vitals`)
- 제목: `필수 바이탈`
- `create_frame` name: `vitals-grid`, layoutMode: **VERTICAL**, itemSpacing **spacing.lg** (**12px**), width **FILL**
- 각 행 `vitals-row`: HORIZONTAL, width **FILL**, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **STRETCH**
- 행당 최대 **2**개의 `vital-cell`(width **FILL** 1:1): 각 셀 내부 VERTICAL — 레이블 **label** **14px** medium **text-primary**, 값 **input-field**(**surface-raised**, **1px** **border-default**, **radius.md** **8px**, padding **spacing.xl** **16px**)
- 필드 매핑(시안): (1행) 수축기 혈압 / 이완기 혈압 (2행) 맥박 / 호흡수 (3행) SpO₂ / 체온 — 단위 표기 **caption** **14px** **text-secondary**: `mmHg`, `회/분`, `%`, `℃`

#### 7d. 섹션 `pre-KTAS 등급·근거` (`section-prektas`)
- 제목: `pre-KTAS 등급·근거`
- **등급 선택**: 세로 스택, itemSpacing **spacing.lg** (**12px**). 등급 **1~5** 각각 `create_frame` name `prektas-option-{n}`, width **FILL**, height **HUG**, fill **surface-raised** **#ffffff**, stroke **1px** **border-default** **#d5d7da**, cornerRadius **radius.xl** (**12px**), padding **spacing.xl** (**16px**)
  - 내부 VERTICAL itemSpacing **spacing.lg** (**12px**)
  - 첫 줄: **body-strong** **18px** medium — 등급 번호·명칭(예: `1 · 소생`, `2 · 긴급` … 스펙 표 준수)
  - 둘째 줄: **caption** **14px** regular **text-secondary** — 스펙의 앱 내 요약 설명 한 줄
  - 선택됨: stroke **border.width.medium** (**2px**) **border-focus** **#7f56d9**, 배경 **primary-subtle** **#f9f5ff**(헤더 배지와 시각 일관)
- **근거 요약**(선택): 읽기 전용 블록 — fill **surface** **#fafafa**, **1px** **border-subtle** **#f5f5f5**, **radius.md** **8px**, padding **spacing.xl** **16px**, 본문 **body** **16px** regular **text-primary**, 상단 **caption** **14px** **text-secondary** `자동 생성 근거`(편집 가능 시 동일 필드에 **accent** **#1570ef** 텍스트 버튼 스타일 `편집` 추가)

#### 7e. 섹션 `특이사항·메모` (`section-notes`)
- 제목: `특이사항·메모`
- 멀티라인 필드: minHeight **120px** 이상, 나머지 토큰은 `input-field`와 동일(**surface-raised**, **border-default**, **radius.md**)

#### 7f. 로딩·빈 제안·오류(시안 변형)
- **로딩**: `main-content` 상단에 **caption** **14px** **text-secondary** `불러오는 중…` 또는 회색 라운드 스켈레톤(**surface** **#fafafa**, **border-subtle**)
- **빈 제안**: 해당 필드 아래 **caption** **14px** **text-secondary** `일지에서 제안이 없습니다. 직접 입력해 주세요.`
- **오류**: **body** **16px** **error** **#d92d20** + **primary** **#7f56d9** **16px** semibold 링크 스타일 `다시 시도`

### 8. 하단 고정 영역 (PAT-004 + 보조 저장)
- `get_node_info` → PAT-004 확인
- `clone_node` → 화면 frame **마지막** 자식으로 삽입(의도: 스크롤 본문 위에 고정)
- PAT-004 내부를 **HORIZONTAL**로 조정 가능하면: 좌측 **보조** `저장`(선택) — **text md** **16px** regular 또는 medium, 색 **accent** **#1570ef**(텍스트 버튼) 또는 테두리 버튼(stroke **1px** **border-default**, fill **surface-raised**)
- 우측 주요 버튼: **「병원 추천·이송」** — fill **primary** **#7f56d9**, 텍스트 **button** `text md` · semibold **16px** / line **24px** / weight **600**, **text-on-primary** **#ffffff**, cornerRadius **radius.md** (**8px**), 가로 비율은 주요 CTA가 더 넓게(예: 주 **FILL** 2 : 보조 **HUG**)
- 하단 안전 영역: PAT-004 패턴 정의에 따름; 패턴에 없으면 paddingBottom 최소 **spacing.xl** (**16px**) 추가

### 9. 필수 미충족 경고 모달 (PAT-005, 별도 프레임)
- 화면과 **동일 문서**에 오버레이용 `create_frame` name: `L2-M4-warning-modal`(또는 스펙 ID에 맞춘 이름), width **390**, height **844**, fill **color.gray.900** (**#181d27**) **50%** 투명(도구가 투명도 미지원 시 반투명 레이어로 대체)
- 중앙 `modal-card`: width **358**(화면 폭 **390** − 좌우 **spacing.xl** **16px** × 2), fill **surface-raised** **#ffffff**, cornerRadius **radius.2xl** (**16px**), stroke **1px** **border-default** **#d5d7da**, padding **spacing.3xl** (**24px**)
- `get_node_info` → PAT-005 확인 후 `clone`하여 제목·본문·버튼 자리에 맞게 배치
- 제목: **subheading** **20px** semibold **text-primary**
- 본문: **body** **16px** regular **text-primary** — 스펙 문구 예: `필수 정보가 부족합니다. 병원 추천 정확도가 떨어질 수 있습니다.`
- 버튼 행 HORIZONTAL, itemSpacing **spacing.lg** (**12px**):
  - **취소**: 보조 — stroke **1px** **border-default**, fill **surface-raised**, 텍스트 **button** **16px** semibold **text-primary**
  - **계속(L4)**: 주요 — fill **warning** **#f79009** 또는 **primary** **#7f56d9**(제품 정책: 파괴적이지 않은 진행이면 **primary** 유지, 강한 경고 강조 시 **warning** 배경 + **text-on-primary** 대비 확인 — **text-on-primary** **#ffffff**는 어두운 배경용이므로 **warning** 배경 시 버튼 글자색 **text-primary** **#181d27** 또는 **white** 중 대비 높은 쪽 선택)
- 시안 기본 권장: **계속** 버튼 fill **primary** **#7f56d9**, 텍스트 **text-on-primary** **#ffffff**(스펙의 리스크는 본문·아이콘으로 전달)

### 10. 검증
- `get_node_info` → 최상위 `L2-증상·pre-KTAS`: 자식 순서 **app-nav → prektas-header → PAT-001 → (PAT-002) → PAT-003 → main-content → PAT-004**, 너비 **390**
- 모달 프레임은 선택적으로 가시성 끄거나 별도 페이지에 배치
- `export_node_as_image` → 시각적 확인(선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| (네비 제목) | `nav-title` | **heading** 30px semibold | **text-primary** **#181d27** |
| pre-KTAS 등급(선택값) | `badge-prektas-selected` | 등급 번호·명칭 칩 | 배경 **primary-subtle** **#f9f5ff**, 테두리 **border-focus** **#7f56d9**, 글자 **text-primary** **#181d27** |
| 케이스·시각·동기화 | PAT-001 영역 | 텍스트·배지·아이콘 | **text-primary** / **text-secondary** / 상태 **success·warning·error** |
| 주호소·주증상 | `section-symptom` | 멀티라인 입력 | 필드 **surface-raised** **#ffffff**, 테두리 **border-default** **#d5d7da** |
| 증상 발생 시각·경과 | 동일 섹션 | 한 줄 입력·시간 피커 시각 | 동일 |
| 동반 증상·특이징후 | 동일 섹션 | 칩 + 보조 텍스트 | 칩 **surface** 또는 **primary-subtle**, 글자 **text-primary** |
| 통증(NRS) | 동일 섹션 | 셀렉트+숫자 | 동일 |
| 의식 수준 | 동일 섹션 | 셀렉트 | 동일 |
| 수축기/이완기 혈압, 맥박, 호흡수, SpO₂, 체온 | `section-vitals` | 2열 그리드 숫자 필드 | 레이블 **text-primary**, 단위 **text-secondary** **#717680** |
| pre-KTAS 등급(1~5 옵션) | `section-prektas` | 카드 리스트 | 기본 **surface-raised**+**border-default**, 선택 **primary-subtle**+**border-focus** |
| pre-KTAS 근거 요약 | 동일 섹션 | 읽기 전용 블록(+편집) | 본문 **text-primary**, 링크 **accent** **#1570ef** |
| 특이사항·메모 | `section-notes` | 멀티라인 | 동일 입력 토큰 |
| 저장(임시) | 하단 바 좌측 | 보조 텍스트/버튼 | **accent** **#1570ef** 또는 테두리 버튼 |
| 병원 추천·이송 | 하단 바 우측 | 주요 CTA | **primary** **#7f56d9** / 글자 **text-on-primary** **#ffffff** |
| 경고 모달 카피 | PAT-005 프레임 | 제목+본문+취소/계속 | 본문 **text-primary**, 버튼 **primary** 또는 보조 테두리 |
