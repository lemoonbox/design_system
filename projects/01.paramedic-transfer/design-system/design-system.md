# Design System — 구급 이송 조율

> foundation `core-visual-tokens.json`·`icon-tokens.json` 기준 확정값. 현장 모바일 맥락(가독성·터치·상태 구분)에 맞춰 역할을 배정함.

## 색상 역할

| 역할 | 팔레트 키 | Hex | 용도 |
|------|----------|-----|------|
| primary | brand.600 | #7F56D9 | 주요 버튼, 강조, 선택 상태 |
| primary-hover | brand.700 | #6941C6 | 버튼 hover·pressed |
| surface | white | #FFFFFF | 카드·시트·모달 등 기본 표면 |
| surface-raised | gray.100 | #F5F5F5 | 텍스트 필드·셀렉트 등 입력 컨트롤 fill (흰 표면 위 계층 구분) |
| background | gray.50 | #FAFAFA | 페이지 배경 |
| text-primary | gray.900 | #181D27 | 본문·제목 텍스트 |
| text-secondary | gray.600 | #535862 | 보조 텍스트·부가 설명 |
| text-disabled | gray.400 | #A4A7AE | 비활성 텍스트·플레이스홀더 |
| border | gray.300 | #D5D7DA | 구분선, 입력·카드 기본 테두리 (`border.color.default`와 동일) |
| success | success.600 | #039855 | 성공·승인 상태 |
| warning | warning.600 | #DC6803 | 경고·대기·주의 상태 |
| error | error.600 | #D92D20 | 오류·거절 상태 |
| accent | blue.600 | #1570EF | 링크·정보성 강조(브랜드 퍼플과 구분) |

## 타이포그래피

| 역할 | foundation 스케일 | 크기 | 굵기 | 용도 |
|------|-----------------|------|------|------|
| heading | display xs — semibold | 24px | 600 | 화면 제목 |
| subheading | text lg — semibold | 18px | 600 | 섹션·카드 제목 |
| body | text md — regular | 16px | 400 | 본문·목록 본문 |
| caption | text xs — regular | 12px | 400 | 타임스탬프·메타·범례 |
| label | text sm — medium | 14px | 500 | 폼 레이블·칩 라벨 |
| button | text md — semibold | 16px | 600 | 버튼·주요 인라인 액션 |

**폰트 패밀리**: foundation 기준 **Inter** (플랫폼별 시스템 폰트 대체 시 동일 역할·크기·굵기 유지).

## 간격 & 반경

- 기본 내부 padding: **spacing.xl** (16px)
- 섹션 간 gap: **spacing.3xl** (24px)
- 카드 radius: **radius.lg** (10px)
- 버튼 radius: **radius.md** (8px)

## 이펙트 토큰

foundation `effect.shadow` 중 이 프로젝트 표준 매핑. (복합 그림자는 동일 토큰명으로 레이어 조합.)

| 이름 | foundation 참조 | type | offset | blur | spread | color | alpha(≈) | 용도 |
|------|------------------|------|--------|------|--------|-------|----------|------|
| shadow-sm | shadow.xs | DROP_SHADOW | x:0 y:1 | 2 | 0 | #0A0D12 | 0.05 | 카드·입력창 |
| shadow-md | shadow.md — 레이어 1 | DROP_SHADOW | x:0 y:4 | 8 | -2 | #0A0D12 | 0.10 | 바텀시트·드롭다운 |
| shadow-lg | shadow.lg — 레이어 1 | DROP_SHADOW | x:0 y:12 | 16 | -4 | #0A0D12 | 0.08 | 플로팅 버튼·강조 오버레이 |

**포커스 링**: 입력·접근성 — `effect.focus ring.4px primary-100` 또는 `4px gray-100` (컨텍스트에 맞게 선택).

## 타이포그래피 세밀값

| 역할 | line-height | letter-spacing |
|------|------------|----------------|
| heading | 32px | 0 |
| body | 24px | 0 |
| caption | 18px | 0 |
| button | 24px | 0 |

## 테두리

- 기본 두께: **border.width.default** (1px)
- 색상: border 역할 — **gray.300** (#D5D7DA)

## 아이콘

- 기본 크기: **md** (행 내 보조는 sm, 강조 액션은 lg)
- 주요 사용 카테고리: **baseicon** (navigation, action, communication, status), **feedback** (alert-circle, alert-triangle, check-circle, zap)

## 공통 패턴 목록

2개 이상 화면에서 동일 목적·구조로 반복되는 UI 조각만 등록.

| ID | 패턴명 | 설명 | 등장 화면 |
|----|--------|------|----------|
| PAT-001 | 비동기·상태 카드 | 상태 배지, 시각(타임스탬프), 근거·사유·재시도 등 조건부 본문 블록 | G1, L1, L3 |
| PAT-002 | 병원 행 카드 | 병원명·식별·한 줄 요약; L2는 체크 선택, L3는 승인 상태 배지로 동일 그리드 확장 | L2, L3 |
| PAT-003 | 하단 요약 액션 바 | 선택 수·한 줄 요약 + 단일 주 CTA(필요 시 보조 텍스트 링크) | L2, L3 |
