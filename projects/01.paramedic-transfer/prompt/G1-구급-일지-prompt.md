# 디자인 명세 — G1 구급 일지

## 화면 개요
- **목적**: 현장에서 음성·STT·NER로 쌓인 구급 일지를 시간순으로 스캔·검토·수정하고, 평가(L1) 또는 병원 추천·이송(L2)으로 넘어갈 수 있는 허브 역할을 한다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 앰뷸런스 현장에서 처치·이동 중, 바쁜 멀티태스킹 상태로 짧은 시선으로 타임라인·동기화·이송 맥락을 확인한다.
- **핵심 행동**: 타임라인 항목을 확인·필요 시 편집한 뒤, 하단에서 **「평가·증상」** 또는 **「병원 추천·이송」**으로 다음 단계로 분기한다.

## 시각적 의도

> 이 화면이 완성되었을 때 **어떻게 보이고 느껴져야 하는지** 서술한다. visual-direction.mdc의 비주얼 톤을 이 화면에 구체적으로 적용한 기술.

- **분위기**: 의료 도구로서의 신뢰를 유지하되, 상태 바·배지·아이콘으로 **친근·활동적** 톤을 낸다. 장식용 대색면 없이 **기능 단위 소면적 컬러**로 상태를 드러낸다.
- **시각적 초점 (focal point)**: 스크롤 영역에서 **가장 최근(또는 사용자가 마지막으로 본) 일지 타임라인 카드** — 시각(타임스탬프)·처리 상태·핵심 필드가 한눈에 들어오도록 한다.
- **색상 톤**: 페이지는 **background(gray.50)** 중립, 카드·고정 바는 **surface(white)** + **1px border(border)** 로 구조를 잡고, 상태는 **좌측 4px 바**·칩·아이콘으로만 강조한다. 주요 CTA는 **primary(brand.600)** 를 **「평가·증상」** 에 집중하고, **「병원 추천·이송」** 은 outline으로 면적 예산을 맞춘다.
- **밀도**: **조밀** — `spacing.xl`(16px) 내부 패딩·카드 간 `spacing.3xl`(24px) 섹션 리듬을 유지하되, 한 화면에 정보를 많이 두어 스크롤 부담을 줄인다. 터치 타깃은 **최소 44px** (하단 CTA·플로팅·헤더 액션).
- **디자인 핵심**: **테두리 우선**으로 카드 윤곽이 현장 조명에서도 흐려지지 않게 하고, **surface-raised(gray.100)** 로 카드 안 입력·보조 블록을 한 단계 띄운다. 이송 중일 때만 **플로팅 바 + shadow-md**로 스크롤 콘텐츠와 레이어를 분리한다.
- **화면 고유 디자인**: 공통 패턴은 **앱 바·상태 배너**에만 두고, **일지 타임라인 카드**는 G1 전용 **세로 타임라인 + 좌측 상태 띠 + 인라인 편집·접기 원문** 조합으로 설계한다. L1·L2와 카드 골격을 억지로 통일하지 않으며, **하단 이중 고정 CTA**·**이송 플로팅 → L4** 흐름이 이 화면만의 식별 요소다.

---

## Visual Recipe

- **고유 레이아웃**: 상단은 **크롬(앱 바 + 조건부 배너)** 이고, 그 아래 **이송 플로팅(조건)** → **STT 한 줄** → **세로 타임라인** 순으로 정보가 쌓인다. 하단은 스크롤과 분리된 **세로 2버튼 고정 바**로 마무리되어, 다른 Local 화면의 단일 CTA 바와 구분된다.
- **시선 흐름**: (1) 동기화·오프라인 배너가 있으면 먼저 스캔 → (2) 이송 중이면 플로팅으로 맥락 확인 → (3) STT 상태 한 줄 → (4) 타임라인을 위에서 아래로 훑으며 카드별 상태 바·배지 → (5) 하단에서 다음 행동 선택.
- **디자인 무드**: **바쁜 현장에서도 통제감** — 구조적 테두리·명확한 위계로 “기록이 쌓이고 다음 단계가 보인다”는 안정감을 준다.
- **차별화 포인트**: **시간축 타임라인** + **카드 좌측 4px 상태 띠**로 반복 항목을 빠르게 구분하고, **음성 인식 상태**를 본문과 분리된 얇은 띠로 상시 노출한다.
- **완성도 포인트**: 빈 상태에서도 **아이콘·짧은 카피·primary 앵커 바**로 화면 중단이 텅 비지 않게 하고, 오류·재시도는 **항목 단위**로 카드 안에 가두어 전체 타임라인을 망가뜨리지 않는다.
- **톤 정합**: 친근·활동적 톤은 **accent 링크·마이크 아이콘·상태 칩**의 절제된 사용으로 표현하고, 카드 전체를 상태색으로 칠하지 않는다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 앱 바 | 상단 — 화면 제목「구급 일지」·우측 동기화 등 액션 | 118:4429 |
| PAT-002 | 시스템·동기화 상태 배너 | 앱 바 직하단 — 오프라인·동기화·재시도 한 줄 | 118:4417 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-003 | 하단 요약 액션 바는 **선택 요약 + 단일 CTA** 구조로 L2·L3 전용 — G1은 **이중 고정 CTA** 전용 레이아웃 |

> **일지 타임라인 카드**·**하단 이중 CTA**·**이송 플로팅 바**는 `design-system.md` 공통 패턴 3종에 포함되지 않는 **화면별 콘텐츠/크롬 확장**이다. PAT-001·002의 토큰·간격 규칙을 따르되, 카드 내부 구성은 본 명세와 `G1-구급-일지.md`에 따른다.

---

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 헤더 동기화 | `refreshCw` (icon.baseicon.tokens.refreshCw) | 2:1058 | 24×24 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| STT·인식 소형 행 | `mic` (icon.baseicon.tokens.mic) | 2:938 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)); 처리 중·경고 시 warning / primary 맥락에 맞게 조정 |
| 오프라인·동기 배너 | `wifiOff` (icon.baseicon.tokens.wifiOff) | 2:1280 | 20×20 | warning — warning.600 #DC6803 (rgba(220,104,3,1)) |
| 동기 배너(정보) | `alertCircle` (icon.feedback.tokens.alertCircle) | 2:467 | 20×20 | text-secondary 또는 warning — 맥락에 맞게 선택 |
| 일지 카드 편집 | `edit2` (icon.baseicon.tokens.edit2) | 2:743 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 기록 시각 | `clock` (icon.baseicon.tokens.clock) | 2:629 | 16×16 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 항목 오류 | `alertTriangle` (icon.feedback.tokens.alertTriangle) | 2:472 | 20×20 | error — error.600 #D92D20 (rgba(217,45,32,1)) |
| 완료·정상 | `checkCircle` (icon.feedback.tokens.checkCircle) | 2:588 | 20×20 | success — success.600 #039855 (rgba(3,152,85,1)) |
| STT 원문 펼치기 | `chevronDown` (icon.baseicon.tokens.chevronDown) | 2:596 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |
| 이송 플로팅 진입 | `chevronRight` (icon.baseicon.tokens.chevronRight) | 2:602 | 20×20 | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 플로팅 닫기(선택) | `x` (icon.baseicon.tokens.x) | 2:1298 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 빈 상태 앵커 | `fileText` (icon.baseicon.tokens.fileText) | 2:779 | 48×48 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 초기·갱신 로딩(선택) | `loader` (icon.baseicon.tokens.loader) | 2:896 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #FAFAFA (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ PAT-001 앱 바               │  h: 56px (콘텐츠 기준)
├─────────────────────────────┤
│ PAT-002 상태 배너 (조건)     │  h: auto
├─────────────────────────────┤
│ 이송 중 플로팅 바 (조건)      │  h: 48~52, shadow-md
├─────────────────────────────┤
│ STT·인식 소형 한 줄          │  h: 40~44
├─────────────────────────────┤
│                             │
│  스크롤: 일지 타임라인        │
│  ┌ 일지 카드 ────────────┐  │  surface + border, radius.lg
│  │ ◀4px 상태바          │  │  gap spacing.3xl
│  └───────────────────────┘  │
│  ┌ 일지 카드 ────────────┐  │
│  └───────────────────────┘  │
│  (빈 상태: 안내 블록)        │
│                             │
├─────────────────────────────┤
│ 하단 이중 CTA                │  각 행 min-h 48~52, border 상단
└─────────────────────────────┘
```

### PAT-001 앱 바

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 390 × 56px (안전영역 제외 본문 기준) | 표준 모바일 앱 바 |
| 배경 | surface — white #FFFFFF (rgba(255,255,255,1)) | 본문과 구분 |
| 배치 | 수평 스택 — 좌: 타이틀, 우: 동기화 아이콘 버튼 | 한 손 엄지 도달·스캔 용이 |
| 주축 정렬 | 양끝 | 제목 고정, 액션 분리 |
| 교차축 정렬 | 중앙 | 수직 정렬 안정 |
| 내부 여백 | 좌16 우16 상12 하12 — spacing.xl | visual-direction 기본 패딩 |
| 요소 간격 | 12px | 타이틀과 액션 분리 |
| 모서리 | 없음 | 전체 너비 붙임 |
| 깊이 | 없음 | 테두리로 경계 |
| 테두리 | 하단 1px — border gray.300 #D5D7DA (rgba(213,215,218,1)) | 헤더·콘텐츠 분리 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 화면 제목 | 텍스트 | "구급 일지" | heading — 24px/32px/0 Semibold | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 동기화 | 아이콘 버튼 | refreshCw (2:1058) 24×24 | — | text-secondary — gray.600 #535862 |

### PAT-002 시스템·동기화 상태 배너 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 전폭, 높이 auto | 한 줄~두 줄 메시지 |
| 배경 | surface-raised — gray.100 #F5F5F5 (rgba(245,245,245,1)) | 본문과 톤 구분, 과한 경고색 면적 방지 |
| 배치 | 수평 스택 — 아이콘 + 문구 + (재시도 텍스트 링크) | 스캔 가능한 한 줄 |
| 내부 여백 | 좌16 우16 상12 하12 — spacing.xl | |
| 테두리 | 하단 1px — border gray.300 | 섹션 분리 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 아이콘 | 아이콘 | wifiOff (2:1280) 또는 alertCircle (2:467) 20×20 | — | warning 또는 text-secondary |
| 메시지 | 텍스트 | "오프라인입니다. 연결 후 동기화됩니다." 등 | body — 16px/24px/0 Regular | text-primary — gray.900 #181D27 |
| 재시도 링크 | 텍스트 버튼 | "다시 시도" | label — 14px Medium, line-height foundation `text sm` 기준 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |

### 이송 중 플로팅 바 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 좌우 margin 12~16, 높이 48~52px | 터치 타깃, 스크롤과 겹치지 않게 떠 있음 |
| 배경 | surface — white #FFFFFF (rgba(255,255,255,1)) | 카드형 플로팅 |
| 깊이 | shadow-md — design-system 이펙트 표 (y:4, blur 8, alpha ≈0.10) | visual-direction: 플로팅·시트류만 그림자 |
| 모서리 | radius.lg — 10px | 카드와 동일 리듬 |
| 테두리 | 없음 (그림자 단독) | shadow와 stroke 동시 사용 금지 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 칩 | 칩 | "이송 진행 중" | label — 14px Medium | 배경은 **subtle**(예: surface-raised 또는 연한 primary 톤의 소면적); 문구·아이콘은 primary — brand.600 #7F56D9 |
| 병원 요약 | 텍스트 | "○○병원" (길면 말줄임) | body — 16px/24px/0 Medium | text-primary — gray.900 #181D27 |
| 보조 시각 | 텍스트 | 확정 시각 등 | caption — 12px/18px/0 Regular | text-secondary — gray.600 #535862 |
| 진입 화살표 | 아이콘 | chevronRight (2:602) 20×20 | — | text-primary — gray.900 #181D27 |
| 닫기(선택) | 아이콘 | x (2:1298) 20×20 | — | text-secondary — gray.600 #535862 |

### STT·인식 소형 영역

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white #FFFFFF | 플로팅이 있으면 **그 아래**로 밀림 |
| 테두리 | 1px — border gray.300, radius.md — 8px | 얇은 상태 띠 |
| 내부 여백 | 좌12 우12 상10 하10 | 조밀 한 줄 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 마이크 | 아이콘 | mic (2:938) 20×20 | — | accent — blue.600 #1570EF |
| 상태 문구 | 텍스트 | "듣는 중…" / "처리 중" 등 | caption — 12px/18px/0 또는 body — 16px/24px/0 | text-secondary 또는 text-primary |

### 스크롤 — 일지 타임라인 카드 (G1 콘텐츠 전용)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 영역 패딩 | 좌16 우16 상0 하 spacing.3xl (24px) | 헤더·플로팅과 리듬 정합 |
| 카드 간격 | spacing.3xl — 24px | 섹션형 리듬 |
| 카드 배경 | surface — white #FFFFFF | background 대비 |
| 카드 테두리 | 1px — border gray.300 | **그림자 없음** (테두리 우선) |
| radius | radius.lg — 10px | design-system |
| 좌측 상태 바 | 너비 4px, 카드 전고 — success / warning / error / primary | visual-direction 허용 위치; 반복 카드 차별화 |

#### 카드 내부 (예시 구조)

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 시각 | 텍스트 | "14:32" | caption — 12px/18px/0 Regular | text-secondary — gray.600 #535862 |
| 처리 상태 | 배지 + 아이콘 | "완료" + checkCircle / "오류" + alertTriangle | label — 14px Medium | success / error 토큰 + **문구 병행** |
| 필드 라벨·값 | 텍스트·필드 | key→value (일지 항목) | 라벨: label 14px Medium; 값: body 16px/24px/0 Regular; 그룹 제목이 필요하면 subheading 18px/28px/0 Semibold | text-primary / text-secondary; 입력면 fill **surface-raised** — gray.100 #F5F5F5 |
| NER 칩 | 칩 | 엔티티 태그 다수 | label — 14px Medium | 테두리 border gray.300, 배경 surface-raised, 텍스트 text-secondary |
| 원문 토글 | 텍스트 + 아이콘 | "STT 원문 보기" + chevronDown | label — 14px Medium | accent — blue.600 #1570EF |
| 오류 메시지 | 텍스트 | 오류 사유 | body — 16px/24px/0 Regular | error — error.600 #D92D20 |
| 재시도 | 텍스트 버튼 | "다시 분석" | label — 14px Medium | primary — brand.600 #7F56D9 |
| 편집 | 아이콘 버튼 | edit2 (2:743) 20×20 | — | text-secondary — gray.600 #535862 |

### 빈 상태 (일지 0건)

| 요소 | 설계 의도 |
|------|----------|
| 중앙 블록 | fileText (2:779) 48×48 + subheading + body — **스크롤 영역 빈 배경 50% 초과 방지** |
| 제목 | subheading — "아직 일지 항목이 없습니다" — 18px/28px/0 Semibold |
| 본문 | body — "마이크로 말하면 기록이 쌓입니다. 평가·증상은 언제든 진행할 수 있어요." — 16px/24px/0 Regular |
| 시각 앵커 | 섹션 느낌을 위해 **좌측 3~4px 바 primary** (visual-direction 허용) |

### 하단 고정 이중 CTA

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white #FFFFFF | 스크롤과 분리 |
| 상단 구분 | 1px — border gray.300 | elevation 대신 테두리 |
| 패딩 | spacing.xl — 16px + safe-area | 터치·엄지 영역 |
| 버튼 간격 | 12px | 세로 스택, 각 버튼 min-height **48~52px** (44px 이상 충족) |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 1차 CTA | 버튼 | "평가·증상" | button — 16px/24px/0 Semibold | fill **primary** — brand.600 #7F56D9, 텍스트 white #FFFFFF |
| 2차 CTA | 버튼 | "병원 추천·이송" | button — 16px/24px/0 Semibold | **outline** — stroke border gray.300 1px, 텍스트 text-primary — gray.900 #181D27 |

> 일지 0건이어도 **두 버튼 모두 비활성화하지 않음** — 시각적 가시성·터치 가능 상태 유지 (screen-spec).

### 적합 요약 배너 (선택, screen-spec)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 위치 | PAT-002 아래 또는 타임라인 상단 1줄 | L2 진입 전 맥락 힌트 |
| 스타일 | body 16px/24px/0 + 선택 시 info 아이콘 | accent 링크·보조 문구 수준 면적 |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|-------------|----------|------|
| STT·인식 진행 상태 | STT 소형 행 | caption / body | accent·text-secondary | 짧은 한 줄 |
| 일지 항목 확정값 | 타임라인 카드 본문 | label + body | text-primary; 입력면 surface-raised | 인라인 편집 |
| 재시도 트리거 | 카드 내 버튼 | label | primary | 오류 시만 |
| NER 추출문 | 카드 보조 블록 | caption | text-secondary | 접기 가능 |
| 엔티티 태그 | 카드 칩 행 | label | text-secondary + border | 다중 |
| 항목 처리 상태 | 배지 + 좌측 4px 바 | label | success/warning/error/primary | 아이콘+문구 병행 |
| 적합 요약(동일 세션) | 선택 배너 1줄 | body | text-primary / accent 링크 | 필드 없으면 생략 |
| 기록 시각 | 카드 상단 | caption | text-secondary | 타임라인 정렬 |
| STT 원문 | 접기/펼치기 | caption | text-secondary | |
| 오류 사유 | 카드 인라인 | body | error | 재시도 인접 |
| 동기화·오프라인 상태 | PAT-002·헤더 맥락 | body / caption | warning·text-primary | |
| 하단 CTA — 평가·증상 | 하단 1행 | button | primary fill | → L1 |
| 하단 CTA — 병원 추천·이송 | 하단 2행 | button | outline | → L2 |
| 이송 플로팅 바(요약) | 플로팅 바 | body·caption·칩 | text-primary·primary | L4 복귀 시 |
| 이송 확정 시각 | 플로팅 보조 | caption | text-secondary | L4와 동일 소스 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 #FAFAFA | — | — | — |
| 앱 바·하단 CTA 바 | white #FFFFFF | gray.50 | 충분 (visual-direction ΔL) | 하단 border로 분리 |
| 일지 카드 | white #FFFFFF | gray.50 | 충분 | border로 보강 |
| 입력·소형 필드·칩 배경 | gray.100 #F5F5F5 | white 카드 내 | 충분 | surface-raised |
| PAT-002 배너 | gray.100 #F5F5F5 | gray.50 / white | 충분 | 하단 border |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 일지 타임라인 카드 | 카드 | 없음 | 테두리 우선 |
| 이송 플로팅 바 | 플로팅 | shadow-md | 플로팅·레이어 분리 |
| 하단 이중 CTA | 고정 바 | 없음 | 상단 1px border |

### 타이포 위계
| 수준 | 역할 | 스펙 (크기/행간/자간/굵기) | 적용 요소 |
|------|------|-------------------------|----------|
| 1 | heading | 24px/32px/0 Semibold | 앱 바 제목 |
| 2 | subheading | 18px/28px/0 Semibold | 빈 상태 제목·카드 그룹 소제목(필요 시) |
| 3 | body / label / caption / button | body 16px/24px/0 Reg; label 14px Medium (foundation `text sm` lh); caption 12px/18px/0 Reg; button 16px/24px/0 Semibold | 본문·폼·타임스탬프·CTA |

### 강조 검증
- focal point: **최신·핵심 일지 카드** — 좌측 상태 바 + 제목/값 행 굵기·크기 — 타임라인 스캔 목적
- primary 사용: **「평가·증상」 CTA fill 1곳** + 플로팅 칩·섹션 좌측 바 등 소면적 **합산 3곳 이내** (visual-direction 면적 예산)
- 상태 표현: 배지 **+ 아이콘 + 문구** 병행

### 밀도 검증
- 터치 가능 요소: 동기화·플로팅 전체·하단 각 CTA·카드 편집 — 높이 **44px 이상**
- 미충족 시: 플로팅·CTA에 세로 패딩 추가

### 시각 밀도 검증
- 스크롤 영역 빈 배경: 항목 다수 시 카드로 채움; **0건 시** 중앙 블록으로 **50% 미만** 유지
- 텍스트 전용 카드: **금지** — 시각(캡션)·배지·좌측 바·칩·아이콘 중 1개 이상 병행
- 반복 카드 차별화: **좌측 4px 바 색** + 처리 상태 배지 차이
- 섹션 헤더: 필요 시 **좌측 3~4px primary 바** + 짧은 소제목 (subheading)
- 네비 무게감: 하단 **fill vs outline** 대비로 이중 CTA의 위계 명확화

### 일관성 체크
- [ ] 모든 색상이 design-system.md 팔레트 키 참조
- [ ] 모든 타이포가 design-system.md 역할 표와 일치
- [ ] heading·body·caption·subheading·button의 행간·자간이 design-system.md 세밀값 표와 일치 (label은 foundation `text sm` 스케일 준수)
- [ ] shadow는 이송 플로팅 등 예외에만 사용
- [ ] visual-direction.mdc(테두리 우선·surface-raised·primary 면적·기능적 색 위치)와 충돌 없음
