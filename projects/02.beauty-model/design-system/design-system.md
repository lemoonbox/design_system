# Design System — 뷰티모델 플랫폼

> 기준 파일: `context/foundation/core-visual-tokens.json`
> 플랫폼: 모바일 웹 (360px~430px), Inter 폰트

---

## 색상 역할

| 역할 | 팔레트 키 | Hex | 용도 |
|------|----------|-----|------|
| primary | brand.600 | #7f56d9 | CTA 버튼, 링크, 활성 탭 |
| primary-hover | brand.700 | #6941c6 | 버튼 pressed 상태 |
| primary-surface | brand.50 | #f9f5ff | 브랜드 틴트 배경 (강조 배너 등) |
| surface | white | #ffffff | 카드, 시트 배경 |
| background | gray.50 | #fafafa | 페이지 전체 배경 |
| text-primary | gray.900 | #181d27 | 본문·제목 텍스트 |
| text-secondary | gray.500 | #717680 | 보조 정보, 레이블 |
| text-disabled | gray.400 | #a4a7ae | 비활성 텍스트, placeholder |
| border | gray.300 | #d5d7da | 인풋, 카드 테두리 |
| border-subtle | gray.100 | #f5f5f5 | 섹션 구분선 |
| success | success.600 | #039855 | 예약 확정, 완료 상태 |
| warning | warning.500 | #f79009 | 대기, 주의 상태 |
| error | error.500 | #f04438 | 오류, 취소, 거절 상태 |

---

## 타이포그래피

| 역할 | foundation 스케일 | 크기 | 굵기 | 용도 |
|------|-----------------|------|------|------|
| heading | text xl · semibold | 20px | 600 | 화면 제목, 상품명 |
| subheading | text lg · semibold | 18px | 600 | 섹션 헤더, 카드 제목 |
| body | text md · regular | 16px | 400 | 본문, 설명 |
| body-medium | text md · medium | 16px | 500 | 강조 본문 |
| caption | text xs · regular | 12px | 400 | 날짜, 메타, 상태 텍스트 |
| label | text sm · medium | 14px | 500 | 폼 레이블, 탭 텍스트 |
| button | text sm · semibold | 14px | 600 | 버튼 텍스트 |

폰트 패밀리: **Inter**

---

## 간격 & 반경

- 기본 내부 padding: spacing.xl (16px)
- 콘텐츠 내부 gap: spacing.lg (12px)
- 섹션 간 gap: spacing.3xl (24px)
- 카드 radius: radius.2xl (16px)
- 버튼 radius: radius.full (pill)
- 인풋 radius: radius.lg (10px)
- 배지/칩 radius: radius.full (pill)

---

## 이펙트 토큰

| 이름 | type | offset | blur | spread | color | alpha | 용도 |
|------|------|--------|------|--------|-------|-------|------|
| shadow-sm | DROP_SHADOW | x:0 y:1 | 3 | 0 | #0a0d12 | 0.06 | 카드, 입력창 |
| shadow-md | DROP_SHADOW | x:0 y:4 | 8 | -2 | #0a0d12 | 0.10 | 모달, 바텀시트 |
| shadow-lg | DROP_SHADOW | x:0 y:12 | 16 | -4 | #0a0d12 | 0.08 | 플로팅 버튼 |

> foundation 원본 참조: `effect.shadow.sm`, `effect.shadow.md`, `effect.shadow.lg`

---

## 타이포그래피 세밀값

| 역할 | line-height | letter-spacing |
|------|------------|----------------|
| heading (text xl) | 30px | 0px |
| subheading (text lg) | 28px | 0px |
| body (text md) | 24px | 0px |
| caption (text xs) | 18px | 0px |
| button (text sm) | 20px | 0px |

---

## 테두리

- 기본 두께: 1px
- 색상: border 토큰 (#d5d7da)
- 구분선: border-subtle 토큰 (#f5f5f5)

---

## 아이콘

- 기본 크기: md (24px 기준)
- 주요 사용 카테고리: baseicon (navigation, action, user, status, commerce), feedback (alertCircle, alertTriangle, checkCircle)

---

## 공통 패턴 목록

| ID | 패턴명 | 설명 | 등장 화면 |
|----|--------|------|----------|
| PAT-001 | 예약 카드 | 예약 상태·일시·시술명 표시 행 | CG2, DG3 |
| PAT-002 | 상품/모집글 카드 | 썸네일+시술 조건 카드 | CG1, DG1 |
| PAT-003 | 신청자 행 | 프로필 사진+이름+상태 배지 행 | DG2, DL3 |
| PAT-004 | 상태 배지 | 대기/승인/거절/완료 등 상태 칩 | CG2, CL4, DG2, DG3, DL3, DL4 |
| PAT-005 | 하단 탭바 | 고객/디자이너 역할별 탭 내비게이션 | CG1~4, DG1~4 |
| PAT-006 | 바텀 시트 | 확인/취소/동의 모달 하단 시트 | CM1, CM2, DM1, DM2 |
| PAT-007 | 사진 썸네일 그리드 | 3열 사진 목록 | CL6, DL3 |
