# Figma 실행 프롬프트 — L1 음성·구급일지

## 사전 확인
- 문서: `context/figma-target.json`의 `fileKey`(프로젝트에 파일이 없으면 생성·기입 후 사용)
- 페이지: Figma 문서 내 **L1 작업용 페이지명**을 확인한 뒤 동일 이름으로 `set_current_page`
- 화면 frame 이름: `L1-음성·구급일지`
- 디바이스 기준: **390×844** 모바일(명령 템플릿 기준)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| nav-bar 뒤로 버튼 | icon.baseicon.tokens.chevronLeft | 2:599 | 20×20 | text-primary color.gray.900 (#181d27) |
| PAT-001 동기화 칩 (동기화됨) | icon.baseicon.tokens.cloud | 2:647 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (오프라인) | icon.baseicon.tokens.cloudOff | 2:638 | 20×20 | text-secondary color.gray.500 (#717680) |
| PAT-001 동기화 칩 (동기화 중) | icon.baseicon.tokens.refreshCw | 2:1058 | 20×20 | text-secondary color.gray.500 (#717680) |
| confidence-row 신뢰도 높음 | icon.feedback.tokens.checkCircle | 2:588 | 20×20 | success color.success.600 (#039855) |
| confidence-row 신뢰도 낮음 | icon.feedback.tokens.alertCircle | 2:467 | 20×20 | warning color.warning.500 (#f79009) |
| PAT-004 CTA 버튼 (증상·pre-KTAS로) | icon.baseicon.tokens.arrowRight | 2:516 | 20×20 | text-on-primary color.white (#ffffff) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 케이스·동기화 헤더 | 네비게이션 바(`nav-bar`) 바로 아래 — 케이스·시각·동기화·(수집 상태와 병치) | 64:4585 |
| PAT-002 | 동기화·네트워크 배너 | PAT-001 바로 아래(오프라인·전송 대기·실패 시만) | 65:4595 |
| PAT-004 | 하단 고정 주요 CTA 바 | 화면 최하단 — 「증상·pre-KTAS로」 단일 CTA | 65:4618 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-003 | `design-system.md`·패턴 인덱스상 **G1·L2·L4** 중심이며, L1 스펙은 **3단계 스텝퍼**를 요구하지 않음 |
| PAT-005 | 상위 이탈 시 **M3**는 별도 모달 화면(M3 스펙) — L1 단일 프레임 구성에 포함하지 않음 |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{작업 페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: `L1-음성·구급일지`
  - x: 0, y: 0, width: **390**, height: **844**
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **0**, paddingBottom: **0**, paddingLeft: **0**, paddingRight: **0**
  - itemSpacing: **0**
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

### 3. 네비게이션 바 (`nav-bar`) — 직접 구현
- `create_frame`
  - name: `nav-bar`
  - parentId: 화면 frame ID
  - width: **390**, height: **56**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
  - 하단 구분: stroke **border.width.default** (**1px**), 색 **border-subtle** → `gray.100` (**#f5f5f5**)(하단만 필요 시 별도 `line` 프레임으로 동일 두께·색 적용)
- `set_auto_layout`
  - layoutMode: **HORIZONTAL**
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.md** (**8px**)
  - counterAxisAlignItems: **CENTER**, primaryAxisAlignItems: **MIN**
- 뒤로 아이콘: Base icons **`chevronLeft`** 등 **icon sm** 규격(피그마 자산 기준), 터치 영역 최소 가로 **44** 권장(내부 여백으로 확보)
- `create_text`
  - name: `nav-title`
  - text: `구급 일지`
  - **heading** `display sm` · semibold **30px** / line **38px** / weight **600**, **text-primary** `color.gray.900` (**#181d27**)

### 4. 케이스·동기화 헤더 (PAT-001)
- `get_node_info` → PAT-001 노드 확인
- `clone_node` → `nav-bar` **바로 아래**에 삽입
- `set_text_content` 등으로 케이스 라벨·출동 시각·동기화 배지 반영(G1 프롬프트와 동일 토큰):
  - 케이스 가독 라벨 — **body** `text md` · regular **16px** / line **24px** / weight **400**, **text-primary** (**#181d27**)
  - 시각 — **caption** `text sm` · regular **14px** / line **20px** / weight **400**, **text-secondary** (**#717680**)
  - 동기화 — 아이콘+문구, **success** (**#039855**) / **warning** (**#f79009**) / 오류·오프라인 시 **error** (**#d92d20**) 등(색만으로 구분 금지)
- **녹음·수집 상태**(진행 중·일시정지 등): PAT-001과 같은 행 또는 바로 아래 보조 행에 **caption** `text sm` · regular **14px** / line **20px** / weight **400** + 상태 배지(배경 **surface** **#fafafa** 또는 **primary-subtle** **#f9f5ff**, 테두리 **1px** **border-default** **#d5d7da**)

### 4b. 동기화 배너 (PAT-002, 조건부)
- 전송 실패·오프라인·대기 등 스펙상 배너가 필요할 때만: PAT-002 `clone` → PAT-001 **바로 아래** 삽입
- 한 줄 요약 + 「재시도」/「자세히(M2)」 라벨 치환
- 배경 **error-subtle** (**#fef3f2**) 또는 **surface** (**#fafafa**) + **border-default** **1px** (**#d5d7da**)

### 5. 주요 콘텐츠 영역 (`main-content`) — 시간순 발화 구간 목록(직접 구현)

- `create_frame`
  - name: `main-content`
  - parentId: 화면 frame ID
  - width: **390**
  - height: **FILL**(상단 스택·하단 PAT-004 제외 남은 세로)
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.3xl** (**24px**), paddingBottom: **spacing.3xl** (**24px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)(리스트 항목 간 gap — `design-system.md`)
  - primaryAxisAlignItems: **MIN**, counterAxisAlignItems: **STRETCH**

#### 5a. 구간 행 템플릿 (`segment-row` — 시안용 2~3개 복제)
- `create_frame`
  - name: `segment-row`
  - parentId: `main-content` ID
  - width: **FILL**, height: **HUG**
  - fillColor: **surface-raised** `color.white` (**#ffffff**)
  - stroke: **border.width.default** (**1px**), **border-default** `color.gray.300` (**#d5d7da**)
  - cornerRadius: **radius.xl** (**12px**)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **spacing.xl** (**16px**), paddingBottom: **spacing.xl** (**16px**)
  - paddingLeft: **spacing.xl** (**16px**), paddingRight: **spacing.xl** (**16px**)
  - itemSpacing: **spacing.lg** (**12px**)
- 상단 가로 행(`segment-row-header`): **HORIZONTAL**, **SPACE_BETWEEN**, counterAxisAlignItems **CENTER**
  - 좌측: `create_text` — **구간 시작·종료 시각**(예: `14:32:01 – 14:32:18`) — **caption** `text sm` · regular **14px** / line **20px** / weight **400**, **text-secondary** (**#717680**)
  - 우측: 편집 진입 — **icon** `edit`(sm) + 선택 시 **caption** 「편집」 동일 **text-secondary**
- `create_text` — **STT 텍스트**(본문, 편집 가능한 필드 시안): **body** `text md` · regular **16px** / line **24px** / weight **400**, **text-primary** (**#181d27**); 멀티라인 허용
- NER 칩 행(`ner-chips`): **HORIZONTAL**, itemSpacing **spacing.lg** (**12px**), wrap 시 별도 프레임으로 2줄 시안 가능
  - 각 칩: `create_frame` cornerRadius **radius.md** (**8px**), fill **primary-subtle** (**#f9f5ff**), padding 세로·가로 **spacing.lg** (**12px**), stroke 선택 **1px** **border-focus** (**#7f56d9**)
  - 칩 내부 `create_text`: **label** `text sm` · medium **14px** / line **20px** / weight **500**, **text-primary** (**#181d27**)
- 신뢰도(`confidence-row`): **HORIZONTAL**, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
  - **icon.feedback** `alertCircle` / `checkCircle` 등(높음·중간·낮음 정책에 맞게) + **caption** **14px** regular — 낮음일 때 **warning** (**#f79009**) 또는 **error** (**#d92d20**)는 **아이콘+문구** 병행(색만으로 상태 구분 금지)
- **구간 ID**: 화면에 표시하지 않음(스펙: 숨김) — 레이어 이름에만 보관 가능

#### 5b. 로딩·빈 상태·오류(시안)
- **로딩**: `main-content`에 **caption** **14px** **text-secondary** 「불러오는 중…」 또는 **surface** (**#fafafa**) 스켈레톤 블록(**border-subtle** **#f5f5f5**)
- **빈 상태**: **body** **16px** **text-primary** 「말로 기록이 시작됩니다」+ **caption** **14px** **text-secondary** 보조 한 줄
- **오류**: **body** **16px** **error** (**#d92d20**) + **button** 톤 **primary** (**#7f56d9**) 「다시 시도」 — **text md** · semibold **16px** / line **24px** / weight **600**

#### 5c. 수집 중(선택 시안)
- 상단 PAT-001 인근 또는 목록 상단에 **caption** **14px** 「수집 중…」+ **accent** (**#1570ef**) 점/아이콘(실시간 구간 추가 암시); 스펙상 **재녹음 UI 없음** 명시 유지

### 6. 하단 고정 영역 (PAT-004)
- `get_node_info` → PAT-004 확인
- `clone_node` → 화면 frame **마지막** 자식으로 삽입
- 주요 버튼 라벨: **「증상·pre-KTAS로」** — **항상 허용**(게이트 없음)
- 버튼 보정 시:
  - fill **primary** `color.brand.600` (**#7f56d9**)
  - 텍스트 **button** `text md` · semibold **16px** / line **24px** / weight **600**, **text-on-primary** (**#ffffff**)
  - cornerRadius **radius.md** (**8px**)
  - 가로 **FILL**, 상하 패딩 **spacing.lg** (**12px**)~**spacing.xl** (**16px**)
- **마이크·수집 제어**는 정책 문서에 따름 — 본 프롬프트에서는 PAT-004 외 별도 FAB/헤더 버튼을 **필요 시에만** 추가(스펙: 재녹음 없음)

### 7. 검증
- `get_node_info` → 최상위 frame: 자식 순서 **`nav-bar` → PAT-001 → (PAT-002) → `main-content` → PAT-004**, 너비 **390**
- `export_node_as_image` → 시각적 확인(선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상(팔레트 키 / Hex) |
|--------|----------|----------|------------------------|
| 구간 ID | (숨김) | 레이어 메타만 | — |
| 구간 시작·종료 시각 | `segment-row-header` 좌측 | `text sm` 14px regular | text-secondary / **#717680** |
| STT 텍스트 | 구간 행 본문 | `text md` 16px regular, 멀티라인 | text-primary / **#181d27** |
| NER 추출 항목 | `ner-chips` | 칩, `text sm` medium | 칩 배경 primary-subtle **#f9f5ff**, 글자 text-primary **#181d27** |
| 구간 신뢰도 | `confidence-row` | 아이콘+배지·캡션 | 아이콘+문구 병행; 강조색 warning **#f79009** / error **#d92d20** 등은 보조 |
| 일지 전체 동기화 상태 | PAT-001 + (PAT-002) | 배지·아이콘·한 줄 | success **#039855** · warning **#f79009** · 오류 **#d92d20** |
| 마지막 저장 시각 | `main-content` 상단 또는 PAT-001 하단 | **caption** `text sm` 14px | text-secondary **#717680** |
| 녹음·수집 상태 | PAT-001 인근 | **caption** + 배지 | text-primary / secondary; 배지는 surface 또는 primary-subtle |
