# Design System — 구급 이송 조율 모바일 앱

본 문서의 **팔레트 키·Hex·숫자**는 `context/foundation/core-visual-tokens.json`, 아이콘은 `context/foundation/icon-tokens.json`에서 읽은 값이다. foundation이 갱신되면 본 표의 Hex·px를 동기화한다.

**토큰 경로 표기**: 색상 `color.{팔레트}.{단계}`, 간격 `spacing.{토큰명}`, 반경 `radius.{토큰명}`, 타이포는 Figma export 그대로 **`typography.{스케일}.{굵기}`** (스케일에 공백 있음, 예: `display sm`, `text md`).

## 색상 역할

| 역할 | 팔레트 키 | Hex | 용도 |
|------|----------|-----|------|
| primary | color.brand.600 | #7f56d9 | 주요 버튼, 링크, 진행·선택 강조 |
| primary-pressed | color.brand.700 | #6941c6 | 버튼 pressed(모바일) |
| primary-subtle | color.brand.50 | #f9f5ff | 칩·선택 배경, 포커스 링 배경색 연계 |
| accent | color.blue.600 | #1570ef | 보조 강조(거리·정보 링크, 지도 등 2차 강조) |
| surface | color.gray.50 | #fafafa | 카드·모달 패널 |
| surface-raised | color.white | #ffffff | 입력 필드, 떠 있는 표면 |
| background | color.gray.25 | #fdfdfd | 페이지 기본 배경(미세 대비) |
| text-primary | color.gray.900 | #181d27 | 본문·제목 |
| text-secondary | color.gray.500 | #717680 | 보조·메타 |
| text-disabled | color.gray.300 | #d5d7da | 비활성 |
| text-on-primary | color.white | #ffffff | primary 버튼 위 텍스트 |
| border-subtle | border.color.subtle → gray.100 | #f5f5f5 | 섹션 구분·얇은 구분선 |
| border-default | border.color.default → gray.300 | #d5d7da | 카드·인풋 기본 테두리 |
| border-strong | border.color.strong → gray.500 | #717680 | 강조 구분선 |
| border-focus | border.color.brand → brand.600 | #7f56d9 | 포커스·선택 테두리 |
| success | color.success.600 | #039855 | 승인·동기 완료 |
| warning | color.warning.500 | #f79009 | 필수 미충족·동기 대기 |
| error | color.error.600 | #d92d20 | 오류·거절·파괴적 확인 |
| error-subtle | color.error.50 | #fef3f2 | 오류 배너 배경 |

**브랜드 방향**: foundation의 **brand(바이올렛 계열)** 를 primary로 사용한다. 상태는 **success / warning / error** 만으로 구분하지 말고 아이콘·문구를 병행한다(프로젝트 디자인 규칙).

**포커스 링**: `effect.focus ring`의 `4px primary-100` 등 foundation 이펙트를 폼·주요 버튼에 적용 가능.

## 타이포그래피

모든 스케일 **fontFamily: Inter**(foundation 기준). 앱 배포 시 플랫폼 정책에 따라 SF Pro / Roboto로 치환 가능.

| 역할 | foundation 스케일 (굵기) | 크기 | 줄간격 | 굵기 | 용도 |
|------|-------------------------|------|--------|------|------|
| heading | `display sm` · semibold | 30px | 38px | 600 | 화면 제목 |
| subheading | `text xl` · semibold | 20px | 30px | 600 | 섹션 제목 |
| body-strong | `text lg` · medium | 18px | 28px | 500 | 카드 제목·강조 한 줄 |
| body | `text md` · regular | 16px | 24px | 400 | 본문·폼 입력 |
| caption | `text sm` · regular | 14px | 20px | 400 | 보조·타임스탬프 |
| meta | `text xs` · regular | 12px | 18px | 400 | 법적 고지·최소 메타 |
| label | `text sm` · medium | 14px | 20px | 500 | 폼 레이블 |
| button | `text md` · semibold | 16px | 24px | 600 | 버튼 라벨 |

**화면 제목 예외**: 기본은 **`display sm` · semibold(30px)**. 제목이 두 줄 이상 자주 넘치는 화면만 **`text xl` · semibold(20px)** 로 바꿀 수 있다(전역 축소는 하지 않음).

## 간격 & 반경

`spacing`·`radius`는 foundation 수치 그대로다.

- 기본 내부 padding: **spacing.xl (16px)** — 카드·리스트 행·모달 본문
- 조밀한 패딩: **spacing.lg (12px)** — 칩·작은 행
- 섹션 간 gap: **spacing.3xl (24px)**
- 리스트 항목 간 gap: **spacing.lg (12px)**
- 화면 좌우 안전 영역: **spacing.xl (16px)** (노치는 플랫폼 가이드 추가)
- 테두리 두께: **border.width.default (1px)**, 강조 시 **border.width.medium (2px)**
- 카드 radius: **radius.xl (12px)**
- 버튼·칩 radius: **radius.md (8px)**
- 모달·시트 상단: **radius.2xl (16px)**

## 아이콘

- **크기 variant**: `icon.*` 컴포넌트에서 **sm / md / lg** (`icon-tokens.json` 내 플래그·피커 등 정의 참조).
- **범용**: **icon.baseicon** — 카테고리 예: `navigation`, `action`, `communication`, `status`, `data` 등.
- **피드백**: **icon.feedback** — `alertCircle`, `alertTriangle`, `checkCircle`, `zap` (성공·경고·강조).

구급 화면에서 빈도 높은 baseicon 예: 뒤로 `chevronLeft`, 시간 `clock`, 위치 `mapPin`(정의 시), 편집 `edit`, 클라우드 `cloud` / `cloudOff`, 확인 `check`, 새로고침 `refreshCw` 등 — 실제 노드는 Figma Base icons 프레임 기준.

## 공통 패턴 목록

| ID | 패턴명 | 설명 | 등장 화면 |
|----|--------|------|----------|
| PAT-001 | 케이스·동기화 헤더 | 케이스 라벨·시각·동기화/오프라인 배지 | G1, L1, L2, L4 |
| PAT-002 | 동기화·네트워크 배너 | 한 줄 요약 + 재시도·자세히(M2) | G1, L1, L2, L4 |
| PAT-003 | 업무 단계 스텝퍼 | 음성일지 → 증상·pre-KTAS → 이송 | G1, (L2/L4 상단 축약) |
| PAT-004 | 하단 고정 주요 CTA 바 | 단일 주요 버튼 + 안전 영역 | G1, L1, L2, L4 |
| PAT-005 | 2버튼 확인 모달 | 제목·본문·취소·주요 확인 | M1, M2, M3, M4, L2→L4 경고 |

**L4 전용(인덱스 미등재)**: 병원 카드(여유병상·거리·의료과·신청·승인·출발) — screen-spec L4.

## 이펙트 토큰 (foundation 실제 값)

foundation `effect.shadow.*` 값을 Figma MCP `set_effects` 파라미터로 변환한 기준표.
색상 base `#0a0d12` → r:0.039 g:0.051 b:0.071

| 토큰 | 레이어 | offset y | radius | spread | alpha | 용도 |
|------|--------|----------|--------|--------|-------|------|
| effect.shadow.xs | 1개 | 1 | 2 | 0 | 0.051 | 구분선 대체 subtle 그림자 |
| effect.shadow.sm | 2개 | L0: y1/r2 · L1: y1/r3 | — | 0 | L0:0.059 · L1:0.102 | **카드, 입력 필드** |
| effect.shadow.md | 2개 | L0: y2/r4 · L1: y4/r8 | — | -2 | L0:0.059 · L1:0.102 | **하단 CTA 바, 드롭다운** |
| effect.shadow.lg | 2개 | L0: y4/r6 · L1: y12/r16 | — | L0:-2 · L1:-4 | L0:0.031 · L1:0.078 | **모달 패널, 시트** |
| effect.shadow.xl | 2개 | L0: y8/r8 · L1: y20/r24 | — | -4 | L0:0.031 · L1:0.078 | **플로팅 알림, 오버레이** |

**Figma set_effects 변환 예시 — shadow.sm:**
```
effects: [
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.059}, offset:{x:0,y:1}, radius:2, spread:0, visible:true },
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.102}, offset:{x:0,y:1}, radius:3, spread:0, visible:true }
]
```

**shadow.md:**
```
effects: [
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.059}, offset:{x:0,y:2}, radius:4, spread:-2, visible:true },
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.102}, offset:{x:0,y:4}, radius:8, spread:-2, visible:true }
]
```

**shadow.lg:**
```
effects: [
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.031}, offset:{x:0,y:4}, radius:6, spread:-2, visible:true },
  { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:0.078}, offset:{x:0,y:12}, radius:16, spread:-4, visible:true }
]
```

## 타이포그래피 세밀값 (자간 · 행간)

행간은 타이포 표의 줄간격과 동일. 자간은 Inter 폰트 광학 기준.

| 역할 | 크기 | 줄간격 (line-height) | 자간 (letter-spacing) | unit |
|------|------|---------------------|----------------------|------|
| heading | 30px | 38px | -0.6px | PIXELS |
| subheading | 20px | 30px | -0.2px | PIXELS |
| body-strong | 18px | 28px | 0px | PIXELS |
| body | 16px | 24px | 0px | PIXELS |
| caption | 14px | 20px | 0px | PIXELS |
| label | 14px | 20px | 0px | PIXELS |
| button | 16px | 24px | 0.1px | PIXELS |
| meta | 12px | 18px | 0.1px | PIXELS |

## 디자인 결정 (확정)

| 주제 | 결정 | 이유 요약 |
|------|------|----------|
| 페이지 배경 | **`color.gray.25` (#fdfdfd) 유지** | 카드·표면과 미세 대비, 현장·차량 등 조도 변화 시 화면 구역 구분 |
| Accent | **`color.blue.600` (#1570ef) 유지** | primary(바이올렛)와 역할 분리, 거리·링크·정보 보조에 익숙한 블루 |
| 화면 제목 크기 | **전역 `display sm` 30px 유지** | 현장에서 단계 인지용; 긴 제목 화면만 `text xl` semibold 예외(위 타이포 절 참고) |
