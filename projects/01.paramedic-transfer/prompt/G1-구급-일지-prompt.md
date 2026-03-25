# 디자인 명세 — G1 구급 일지

## 화면 개요
- **목적**: 현장에서 음성·STT·NER로 쌓인 구급 일지를 시간순으로 스캔·검토·수정하고, 평가(L1) 또는 병원 추천(L2)으로 넘어갈 수 있는 허브 역할을 한다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 앰뷸런스 현장에서 처치·이동 중, 바쁜 멀티태스킹 상태로 짧은 시선으로 타임라인과 동기화·이송 맥락을 확인한다.
- **핵심 행동**: 타임라인 카드를 확인·필요 시 편집한 뒤, 하단에서 **「평가·증상」** 또는 **「병원 추천·이송」** 중 다음 단계로 분기한다.

## 시각적 의도

- **분위기**: 의료 도구로서의 신뢰감을 유지하되, 카드·배지·아이콘으로 **친근하고 활동적인** 스캔 경험을 준다. 장식용 대색면 없이 **기능 단위 소면적 컬러**로 상태를 드러낸다.
- **시각적 초점 (focal point)**: 스크롤 영역 중앙부의 **최신(또는 가장 최근 상호작용) 일지 타임라인 카드** — 시각·상태 배지·핵심 필드가 한눈에 들어오도록 한다.
- **색상 톤**: 페이지 배경은 중립 **background(gray.50)**, 카드는 **surface(white)** + **1px border**로 구조를 잡고, 상태는 좌측 4px 바·배지·아이콘으로만 강조한다. 주 CTA는 **primary(brand.600)** 를 **하단 1차 버튼 1곳**에 집중한다.
- **밀도**: **중간** — `spacing.xl`(16px) 패딩, 카드 간 `spacing.3xl`(24px) 리듬. 터치 타깃 최소 **44px** (하단 CTA·플로팅·헤더 액션).
- **디자인 핵심**: 타임라인 카드가 **PAT-001** 구조(상태·시각·조건부 본문)로 통일되어 스캔 속도가 나고, **surface-raised** 입력면으로 카드 위 필드 계층이 분리된다. 이송 중일 때만 **플로팅 바 + shadow-md**로 레이어가 분리된다.

---

## Visual Recipe

화면 전체는 **gray.50** 바탕에 **흰 카드 타임라인**이 세로로 이어지는 **일지 허브**로 보인다. 상단은 제목과 동기화가 한 행에 정리되고, 조건부 배너·STT 한 줄·(이송 중이면) 플로팅 바가 그 아래를 **얇고 밀도 있게** 차지한 뒤 스크롤이 시작된다. 시선은 자연스럽게 **가장 위 또는 강조된 카드**로 이동하고, 하단에는 두 개의 넓은 버튼이 **안전한 다음 행동**을 제시한다. 카드는 **테두리만**으로 구분해 현장 조명에서도 윤곽이 흐려지지 않게 한다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 비동기·상태 카드 | 일지 타임라인 각 항목 — 시각·상태 배지·필드/원문·오류·재시도 영역 | 94:4467 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-002 | 병원 행 카드는 L2·L3 전용 — G1에는 병원 목록이 없음 |
| PAT-003 | 하단 요약 액션 바는 선택 요약+단일 CTA 구조로 L2·L3에 맞춤 — G1은 **이중 고정 CTA** 전용 레이아웃 |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 헤더 동기화 | refreshCw (`icon.baseicon.tokens.refreshCw`) | 2:1058 | 24×24 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| STT·인식 소형 행 | mic (`icon.baseicon.tokens.mic`) | 2:938 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) 또는 상태에 따라 primary / warning |
| 오프라인·동기 배너 | wifiOff (`icon.baseicon.tokens.wifiOff`) | 2:1280 | 20×20 | warning — warning.600 #DC6803 (rgba(220,104,3,1)) |
| 일지 카드 편집 | edit2 (`icon.baseicon.tokens.edit2`) | 2:743 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 기록 시각 | clock (`icon.baseicon.tokens.clock`) | 2:629 | 16×16 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 항목 오류 | alertTriangle (`icon.feedback.tokens.alertTriangle`) | 2:472 | 20×20 | error — error.600 #D92D20 (rgba(217,45,32,1)) |
| 완료·정상 | checkCircle (`icon.feedback.tokens.checkCircle`) | 2:588 | 20×20 | success — success.600 #039855 (rgba(3,152,85,1)) |
| 이송 플로팅 진입 | chevronRight (`icon.baseicon.tokens.chevronRight`) | 2:602 | 20×20 | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 플로팅 닫기(선택) | x (`icon.baseicon.tokens.x`) | 2:1298 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 빈 상태 앵커 | fileText (`icon.baseicon.tokens.fileText`) | 2:779 | 48×48 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #FAFAFA (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ 앱 바 / 헤더                 │  h: 56px (콘텐츠 영역 기준)
├─────────────────────────────┤
│ 동기화·오프라인 배너 (조건)   │  h: auto, 패딩 세로 12
├─────────────────────────────┤
│ 이송 중 플로팅 바 (조건)      │  h: 48~52, shadow-md
├─────────────────────────────┤
│ STT·인식 소형 한 줄          │  h: 40~44, surface 카드 또는 인라인
├─────────────────────────────┤
│                             │
│  스크롤: 타임라인            │
│  ┌ PAT-001 카드 ─────────┐  │  surface + border, radius.lg
│  └───────────────────────┘  │  gap spacing.3xl
│  ┌ PAT-001 카드 ─────────┐  │
│  └───────────────────────┘  │
│  (빈 상태: 일러스트+카피)      │
│                             │
├─────────────────────────────┤
│ 하단 이중 CTA                │  각 행 min-h 48~52, 상단 구분선 또는 그림자 없음(바 자체 surface)
└─────────────────────────────┘
```

### 앱 바 / 헤더

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 390 × 56px (안전영역 제외 본문 기준) | 표준 모바일 앱 바 |
| 배경 | surface — white #FFFFFF (rgba(255,255,255,1)) | 본문과 구분; 하단에 1px border — gray.300 #D5D7DA (rgba(213,215,218,1)) |
| 배치 | 수평 스택 — 좌: 타이틀, 우: 동기화 아이콘 버튼 | 한 손 엄지 도달·스캔 용이 |
| 주축 정렬 | 양끝 | 제목 고정, 액션 분리 |
| 교차축 정렬 | 중앙 | 수직 정렬 안정 |
| 내부 여백 | 좌16 우16 상12 하12 — spacing.xl | visual-direction 기본 패딩 |
| 요소 간격 | 12px — 내부 고정 | 타이틀과 액션 분리 |
| 모서리 | 없음 | 전체 너비 붙임 |
| 깊이 | 없음 (테두리만) | 구조적 경계 |
| 테두리 | 하단 1px border — gray.300 | 헤더·콘텐츠 분리 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 화면 제목 | 텍스트 | "구급 일지" | heading — 24/32/0 Semibold | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 동기화 | 아이콘 버튼 | refreshCw (2:1058) 24×24 | — | text-secondary — gray.600 |

### 동기화·오프라인 배너 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭, 높이 auto | 한 줄~두 줄 메시지 |
| 배경 | surface-raised — gray.100 #F5F5F5 (rgba(245,245,245,1)) | 본문과 톤 구분, 과한 경고색 면적 방지 |
| 배치 | 수평 스택 — 아이콘 + 문구 + (재시도 텍스트 링크) | 스캔 가능한 한 줄 |
| 내부 여백 | 좌16 우16 상12 하12 — spacing.xl |
| 테두리 | 하단 1px border — gray.300 | 섹션 분리 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 아이콘 | 아이콘 | wifiOff 또는 alertCircle (2:467) 20×20 | — | warning 또는 text-secondary |
| 메시지 | 텍스트 | "오프라인입니다. 연결 후 동기화됩니다." 등 | body — 16/24/0 Regular | text-primary — gray.900 |
| 재시도 링크 | 텍스트 버튼 | "다시 시도" | label — 14/20/0 Medium | accent — blue.600 #1570EF |

### 이송 중 플로팅 바 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 좌우 margin 12~16, 높이 48~52px | 터치 타깃, 스크롤과 겹치지 않게 떠 있음 |
| 배경 | surface — white #FFFFFF | 카드형 플로팅 |
| 깊이 | shadow-md — foundation shadow.md (레이어 겹침) | visual-direction: 플로팅·시트만 그림자 |
| 모서리 | radius.lg 10px | 카드와 동일 리듬 |
| 테두리 | 없음 또는 아주 얇은 border — gray.300 | shadow 단독 우선 시 테두리 생략 가능 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 칩 | 칩 | "이송 진행 중" | label — 14/20/0 Medium, 배경 primary 8~10% 느낌의 밝은 보라(구현 시 surface 위 subtle fill 또는 border-primary) | primary 문구 — brand.600 |
| 병원 요약 | 텍스트 | "○○병원" (길면 말줄임) | body — 16/24/0 Medium | text-primary — gray.900 |
| 보조 시각 | 텍스트 | 확정 시각 등 | caption — 12/18/0 Regular | text-secondary — gray.600 |
| 진입 화살표 | 아이콘 | chevronRight (2:602) 20×20 | — | text-primary — gray.900 |
| 닫기(선택) | 아이콘 | x (2:1298) | — | text-secondary — gray.600 |

### STT·인식 소형 영역

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white, 좌우 margin으로 살짝 띄움 또는 전폭 얇은 띠 | 플로팅 아래로 밀림 — 플로팅 우선 |
| 테두리 | 1px border — gray.300, radius.md 8px | 입력·상태 띠 구분 |
| 내부 여백 | 좌12 우12 상10 하10 | 컴팩트 한 줄 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 마이크 | 아이콘 | mic (2:938) 20×20 | — | accent — blue.600 |
| 상태 문구 | 텍스트 | "듣는 중…" / "처리 중" 등 | caption 또는 body — 12~16 | text-secondary 또는 text-primary |

### 스크롤 — 타임라인 (PAT-001 일지 카드)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 영역 패딩 | 좌16 우16 상0 하 spacing.3xl | 헤더·플로팅과 리듬 맞춤 |
| 카드 간격 | spacing.3xl 24px | 섹션형 리듬 |
| 카드 배경 | surface — white #FFFFFF | background 대비 |
| 카드 테두리 | 1px border — gray.300 | **그림자 없음** (visual-direction 테두리 우선) |
| radius | radius.lg 10px | design-system |
| 좌측 상태 바 | 너비 4px, 카드 전고 — success / warning / error / primary | 상태 즉시 인지, 반복 카드 차별화 |

#### 카드 내부 (예시 구조 — PAT-001에 맞춤)

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 시각 | 텍스트 | "14:32" | caption — 12/18/0 Regular | text-secondary — gray.600 |
| 처리 상태 | 배지·아이콘 | "완료" + checkCircle / "오류" + alertTriangle | label — 14/20/0 Medium | success / error 토큰 |
| 필드 라벨·값 | 텍스트 | key→value (일지 항목) | subheading·body 조합 — 18/28/0 Semibold 제목행, 값은 body 16/24/0 | text-primary / text-secondary |
| NER 칩 | 칩 | 엔티티 태그 다수 | label — 14/20/0 Medium | border + text-secondary, 배경 surface-raised |
| 원문 토글 | 텍스트+아이콘 | "STT 원문 보기" + chevronDown | label | accent — blue.600 |
| 오류 메시지 | 텍스트 | 오류 사유 | body — 16/24/0 Regular | error — error.600 |
| 재시도 | 텍스트 버튼 | "다시 분석" | label — 14 Medium | primary — brand.600 |
| 편집 | 아이콘 버튼 | edit2 (2:743) | — | text-secondary |

### 빈 상태 (일지 0건)

| 요소 | 설계 의도 |
|------|----------|
| 중앙 영역 | fileText 또는 mic 아이콘 48px + 제목·본문 — **빈 배경 50% 초과 방지**를 위해 아이콘·짧은 bullet·음성 유도 카드형 블록 사용 |
| 제목 | subheading — "아직 일지 항목이 없습니다" |
| 본문 | body — "마이크로 말하면 기록이 쌓입니다. 평가·증상은 언제든 진행할 수 있어요." |
| 시각적 앵커 | 3~4px 세로 바 primary — 섹션 느낌 | 

### 하단 고정 이중 CTA

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white | 스크롤과 분리 |
| 상단 구분 | 1px border — gray.300 | elevation 대신 테두리 |
| 패딩 | spacing.xl 16px + safe-area | 터치·엄지 영역 |
| 버튼 간격 | 12px | 이중 행 세로 스택, 각 버튼 min-height **48~52px** (44px 이상) |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 1차 CTA | 버튼 | "평가·증상" | button — 16/24/0 Semibold | **fill primary** — brand.600 #7F56D9 (rgba(127,86,217,1)), 텍스트 white |
| 2차 CTA | 버튼 | "병원 추천·이송" | button — 16/24/0 Semibold | **outline** — border gray.300, 텍스트 text-primary (또는 secondary); primary 면적 예산 점유 최소화 |

> 일지 0건이어도 **두 버튼 모두 비활성화하지 않음** — 시각적으로 동일한 가시성 유지.

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|-------------|----------|------|
| STT·인식 진행 상태 | STT 소형 행 | caption / body | accent·text-secondary | 짧은 한 줄 |
| 일지 항목 확정값 | PAT-001 카드 본문 | body, 라벨은 label | text-primary | 인라인 편집 필드는 surface-raised fill |
| 재시도 트리거 | 카드 내 버튼 | label | primary | 오류 시만 |
| NER 추출문 | 카드 보조 블록 | caption | text-secondary | 접기 가능 |
| 엔티티 태그 | 카드 칩 행 | label | text-secondary + border | 다중 |
| 항목 처리 상태 | 배지 + 좌측 4px 바 | label | success/warning/error | 상태색은 피드백 전용 |
| 기록 시각 | 카드 상단 | caption | text-secondary | 타임라인 정렬 |
| STT 원문 | 접기/펼치기 | caption | text-secondary | |
| 오류 사유 | 카드 인라인 | body | error | 재시도 인접 |
| 동기화·오프라인 상태 | 배너·헤더 | body / caption | warning·text-primary | |
| 하단 CTA 평가·증상 | 하단 1행 | button | primary fill | → L1 |
| 하단 CTA 병원 추천 | 하단 2행 | button | outline | → L2 |
| 이송 플로팅 요약 | 플로팅 바 | body·caption | text-primary·primary 칩 | 조건부 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 | — | — | — |
| 헤더·하단 바 | white | gray.50 | 충분 | — |
| 일지 카드 | white | gray.50 | 충분 | border로 보강 |
| 입력·소형 필드 | gray.100 | white 카드 내 | 충분 | surface-raised 확정 |
| 배너 | gray.100 | gray.50 / white | 충분 | 하단 border |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 일지 카드 | 카드 | 없음 | 테두리 우선 |
| 이송 플로팅 바 | 플로팅 | shadow-md | 레이어 겹침 |
| 하단 CTA 영역 | 고정 바 | 없음 | 상단 1px border |

### 타이포 위계
| 수준 | 역할 | 스펙 (크기/행간/자간/굵기) | 적용 요소 |
|------|------|-------------------------|----------|
| 1 | heading | 24/32/0 Semibold | 앱 바 제목 |
| 2 | subheading | 18/28/0 Semibold | 빈 상태 제목·카드 섹션 소제목 |
| 3 | body / caption | 16/24/0 Reg · 12/18/0 Reg | 본문·타임스탬프 |

### 강조 검증
- focal point: **최상단 또는 최신 PAT-001 카드** — 좌측 상태 바·제목 행 굵기 — 타임라인 스캔 목적
- primary 사용: **「평가·증상」 CTA 1곳** + (플로팅 칩·섹션 바 등) 소면적 **최대 3곳 이내**
- 상태 표현: 배지 **+ 아이콘 + 문구** 병행

### 밀도 검증
- 터치 가능 요소: 동기화·플로팅·하단 각 CTA·카드 편집 — 높이 **44px 이상** 권장
- 미충족 시: 플로팅·CTA에 세로 패딩 추가

### 시각 밀도 검증
- 스크롤 영역 빈 배경: 항목 다수 시 카드로 채움; **0건 시** 중앙 블록(아이콘+카피+primary 바)으로 50% 미만 유지
- 텍스트 전용 카드: **금지** — 항상 시각·배지·좌측 바·칩·아이콘 중 1개 이상
- 반복 카드 차별화: **좌측 4px 바 색** + 배지 문구 차이
- 섹션 헤더: 타임라인 상단에 선택 시 **좌측 3~4px primary 바** + "오늘" 등 소제목 가능
- 네비 요소: 하단 CTA **버튼 스타일 대비**로 무게감 확보 (1 fill + 1 outline)

### 일관성 체크
- [ ] 모든 색상이 design-system.md 팔레트 키 참조
- [ ] 모든 타이포가 design-system.md 역할 표와 일치
- [ ] 행간·자간이 design-system.md 세밀값 표와 일치 (subheading은 visual-direction 28px 준수)
- [ ] shadow는 이송 플로팅 등 예외에만 사용
- [ ] visual-direction.mdc(테두리 우선·surface-raised·primary 면적 예산)와 충돌 없음
