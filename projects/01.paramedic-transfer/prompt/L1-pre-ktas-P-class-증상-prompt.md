# 디자인 명세 — L1 pre-KTAS / P-class·증상

## 화면 개요
- **목적**: 주·부증상과 증상 요약을 다루고, **pre-KTAS**와 **P-class**를 **서로 독립된 비동기 흐름**으로 입력·확인하며, 필요 시 병원 단계(L2)로 넘어간다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: G1에서 **「평가·증상」**으로 진입한 직후 또는 이송 준비 중 잠시 멈춰 평가를 마무리·보완하는 순간.
- **핵심 행동**: 주증상을 확정하고(필수), pre-KTAS·P-class 블록의 상태를 확인한 뒤 **「병원 추천·이송」**으로 다음 단계로 이동한다(pre-KTAS 미확정도 허용).

## 시각적 의도

- **분위기**: G1과 동일 톤의 **신뢰·친근**을 유지하되, **두 개의 비동기 엔진**이 동시에 돌아가는 느낌을 **두 개의 명확한 카드 블록**과 **독립 상태 배지**로 전달한다.
- **시각적 초점 (focal point)**: 상단 **주증상 선택 행(필드 전체)** — 필수·최우선 입력으로 시선을 먼저 보낸다. 처리 중이면 **해당 블록의 스텝퍼/배지**가 보조 초점이 된다.
- **색상 톤**: 페이지 **background — gray.50**, 카드 **surface — white** + **1px border**. 블록 제목 옆·좌측에 **3~4px primary 바**로 섹션 앵커. 상태는 **success / warning / error** 배지+아이콘으로만. 링크형 보조는 **accent — blue.600**.
- **밀도**: **중간** — 섹션 간 `spacing.3xl`(24px), 카드 내부 `spacing.xl`(16px). 주요 버튼·스텝퍼 행 **최소 높이 44px**.
- **디자인 핵심**: **pre-KTAS**와 **P-class**가 **세로 스택된 두 카드**로 분리되어 타임라인 혼동이 없고, 각 카드가 **PAT-001** 변형(비동기·근거·재시도)으로 통일된다. Class III 안내는 **인포 배너**로 한 번만 읽히게 한다.

---

## Visual Recipe

상단 앱 바 아래로 **주증상→부증상→증상 요약**이 **한 덩어리의 밝은 표면(흰 카드 또는 연한 구획)** 안에서 읽히고, 스크롤을 내리면 **pre-KTAS 카드**와 **P-class 카드**가 **동일한 너비·같은 테두리 리듬**으로 쌓인다. 각 비동기 블록 상단에는 **가로 스텝 또는 단계 배지**가 **무게감 있게(높이 40px 이상 영역)** 자리해 진행 상황이 즉시 보인다. 하단에는 **넓은 primary 한 방**으로 **「병원 추천·이송」**이 고정되어 다음 행동이 흔들리지 않는다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 비동기·상태 카드 | **pre-KTAS** 블록 전체 — 단계 배지·시각·근거 요약·오류·재시도 | 94:4467 |
| PAT-001 (변형) | 비동기·상태 카드 | **P-class** 블록 상단 상태 영역 — 단계 배지·요약 한 줄; 하부는 아코디언+체크로 확장 | 94:4467 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-002 | 병원 행 선택 UI는 L2·L3 전용 |
| PAT-003 | 선택 수 요약+단일 CTA 구조가 아님 — L1은 증상·등급 입력 중심이며 하단은 **병원 추천·이송** 단일 주 CTA |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 뒤로가기 | chevronLeft (`icon.baseicon.tokens.chevronLeft`) | 2:599 | 24×24 | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 주증상 필드(검색형) | search (`icon.baseicon.tokens.search`) | 2:1082 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 일지 미연계 배너 | info (`icon.baseicon.tokens.info`) | 2:863 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |
| 비동기 처리 중 | loader (`icon.baseicon.tokens.loader`) | 2:896 | 20×20 | text-secondary — gray.600 |
| 완료 | checkCircle (`icon.feedback.tokens.checkCircle`) | 2:588 | 20×20 | success — success.600 #039855 (rgba(3,152,85,1)) |
| 오류·주의 | alertTriangle (`icon.feedback.tokens.alertTriangle`) | 2:472 | 20×20 | error / warning — error.600 또는 warning.600 |
| 재시도·재분석 | refreshCw (`icon.baseicon.tokens.refreshCw`) | 2:1058 | 20×20 | primary — brand.600 #7F56D9 (rgba(127,86,217,1)) |
| P-class 아코디언 | chevronDown (`icon.baseicon.tokens.chevronDown`) | 2:596 | 20×20 | text-secondary — gray.600 |
| Class 체크 | check (`icon.baseicon.tokens.check`) | 2:593 | 18×18 | primary(선택 시)·text-disabled(미선택) |
| 저장·확정(블록 내) | save (`icon.baseicon.tokens.save`) | 2:1076 | 20×20 | text-secondary 또는 primary |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #FAFAFA (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ 앱 바: 뒤로 + 제목            │  h: 56px
├─────────────────────────────┤
│ 일지 미연계 배너 (조건)       │
├─────────────────────────────┤
│ ┌ 증상 입력 카드 ─────────┐  │  surface, border, radius.lg
│ │ 주증상·부증상·요약        │  │
│ └─────────────────────────┘  │
│        gap 24 (spacing.3xl)   │
│ ┌ pre-KTAS (PAT-001) ─────┐  │
│ │ 스텝퍼/배지·본문·재시도    │  │
│ └─────────────────────────┘  │
│        gap 24                 │
│ ┌ P-class (PAT-001+아코디언)┐  │
│ │ 상태행·Class I~V          │  │
│ └─────────────────────────┘  │
│ ┌ Class III 인포 (조건)     ┐  │
│ └─────────────────────────┘  │
│         (스크롤)              │
├─────────────────────────────┤
│ 고정: 병원 추천·이송 CTA      │  primary fill, min-h 48~52
└─────────────────────────────┘
```

### 앱 바

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white #FFFFFF | G1 헤더와 동일 |
| 하단 테두리 | 1px border — gray.300 | 구조적 분리 |
| 높이 | 56px | 표준 |
| 패딩 | 좌8~12(뒤로) + 좌16 콘텐츠 — spacing 정렬 | 뒤로 44px 터치 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 뒤로 | 아이콘 버튼 | chevronLeft (2:599) 24×24 | — | text-primary — gray.900 |
| 제목 | 텍스트 | "평가·증상" | heading — 24/32/0 Semibold | text-primary — gray.900 |

### 일지 미연계 배너 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface-raised — gray.100 #F5F5F5 | 강조 면적 최소 |
| 좌측 앵커 | 3px 세로 바 — accent blue.600 | visual-direction 섹션 바 변형(정보성은 accent 허용) |
| 테두리 | 하단 1px border — gray.300 | |

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 아이콘 | 아이콘 | info (2:863) 20×20 | — | accent — blue.600 |
| 문구 | 텍스트 | "일지가 없습니다. 음성 기록을 권장하지만, 평가는 계속할 수 있어요." | body — 16/24/0 Regular | text-primary — gray.900 |

### 증상 입력 카드 (주·부·요약)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white | |
| 테두리 | 1px border — gray.300 | shadow 없음 |
| radius | radius.lg 10px | |
| 내부 패딩 | spacing.xl 16px | |
| 섹션 제목 행 | 좌측 **4px primary 바** + "증상" 또는 분리된 소제목 | visual-direction 색상 허용 위치 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 섹션 타이틀 | 텍스트 | "주증상" / "부증상" / "증상 요약" | subheading — 18/28/0 Semibold | text-primary — gray.900 |
| 주증상 필드 | 입력/피커 | placeholder "주증상 선택" | body — 16/24/0 Regular | text-primary; placeholder — text-disabled gray.400 #A4A7AE (rgba(164,167,174,1)) |
| 필드 배경 | surface-raised | gray.100 | — | 카드 white와 대비 |
| 필드 테두리 | 1px border — gray.300 | radius.md 8px | |
| 검색 아이콘 | 아이콘 | search (2:1082) 20×20 | — | text-secondary |
| 부증상 칩 | 칩 + 입력 | 다중 태그 | label — 14/20/0 Medium | border gray.300, 배경 white 또는 gray.50 |
| 증상 요약 | 멀티라인 필드 또는 카드 본문 | 비동기 생성+수동 편집 | body — 16/24/0 Regular | text-primary |
| 일지 연계 한 줄 | 텍스트 | "일지에서 반영된 항목이 있어요" 등 | caption — 12/18/0 Regular | accent 링크 가능 — blue.600 |

### pre-KTAS 블록 (PAT-001)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 카드 동일 | white + border + radius.lg | G1 타임라인 카드와 톤 통일 |
| 상단 스텝퍼 행 | **최소 높이 44px** | visual-direction 네비 무게감 |
| 스텝 노드 | 지름 28px 권장 | 현재: **primary fill + 흰 숫자/체크**, 완료: **success**, 미완: **gray.200 배경 + gray.500 텍스트** (문구는 caption) |

#### 스텝퍼·상태 (예시 4단계)

| 단계 | 표시 | 색상 |
|------|------|------|
| 대기 | 원 gray.200, 숫자 gray.600 | 중립 |
| 처리 중 | 원 primary + loader 아이콘 병치 가능 | primary |
| 완료 | checkCircle 또는 원 success | success |
| 오류 | alertTriangle + 재시도 | error + primary 텍스트 버튼 |

#### 본문 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 등급 표시 | 텍스트/세그먼트 | 확정 전 placeholder "등급 분석 중…" | body | text-secondary |
| 근거 요약 | 텍스트 | 접기/펼치기 | caption·body | text-secondary / text-primary |
| 재시도 | 텍스트 버튼 | "다시 분석" + refreshCw | label | primary |
| 확정·저장 | 버튼(보조) | 블록 하단 또는 툴바 | button | outline primary 또는 secondary |

### P-class 블록 (PAT-001 변형 + 아코디언)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 상단 | pre-KTAS와 **동일 높이의** 스텝퍼/배지 행 | 병렬 비동기 **대등함** 시각화 |
| 본문 | Class I~V **아코디언** — 헤더 행 48px, chevronDown | 한 손으로 펼치기 |
| Class II delivery | 기본 체크 ON 시각 | check (2:593) + label "분만(제안)" |

#### 아코디언 헤더

| 요소 | 타이포 | 색상 |
|------|--------|------|
| Class 명 | subheading — 18/28/0 Semibold | text-primary |
| 선택 개수 | caption | text-secondary |
| chevronDown | 20×20 | text-secondary |

#### 체크 행

| 요소 | 설명 |
|------|------|
| 터치 행 | 최소 높이 44px, 좌 체크 24px 영역 |
| 라벨 | body — 16/24/0 Regular, text-primary |

### Class III 인포 배너 (조건부)

| 속성 | 값 |
|------|-----|
| 배경 | surface-raised gray.100 |
| 좌측 바 | 3px warning.600 또는 accent (정보성 — **아이콘 info 병행** 권장) |
| 본문 | body 16/24 — "ICU·NICU·IR 병원 추천에 반영됩니다" 류 |

### 하단 고정 CTA

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface white | |
| 상단 | 1px border — gray.300 | |
| 버튼 | 전폭, min-height **48~52px**, radius.md 8px | |
| 문구 | "병원 추천·이송" | button — 16/24/0 Semibold |
| 색상 | **fill primary** — brand.600 | 화면당 주 CTA **이 1곳**이 primary 면적의 중심 |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|-------------|----------|------|
| 주증상 선택 | 증상 카드 필드 | body / label | text-primary | 필수 |
| 부증상 | 칩·입력 | label / body | text-primary | |
| P-class 서브클래스 | 아코디언 내 체크 | body | text-primary | delivery 기본 ON |
| pre-KTAS 등급 | pre-KTAS 카드 | body | text-primary / secondary | 미확정 시 placeholder |
| L1 필수 보완 필드 | 인라인 | label + body | error 인접 | 플로우 3 |
| pre-KTAS 비동기 단계 | 스텝퍼·배지 | caption / label | primary·success·gray | |
| P-class 비동기 단계 | 동일 | 동일 | 독립 표시 | pre-KTAS와 혼동 금지 |
| 증상 요약 | 증상 카드 | body | text-primary | |
| pre-KTAS 근거 요약 | pre-KTAS 카드 접이식 | caption | text-secondary | |
| Class III 안내 | 인포 배너 | body | text-primary | 조건부 |
| 일지 연계 | 증상 카드 한 줄 | caption | accent | 선택 |
| 엔진 오류 | 해당 블록 | body | error | 재시도 인접 |
| 병원 추천·이송 CTA | 하단 고정 | button | primary fill | → L2 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 | — | — | — |
| 증상·비동기 카드 | white | gray.50 | 충분 | border |
| 입력·요약 필드 | gray.100 | white | 충분 | surface-raised |
| 배너 | gray.100 | white/gray.50 | 충분 | |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 |
|------|------|------------|------|
| 카드·고정 바 | — | 없음 | 테두리 우선 |
| (모달·시트 도입 시) | 오버레이 | shadow-md / lg | 레이어 겹침 시만 |

### 타이포 위계
| 수준 | 역할 | 스펙 | 적용 요소 |
|------|------|------|----------|
| 1 | heading | 24/32/0 Semibold | 앱 바 제목 |
| 2 | subheading | 18/28/0 Semibold | 섹션·아코디언 헤더 |
| 3 | body / caption / label | 16/24/0 · 12/18/0 · 14/20/0 | 본문·메타·칩 |

### 강조 검증
- focal point: **주증상 필드** — 큰 터치 영역·surface-raised·아이콘
- primary 사용: **하단 「병원 추천·이송」** + 스텝퍼 현재 단계 + 소면적 강조 **≤3곳**
- 상태: 아이콘(loader/checkCircle/alertTriangle) + 배지 + 문구

### 밀도 검증
- 스텝퍼 행·아코디언 헤더·하단 CTA·뒤로: **44px 이상**

### 시각 밀도 검증
- 스크롤 영역: 카드 2~3개 + 배너 + 증상 카드로 **빈 단색면 50% 미만** 유지
- 텍스트만 블록 금지 — 각 블록에 스텝퍼·바·아이콘·배지 중 택1 이상
- pre-KTAS vs P-class: **동일 카드 크기감** + **상태 색 차이**로 구분
- 섹션 헤더: 좌측 **3~4px primary 바** 필수에 가깝게 적용
- 스텝퍼: visual-direction 무게감 기준 충족

### 일관성 체크
- [ ] 색상·타이포·간격·radius가 design-system.md와 일치
- [ ] shadow 남용 없음
- [ ] visual-direction.mdc와 충돌 없음
