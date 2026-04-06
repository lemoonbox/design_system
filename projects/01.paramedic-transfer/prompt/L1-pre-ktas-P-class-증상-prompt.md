# 디자인 명세 — L1 pre-KTAS / P-class·증상

## 화면 개요
- **목적**: 주·부증상과 증상 요약을 다루고, **pre-KTAS**와 **P-class**를 **서로 독립된 비동기 흐름**으로 입력·확인하며, 필요 시 병원 단계(L2)로 넘어간다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: G1에서 **「평가·증상」**으로 진입한 직후 또는 이송 준비 중 잠시 멈춰 평가를 마무리·보완하는 순간. **일지 0건**이어도 진입 가능 — 상단에서만 맥락을 안내한다.
- **핵심 행동**: 주증상을 확정하고(필수), pre-KTAS·P-class 블록의 상태를 확인한 뒤 **「병원 추천·이송」**으로 다음 단계로 이동한다(pre-KTAS 미확정도 허용).

## 시각적 의도

> G1의 **타임라인·일지 허브**와 달리, L1은 **평가 워크시트 + 이중 비동기 트랙**이 주인공이다. 공통 크롬은 `design-system.md`의 PAT-001·002에 맞추고, pre-KTAS / P-class / Class 아코디언은 **화면별 창작 콘텐츠**로 설계한다.

- **분위기**: 친근·활동적 톤을 유지하되, **두 엔진이 동시에 도는** 느낌을 **대등한 두 개의 테두리 카드**·**독립 단계 배지**·**서로 다른 좌측 상태 바 색( primary 트랙 vs accent 트랙 )**으로 한눈에 읽히게 한다.
- **시각적 초점 (focal point)**: 스크롤 상단 **주증상 선택 행 전체**(필수 입력면 + 검색 아이콘). 처리 중에는 같은 화면 안에서 **해당 블록의 스텝퍼/배지 행**이 보조 초점이 된다.
- **색상 톤**: 페이지 **background — gray.50 #FAFAFA**, 카드 **surface — white #FFFFFF** + **border — gray.300 #D5D7DA 1px**(그림자 없음). 섹션 앵커는 **좌측 3~4px 바**(증상 묶음·pre-KTAS는 **primary**, P-class는 **accent**로 트랙 구분). 상태는 **success / warning / error**를 **아이콘+짧은 문구+칩**으로만.
- **밀도**: **조밀**(`visual-direction.mdc`) — 내부 패딩 **spacing.xl 16px**, 블록 간 **spacing.3xl 24px** 리듬을 지키되 필드·스텝 행을 **한 화면에 최대한 모아** 스크롤·전환 비용을 줄인다. 터치 타깃 **최소 44px**는 깨지 않게 한다.
- **디자인 핵심**: **pre-KTAS**와 **P-class**가 **세로로 풀폭 스택**되어 타임라인(G1)과 혼동되지 않고, 각 카드 상단 **동일 높이의 진행 행**으로 **병렬·대등**함을 표현한다. Class III 안내는 **짧은 인포 배너**로 한 번만 스캔되게 한다.
- **화면 고유 디자인**: **증상 입력 덩어리(주·부·요약)** + **독립 이중 비동기 카드** + **Class I~V 아코디언 멀티 체크**(delivery 기본 제안 ON) + **하단 단일 primary 이송 CTA** — G1 타임라인·L2 병원 리스트와 레이아웃 언어가 명확히 다르다.

---

## Visual Recipe

**배경 gray.50** 위에 **흰색 테두리 카드**가 위에서 아래로 **증상 → pre-KTAS → P-class** 순으로 쌓이며, 각 블록은 **좌측 얇은 컬러 바**로 “어떤 일의 흐름인지”가 먼저 구분된다. 시선은 **주증상 필드**에 고정된 뒤, 스크롤로 내려가며 **두 트랙의 단계 배지**를 **나란히 같은 무게**로 비교한다. **스텝퍼·로더·체크·경고** 아이콘이 텍스트만인 구역 없이 상태를 대신 말하고, 하단은 **보라 primary 한 줄**로 **「병원 추천·이송」**만이 다음 행동을 제시한다. **일지 미연계**일 때는 카드 위에 **얇은 accent 바 배너**가 한 번 끊어 준다. 전체 무드는 **바쁜 현장 도구**처럼 정보 밀도는 높지만 **테두리 구조**로 숨 쉴 틈이 있다. **차별화 포인트**는 “한 화면에 **두 개의 비동기 진행률**이 **동등한 카드 두 장**으로 공존한다”는 점이다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-001 | 앱 바 | 상단 — 뒤로·화면 타이틀「평가·증상」(우측 보조 액션 없음 가정) | 118:4429 |
| PAT-002 | 시스템·동기화 상태 배너 | PAT-001 바로 아래 — **오프라인·동기화 대기·재시도** 등이 있을 때만 노출 | 118:4417 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-003 | **선택 수·한 줄 요약 + 주 CTA** 구조는 L2·L3 전용(`design-system.md`). L1 하단은 **단일 주 CTA**(병원 추천·이송)만 고정하며, 블록 내 보조 **저장·확정**은 콘텐츠 영역 버튼으로 처리한다. |

> **콘텐츠 영역(패턴 ID 없음)**: **증상 입력 카드**, **pre-KTAS 비동기 카드**, **P-class 비동기+아코디언 카드**, **일지 미연계 안내**, **Class III 인포**는 본 화면 스펙에 따른 **창작 레이아웃**이다(`design-system.md` 공통 패턴 3종의 크롬 밖).

---

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 뒤로가기(앱 바) | chevronLeft (`icon.baseicon.tokens.chevronLeft`) | 2:599 | 24×24 | text-primary — gray.900 #181D27 (rgba(24,29,39,1)) |
| 주증상 필드(검색·피커) | search (`icon.baseicon.tokens.search`) | 2:1082 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| PAT-002(오프라인·동기) | wifiOff (`icon.baseicon.tokens.wifiOff`) | 2:1280 | 20×20 | warning — warning.600 #DC6803 (rgba(220,104,3,1)) |
| PAT-002 재시도 | refreshCw (`icon.baseicon.tokens.refreshCw`) | 2:1058 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |
| 일지 미연계 배너 | info (`icon.baseicon.tokens.info`) | 2:863 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |
| 일지 연계 한 줄(선택) | fileText (`icon.baseicon.tokens.fileText`) | 2:779 | 20×20 | accent — blue.600 #1570EF (rgba(21,112,239,1)) |
| 비동기 처리 중 | loader (`icon.baseicon.tokens.loader`) | 2:896 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| 완료 | checkCircle (`icon.feedback.tokens.checkCircle`) | 2:588 | 20×20 | success — success.600 #039855 (rgba(3,152,85,1)) |
| 오류·주의 | alertTriangle (`icon.feedback.tokens.alertTriangle`) | 2:472 | 20×20 | error — error.600 #D92D20 (rgba(217,45,32,1)) 또는 warning — warning.600 #DC6803 (rgba(220,104,3,1)) |
| 재시도·재분석(블록 내) | refreshCw (`icon.baseicon.tokens.refreshCw`) | 2:1058 | 20×20 | primary — brand.600 #7F56D9 (rgba(127,86,217,1)) |
| P-class 아코디언 | chevronDown (`icon.baseicon.tokens.chevronDown`) | 2:596 | 20×20 | text-secondary — gray.600 #535862 (rgba(83,88,98,1)) |
| Class 체크 | check (`icon.baseicon.tokens.check`) | 2:593 | 20×20 | primary — brand.600(선택) / text-disabled — gray.400 #A4A7AE (rgba(164,167,174,1))(미선택) |
| 저장·확정(블록 내 보조) | save (`icon.baseicon.tokens.save`) | 2:1076 | 20×20 | text-secondary — gray.600 또는 primary — brand.600 |
| 하단 CTA 시각 앵커(선택) | truck (`icon.baseicon.tokens.truck`) | 2:1208 | 20×20 | surface 상에서 **버튼 내부**만 — 흰색 또는 primary 대비에 맞는 단색(아이콘 면적만) |

---

## 레이아웃 구조

### 전체 구조

화면 배경: background — gray.50 #FAFAFA (rgba(250,250,250,1))

```
┌─────────────────────────────┐  390 × 844
│ PAT-001 앱 바                │  h: 56px
├─────────────────────────────┤
│ PAT-002 (조건: 동기·오프라인) │
├─────────────────────────────┤
│ 일지 미연계 배너 (조건)       │
├─────────────────────────────┤
│ ┌ 증상 입력 카드 ─────────┐  │  surface, border, radius.lg
│ │ 주증상·부증상·요약        │  │
│ └─────────────────────────┘  │
│        gap 24 — spacing.3xl  │
│ ┌ pre-KTAS 카드 ──────────┐  │  좌측 바 primary 4px
│ │ 스텝·등급·근거·오류·재시도 │  │
│ └─────────────────────────┘  │
│        gap 24                │
│ ┌ P-class 카드 ───────────┐  │  좌측 바 accent 4px
│ │ 스텝·Class I~V 아코디언   │  │
│ └─────────────────────────┘  │
│ ┌ Class III 인포 (조건)    ┐  │
│ └─────────────────────────┘  │
│         (스크롤)             │
├─────────────────────────────┤
│ 고정: 병원 추천·이송 CTA      │  primary fill, min-h 48, border-top 1px
└─────────────────────────────┘
```

### PAT-001 앱 바

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 390 × 56px | 표준 앱 바 |
| 배경 | surface — white #FFFFFF (rgba(255,255,255,1)) | 콘텐츠와 동일 계열 |
| 하단 구분 | 1px border — gray.300 #D5D7DA | 테두리 우선, shadow 없음 |
| 배치 | 수평 스택 — 뒤로 \| 제목 중앙 또는 좌측 정렬(제품 정책에 맞춤) | 한 손 엄지 도달 |
| 내부 여백 | 좌우 16px — spacing.xl | |
| 교차축 정렬 | 중앙 | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 뒤로 | 아이콘 버튼 | chevronLeft (2:599) 24×24, 히트 영역 ≥44×44 | — | text-primary — gray.900 #181D27 |
| 제목 | 텍스트 | "평가·증상" | heading — 24px / line-height 32px / letter-spacing 0 / Semibold | text-primary — gray.900 #181D27 |

### PAT-002 시스템·동기화 배너 (조건부)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface-raised — gray.100 #F5F5F5 (rgba(245,245,245,1)) | 한 줄 시스템 피드백 |
| 패딩 | 세로 12px, 좌우 16px — spacing.xl | |
| 테두리 | 하단 1px border — gray.300 | PAT-001과 스크롤 콘텐츠 사이 리듬 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 상태 아이콘 | 아이콘 | wifiOff (2:1280) 20×20 | — | warning — warning.600 #DC6803 |
| 메시지 | 텍스트 | "오프라인입니다" 등 | body — 16px / 24px / 0 / Regular | text-primary — gray.900 #181D27 |
| 재시도 | 텍스트 버튼 | "다시 시도" + refreshCw (2:1058) | label — 14px / 20px / 0 / Medium | accent — blue.600 #1570EF |

### 일지 미연계 배너 (조건부 · PAT-002와 별도)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface-raised — gray.100 #F5F5F5 (rgba(245,245,245,1)) | 기능적 안내, 장식 색면 금지 |
| 좌측 앵커 | 3px 세로 바 — accent blue.600 #1570EF | 정보성 링크·안내에 accent 허용(`visual-direction.mdc`) |
| 하단 | 1px border — gray.300 | |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 아이콘 | 아이콘 | info (2:863) 20×20 | — | accent — blue.600 #1570EF |
| 문구 | 텍스트 | "일지가 없습니다. 음성 기록을 권장하지만, 평가는 계속할 수 있어요." | body — 16px / 24px / 0 / Regular | text-primary — gray.900 #181D27 |

### 증상 입력 카드 (주·부·요약)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white #FFFFFF | |
| 테두리 | 1px border — gray.300 #D5D7DA | shadow 없음 |
| radius | radius.lg — 10px | |
| 내부 패딩 | spacing.xl — 16px | |
| 좌측 바 | 4px — primary brand.600 #7F56D9 | 증상 묶음 앵커 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 섹션 타이틀 | 텍스트 | "주증상" / "부증상" / "증상 요약" | subheading — 18px / 28px / 0 / Semibold | text-primary — gray.900 #181D27 |
| 주증상 필드 | 입력/피커 | placeholder "주증상 선택" | body — 16px / 24px / 0 / Regular | 본문 text-primary; placeholder — text-disabled gray.400 #A4A7AE |
| 필드 배경 | 표면 | surface-raised gray.100 #F5F5F5 | — | 카드 white와 계층 분리 |
| 필드 테두리 | 1px border — gray.300 | radius.md — 8px | |
| 검색 아이콘 | 아이콘 | search (2:1082) 20×20 | — | text-secondary — gray.600 #535862 |
| 부증상 칩 | 칩 + 입력 | 다중 태그 | label — 14px / 20px / 0 / Medium | 테두리 border gray.300, fill white 또는 background gray.50 |
| 증상 요약 | 멀티라인 | 비동기 생성 + 수동 편집 | body — 16px / 24px / 0 / Regular | text-primary — gray.900 #181D27 |
| 일지 연계 한 줄 | 텍스트(선택) | "일지에서 반영된 항목이 있어요" + fileText (2:779) | caption — 12px / 18px / 0 / Regular | accent — blue.600 #1570EF |

### pre-KTAS 블록 (창작 카드)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경·테두리·radius | surface white + 1px border gray.300 + radius.lg 10px | 프로젝트 구조적 서피스 |
| 좌측 바 | 4px — primary brand.600 #7F56D9 | pre-KTAS 트랙 식별 |
| 상단 진행 행 | **최소 높이 44px** | 스텝퍼·배지 **네비 무게감**(`visual-direction.mdc`) |
| 스텝 노드 | 지름 28px 권장 | 현재: **primary** fill + 흰 아이콘/숫자, 완료: **success**, 미완: **gray.100** 배경 + **text-secondary** 문구(caption) |

#### 스텝퍼·상태 (예시)

| 단계 | 표시 | 색상 |
|------|------|------|
| 대기 | 원 + 숫자 | gray.100 배경, text-secondary |
| 처리 중 | 원 + loader (2:896) | primary brand.600 |
| 완료 | checkCircle (2:588) | success.600 |
| 오류 | alertTriangle (2:472) + 재시도 | error.600 + primary 텍스트 버튼 |

#### 본문 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|-------|------|
| 등급 표시 | 텍스트/세그먼트 | 미확정 시 "등급 분석 중…" 등 | body — 16px / 24px / 0 / Regular | text-secondary — gray.600 #535862 |
| 근거 요약 | 텍스트 | 접기/펼치기 | caption — 12px / 18px / 0 / Regular 본문 | text-secondary / text-primary |
| 재시도 | 텍스트 버튼 | "다시 분석" + refreshCw (2:1058) | label — 14px / 20px / 0 / Medium | primary — brand.600 #7F56D9 |
| 확정·저장 | 보조 버튼 | outline 또는 secondary | button — 16px / 24px / 0 / Semibold | 테두리 border, 텍스트 primary 또는 text-primary |
| 필수 보완 필드 | 인라인 입력 | 플로우 3 | label + body | 오류 시 error + 인접 메시지 |

### P-class 블록 (창작 카드 + 아코디언)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 좌측 바 | 4px — accent blue.600 #1570EF | P-class 트랙 = 정보·보조 강조 색으로 pre-KTAS와 분리 |
| 상단 진행 행 | pre-KTAS와 **동일 최소 높이 44px** | 병렬 비동기 **대등** |
| 본문 | Class I~V **아코디언** — 헤더 행 min-height 48px | chevronDown (2:596) |
| Class II delivery | 기본 제안 ON | check (2:593) + label "분만(제안)" |

#### 아코디언 헤더

| 요소 | 타이포 | 색상 |
|------|--------|------|
| Class 명 | subheading — 18px / 28px / 0 / Semibold | text-primary — gray.900 #181D27 |
| 선택 개수 | caption — 12px / 18px / 0 / Regular | text-secondary — gray.600 #535862 |
| chevronDown | 20×20 | text-secondary — gray.600 #535862 |

#### 체크 행

| 요소 | 설명 |
|------|------|
| 터치 행 | min-height 44px, 좌측 체크 히트 영역 확보 |
| 라벨 | body — 16px / 24px / 0 / Regular, text-primary — gray.900 #181D27 |

### Class III 인포 배너 (조건부)

| 속성 | 값 |
|------|-----|
| 배경 | surface-raised gray.100 #F5F5F5 |
| 좌측 바 | 3px — warning.600 #DC6803 |
| 아이콘 | info (2:863) 20×20 — accent 또는 text-secondary(맥락에 맞게 단일 규칙 유지) |
| 본문 | body 16px / 24px — "ICU·NICU·IR 병원 추천에 반영됩니다" 류 |

### 하단 고정 CTA (창작 · PAT-003 아님)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white #FFFFFF | |
| 상단 | 1px border — gray.300 #D5D7DA | shadow 없음(테두리 우선) |
| 안전 영역 | 하단 inset 대응 | 시스템 홈 인디케이터 |
| 버튼 | 전폭, min-height **48px**, radius.md — 8px | 터치 44px 이상 확보 |
| 문구 | "병원 추천·이송" | button — 16px / 24px / 0 / Semibold |
| fill | primary — brand.600 #7F56D9 | 화면 **유일한 대면적 primary 면** |
| 선행 아이콘(선택) | truck (2:1208) 20×20 | 텍스트 왼쪽, 아이콘만 흰색 처리 |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|-------------|----------|------|
| 주증상 선택 | 증상 카드 필드 | body / label | text-primary | 필수 |
| 부증상 | 칩·입력 | label / body | text-primary | |
| P-class 서브클래스 | 아코디언 내 체크 | body | text-primary | delivery 기본 ON, 해제 가능 |
| pre-KTAS 등급 확정/수정 | pre-KTAS 카드 | body / button | text-primary | 세그먼트·리스트 |
| L1 필수 보완 필드(동적) | pre-KTAS 또는 증상 영역 인라인 | label + body | error 인접 | 플로우 3 |
| pre-KTAS 비동기 단계 | pre-KTAS 스텝 행·배지 | caption / label | primary · success · text-secondary | |
| P-class 비동기 단계 | P-class 스텝 행·배지 | caption / label | 독립 표시 | pre-KTAS와 타임라인 혼동 금지 |
| 증상 요약 | 증상 카드 | body | text-primary | |
| pre-KTAS 근거 요약 | pre-KTAS 카드 접이식 | caption | text-secondary | |
| Class III 안내 | 인포 배너 | body | text-primary | 조건부 |
| 일지 연계 링크/요약 | 증상 카드 한 줄 | caption | accent | 선택 |
| pre-KTAS 등급(표시값) | pre-KTAS 본문 | body | text-secondary | 처리 중 placeholder |
| 엔진 오류 메시지 | 해당 블록 | body | error | 재시도 인접 |
| 병원 추천·이송 CTA | 하단 고정 | button | primary fill | → L2, 미확정 허용 |

---

## 시각 품질 검증

### Surface Depth

| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|--------------|------|------|
| 화면 배경 | gray.50 #FAFAFA | — | — | — |
| 증상·비동기 카드 | white #FFFFFF | gray.50 | 충분(ΔL·border) | shadow 불필요 |
| 입력·요약 필드 | gray.100 #F5F5F5 | white 카드 | 충분 | surface-raised |
| PAT-002·안내 배너 | gray.100 #F5F5F5 | white/gray.50 | 충분 | 인접 카드와 동일 시 1px border로 분리 |

### Elevation

| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 카드·고정 CTA 바 | 본 화면 | 없음 | **테두리 우선** — shadow와 border 동시 사용 금지 |
| (향후 바텀시트·드롭다운) | 오버레이 | shadow-md / shadow-lg | `design-system.md` 이펙트 토큰 |

### 타이포 위계

| 수준 | 역할 | 스펙 (크기/행간/자간/굵기) | 적용 요소 |
|------|------|-------------------------|----------|
| 1 (최강) | heading | 24px / 32px / 0 / Semibold | 앱 바 제목 |
| 2 (중간) | subheading | 18px / 28px / 0 / Semibold | 섹션·아코디언 Class 헤더 |
| 3 (본문·보조) | body / caption / label / button | 16px / 24px / 0; 12px / 18px / 0; 14px / 20px / Medium; 16px / 24px / Semibold | 본문·메타·칩·주 CTA |

### 강조 검증

- focal point: **주증상 필드** — 넓은 터치 영역·surface-raised·search 아이콘
- primary 사용: **하단 「병원 추천·이송」** 1곳(대면적) + **스텝퍼 현재 노드** + **좌측 4px primary 바(pre-KTAS·증상)** + 블록 내 **재시도** 등 소면적 — `visual-direction.mdc` **소면적 강조 최대 3곳**을 넘지 않도록 텍스트 버튼은 accent로 돌리는 변형 허용
- 상태 표현: loader / checkCircle / alertTriangle + 짧은 문구 + 칩 병행

### 밀도 검증

- 스텝퍼 행·아코디언 헤더·하단 CTA·뒤로: **min-height 44px 이상** 권장(CTA 48px)

### 시각 밀도 검증

- 스크롤 영역: 증상 카드 + 이중 비동기 카드 + 조건부 배너로 **빈 배경 50% 미만** 유지
- 텍스트 전용 블록 지양 — 각 비동기 카드에 스텝·아이콘·배지 중 1개 이상
- pre-KTAS vs P-class: **동일 카드 폭·동일 상단 행 높이** + **좌측 바 색(primary vs accent)** 으로 트랙 구분
- 섹션 헤더: 증상·pre-KTAS에 **좌측 컬러 바** 적용
- 네비 무게감: 스텝퍼 행 **≥44px**

### 일관성 체크

- [ ] 모든 색상이 `design-system.md` 팔레트 키 참조
- [ ] 모든 타이포가 `design-system.md` 역할 표와 일치
- [ ] 행간·자간이 `design-system.md` 세밀값 표와 일치
- [ ] shadow는 본 화면 카드/CTA에 사용하지 않음(예외 시 토큰명 명시)
- [ ] `visual-direction.mdc` 확정 디자인 결정과 충돌 없음
