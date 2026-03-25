# 디자인 명세 — DL4 예약 상세

## 화면 개요
- **목적**: 확정된 예약의 고객·시술·결제 정보를 확인하고, 시술 완료 플로우로 이어간다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 예약 목록(DG3)에서 항목을 연 직후, 당일 방문 전·후 확인
- **핵심 행동**: 확정 상태에서 **시술 완료**를 눌러 DM2로 진입

## 시각적 의도

- **분위기**: 고객 화면(CL4)과 **동일한 카드·타이포 리듬**을 유지하되, 디자이너 업무 효율을 위해 **고객 정보 블록을 최상단 카드**로 두어 먼저 읽히게 한다.
- **시각적 초점 (focal point)**: **고객 정보 카드**(이름·연락처·노쇼 배지)와, 확정 시 하단 **시술 완료 Primary CTA**.
- **색상 톤**: background gray.50, 카드 surface+border. 노쇼 배지만 warning 틴트로 주의 환기.
- **밀도**: 조밀 — 행 구분은 border-subtle, 섹션 간 spacing.3xl.
- **디자인 핵심**: 플랫(무 shadow 카드) + **섹션 좌측 3px brand 앵커**로 CL4·CL3와 일관.

---

## Visual Recipe

배경은 CL4와 동일한 밝은 그레이 톤이고, 첫 카드부터 흰색 surface에 **고객명이 subheading**으로 박혀 있어 “누구 예약인지”가 바로 드러난다. 연락처는 마스킹된 monospace 느낌의 body로 읽기 쉽게, 노쇼 이력이 있을 때만 **warning.50 배경의 작은 칩**이 이름 옆·아래에 붙는다. 시술·결제 카드는 CL4와 대칭되는 레이아웃으로 **한 서비스 안에서 같은 언어**를 쓴다. 확정이면 하단 고정 바에 보라색 Pill CTA 하나만 두어 오동작을 줄인다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-004 | 상태 배지 | 헤더 히어로 — 예약 상태(확정/완료/취소) | 75:4411 및 변형 참조 _index |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-001 | 목록 카드 아님 |
| PAT-002 | 모집글 카드 없음 |
| PAT-003 | 신청자 행 없음(이미 확정 예약 상세) |
| PAT-005 | Local 스택 — 탭바 숨김 |
| PAT-006 | DM2는 별도 모달 |
| PAT-007 | 사진 그리드 없음 |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 뒤로 | chevronLeft | 2:599 | 24×24 | text-primary — gray.900 #181d27 |
| 고객 섹션 | user | 2:1250 | 20×20 | text-secondary — gray.500 #717680 |
| 연락처 | phone | 2:1022 | 20×20 | text-secondary — gray.500 |
| 노쇼 배지 보조 | alertTriangle | 2:472 | 16×16 | warning — warning.500 #f79009 |
| 시술 섹션 | scissors | 2:1079 | 20×20 | text-secondary — gray.500 |
| 일정 | calendar | 2:576 | 20×20 | text-secondary — gray.500 |
| 결제 | creditCard | 2:701 | 20×20 | text-secondary — gray.500 |
| 정산 안내 | info | 2:863 | 20×20 | text-secondary — gray.500 |
| 동의 링크 | chevronRight | 2:602 | 20×20 | primary — brand.600 #7f56d9 |
| 완료 안내 | checkCircle | 2:588 | 20×20 | success — success.600 #039855 |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #fafafa (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ 상단 바                      │  56px
├─────────────────────────────┤
│ 상태 히어로 (PAT-004)        │
├─────────────────────────────┤
│ 스크롤                       │
│ [고객 정보 카드] ★ focal      │
│ [시술 정보 카드]              │
│ [결제·정산 카드]              │
│ 동의 내역 링크                │
│ 완료/취소 시 안내 문구        │
├─────────────────────────────┤
│ 고정 CTA (확정만)             │
└─────────────────────────────┘
```

### 상단 바

| 속성 | 상단 바 표준 — CL4와 동일 | 하단 border-subtle |

#### 내부 요소

| 요소 | 내용 | 타이포 | 색상 |
|------|------|-------|------|
| 뒤로 | chevronLeft | — | text-primary |
| 제목 | "예약 상세" | heading 20/30 Semibold | text-primary |

### 상태 히어로 스트립

| 속성 | CL4와 동일 — 확정=success 틴트, 완료=success, 취소=error 틴트 |
| PAT-004 변형 + 예약 번호 caption |

### 고객 정보 카드 (최상단 본문 카드)

| 속성 | surface white, border gray.300 1px, radius.2xl, padding xl |
| 좌측 4px 바 | 확정=success.600, 완료=success.600, 취소=error.500 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 섹션 헤더 | 행 | 3px 앵커 + user 아이콘 + "고객 정보" | subheading | text-primary |
| 고객명 | 텍스트 | 데이터 | subheading 18/28 Semibold | text-primary |
| 노쇼 배지 | 칩 | "노쇼 이력 N회" | caption Medium | warning 텍스트 + warning.50 배경 |
| 연락처 행 | 행 | phone + 마스킹 번호 | body | text-primary |
| 탈퇴 케이스 | 텍스트 | "탈퇴한 사용자" | body | text-disabled |

### 시술 정보 카드

| 섹션 헤더 | scissors + "시술 정보" + 3px 앵커 |
| 시술명 body-medium | 일정 calendar + body-medium 강조 |

### 결제 정보 카드

| 섹션 헤더 | creditCard + "결제 정보" |
| 키-값 행 | 가격·방식·결제금액·결제일시 — CL4 결제 카드와 동일 규칙 |
| 정산 예정일 | 완료 후에만 info 아이콘 + caption "정산 예정: YYYY.MM.DD (시술 완료 기준 T+3 영업일)" |

### 동의 내역 링크

| "동의 내역 보기" | label Medium primary + chevronRight → CM2 |

### 하단 고정 CTA

| 확정 | Primary "시술 완료" 단일, 높이 ≥ 48px, brand.600, radius.full |
| 완료/취소 | 바 숨김 — 카드 하단 또는 별도 안내 박스에 caption + checkCircle(완료) 또는 본문 안내(취소) |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|------------|----------|------|
| 예약 상태 | 히어로 PAT-004 | caption/label | 상태 tint | 확정/완료/취소 |
| 예약 번호 | 히어로 | caption | text-secondary | |
| 고객명 | 고객 카드 | subheading | text-primary | |
| 고객 연락처 | 고객 카드 | body | text-primary | 마스킹 |
| 고객 노쇼 이력 | 고객 카드 칩 | caption | warning | 1회 이상만 |
| 시술명 | 시술 카드 | body-medium | text-primary | |
| 시술 일정 | 시술 카드 | body-medium | text-primary | |
| 시술 가격 | 결제 카드 | body | text-primary | |
| 결제 방식 | 결제 카드 | body | text-secondary | |
| 결제 금액·일시 | 결제 카드 | body / caption | primary / secondary | |
| 정산 예정일 | 결제 카드 하단 | caption | text-secondary | 완료 처리 후 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 인접 | 대비 |
|------|------|------|------|
| 페이지 | gray.50 | 카드 white | 충분 |
| 고객 카드 | white | 일정 카드 white | 카드 간 세로 gap 24px + 그림자 없이 border로 구분 |

### Elevation
| 카드·바 | 없음 | 플랫 border |
| DM2 | shadow-md | 시트/모달만 |

### 타이포 위계
| heading / subheading / body / caption | CL4와 동일 3단계 |

### 강조 검증
- focal: 고객 카드 + 시술 완료 CTA
- primary: CTA 1곳, 링크, 섹션 앵커

### 밀도 검증
- CTA ≥ 48px 권장

### 시각 밀도 검증
- 카드 3 + 링크 + 상태 히어로로 빈 화면 비율 낮음
- 고객 카드에 아이콘·배지·좌측 바로 최소 구성 충족
- 섹션 헤더 3px 바 + 아이콘

### 일관성 체크
- [x] CL4·CL3 결제 행 레이아웃과 정합(screen-spec 패턴 후보)
