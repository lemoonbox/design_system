# Design System — 구급 이송 조율 모바일 앱

> `context/foundation/core-visual-tokens.json`·`icon-tokens.json`에서 읽은 값만 사용. 현장 모바일(가독성·터치·상태 구분)에 맞춰 역할을 배정함.

## 색상 역할

| 역할 | 팔레트 키 | Hex | 용도 |
|------|----------|-----|------|
| primary | brand.600 | #7F56D9 | 주요 버튼, 강조, 선택 상태 |
| primary-hover | brand.700 | #6941C6 | 버튼 pressed·hover |
| surface | white | #FFFFFF | 카드·시트·모달 기본 표면 |
| surface-raised | gray.100 | #F5F5F5 | 입력 필 등 표면 위 한 단계 구분 |
| background | gray.50 | #FAFAFA | 페이지 배경 |
| text-primary | gray.900 | #181D27 | 본문·제목 텍스트 |
| text-secondary | gray.600 | #535862 | 보조 텍스트·부가 설명 |
| text-disabled | gray.400 | #A4A7AE | 비활성·플레이스홀더 |
| border | gray.300 | #D5D7DA | 구분선, 입력·카드 기본 테두리 (`border.color.default` ref) |
| success | success.600 | #039855 | 성공·승인 상태 |
| warning | warning.600 | #DC6803 | 경고·대기·주의 상태 |
| error | error.600 | #D92D20 | 오류·거절 상태 |
| accent | blue.600 | #1570EF | 링크·정보 강조(브랜드 퍼플과 구분) |

## 타이포그래피

| 역할 | foundation 스케일 | 크기 | 굵기 | 용도 |
|------|-----------------|------|------|------|
| heading | display xs — semibold | 24px | 600 | 화면 제목 |
| subheading | text lg — semibold | 18px | 600 | 섹션 제목 |
| body | text md — regular | 16px | 400 | 본문 |
| caption | text xs — regular | 12px | 400 | 보조, 메타, 타임스탬프 |
| label | text sm — medium | 14px | 500 | 폼 레이블 |
| button | text md — semibold | 16px | 600 | 버튼 텍스트 |

**폰트 패밀리**: foundation typography 기준 **Inter** (OS 대체 폰트 시 동일 역할·크기·굵기 유지).

## 간격 & 반경

- 기본 내부 padding: **spacing.xl** (16px)
- 섹션 간 gap: **spacing.3xl** (24px)
- 카드 radius: **radius.lg** (10px)
- 버튼 radius: **radius.md** (8px)

## 이펙트 토큰

foundation `effect.shadow` 매핑. 색상은 토큰 원문 8자리 HEX(RRGGBBAA); alpha는 마지막 바이트 기준 근사값.

| 이름 | foundation 참조 | type | offset | blur | spread | color (토큰값) | alpha(≈) | 용도 |
|------|------------------|------|--------|------|--------|----------------|----------|------|
| shadow-sm | shadow.xs | DROP_SHADOW | x:0 y:1 | 2 | 0 | #0A0D12 | 0.05 | 카드, 입력창 |
| shadow-md | shadow.md — 레이어 1 | DROP_SHADOW | x:0 y:4 | 8 | -2 | #0A0D12 | 0.10 | 바텀시트, 드롭다운 |
| shadow-lg | shadow.lg — 레이어 1 | DROP_SHADOW | x:0 y:12 | 16 | -4 | #0A0D12 | 0.08 | 플로팅 요소, 알림 |

**포커스 링**(입력·접근성): `effect.focus ring.4px primary-100` (#F4EBFF spread 4) 또는 `4px gray-100` — 맥락에 맞게 선택.

## 타이포그래피 세밀값

foundation 해당 스케일·굵기의 `lineHeight`·`letterSpacing` 그대로.

| 역할 | line-height | letter-spacing |
|------|------------|----------------|
| heading | 32px | 0 |
| body | 24px | 0 |
| caption | 18px | 0 |
| button | 24px | 0 |

**subheading** (text lg semibold): line-height **28px**, letter-spacing **0**.

## 테두리

- 기본 두께: **border.width.default** (1px)
- 색상: **border** 역할 — gray.300 (#D5D7DA), `border.color.default`와 동일

## 아이콘

- 기본 크기: **md** (보조 인라인은 sm, 강조 액션은 lg — 픽셀은 스펙·Figma에서 정합)
- 주요 사용 카테고리: **baseicon** (navigation, action, communication, status 등), **feedback** (alert-circle, alert-triangle, check-circle, zap)

## 공통 패턴 목록

**크롬(구조)만** 등록. 구급 일지 타임라인 카드·병원 행·pre-KTAS 블록 등 **콘텐츠 영역**은 화면별 스펙에서 설계한다.

| ID | 패턴명 | 설명 | 등장 화면 |
|----|--------|------|----------|
| PAT-001 | 앱 바 | 뒤로·화면 타이틀·우측 보조 액션(옵션). **M1**은 동일 역할의 모달 헤더 변형 | G1, L1, L2, L3, L4, M1 |
| PAT-002 | 시스템·동기화 상태 배너 | 오프라인·동기화·재시도 등 **한 줄** 시스템 피드백(IA: 화면별 상단·토스트 수준) | G1, L1, L2, L3 |
| PAT-003 | 하단 요약 액션 바 | 선택 수·한 줄 요약 + **주 CTA** 고정 영역(safe-area 대응은 스펙 참조) | L2, L3 |

> **참고**: 과거 산출물에 `병원 행 카드`·`비동기 상태 카드` 등 **콘텐츠 패턴** 프롬프트가 있을 수 있으나, 본 디자인 시스템의 공통 패턴 정의는 위 크롬 3종으로 한정한다. 카드·리스트 밀도는 각 `screen-spec`에 따른다.
