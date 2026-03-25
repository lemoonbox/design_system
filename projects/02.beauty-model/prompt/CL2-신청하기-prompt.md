# 디자인 명세 — CL2 신청하기

## 화면 개요
- **목적**: 고객이 희망 일정·사진·동의를 완료하고 시술 신청을 제출한다.
- **디바이스**: 390 × 844 모바일
- **사용자 맥락**: 상품 상세(CL1)에서 ‘신청하기’로 진입한 직후, 예약을 확정하기 전 단계에서 집중 입력한다.
- **핵심 행동**: 필수 항목을 채우고 하단 ‘신청하기’로 제출한다.

## 시각적 의도

- **분위기**: 플랫하고 조밀한 폼 화면. 요약 카드로 맥락(시술·디자이너·가격)을 고정하고, 아래는 단계별로 스캔하기 쉬운 블록으로 나뉜다.
- **시각적 초점 (focal point)**: **희망 일정 슬롯 선택 영역** — 섹션 앵커(브랜드 바·아이콘)와 슬롯 행/칩이 시선을 먼저 받는다.
- **색상 톤**: 페이지는 중립 배경(gray.50), 카드·필드는 흰 surface + border(gray.300). CTA·현재 단계만 brand.600. 경고·제한은 상태 tint + 텍스트색 병행.
- **밀도**: visual-direction 조밀 기준 — 리스트형 슬롯, 구분선(border-subtle) 위주, 터치 타깃 최소 44px.
- **디자인 핵심**: 상단 요약 카드와 본문 폼의 fill 대비, 섹션 좌측 4px 앵커 바로 리듬을 잡고, 사진 영역은 PAT-007 그리드로 빈 면을 피한다.

---

## Visual Recipe

배경은 **background — gray.50 #fafafa (rgba(250,250,250,1))** 로 깔고, 그 위에 **헤더 바 + 시술 요약 카드(surface + border 1px)** 가 스크롤 상단에 붙는 구조다. 스크롤 본문은 **일정 → 사진 → 동의 → (선택) 참고사항** 순 수직 스택이며, 각 섹션 제목 행에는 **좌측 4px 세로 바(primary)** 와 **20px 아이콘(text-secondary)** 을 붙여 시각 앵커를 만든다. 사진 구역은 **3열 썸네일 + 빈 슬롯(점선 테두리)** 으로 채워 스크롤 영역의 단색 빈 면을 줄인다. 하단은 **고정 CTA 바(surface + 상단 1px border-subtle)** 에 pill 형 primary 버튼을 두어 제출 행동을 명확히 한다.

---

## 사용 패턴

| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-007 | 사진 썸네일 그리드 | ‘신청용 사진’ 섹션 — 업로드/썸네일 표시 | 77:4475 |

## 미사용 패턴 및 사유

| PAT ID | 사유 |
|--------|------|
| PAT-001 | 예약 카드가 아닌 ‘신청 폼’ 화면이라 예약 상태 카드 패턴 불필요 |
| PAT-002 | 상품 카드 목록이 아님 |
| PAT-003 | 신청자 행은 디자이너 관점(DG2/DL3) 전용 |
| PAT-004 | 상태 배지가 주 정보가 아님(입력 폼 중심). 필요 시 슬롯 ‘마감’만 캡션·비활성 처리 |
| PAT-005 | 스택 진입 화면으로 하단 탭바 미표시(IA상 CL1→CL2 흐름) |
| PAT-006 | 동의 상세는 CM2 모달/시트로 분기; CL2 본문에는 체크박스+링크만 둠 |

## 사용 아이콘

| 위치 | 아이콘명 | figmaId | 크기 | 색상 역할 |
|------|---------|---------|------|----------|
| 상단 뒤로가기 | chevronLeft (`icon.baseicon.tokens.chevronLeft`) | 2:599 | 24×24 | text-primary — gray.900 #181d27 (rgba(24,29,39,1)) |
| 일정 섹션 | calendar | 2:576 | 20×20 | text-secondary — gray.500 #717680 (rgba(113,118,128,1)) |
| 사진 섹션 | image | 2:857 | 20×20 | text-secondary — gray.500 #717680 |
| 동의 섹션 | fileText | 2:779 | 20×20 | text-secondary — gray.500 #717680 |
| 동의 ‘내용 보기’ | externalLink | 2:752 | 16×16 | primary 링크 — brand.600 #7f56d9 (rgba(127,86,217,1)) |
| 사진 추가(빈 슬롯) | upload | 2:1235 | 24×24 | text-secondary — gray.500 #717680 |
| 썸네일 삭제 | x | 2:1298 | 20×20 | text-secondary — gray.500 #717680 (원형 hit 44px) |
| 노쇼 제한 배너 | alertCircle (`feedback.alertCircle`) | 2:467 | 20×20 | warning 강조 — warning.500 #f79009 (rgba(247,144,9,1)) |
| 참고사항(선택) | messageSquare | 2:932 | 20×20 | text-secondary — gray.500 #717680 |

---

## 레이아웃 구조

### 전체 구조

화면 배경: **background — gray.50 #fafafa (rgba(250,250,250,1))**

```
┌─────────────────────────────┐  390 × 844
│ 상단 바 (뒤로 + 제목)          │  h: 56px
├─────────────────────────────┤
│ 시술 요약 카드 (고정/스티키)    │  surface + border
├─────────────────────────────┤
│ (선택) 진행 스텝퍼 1·2·3       │  h: ≥40px
│ ─────────────────────────── │
│ ① 일정 슬롯 리스트            │
│ ② 사진 그리드 (PAT-007)       │
│ ③ 동의 체크 2행               │
│ ④ 참고사항 인풋               │
│         ↓ 스크롤              │
├─────────────────────────────┤
│ 고정 CTA 바 ‘신청하기’         │  surface + border-top
└─────────────────────────────┘
```

### 상단 바

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 390 × 56px | 표준 모바일 헤더 |
| 배경 | surface — white #ffffff (rgba(255,255,255,1)) | 본문 스크롤과 분리 |
| 배치 | 수평 스택 | 뒤로 / 제목 중앙 또는 시작 정렬 |
| 주축 정렬 | 양끝(뒤로·타이틀 영역) | 한 손 조작 고려 |
| 내부 여백 | 좌우 16px — spacing.xl | |
| 요소 간격 | 12px — spacing.lg | |
| 모서리 | 없음 | |
| 깊이 | 없음 (플랫) | visual-direction: 카드 외 그림자 최소 |
| 테두리 | 하단 1px — border-subtle #f5f5f5 (rgba(245,245,245,1)) | 헤더·콘텐츠 구분 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|--------|------|
| 뒤로 | 아이콘 버튼 | chevronLeft (2:599) 24px | — | text-primary — gray.900 |
| 제목 | 텍스트 | "신청하기" | heading — 20px/30px/0px Semibold | text-primary — gray.900 |

### 시술 요약 카드 (헤더 하단)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 크기 | 폭 390−32=358px(좌우 margin 16), 높이 auto | 가독성 있는 요약 블록 |
| 배경 | surface — white #ffffff | background와 대비 |
| 배치 | 수직 스택 | 시술명 → 디자이너 → 가격 |
| 내부 여백 | 16px — spacing.xl | |
| 요소 간격 | 8~12px — spacing.sm~lg | |
| 모서리 | 16px — radius.2xl | design-system 카드 반경 |
| 깊이 | 없음 | **border 1px — gray.300 #d5d7da** 로만 구분 (shadow 금지) |
| 테두리 | 1px border — gray.300 | 플랫 카드 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|--------|------|
| 시술명 | 텍스트 | "{시술명}" | subheading — 18px/28px/0 Semibold | text-primary — gray.900 |
| 디자이너 | 텍스트 | "{디자이너명}" | body — 16px/24px/0 Regular | text-secondary — gray.500 |
| 가격 | 텍스트 | "{가격}원" | body-medium — 16px/24px/0 Medium | text-primary — gray.900 |

### (선택) 진행 스텝퍼

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 높이 | 최소 40px (터치·시각 무게) | 네비 요소 무게감 규칙 |
| 현재 단계 | 원형 fill **primary — brand.600** + 흰 숫자/체크 | 시선 유도 |
| 미완료 | 원형 fill **gray.100** + 텍스트 **gray.500** | |
| 라벨 | caption — 12px/18px/0 | 현재 단계만 body-medium 색 primary |

### 일정 선택 섹션

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 섹션 헤더 | 좌측 4px 바 **brand.600** + calendar 아이콘 + "희망 일정" | 섹션 앵커 |
| 슬롯 행 | 각 행 최소 높이 48~52px, 행간 **border-subtle 1px** | 조밀 리스트 |
| 선택됨 | 행 배경 **primary-surface — brand.50 #f9f5ff** + 좌측 4px bar brand.600 | 상태를 색만으로 말하지 않음 |
| 비활성/마감 | caption + text-disabled — gray.400 #a4a7ae | |
| 슬롯 없음 | 전체 폭 배너 배경 **warning.50 #fffaeb** + 본문 **warning.500** | foundation warning.50 |

#### 내부 요소

| 요소 | 유형 | 내용 | 타이포 | 색상 |
|------|------|------|--------|------|
| 섹션 제목 | 텍스트 | "희망 일정" | subheading — 18px/28px/0 Semibold | text-primary — gray.900 |
| 슬롯 라벨 | 텍스트 | "{요일·날짜·시간}" | body — 16px/24px/0 Regular | text-primary — gray.900 |
| 보조 | 텍스트 | "마감" 등 | caption — 12px/18px/0 Regular | text-disabled / warning |

### 사진 제출 섹션 (PAT-007)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 그리드 | PAT-007 3열, 셀 간 gap **spacing.lg 12px** | 스펙과 CL6 동일 구조 |
| 빈 슬롯 | surface white, **border dashed 1px gray.300**, 중앙 upload 아이콘 | placeholder 금지 |
| 썸네일 오버레이 | 우상단 x 버튼 44px 히트 | 삭제 |

### 동의 섹션

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 각 동의 행 | 수평: 체크(44px) + 세로 스택(요약 + 내용 보기 링크) | |
| 체크박스 선택 | 테두리/내부 **brand.600** | primary 1차 사용처 |
| 요약 | body — 16px/24px | text-primary |
| 링크 | label 14px + externalLink 아이콘 | brand.600 |

### 시술 참고사항 (선택)

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 필드 | multiline, 높이 min 96px, **radius.lg 10px**, border gray.300 | surface white |
| placeholder | body, **text-disabled — gray.400** | |
| 글자 수 | caption 우하단 "0/200" | text-secondary |

### 하단 CTA 바

| 속성 | 값 | 설계 의도 |
|------|-----|----------|
| 배경 | surface — white | |
| 상단 테두리 | 1px border-subtle | shadow 대신 분리 |
| 패딩 | 16px spacing.xl, 하단 safe area 고려 | |
| 버튼 | 높이 ≥48px, **radius.full**, fill **primary brand.600**, 텍스트 button 14px Semibold 흰색 | |
| 비활성 | fill gray.100, 텍스트 gray.400 | |

---

## 데이터 매핑

| 데이터 필드 | 표시 위치 | 타이포 역할 | 색상 역할 | 비고 |
|------------|----------|-------------|----------|------|
| 시술명 | 요약 카드 | subheading | text-primary | 읽기 전용 |
| 디자이너명 | 요약 카드 | body | text-secondary | 읽기 전용 |
| 시술 가격 | 요약 카드 | body-medium | text-primary | 읽기 전용 |
| 희망 일정 | 슬롯 행 | body / caption | text-primary / disabled | 마감 시 비활성 |
| 신청용 사진 | PAT-007 셀 | — | — | 최소 1장 |
| 초상권 동의 | 체크 행 | body + 링크 label | primary 링크 | 내용 보기 → CM2 |
| SNS·후기 동의 | 체크 행 | 동일 | 동일 | 동일 |
| 시술 참고사항 | 텍스트 필드 | body | text-primary | 최대 200자 |

---

## 시각 품질 검증

### Surface Depth
| 요소 | fill | 부모/인접 fill | 대비 | 조치 |
|------|------|----------------|------|------|
| 화면 배경 | gray.50 | — | — | — |
| 요약 카드 | white | gray.50 | 충분 | — |
| 선택 슬롯 행 | brand.50 | white 카드 인접 시 본문 영역도 gray.50 배경 위면 대비 유지 | 충분 | 카드 바깥은 페이지 배경과 이웃 |
| 인풋 | white | gray.50 스크롤 영역 | 충분 | — |

### Elevation
| 요소 | 유형 | shadow 토큰 | 근거 (visual-direction) |
|------|------|------------|----------------------|
| 카드·CTA 바 | 플랫 바/카드 | 없음 | border로 구분, 그림자 최소 |
| CM2 (연동) | 모달/시트 | shadow-md | 오버레이만 elevation |

### 타이포 위계
| 수준 | 역할 | 스펙 (크기/행간/자간/굵기) | 적용 요소 |
|------|------|---------------------------|----------|
| 1 | heading | 20/30/0 Semibold | 상단 제목 |
| 2 | subheading | 18/28/0 Semibold | 섹션 제목·시술명 |
| 3 | body / label / caption | 16/24/0, 14/20/0, 12/18/0 | 본문·폼·메타 |

### 강조 검증
- focal point: **일정 슬롯 영역** — 앵커 바·선택 시 brand.50 행 + 좌측 바
- primary 사용: CTA, 체크 선택, 링크, 스텝퍼 현재 단계, 섹션 바
- 상태 표현: 마감·슬롯 없음은 **문구 + 색 + (배너 시) 아이콘**

### 밀도 검증
- 터치 가능 요소: 뒤로, 슬롯 행, 체크, 링크, 사진 셀, 삭제, CTA — 높이/히트 **≥44px** 목표
- ❌ 미충족 시: 아이콘만 있는 버튼에 투명 패딩 확장

### 시각 밀도 검증
- 스크롤 영역 빈 배경 비율: **낮게 유지** — 요약 카드·스텝퍼·3섹션·그리드로 50% 미만 목표
- 텍스트 전용 카드: **없음** — 동의 행에 아이콘·체크·링크 병치
- 반복 카드 차별화: 슬롯 행 다수 — **선택/마감**으로 행 배경·좌측 바 차별
- 섹션 헤더 앵커: **있음** — 4px primary 바 + 20px 아이콘
- 네비 요소 무게감: 스텝퍼 **현재=brand.600**, 미완=gray.100+gray.500

### 일관성 체크
- [ ] 모든 색상이 design-system.md·foundation 팔레트 키 참조
- [ ] 모든 타이포가 design-system.md 역할 표와 일치
- [ ] 행간·자간이 design-system.md 세밀값 표와 일치
- [ ] 카드·바는 shadow 대신 border (visual-direction)
- [ ] visual-direction.mdc 확정 디자인 결정과 충돌 없음
