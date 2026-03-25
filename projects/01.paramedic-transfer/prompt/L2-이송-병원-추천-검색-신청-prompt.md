# 디자인 명세 — L2 이송 병원 추천·검색·신청

## 화면 개요
- **목적**: 세션 맥락 기반 추천과 직접 검색을 한 화면에서 다루며, 복수 병원을 선택한 뒤 일괄 이송 신청까지 완료한다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 구급 현장에서 일지·증상 맥락을 두고 병원을 고르고 신청하는 바쁜 멀티태스킹 상황.
- **핵심 행동**: 병원을 1곳 이상 선택한 후 **「일괄 이송 신청」**을 눌러 제출한다.

## 시각적 의도

> 이 화면이 완성되었을 때 **어떻게 보이고 느껴져야 하는지** 서술한다.
> visual-direction.mdc의 비주얼 톤을 이 화면에 구체적으로 적용한 기술.

- **분위기**: 의료 도구의 신뢰감을 유지하되, 친근하고 스캔하기 쉬운 목록·탭 구조. 정보는 흰 카드와 회색 배경 대비로 블록 단위 구분.
- **시각적 초점 (focal point)**: 스크롤 영역의 **체크 가능한 병원 행 카드 스택** — 병원명·적합 요약·추천 사유(추천 탭)가 한눈에 들어오도록 밀도를 맞춘다.
- **색상 톤**: 페이지는 중립 배경, 카드는 surface 흰색 + **1px border(gray.300)** 로 경계. primary는 탭 활성·선택 체크·주 CTA에만 소면적 집중. accent는 링크·거리 등 보조 정보.
- **밀도**: 중간 — `spacing.xl`(16px) 패딩, 섹션 간 `spacing.3xl`(24px). 터치 타깃 최소 44px(탭 행·칩·체크 영역·CTA).
- **디자인 핵심**: 카드 내부는 **surface-raised** 입력면과 흰 카드 면의 휘도 차로 계층을 잡고, 선택된 카드는 **primary 좌측 4px 상태 바** 또는 체크 강조로 즉시 구분. 하단 바는 콘텐츠 위에 떠 있는 레이어로 **shadow-md**만 사용(테두리와 그림자 동시 사용 금지).

---

## Visual Recipe

배경은 **background — gray.50 (#FAFAFA)** 로 전체를 깔고, 상단부터 헤더·조건부 배너·탭·(검색 탭 시) 검색·필터 줄·목록이 수직으로 이어진다. 병원 카드는 **surface — white (#FFFFFF)** 에 **border — gray.300 (#D5D7DA)** 1px, **radius.lg (10px)**; 카드 좌측에 미선택은 얇은 중립 바 또는 여백, **선택 시 primary — brand.600 (#7F56D9) 4px 세로 바**로 반복 카드 간 상태를 분리한다. 추천 탭 카드에는 **「추천」칩 + 불릿 요약**으로 텍스트만 있는 카드를 피한다. 하단 **PAT-003** 영역은 선택 수·한 줄 요약과 **primary fill CTA** 한 줄로 시선을 마무리하며, 신청 대기 중에는 **warning 계열 아이콘+문구**와 **accent 링크형 「병원 응답 보기」**를 보조 행에 둔다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-002 | 병원 행 카드 | 추천·검색 목록 전체 — 체크 선택 변형(좌측 체크 + 병원명·식별·요약·적합·추천 사유/거리) | 94:4470 |
| PAT-003 | 하단 요약 액션 바 | 화면 하단 고정 — 「N곳 선택」요약 + 「일괄 이송 신청」CTA; 신청 중·대기 중 보조 문구 | 94:4475 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-001 | 비동기·상태 카드는 일지·승인 단계(G1·L1·L3)용 구조이며, L2는 병원 **선택·목록**이 주 흐름이라 PAT-002·003으로 충분하다. |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 헤더 뒤로 | chevronLeft | 2:510 | 24×24 | text-primary — gray.900 #181D27 |
| 검색 필드 선행 | search | 2:1082 | 20×20 | text-secondary — gray.600 #535862 |
| 필터 칩·시트 진입 | filter | 2:788 | 20×20 | text-secondary — gray.600 #535862 |
| pre-KTAS·안내 배너 | info | 2:863 | 20×20 | accent — blue.600 #1570EF (아이콘) / 본문은 text-primary |
| 오류 배너 | alertCircle (feedback) | 2:467 | 20×20 | error — error.600 #D92D20 |
| 오프라인 배너 | wifiOff | 2:1280 | 20×20 | warning — warning.600 #DC6803 |
| 신청 대기·시간 맥락 | clock | 2:629 | 20×20 | warning — warning.600 #DC6803 |
| 재시도 | refreshCw | 2:1058 | 20×20 | accent — blue.600 #1570EF |
| 응답 보기·외부 진행 | chevronRight | 2:602 | 20×20 | accent — blue.600 #1570EF |
| 카드 거리·위치 보조 줄 | mapPin | 2:911 | 20×20 | accent — blue.600 #1570EF |
| 전문·태그 칩(선택) | tag | 2:1163 | 20×20 | text-secondary — gray.600 #535862 |
| L1 보완 링크 | link | 2:887 | 20×20 | accent — blue.600 #1570EF |
| 체크 선택(카드 내) | check | 2:593 | 20×20 | 선택 시 primary — brand.600 #7F56D9 / 미선택 시 border 톤 gray.300 |
| 신청 진행 중 | loader | 2:896 | 24×24 | primary — brand.600 #7F56D9 |
| 추천 칩 | star | 2:1145 | 16×16 | text-secondary — gray.600 #535862 |

---

## 레이아웃 구조

### 전체 구조

화면 배경: **background — gray.50 (#FAFAFA)**

```
┌─────────────────────────────┐  390 × 844
│ 앱 바: 뒤로 + 제목            │  h: 56px
├─────────────────────────────┤
│ 조건부 배너(스크롤 상단 포함) │
├─────────────────────────────┤
│ 탭: 추천 | 검색               │  h: ≥44px
│ [검색 탭만] 검색행 + 필터칩    │
│ [추천: 필터 요약 칩만 조건부]  │
├─────────────────────────────┤
│                              │
│  병원 목록 (스크롤)            │  flex 1
│  ┌ PAT-002 카드 ─────────┐   │
│  │ □ 병원명 (subheading)   │   │
│  │   식별·전문 요약 body   │   │
│  │   적합·추천·거리        │   │
│  └───────────────────────┘   │
│         ⋮                    │
├─────────────────────────────┤
│ PAT-003 하단 바 + shadow-md   │
└─────────────────────────────┘
```

### 앱 바 (헤더)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭 × **56px** (콘텐츠 기준) | 표준 모바일 타이틀 바. |
| 배경 | **surface — white (#FFFFFF)** | 본문 스크롤과 분리된 고정 상단. |
| 배치 | 수평 스택 — 뒤로 / 제목 중앙 또는 시작 정렬 | 한 손 조작 시 뒤로 접근성. |
| 주축 정렬 | 양끝 또는 시작+중앙 | 플랫폼 네이티브에 맞추되 제목 가독 우선. |
| 교차축 정렬 | 중앙 | |
| 내부 여백 | 좌우 **spacing.xl (16px)** | visual-direction 기본 패딩. |
| 요소 간격 | **foundation spacing.md (8px)** — 인접 아이콘~제목 | design-system은 xl·3xl 위주; 세밀 간격은 foundation `spacing` 스케일. |
| 모서리 | 없음 | |
| 깊이 | 하단 **1px border — gray.300 (#D5D7DA)** | surface와 스크롤 영역 구분(shadow 없음). |
| 테두리 | 하단만 border | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 뒤로 | 아이콘 버튼 | chevronLeft (2:510) 24×24 | — | text-primary — gray.900 #181D27 |
| 제목 | 텍스트 | "이송 병원" 등 | **heading** — 24px/32px/0 semibold | text-primary — gray.900 #181D27 |

### 조건부 배너 영역 (pre-KTAS·대기·오류)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭, 내용 높이 가변 | 여러 배너가 동시에면 **foundation spacing.md (8px)** 간 수직 스택. |
| 배경 | 안내: **surface — white (#FFFFFF)** 카드형 또는 상단 인셋 블록 / 오류: 동일 surface + 좌측 **warning 또는 error 4px 바** 선택 | 정보 vs 경고 위계. |
| 배치 | 수직 스택 | |
| 내부 여백 | **spacing.xl (16px)** | |
| 모서리 | 하단만 또는 전체 **radius.lg (10px)** (페이지 패딩 안에 떠 있는 카드 느낌) | |
| 깊이 | **없음** — **1px border — gray.300** | 구조적 구분. |
| 테두리 | 1px border | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 안내 아이콘 | 아이콘 | info (2:863) 20×20 | — | accent — blue.600 #1570EF |
| pre-KTAS 미확정 문구 | 텍스트 | (스펙 문구) | **body** — 16px/24px/0 regular | text-primary — gray.900 #181D27 |
| 보조 한 줄 | 텍스트 | 미확정이어도 신청 가능 등 | **caption** — 12px/18px/0 regular | text-secondary — gray.600 #535862 |
| L1 보완 | 텍스트 링크 | "평가 보완하기" 등 | **label** — 14px medium + 밑줄 또는 accent | accent — blue.600 #1570EF |
| 대기 배지 행 | 아이콘+텍스트 | clock + "이송 신청 대기 중" | body + caption | warning 아이콘 — warning.600 #DC6803 |
| 응답 보기 | 텍스트 버튼 | "병원 응답 보기" | **label** medium | accent — blue.600 #1570EF + chevronRight 20px |
| 오류 | 아이콘+텍스트 | alertCircle + 메시지 | body | error — error.600 #D92D20 |
| 재시도 | 텍스트 버튼 | refreshCw + "다시 시도" | label | accent — blue.600 #1570EF |

### 탭 행 (추천 / 검색)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭 × **min 44px** | 터치 타깃. |
| 배경 | **surface — white (#FFFFFF)** 또는 background와 동일 영역 내 인셋 | 목록과 한 덩어리로 읽히게. |
| 배치 | 두 탭 **수평 균등 분할** 또는 중앙 기준 균형 | |
| 주축 정렬 | 중앙 | |
| 내부 여백 | 상하 **foundation spacing.md (8px)** 좌우 **spacing.xl (16px)** | |
| 활성 표시 | **하단 2~3px 바 — primary brand.600** | visual-direction 탭 규칙. |
| 비활성 라벨 | **body** regular, **text-secondary — gray.600** | |
| 활성 라벨 | **body** semibold(또는 subheading 스케일 생략 시 굵기만 강화), **text-primary** | 타이포 위계 3단 이내 유지. |

### 검색 탭 전용 — 검색 필드 행

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 컨테이너 | 전폭, 높이 **min 48px** | 입력 터치 영역. |
| 입력 fill | **surface-raised — gray.100 (#F5F5F5)** | 카드/배경과 휘도 계층. |
| 테두리 | **1px border — gray.300** | |
| radius | **radius.md (8px)** | 버튼과 리듬 맞춤. |
| 내부 여백 | 좌우 **spacing.xl (16px)** | |
| 플레이스홀더 | **caption** 색상 역할 **text-disabled — gray.400 #A4A7AE** | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 검색 아이콘 | 아이콘 | search (2:1082) 20×20 | — | text-secondary — gray.600 #535862 |
| 입력 텍스트 | 텍스트 필드 | 검색어 | **body** 16px/24px | text-primary — gray.900 #181D27 |
| 검색 실행 | 아이콘 버튼·엔터 | 우측 send (2:1085) 20×20 또는 키보드 엔터(스펙 동일) | — | primary — brand.600 #7F56D9 (아이콘 버튼) / 엔터만 시 별도 버튼 생략 가능 |

### 필터 칩 행 (검색 탭 / 추천 탭 요약)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배치 | 수평 스크롤 칩 행 | 많은 필터를 한 줄에 노출. |
| 추천 탭 동작 | 적용 중인 **필터 요약 칩**이 보일 때, **칩 행(또는 「필터」진입) 탭 → 검색 탭과 동일 필터 시트** 오픈 | screen-spec: 추천 탭은 요약 칩 + 탭 시 시트. |
| 칩 높이 | **32~36px** (터치 ≥44px이면 행 패딩으로 보완) | |
| 칩 배경 | 미적용: **surface-raised gray.100** / 적용됨: **primary hover 톤의 연한 대비**(소면적 primary — 동일 톤 8~12% 알파 느낌을 단색으로 시뮬레이션 시 **surface** + **border primary** 1px로 대체 가능) | 장식적 대면적 색 블록 금지 원칙 준수. |
| 칩 텍스트 | **label** — 14px/500 | text-primary 또는 primary 텍스트(활성 칩). |
| 「필터」칩 | filter 아이콘 + 라벨 | 전체 시트 오픈. |

> **필터 바텀시트**(별도 오버레이): 시트 표면 **surface white**, 상단 핸들 또는 제목, 본문 스크롤, 하단 고정 **「초기화」** — 시트는 **shadow-md** (레이어 겹침). 시트 테두리 상단 1px **border gray.300** 선택 가능(shadow와 중복 강조는 피함).

### 병원 목록 (스크롤)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 영역 배경 | **background — gray.50** | 카드와 대비. |
| 카드 간격 | **foundation spacing.md (8px)** 또는 **spacing.xl (16px)** | 스캔 리듬; 블록 단위 구분은 **spacing.3xl (24px)**. |
| 카드 | **PAT-002** — **border 1px gray.300**, **radius.lg 10px**, 패딩 **spacing.xl 16px** | 그림자 없음. |
| 선택 강조 | 좌측 **4px bar — brand.600** + 체크 영역 primary | visual-direction 상태 바 규칙. |
| 빈 상태 | 중앙 정렬 일러스트 대신 **아이콘 48px 영역**(search 또는 info) + 제목 subheading + body 안내 + **「필터 초기화」 링크**(조합 0건 시) | screen-spec 엣지: 0건 시 초기화 제안. |
| 로딩 | 3~5개 **스켈레톤 카드**(회색 막대) | 단색 빈 화면 50% 초과 금지. |

#### PAT-002 카드 내부 요소 (L2 변형)

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 체크 | 터치 영역 + 아이콘 | square/check 토글 44×44 터치 | — | 미선택 border gray.300 / 선택 primary fill + 흰 check |
| 병원명 | 텍스트 | (데이터) 2줄까지 허용(clamp) | **subheading** — 18px/28px/0 semibold | text-primary — gray.900 #181D27 |
| 식별·전문 요약 | 텍스트 | 1~2줄 | **body** 16px/24px | text-secondary — gray.600 #535862 |
| 적합 요약 | 텍스트 | 의사결정 한 줄 | **body** 16px/24px | text-primary — gray.900 #181D27 |
| 추천 사유 | 텍스트·불릿 | 추천 탭만 | **body** + bullet accent dot 소형 | text-secondary / bullet accent |
| 추천 칩 | 칩 | "추천" | **label** | surface-raised 배경 + border + **star 아이콘** 선택 시 2:1145 16px text-secondary |
| 거리 줄 | 아이콘+텍스트 | mapPin + "약 N km" | **caption** 12px/18px | accent — blue.600 #1570EF |

### 하단 고정 — PAT-003

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭 × **min 80px** (요약+CTA+보조) | 안전 영역 포함. |
| 배경 | **surface — white (#FFFFFF)** | |
| 내부 여백 | **spacing.xl (16px)** 상하좌우 | |
| 깊이 | **shadow-md** — foundation 매핑(y:4 blur:8 α≈0.10) | 콘텐츠 위 레이어만 그림자 허용. |
| 테두리 | 없음 | visual-direction: 테두리와 그림자 동시 사용 금지 → 하단 바는 **shadow-md**만으로 목록과 분리. |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 선택 요약 | 텍스트 | "3곳 선택" 등 | **subheading** 또는 **body** semibold | text-primary — gray.900 #181D27 |
| 진행 상태 | 텍스트·스피너 | 신청 중 문구 + loader | **caption** + loader 아이콘 | text-secondary / primary 아이콘 |
| 보조 링크 | 텍스트 | "신청 대기 중 · 응답 보기" | **label** | accent — blue.600 #1570EF |
| 주 CTA | 버튼 전폭 | "일괄 이송 신청" | **button** — 16px/24px semibold | 배경 primary brand.600 #FFFFFF 텍스트 / 비활성 surface-raised + text-disabled |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|------------|----------|------|
| 병원 선택(체크) | PAT-002 카드 좌측 | — | primary / border | 탭 간 동기화 |
| 검색어 | 검색 필드 | body | text-primary | 검색 탭만 |
| 필터 세트 | 칩·시트 | label | text-primary / accent | 정렬·거리·전문 등 |
| 이송 신청 대기 상태 | 배너·하단 보조 | body / label | warning·accent | 조건부 |
| 병원 응답 보기 | 배너·하단 | label | accent | 대기 중만 |
| 일괄 이송 신청 CTA | PAT-003 | button | primary | 0선택 시 비활성 |
| 병원명 | 카드 제목 | subheading | text-primary | 다줄 허용 |
| 병원 식별·위치·전문 요약 | 카드 본문 | body | text-secondary | |
| 적합 요약 | 카드 본문 | body | text-primary | |
| 추천 사유 | 카드 본문 | body | text-secondary | 추천 탭 |
| 거리·이동 정보 | 카드 보조 줄 | caption | accent | 제공 시만 |
| pre-KTAS 미확정 안내 | 상단 배너 | body / caption | text-primary / secondary | |
| L1 보완 유도 링크 | 배너 내 | label | accent | 선택 |
| 선택 병원 수(N) | 하단 요약 | subheading/body | text-primary | |
| 신청 진행 상태 | 하단·CTA | caption | text-secondary | |
| 신청 시각·병원 ID 목록(성공 후) | 토스트·전환 직전 요약(구현 정책에 따름) | caption / body | text-secondary / text-primary | L3 전달·ia; 화면 체류 짧을 수 있음 |
| 오류 메시지 | 배너·토스트 | body | error | |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 #FAFAFA | — | — | — |
| 카드 | white #FFFFFF | gray.50 | 충분 | border로 추가 구분 |
| 검색 입력 | gray.100 #F5F5F5 | 흰 배너 또는 gray.50 | 충분 | surface-raised 유지 |
| 하단 바 | white #FFFFFF | 목록 마지막 카드 white | 인접 동일 가능 | 상단 **shadow-md**로 분리 |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 병원 카드 | 카드 | 없음 (border만) | 구조적 UI는 테두리 우선 |
| 필터 바텀시트 | 오버레이 시트 | **shadow-md** | 레이어 겹침 시 허용 |
| 하단 PAT-003 바 | 고정 바 | **shadow-md** | 스크롤 콘텐츠 위 플로팅 레이어 |

### 타이포 위계
| 수준 | 역할 | 스펙 (크기/행간/자간/굵기) | 적용 요소 |
|------|------|-------------------------|----------|
| 1 | heading | 24/32/0 semibold | 앱 바 제목 |
| 2 | subheading | 18/28/0 semibold | 카드 병원명·하단 선택 수 강조 |
| 3 | body | 16/24/0 regular | 본문·목록·입력 |
| (보조) | caption | 12/18/0 regular | 거리·타임스탬프·배너 보조 |
| (액션) | label / button | 14 medium / 16 semibold | 칩·링크·CTA |

### 강조 검증
- focal point: **병원 행 카드 목록** — 밀도 있는 본문·좌측 상태 바·추천 칩으로 스캔성 확보 — 근거: screen-spec 주요 영역.
- primary 사용: **탭 활성 바**, **선택 상태(체크·좌측 바)**, **주 CTA**, **로더**(신청 중) — 화면당 주 CTA 1곳 + 소면적 강조 ≤3 원칙 준수.
- 상태 표현: 대기·오류는 **아이콘 + 색 + 문구** 병행.

### 밀도 검증
- 터치 가능 요소: 뒤로·탭·칩·카드 행·체크·CTA — 높이 **≥44px** 또는 패딩으로 충족.
- ❌ 미충족 시: 탭·칩 행 세로 패딩 증가.

### 시각 밀도 검증
- 스크롤 영역 중 빈 배경 비율 추정: 목록 정상 시 **50% 미만** (카드·스켈레톤·빈 상태 블록으로 충전).
- 텍스트 전용 카드: **금지** — 아이콘·칩·좌측 바·불릿으로 보강.
- 반복 카드 차별화: 동일 구조 **3장 이상** 시 **선택 여부에 따른 primary 좌측 4px 바** + 체크 상태로 구분.
- 섹션 헤더 앵커: 탭이 섹션 역할 — 추천/검색 **활성 탭 하단 primary 바 2~3px**로 앵커 충족.
- 네비 요소 무게감: **탭 활성 = primary 하단 바 + 굵은 라벨**, 높이 **≥44px** — 충분.

### 일관성 체크
- [ ] 모든 색상이 design-system.md 팔레트 키 참조
- [ ] 모든 타이포가 design-system.md·visual-direction 역할 표와 일치
- [ ] 행간·자간이 design-system.md 세밀값·visual-direction 보조값과 일치
- [ ] shadow는 레이어 겹침 요소에만 design-system.md 이펙트 토큰 사용
- [ ] visual-direction.mdc 확정 디자인 결정과 충돌 없음
