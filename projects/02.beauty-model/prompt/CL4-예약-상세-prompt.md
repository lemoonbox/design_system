# 디자인 명세 — CL4 예약 상세

## 화면 개요
- **목적**: 개별 예약의 상태·상세 정보를 한눈에 확인하고, 승인 후 결제 또는 조건에 맞는 취소를 진행한다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 내 예약 목록에서 특정 건을 탭한 직후, 결제 마감·취소 규정을 확인해야 할 때
- **핵심 행동**: 상태에 따라 **결제하기** 또는 **예약 취소**(또는 안내 확인만)

## 시각적 의도

- **분위기**: 플랫·조밀한 정보 화면. 상태는 색·틴트·배지로 즉시 읽히고, 본문은 행 단위 스캔에 최적화된다.
- **시각적 초점 (focal point)**: 상단 **예약 상태 대형 배지(PAT-004)** 와, 승인됨일 때 **결제 마감 배너 + 결제하기 CTA** 가 시선을 나란히 잡는다.
- **색상 톤**: 페이지는 gray.50, 정보 블록은 surface(흰색)+border로 구분. 상태만 success/warning/error/brand 틴트로 강조한다.
- **밀도**: visual-direction **조밀** — padding spacing.xl, 섹션 간 spacing.3xl, 행 간은 border-subtle 구분선으로 리듬 유지.
- **디자인 핵심**: 카드는 **그림자 없이** border(gray.300)만 사용하고, 섹션 제목 옆 **3px 세로 앵커 바(brand.600)** 로 스캔 축을 준다.

---

## Visual Recipe

전체 배경은 밝은 gray.50으로 깔고, 첫 화면부터 헤더 아래에 **큰 상태 칩**이 들어간 틴트 스트립(상태별 success/warning/error/gray 틴트)을 두어 “지금 이 예약이 어디쯤인지”를 한 번에 전달한다. 그 아래로 시술·일정·결제·규정이 **동일한 카드 뼈대**(radius.2xl, 1px border)로 반복되며, 승인됨이면 **brand.50 배너**에 시계 아이콘과 결제 마감 카운트다운이 눈에 띈다. 하단은 흰색 고정 액션 바(상단 1px border-subtle)에 Primary/Secondary 버튼을 얹고, 본문과의 계층이 끊기지 않게 한다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-004 | 상태 배지 | 헤더 영역 — 예약 상태(대형 변형) | 75:4411 (컨테이너) / 상태별 변형 노드 참조 _index |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-001 | 목록용 예약 카드가 아니라 상세 스크롤 구조 |
| PAT-002 | 상품/모집글 카드 미사용 |
| PAT-003 | 신청자 행 미사용 |
| PAT-005 | Local 상세 스택 — 하단 탭바 숨김(뒤로가기만) |
| PAT-006 | CM1/CM2는 링크·버튼으로 열리는 별도 모달 |
| PAT-007 | 사진 그리드 없음 |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 상단 뒤로 | chevronLeft | 2:599 | 24×24 | text-primary — gray.900 #181d27 (rgba(24,29,39,1)) |
| 결제 마감 배너 | clock | 2:629 | 20×20 | primary — brand.600 #7f56d9 (rgba(127,86,217,1)) |
| 섹션 시술 정보 | scissors | 2:1079 | 20×20 | text-secondary — gray.500 #717680 (rgba(113,118,128,1)) |
| 행 디자이너 | user | 2:1250 | 20×20 | text-secondary — gray.500 #717680 |
| 행 위치 | mapPin | 2:911 | 20×20 | text-secondary — gray.500 #717680 |
| 섹션 일정 | calendar | 2:576 | 20×20 | text-secondary — gray.500 #717680 |
| 섹션 결제 | creditCard | 2:701 | 20×20 | text-secondary — gray.500 #717680 |
| 안내 박스(거절/대안) | alertCircle | 2:467 | 20×20 | 상태 텍스트색과 정렬(success/warning/error 토큰) |
| 취소 규정 접기 | chevronDown | 2:596 | 20×20 | text-secondary — gray.500 #717680 |
| 동의 링크 보조 | chevronRight | 2:602 | 20×20 | primary — brand.600 #7f56d9 |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #fafafa (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ 상단 바 (뒤로 + 제목)         │  h: 56px
├─────────────────────────────┤
│ 상태 히어로 스트립            │  패딩 xl, 배지+번호
├─────────────────────────────┤
│ ▲ 승인됨: 결제 마감 배너       │  조건부 — primary-surface
├─────────────────────────────┤
│                              │
│  스크롤 본문                  │
│  [시술 정보 카드]             │  surface + border
│  [일정 카드]                  │  일정 행 강조(body-medium)
│  [결제 정보 카드]             │  조건부 필드
│  [조건부 안내 박스]            │  거절/대안 일정
│  [취소 규정 접힘]             │  border-subtle 구분
│  동의 내역 링크                │  본문 하단
│                              │
├─────────────────────────────┤
│ 고정 CTA 바 (조건부)          │  surface, 상단 구분선
└─────────────────────────────┘
```

### 상단 바 (네비게이션)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | full × 56px | 표준 터치 타이틀 바 |
| 배경 | surface — white #ffffff (rgba(255,255,255,1)) | 본문 스크롤과 대비 |
| 배치 | 수평 스택 | 좌: 뒤로, 중앙: 제목 |
| 주축 정렬 | 양끝(뒤로-여백-제목 중앙 정렬 처리) | 제목 시각적 중앙 |
| 교차축 정렬 | 중앙 | |
| 내부 여백 | 좌우 spacing.xl (16px) | |
| 요소 간격 | spacing.lg (12px) | |
| 모서리 | 없음 | |
| 깊이 | 없음 | 하단 1px border-subtle로 본문과 분리 |
| 테두리 | 하단 1px border-subtle #f5f5f5 | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 뒤로 | 아이콘 버튼 | chevronLeft (2:599) 24×24 | — | text-primary |
| 제목 | 텍스트 | "예약 상세" | heading — 20/30/0 Semibold | text-primary — gray.900 #181d27 |

### 상태 히어로 스트립

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | 상태별 tint (success.50 / warning.50 / error.50 / gray.100) | visual-direction 상태 원칙 |
| 내부 여백 | 상하좌우 spacing.xl | |
| 요소 간격 | spacing.lg | 배지와 예약 번호 분리 |
| 좌측 앵커 | 선택: 4px 세로 바 — 상태색( success.600 / warning.500 / error.500 / gray.500 ) | 카드 최소 구성·상태 즉시 구분 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 배지 | 패턴 | PAT-004 (크기 확대: 패딩 상하 8px 좌우 14px 수준) | caption→label 스케일 혼합 허용 | 상태별 PAT-004 변형 |
| 예약 번호 | 텍스트 | "예약번호 · BM-2026-00000" | caption — 12/18/0 Regular | text-secondary — gray.500 |

### 결제 마감 배너 (승인됨 전용)

| 속성 | 값 |
|------|-----|
| 배경 | primary-surface — brand.50 #f9f5ff (rgba(249,245,255,1)) |
| 테두리 | 없음 (인접 카드와 구분은 상하 여백 spacing.lg) |
| 내부 여백 | spacing.xl |
| 깊이 | 없음 (플랫) |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 아이콘+문구 행 | 수평 스택 | clock + "결제 마감까지 OO:OO:OO" | body-medium — 16/24/0 Medium | text-primary + primary 브랜드 포인트(숫자만 brand.600) |
| 보조 | 텍스트 | "24시간 이내 결제를 완료해 주세요" | caption — 12/18/0 Regular | text-secondary |

### 스크롤 — 공통 카드 컨테이너

| 속성 | 값 |
|------|-----|
| 좌우 마진 | spacing.xl |
| 카드 간 세로 간격 | spacing.3xl (24px) |
| 카드 배경 | surface — white #ffffff |
| 테두리 | 1px border — gray.300 #d5d7da |
| 모서리 | radius.2xl (16px) |
| 내부 패딩 | spacing.xl |
| 행 구분 | 카드 내부 행 사이 1px border-subtle |

### 섹션 헤더 행 (각 카드 상단)

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 앵커 바 | 도형 | 3px × 18px 세로, radius 1px | — | brand.600 #7f56d9 |
| 아이콘 | 아이콘 | 섹션별 (위 표) 20×20 | — | text-secondary |
| 제목 | 텍스트 | "시술 정보" / "일정" / "결제 정보" | subheading — 18/28/0 Semibold | text-primary |

### 시술 정보 카드 — 내부 행

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 시술명 | 텍스트 | 데이터 | body-medium — 16/24/0 Medium | text-primary |
| 디자이너명 | 텍스트 행 | 아이콘+라벨+값 | body — 16/24/0 Regular | 라벨 text-secondary, 값 text-primary |
| 주소 | 텍스트 행 | mapPin+값 | body — 16/24/0 | 동일 |

### 일정 카드

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 일시 | 텍스트 | "2026년 3월 28일 (토) 14:00" | body-medium — 16/24/0 Medium | text-primary |
| 보조 | 텍스트 | "시술 시작 기준" | caption — 12/18/0 | text-secondary |
| 좌측 상태 바 | 4px bar | 카드 전고 — 예약 상태색 | — | 상태 팔레트 키 |

### 결제 정보 카드

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 가격·방식 | 키-값 행 | spacing.lg 간격 수직 스택 | body / caption | text-primary / text-secondary |
| 결제 완료 필드 | 조건부 | 금액·일시 | caption | text-secondary |

### 조건부 안내 박스 (거절 / 대안 일정)

| 속성 | surface + 좌측 4px error.500 또는 warning.500 바, 내부 padding xl |
| 내부 | alertCircle + 제목(body-medium) + 본문(body) |

### 취소 규정 (접힘)

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 헤더 행 | 버튼 | "취소 규정 안내" + chevronDown | label — 14/20/0 Medium | text-primary |
| 본문 | 텍스트 | 고정 카피 | body — 16/24/0 | text-secondary |

### 동의 내역 링크

| 요소 | 텍스트 링크 "동의 내역 보기" + chevronRight | label Medium | primary brand.600 |

### 하단 고정 CTA 바

| 속성 | 값 |
|------|-----|
| 배경 | surface white |
| 상단 테두리 | 1px border-subtle |
| 패딩 | spacing.xl, 하단 safe-area 추가 |
| 버튼 높이 | 최소 48px (조밀 환경에서도 44px 이상) |
| 버튼 간격 | spacing.lg |
| Primary | brand.600 fill, 흰 텍스트, radius.full, button 타이포 |
| Secondary | 투명 또는 white + border gray.300, 텍스트 error 또는 text-primary(취소 시 error.500 텍스트 권장) |

#### 내부 요소 (상태별)

| 상태 | 요소 |
|------|------|
| 대기 중 | Secondary만 "예약 취소" |
| 승인됨 | Primary "결제하기" + Secondary "예약 취소" |
| 확정 | Secondary "예약 취소" |
| 완료/취소/거절 | CTA 바 숨김 — 스크롤 하단에 caption 안내 문구만 |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|------------|----------|------|
| 예약 상태 | 상태 히어로 > PAT-004 | caption~label | 상태 tint+텍스트 | 대기/승인/확정/완료/취소/거절 |
| 예약 번호 | 상태 히어로 | caption | text-secondary | |
| 시술명 | 시술 정보 카드 | body-medium | text-primary | |
| 디자이너명 | 시술 정보 행 | body | text-primary | |
| 살롱 주소 | 시술 정보 행 | body | text-primary | |
| 시술 일정 | 일정 카드 | body-medium | text-primary | |
| 시술 가격 | 결제 카드 | body | text-primary | |
| 결제 방식 | 결제 카드 | body | text-secondary | |
| 결제 금액 | 결제 카드 | body | text-primary | 결제 완료 후 |
| 결제 일시 | 결제 카드 | caption | text-secondary | 결제 완료 후 |
| 거절 사유 | 안내 박스 | body | error 계열 | 거절만 |
| 대안 일정 제안 | 안내 박스 | body | warning 계열 | 대안 제안만 |
| 결제 마감 카운트다운 | 배너 | body-medium + caption | brand + text-secondary | 승인됨만 |
| 취소 규정 | 접힘 본문 | body | text-secondary | |
| 동의 링크 | 링크 행 | label | primary | → CM2 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 | — | — | — |
| 상단 바 | white | gray.50 | 충분 | — |
| 카드 | white | gray.50 | 충분 | border 유지 |
| 상태 스트립 | tint | gray.50 | 충분 | — |
| 결제 배너 | brand.50 | tint/white | 충분 | 카드 직접 인접 시 여백으로 분리 |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 카드·바 | 플랫 | 없음 | border만 사용 |
| CM1/CM2 | 모달/시트 | shadow-md | 오버레이만 elevation |

### 타이포 위계
| 수준 | 역할 | 스펙 | 적용 요소 |
|------|------|------|----------|
| 1 | heading | 20/30/0 Semibold | 화면 제목 |
| 2 | subheading | 18/28/0 Semibold | 섹션 제목 |
| 3 | body / caption | 16/24/0, 12/18/0 | 본문·메타 |

### 강조 검증
- focal point: 상태 배지 + (승인 시) 결제 배너·Primary CTA — 시간 민감 액션
- primary 사용: 링크, 결제 CTA, 섹션 앵커 바, 카운트다운 숫자 강조
- 상태: PAT-004 tint + 문구 + 필요 시 아이콘(안내 박스)

### 밀도 검증
- 뒤로·CTA·접힘 헤더: 높이 ≥ 44~48px

### 시각 밀도 검증
- 스크롤 영역: 카드 4~6블록 + 조건부 박스로 **빈 배경 50% 미만** 충족
- 텍스트 전용 카드 없음 — 각 카드에 아이콘·앵커·행 구분선
- 반복 카드: 단일 예약이므로 **상태 스트립 + 일정 카드 좌측 바**로 위계
- 섹션 헤더: **3px 브랜드 바 + 아이콘** 적용
- 네비: 단일 상단 바 — **56px** 유지

### 일관성 체크
- [x] 색상·타이포·행간·자간·border·visual-direction과 충돌 없음
