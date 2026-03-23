# AI + Figma MCP 디자인 품질 향상 종합 가이드 v2
> 웹 리서치 기반 — 블로그·포스팅·공식 문서 직접 수집 정리

---

## 📌 핵심 진단: 왜 AI 디자인은 허하고 평범한가?

여러 연구와 실무 사례를 종합한 결론:

> **"출력 품질 향상의 절반은 더 나은 AI 도구로 바꾸는 것이 아니라, 더 나은 프롬프트를 쓰는 법을 배우는 것에서 온다."**
> — ClickUp Figma AI Prompts 연구

AI 디자인이 평범해지는 가장 큰 이유 3가지:

1. **맥락(Context) 없이 시작**: AI는 항상 "가장 안전한 평균값"을 선택. 브랜드 방향성 없이 시작하면 Generic UI가 나옴
2. **토큰(Token)이 AI에게 읽히지 않음**: `blue-5` 같은 원시적 네이밍은 AI가 어디에 써야 하는지 모름
3. **구조만 지시하고 시각적 연출은 생략**: "카드를 만들어라"는 말하지만 "이 카드가 어떤 인상을 줘야 하는가"는 말하지 않음

---

## 🔑 해결책 1: Design Token에 AI가 읽을 수 있는 의미(Semantic) 부여

**출처**: [Design tokens that AI can actually read — The Design System Guide](https://learn.thedesignsystem.guide/p/design-tokens-that-ai-can-actually)

### 현재 방식 vs 개선 방식

**❌ AI가 이해 못 하는 토큰 (현재 방식)**
```json
{
  "red-6": { "value": "#DE3E25", "type": "color" },
  "space-4": { "value": "20px", "type": "spacing" }
}
```

**✅ AI가 정확히 이해하는 토큰 (개선 방식)**
```json
{
  "color-feedback-error": {
    "value": "#DE3E25",
    "description": "오류 상태 색상. 오류 메시지, 파괴적 버튼 배경, 유효하지 않은 입력 테두리에 사용",
    "pairedWith": ["color-feedback-errorText", "color-feedback-errorIcon"],
    "components": ["Alert.error", "Button.destructive", "Input.invalidBorder"],
    "doNot": ["경고 상태에 사용 금지", "어두운 배경 위 대비 확인 없이 사용 금지"]
  }
}
```

### 프로젝트 적용 방법

현재 `core-visual-tokens.json`과 `design-system.md`에 각 색상 토큰마다 다음을 추가:

```markdown
## 색상 역할 (AI 가이드 포함)

| 토큰명 | Hex | AI 사용 지침 | 절대 금지 |
|--------|-----|------------|---------|
| color.primary | #7f56d9 | 주요 CTA 버튼, 선택 상태, 진행 표시 | 배경 전체, 텍스트 단독 사용 |
| color.primary-subtle | #f9f5ff | 선택된 카드 배경, 아이콘 컨테이너 | 경계선 없이 단독 사용 |
| color.surface-raised | #ffffff | 카드, 모달, 입력 필드 — shadow.sm 필수 동반 | 보더와 동시 사용 금지 |
```

**핵심 원칙**: 토큰은 AI가 닿는 유일한 레이어. 토큰에 의미가 담기면 모든 컴포넌트에 정확성이 전파된다.

---

## 🎨 해결책 2: 프롬프트에 "비주얼 방향성(Visual Direction)" 필수 포함

**출처**: [Figma Blog — AI Brand Guidelines Generator](https://www.figma.com/solutions/ai-brand-guideline-generator/), [ClickUp — 40+ Best Figma AI Prompts](https://clickup.com/blog/figma-ai-prompts/)

AI에게 디자인을 시킬 때 **무드와 방향성을 자연어로 먼저 선언**하면 일관성과 개성이 동시에 확보된다.

### 비주얼 방향성 선언 템플릿

`04-design-system.md` 커맨드에서 디자인 시스템 정의 시 필수 추가:

```markdown
## 비주얼 방향성 선언 (AI에게 전달되는 무드 가이드)

### 브랜드 무드 키워드 (3개 선택)
예: "Clinical Confidence" / "Calm Authority" / "Precision in Motion"

이 3가지 키워드를 충족하는 디자인 결정 원칙:
- 색상: 차분하고 신뢰감 있는 조합. 강렬한 원색보다 깊이감 있는 파스텔+딥 조합
- 형태: 날카로운 각보다 의도적인 라운드. 단, 너무 부드러우면 권위 손실
- 간격: 넉넉한 여백으로 "전문가의 여유"를 표현. 빽빽하지 않게
- 타이포: 제목은 굵고 자신감 있게, 본문은 가볍고 읽기 쉽게

### 표면 스타일 전략
- Hero 표면 (최우선 콘텐츠): primary-subtle 배경 + shadow.md + accent-bar
- Standard 표면 (일반 카드): white + shadow.sm (보더 없음)
- Recessed 표면 (배경): gray.50 또는 gray.100
- Floating 표면 (모달/알림): white + shadow.xl

### 시각적 금지 목록
- 모든 카드에 동일한 shadow 사용 금지
- 모든 아이콘을 gray로 두는 것 금지
- 헤더/섹션 제목 없이 콘텐츠 나열 금지
```

---

## 🏗️ 해결책 3: 3단계 표면 깊이 시스템 (Surface Depth)

**출처**: [LogRocket — Shadows in UI Design](https://blog.logrocket.com/ux-design/shadows-ui-design-tips-best-practices/), [Smashing Magazine — Dominance, Focal Points and Hierarchy](https://www.smashingmagazine.com/2015/02/design-principles-dominance-focal-points-hierarchy/)

### 왜 지금 디자인이 평평하게 느껴지는가

현재 프로젝트의 `summary-card`는 `fillColor: #fafafa + stroke 1px`로 만들어집니다. 이것이 문제입니다.

- `#fdfdfd` (배경) vs `#fafafa` (카드) = **육안으로 구별 거의 불가**
- 보더가 있으면 "벽에 그려진 카드"처럼 평평해 보임
- 쉐도우가 없으면 "떠있는 느낌"이 전혀 없음

### 표면 깊이 시스템 전체 구조

```markdown
## 표면 4단계 깊이 시스템

| 레벨 | 이름 | 배경색 | 쉐도우 | 보더 | 언제 사용 |
|------|------|--------|--------|------|----------|
| L0 | Recessed | gray.100 (#f0f0f0) | 없음 | 없음 | 전체 배경, 비활성 섹션 |
| L1 | Base (★현재 missing) | white (#ffffff) | shadow.sm | 없음 | 일반 카드, 리스트 |
| L2 | Elevated | white (#ffffff) | shadow.md | 없음 | 주요 카드, CTA 영역 |
| L3 | Floating | white (#ffffff) | shadow.lg~xl | 없음 | 모달, 바텀시트, 알림 |
```

### shadow 값 상세 (LogRocket 권장 방식 적용)

```
★ 일반 카드 (shadow.sm 개선):
effects: [
  { offset: {x:0, y:1}, radius: 3,  alpha: 0.04, spread: 0 },
  { offset: {x:0, y:4}, radius: 12, alpha: 0.08, spread: -2 }
]

★ 중요 카드 (shadow.md 개선):
effects: [
  { offset: {x:0, y:2}, radius: 6,  alpha: 0.06, spread: 0 },
  { offset: {x:0, y:8}, radius: 24, alpha: 0.10, spread: -4 }
]
→ 핵심: 낮은 opacity + 높은 blur = 자연스럽고 세련된 쉐도우
```

### 쉐도우 사용 원칙 (LogRocket 리서치 기반)

1. **모든 요소에 동일한 쉐도우 쓰지 말 것** — 쉐도우가 위계를 잃음
2. **보더와 쉐도우는 같이 쓰지 말 것** — 이미 프로젝트에 있는 규칙, 더 엄격히 적용
3. **배경 색상에 따라 쉐도우 색상 조정** — 항상 #0a0d12 아닌, 배경의 어두운 변형 사용
4. **인터랙티브 요소에 쉐도우 추가** — 버튼에 작은 쉐도우는 "탭 가능함"을 암시

---

## 💡 해결책 4: 시각적 위계의 3단계 법칙

**출처**: [Smashing Magazine — Dominance, Focal Points and Hierarchy](https://www.smashingmagazine.com/2015/02/design-principles-dominance-focal-points-hierarchy/)

> "동일한 요소들은 서로를 지배할 수 없다. 지배하려면 달라 보여야 한다."

### 화면마다 반드시 3단계 위계를 만들 것

```
★ 1단계 (Dominant) — 화면당 1개만
→ 가장 크고, 가장 굵고, 가장 눈에 띄는 요소
→ 이 화면에서 사용자가 "즉시" 봐야 할 정보

★ 2단계 (Sub-dominant) — 2~3개
→ 보조 정보, 섹션 제목, 상태 표시

★ 3단계 (Subordinate) — 나머지 전부
→ 본문, 메타 정보, 배경 요소
```

### 현재 프로젝트 화면별 Focal Point 설정 예시

```markdown
| 화면 | 1단계 (Dominant) | 2단계 | 3단계 |
|------|----------------|-------|-------|
| G1 홈 | 스텝퍼 현재 단계 강조 | 진행 요약 카드 | 시각·메타 텍스트 |
| L1 음성일지 | 마이크 버튼 (크고 둥글게) | 현재 녹음 상태 | 이전 기록 |
| L4 병원 추천 | 최우선 추천 병원 카드 | 거리·여유병상 | 기타 병원 목록 |
```

### 프롬프트에 Focal Point 명시하기

`05-screen-prompt.md`에서 각 화면 프롬프트 생성 시 추가:

```markdown
## 이 화면의 시각적 우선순위

★ 1단계 포컬 포인트: [요소명]
→ 처리: font-size 증가 / 컬러 primary 적용 / shadow.md / 충분한 여백

★ 2단계 포컬 포인트: [요소명], [요소명]
→ 처리: subheading 스케일 / 일반 쉐도우 적용

★ 3단계 (나머지): 전부 caption / text-secondary / 최소 시각적 무게
```

---

## ✨ 해결책 5: 장식 요소(Decorative Elements) 시스템

**출처**: [Figma Blog — Glassmorphism Guide 2025](https://edesignify.com/blogs/mastering-figmas-new-glass-effect-a-complete-guide-2025-update), [Weavely — Glassmorphism in Figma](https://www.weavely.ai/blog/the-glassmorphism-design-trend-in-figma)

"허한 느낌"은 장식 요소의 부재입니다. 아래 5가지를 추가하면 즉시 개선됩니다.

### 장식 요소 5가지 레시피

**① Accent Bar (좌측 컬러 바)**
```
create_rectangle
  width: 4, height: FILL
  fillColor: primary #7f56d9
  cornerRadius: 좌상 12px, 좌하 12px, 우상 0, 우하 0
→ 카드 frame을 HORIZONTAL auto layout으로 변경 후 첫 번째 자식으로 삽입
→ 상태별 색상 변경: 진행=primary, 완료=success, 경고=warning
```

**② Icon Container Circle (아이콘 배경 원)**
```
create_frame
  width: 40, height: 40
  cornerRadius: 20 (완전한 원)
  fillColor: primary-subtle #f9f5ff
  set_auto_layout: CENTER/CENTER
→ 아이콘을 자식으로 insert_child
→ 아이콘 색상: primary #7f56d9
```

**③ Micro-Gradient Header (헤더 그래디언트)**
```
create_rectangle (헤더 프레임 위에 올리기)
  width: FILL, height: FILL
  fill: LINEAR_GRADIENT
  stops: [
    { color: {r:0.498, g:0.337, b:0.851, a:0.05}, position: 0 },
    { color: {r:0.498, g:0.337, b:0.851, a:0},    position: 1 }
  ]
→ 헤더 하단 방향으로 미세하게 브랜드 컬러가 스며드는 효과
```

**④ Status Surface Color (상태별 카드 배경)**
```
진행 중:  fillColor #ffffff,    shadow.sm, accent-bar primary #7f56d9
완료:     fillColor #ecfdf3,    shadow.xs, accent-bar success #039855
경고:     fillColor #fffaeb,    shadow.xs, accent-bar warning #f79009
오류:     fillColor #fef3f2,    shadow.xs, accent-bar error   #d92d20
→ 동일한 카드 구조로 상태를 시각적으로 즉시 구분
```

**⑤ Stat Block (숫자·핵심 데이터 강조)**
```
create_frame
  fillColor: primary-subtle #f9f5ff
  cornerRadius: 12px (radius.xl)
  padding: 16px
  auto_layout: VERTICAL, gap: 4px

create_text (숫자)
  fontSize: 30, fontWeight: 700
  color: primary #7f56d9
  letterSpacing: -0.6px

create_text (라벨)
  fontSize: 12, fontWeight: 400
  color: text-secondary #717680
→ 핵심 데이터가 "팝" 되어 정보 밀도 높은 화면에서 특히 효과적
```

---

## 📐 해결책 6: 간격의 "관계 기반 차등 시스템"

**출처**: [Smashing Magazine — Compositional Flow and Rhythm](https://www.smashingmagazine.com/2015/04/design-principles-compositional-flow-and-rhythm/)

> "리듬은 반복이지만, 반복 요소들 사이의 간격과 배치에 집중한다."

현재 모든 간격이 `itemSpacing: 24px`로 동일한 것이 문제입니다.

### 관계 기반 간격 원칙

```
관계가 가까울수록 → 간격이 좁다
관계가 멀수록    → 간격이 넓다

★ 아이콘 ↔ 라벨 텍스트:        8px (같은 의미 단위)
★ 제목 ↔ 본문:                  8px (직접 연관)
★ 본문 ↔ 보조 텍스트:           4px (종속 관계)
★ 카드 내 섹션 ↔ 섹션:         16px (구분되지만 관련)
★ 카드 ↔ 카드:                 12px (독립적 아이템)
★ 섹션 ↔ 섹션:                 24px (구분되는 그룹)
★ 화면 내 주요 블록 ↔ 블록:    32px (시각적 "숨 고르기")
```

### 프롬프트 적용 예시 (개선)

**Before (현재):**
```
itemSpacing: 24px (모든 요소에 동일)
```

**After (개선):**
```
카드 내부 auto_layout:
  itemSpacing: 8px (제목↔본문)
  — 단, 섹션 구분 시 separatorFrame (height:1, color:border-subtle) 삽입 후
  — 섹션 간격은 paddingTop:16px 적용

화면 전체 auto_layout:
  itemSpacing: 0 (섹션 간 직접 gap 대신)
  — 각 섹션 프레임의 paddingTop/Bottom으로 개별 제어
```

---

## 🧩 해결책 7: 프롬프트 체이닝(Prompt Chaining) 전략

**출처**: [ClickUp — 40+ Best Figma AI Prompts](https://clickup.com/blog/figma-ai-prompts/), [TJ Pitre — AI Design Systems with Figma MCP](https://www.aiverse.design/insights/tj-pitre-design-systems)

> "모든 것을 한 번에 요청하지 말라. 원자(Atom) → 분자(Molecule) → 유기체(Organism) 순서로 빌드하라."

### 현재 방식의 문제

현재 `08-build-screen.md`는 한 화면을 처음부터 끝까지 한 번에 실행합니다. AI가 동시에 너무 많은 결정을 내리면 각 결정의 품질이 떨어집니다.

### 개선된 4단계 프롬프트 체이닝

```markdown
## Phase 1: 구조 (Structure Only)
→ 프레임, 레이아웃, 섹션 배치만
→ 색상/텍스트/아이콘 없이 뼈대만 확인
→ 검증: "이 구조가 화면 목적에 맞는가?"

## Phase 2: 콘텐츠 (Content Fill)
→ 실제 텍스트, 데이터 값, 아이콘 배치
→ 디자인 토큰 적용 (색상, 간격, 반경)
→ 검증: "모든 스펙 데이터가 표시되는가?"

## Phase 3: 시각 처리 (Visual Polish)
→ 쉐도우 레벨 적용 (L0~L3)
→ Accent Bar, Icon Container 등 장식 요소 추가
→ 간격 차등화 (관계 기반으로 조정)
→ 검증: "3단계 시각적 위계가 명확한가?"

## Phase 4: 일관성 검증 (Consistency Check)
→ 09-audit.md의 비주얼 품질 체크리스트 실행
→ 패턴 재사용 여부 확인
→ 전체 스크린샷 비교
```

### 체이닝 예시 프롬프트

```
[Phase 1 프롬프트 예시]
"G1 홈 화면의 뼈대 구조만 만들어라.
- 390×844 프레임
- 헤더 영역 (높이 확인 필요)
- 스크롤 가능한 콘텐츠 영역
- 하단 고정 CTA 바
색상, 텍스트, 아이콘은 이 단계에서 넣지 말 것."

[Phase 3 프롬프트 예시]
"기존 구조를 유지하면서 다음 시각적 처리를 추가하라:
1. summary-card의 stroke 제거 → shadow.sm 적용
2. 스텝퍼 마커 아이콘에 40×40 primary-subtle 원형 배경 추가
3. summary-card 좌측에 4px primary accent-bar 추가
4. 헤더 배경에 primary 5% → 0% 그래디언트 오버레이 추가"
```

---

## 📊 해결책 8: 디자인 레퍼런스 스크린샷 활용법

**출처**: [Sergei Chyrkov — Better UI Design with Figma Make](https://sergeichyrkov.com/blog/how-to-get-better-ui-design-with-figma-make-and-ai-(without-generic-results))

> "AI는 완성된 디자인을 분석하는 것이 백지에서 창조하는 것보다 훨씬 뛰어나다. 레퍼런스 이미지를 활용하라."

### 레퍼런스 활용 워크플로우

```markdown
## 새 프로젝트 시작 시 레퍼런스 수집 단계 추가

### 1. 무드 레퍼런스 3~5장 수집
→ Dribbble, Muzli, Mobbin에서 비슷한 성격의 앱 스크린샷
→ "이런 느낌" 기준: 색감, 밀도, 타이포 스타일

### 2. 컴포넌트 레퍼런스 수집
→ 잘 만들어진 카드 UI 예시
→ 헤더 디자인 예시
→ 버튼 스타일 예시

### 3. AI에게 레퍼런스와 함께 프롬프트
"첨부한 스크린샷의 카드 스타일(쉐도우 깊이, 코너 반경, 내부 패딩 비율)을
참고하여 summary-card를 디자인하라.
단, 색상은 design-system.md의 primary #7f56d9 팔레트를 따를 것."

→ AI가 스타일을 "분석→추출→적용"하는 방식으로 훨씬 세련된 결과
```

---

## 🔧 해결책 9: `core-visual-tokens.json` AI 가이드 레이어 추가

**출처**: [The Design System Guide — AI-Readable Tokens](https://learn.thedesignsystem.guide/p/design-tokens-that-ai-can-actually)

현재 `core-visual-tokens.json`은 값만 있고 의미가 없습니다. 별도 `token-ai-guide.md` 파일을 추가하는 것을 권장합니다.

### 생성할 파일: `context/foundation/token-ai-guide.md`

```markdown
# Design Token AI 사용 가이드

## 색상 토큰 사용 규칙

### primary (#7f56d9)
- 쓸 곳: CTA 버튼 배경, 활성 탭, 선택된 체크박스, 진행 표시
- 쓰지 말 곳: 배경 전체 색상, 본문 텍스트, 보조 요소

### primary-subtle (#f9f5ff)
- 쓸 곳: 선택된 카드 배경, 아이콘 컨테이너, 포커스 링 배경
- 항상 primary 컬러 요소(아이콘, 보더)와 함께 사용

### surface-raised / white (#ffffff)
- 쓸 곳: 카드, 입력 필드, 모달 배경
- 반드시 shadow.sm 이상과 함께 사용 (보더 없이)

### background / gray.25 (#fdfdfd)
- 쓸 곳: 페이지 배경 전용
- 카드/콘텐츠 배경에 사용 금지 (대비 없어짐)

## 쉐도우 토큰 페어링

| 표면 레벨 | 배경색 | 쉐도우 | 보더 |
|----------|--------|--------|------|
| 기본 카드 | white | shadow.sm | 없음 |
| 강조 카드 | white | shadow.md | 없음 |
| 모달/시트 | white | shadow.lg | 없음 |
| 배경 섹션 | gray.50~100 | 없음 | 없음 |

## 타이포그래피 페어링 규칙

- heading (30px) 다음엔 반드시 body (16px) 이하로 점프
- subheading (20px) + body (16px) + caption (14px) = 3단계 위계 표준 조합
- meta (12px)는 항상 text-secondary (#717680), 단독 사용 금지
```

---

## 📺 추천 학습 리소스 (YouTube 채널 + 블로그)

### YouTube 채널
| 채널 | 특화 | 관련 주제 |
|------|------|---------|
| **Design+Code** | Figma 고급 기법, 실시간 UI 리뷰 | 쉐도우, 그래디언트, 프리미엄 feel |
| **Juxtopposed** | 독창적 UI 디자인, 개성 있는 스타일 | 평범함 탈피, 비주얼 실험 |
| **AJ&Smart** | UX/UI 전략, 체계적 접근 | 위계, 정보 구조 |
| **femke.design** | 시니어 프로덕트 디자이너 인사이트 | 품질 기준, 의사결정 |

### 블로그/아티클
| 출처 | 추천 이유 |
|------|---------|
| [Smashing Magazine — Design Principles](https://www.smashingmagazine.com/category/design-principles/) | 시각적 위계, 리듬, 지배의 근본 원리 |
| [LogRocket — Shadows Best Practices](https://blog.logrocket.com/ux-design/shadows-ui-design-tips-best-practices/) | 쉐도우 심층 가이드 |
| [The Design System Guide — AI Tokens](https://learn.thedesignsystem.guide/p/design-tokens-that-ai-can-actually) | AI 친화적 토큰 설계 |
| [ClickUp — 40+ Figma AI Prompts](https://clickup.com/blog/figma-ai-prompts/) | 42가지 실전 프롬프트 템플릿 |
| [Figma Blog — MCP & Design Systems](https://www.figma.com/blog/design-systems-ai-mcp/) | MCP + AI 최신 동향 |
| [AIVerse Design — TJ Pitre Interview](https://www.aiverse.design/insights/tj-pitre-design-systems) | 실무 Figma MCP 워크플로우 |

---

## 🚀 즉시 실행 가능한 우선순위 액션

### ✅ 오늘 할 수 있는 것 (1~2시간)

1. **`design-system.md`에 "비주얼 방향성 선언" 섹션 추가**
   - 브랜드 무드 키워드 3개 결정
   - 표면 전략 4단계 정의
   - AI 사용 금지 목록 작성

2. **`summary-card` 수정** (즉시 효과 가장 큰 것)
   - stroke 제거 → shadow.sm 적용
   - fillColor: #ffffff로 변경

3. **`context/foundation/token-ai-guide.md` 파일 생성**
   - 토큰 사용 규칙 10줄만 작성해도 효과 큼

### ✅ 이번 주 할 것 (3~5시간)

4. **`05-screen-prompt.md`에 Phase 1~4 체이닝 구조 추가**
5. **Accent Bar 장식 요소를 PAT-001 헤더에 적용**
6. **`09-audit.md`에 비주얼 품질 체크리스트 7항목 추가**

### ✅ 다음 버전 개선 (장기)

7. **레퍼런스 이미지 수집 단계를 00-new-project.md에 추가**
8. **Mobbin/Dribbble에서 앱 카테고리별 레퍼런스 라이브러리 구축**
9. **FigmaLint로 디자인 시스템 준수율 자동 점수화**

---

## 한 줄 요약

> 현재 프로젝트의 구조(Structure)는 훌륭합니다. 지금 빠진 것은 딱 세 가지입니다:
> **① AI가 읽을 수 있는 토큰 의미** + **② 시각적 방향성 선언** + **③ 장식 요소 레시피**.
> 이 세 가지를 프롬프트 시스템에 추가하면 동일한 MCP 도구로도 즉시 세련된 디자인이 나옵니다.
