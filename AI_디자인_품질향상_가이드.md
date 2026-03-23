# AI + Figma MCP 디자인 품질 향상 종합 가이드

## 현재 문제 진단

프로젝트의 기존 프롬프트 시스템(`04-design-system.md` ~ `09-audit.md`)과 실제 생성된 디자인 시스템(`design-system.md`)을 분석한 결과, **구조적으로는 매우 잘 설계되어 있지만** 다음과 같은 이유로 "허하고 평범한" 디자인이 나오고 있습니다.

### 근본 원인 5가지

**1. 프롬프트가 "무엇을 배치할지"만 지시하고, "어떻게 보여야 하는지"는 지시하지 않음**
현재 프롬프트는 `create_frame → set_auto_layout → create_text` 순서로 구조적 배치에 집중합니다. 하지만 시각적 분위기, 감성, 밀도감에 대한 지시가 없어 AI가 가장 안전한(= 가장 평범한) 선택을 합니다.

**2. 디자인 토큰이 기능적이지만 감성적이지 않음**
`color.gray.50`, `border.width.default 1px` 같은 토큰은 정확하지만, 표면 간 대비가 약하고(#fdfdfd vs #fafafa는 육안으로 거의 구분 불가), 시각적 깊이감을 만들지 못합니다.

**3. 장식 요소(Decorative Elements) 부재**
카드에 stroke만 있고 그래디언트, 배경 패턴, 일러스트, 컬러 악센트 바 같은 시각적 흥미 요소가 없습니다. 모든 카드가 동일한 `#fafafa + 1px border`라서 단조롭습니다.

**4. 시각적 위계(Visual Hierarchy)의 단조로움**
모든 섹션이 동일한 패딩(16px), 동일한 간격(24px), 동일한 카드 스타일을 사용합니다. 중요도에 따른 시각적 차별화가 없어 "평평한" 느낌을 줍니다.

**5. 비주얼 스타일 방향성(Visual Direction) 미정의**
디자인 시스템에 "우리 앱은 이런 느낌이어야 한다"는 비주얼 컨셉이 없습니다. NN/g 연구에 따르면 이 부분이 빠지면 AI는 항상 가장 generic한 결과를 내놓습니다.

---

## 해결책 1: 디자인 시스템에 "Visual Direction" 섹션 추가

`04-design-system.md` 커맨드에서 디자인 시스템을 정의할 때 **비주얼 방향성**을 필수 항목으로 추가합니다.

### 추가할 섹션 구조

```markdown
## 비주얼 방향성 (Visual Direction)

### 무드 키워드
| 키워드 | 설명 | 적용 방식 |
|--------|------|----------|
| 예: Calm Professional | 차분하지만 신뢰감 | 저채도 그래디언트, 넉넉한 여백, 라운드 코너 강조 |
| 예: Bold & Energetic | 대담하고 활기찬 | 컬러 블록, 높은 대비, 기하학 패턴 |

### 표면 스타일 전략
- **Hero 표면**: (가장 중요한 카드/섹션) → 그래디언트 배경 또는 컬러 악센트
- **Standard 표면**: (일반 카드) → 쉐도우 + 미세 보더
- **Recessed 표면**: (배경 영역) → 배경보다 살짝 어두운 표면

### 장식 요소 (Decorative Tokens)
- accent-bar: primary 컬러 4px 좌측 또는 상단 바
- gradient-hero: primary → primary-subtle 방향 그래디언트
- icon-bg-circle: 아이콘 뒤에 subtle 원형 배경
- divider-style: 단순 1px 선 대신 gradient fade 또는 dot pattern
```

### 왜 효과적인가
Figma 블로그의 "Cooking with Constraints" 프레임워크에 따르면, AI에게 **제약 조건과 방향성을 동시에 제공**하면 창의적이면서도 일관된 결과를 얻습니다. 비주얼 키워드는 AI가 모호한 선택을 해야 할 때 일관된 방향으로 결정하게 하는 "나침반" 역할을 합니다.

---

## 해결책 2: 표면 깊이 시스템(Surface Depth System) 도입

현재 모든 카드가 동일한 표면 스타일을 사용합니다. **3단계 표면 시스템**을 도입하면 시각적 위계가 즉시 개선됩니다.

### 표면 3단계 정의

```markdown
## 표면 깊이 시스템

| 레벨 | 이름 | 배경 | 쉐도우 | 보더 | 용도 |
|------|------|------|--------|------|------|
| L0 | Recessed | gray.100 (#f0f0f0) | 없음 | 없음 | 전체 배경, 비활성 영역 |
| L1 | Base | white (#ffffff) | shadow.sm | 없음 | 일반 카드, 리스트 항목 |
| L2 | Elevated | white (#ffffff) | shadow.md | 없음 | 주요 카드, 액션 영역 |
| L3 | Floating | white (#ffffff) | shadow.lg | 없음 | 모달, 바텀시트, 오버레이 |
```

### 핵심 규칙: 쉐도우와 보더를 같이 쓰지 않는다
현재 프로젝트에서 이미 이 규칙이 있지만, 실제 프롬프트에서는 `summary-card`에 `stroke 1px + fillColor #fafafa`를 사용하고 있어 쉐도우 없이 보더만 쓰는 "평평한" 카드가 됩니다. **보더를 제거하고 쉐도우로 깊이를 표현**하면 즉시 프리미엄 느낌이 살아납니다.

### 적용 예시: summary-card 개선

**Before (현재):**
```
fillColor: #fafafa (surface)
stroke: 1px #d5d7da (border-default)
shadow: 없음
→ 결과: 평평하고 밋밋한 카드
```

**After (개선):**
```
fillColor: #ffffff (surface-raised)
stroke: 없음
shadow: shadow.sm (2레이어)
cornerRadius: 16px (radius.2xl로 업그레이드)
→ 결과: 부드럽게 떠있는 프리미엄 카드
```

---

## 해결책 3: 프롬프트에 "시각적 연출 지시" 레이어 추가

`05-screen-prompt.md` 커맨드에서 프롬프트를 생성할 때, 구조 지시 뒤에 **비주얼 연출 지시**를 추가합니다.

### 추가할 프롬프트 섹션

```markdown
## 비주얼 연출 (Visual Enhancement)

### 포컬 포인트 (Focal Point)
이 화면에서 시선이 가장 먼저 가야 할 곳:
→ [요소명], 강조 방법: [구체적 시각 처리]

### 시각적 리듬 (Visual Rhythm)
- 콘텐츠 밀도: [dense / balanced / spacious]
- 섹션 간 구분: [shadow 단계 차이 / 배경색 변화 / accent bar / 여백]
- 반복 패턴의 변주: [동일 구조 내 색상·크기 미세 변화]

### 장식 요소 적용
| 요소 | 위치 | 구현 방법 |
|------|------|----------|
| accent-bar | summary-card 좌측 | create_rectangle 4px × FILL, primary color, radius 상좌·하좌만 12px |
| icon-bg | 스텝퍼 마커 | create_rectangle 40×40, fill primary-subtle, cornerRadius 20(원형) |
| gradient-header | 헤더 배경 | 그래디언트 fill (primary 5% → transparent) |
```

### 왜 효과적인가
Medium의 "Prompt Engineering for UI" 연구에 따르면, 프롬프트를 **구조 → 콘텐츠 → 인터랙션 → 폴리싱** 4단계로 나누면 AI 혼란이 줄고 최종 품질이 크게 향상됩니다. 현재 프로젝트는 1~2단계까지만 하고 있어서 3~4단계를 추가하는 것입니다.

---

## 해결책 4: "컬러 악센트 전략" 도입

평범한 디자인의 가장 큰 원인 중 하나는 **컬러 사용이 너무 보수적**인 것입니다.

### 컬러 임팩트 토큰 추가

```markdown
## 컬러 악센트 전략

### Accent Surface (강조 표면)
| 토큰명 | 값 | 용도 |
|--------|-----|------|
| surface-primary-subtle | brand.50 (#f9f5ff) + brand.100 보더 | 선택된 상태, 주요 카드 배경 |
| surface-success-subtle | success.50 (#ecfdf3) | 완료 상태 카드 |
| surface-warning-subtle | warning.50 (#fffaeb) | 주의 필요 카드 |
| surface-accent-gradient | brand.600→brand.400 linear | Hero 카드 상단 배경 |

### 컬러 적용 규칙
1. **단일 화면 내 강조색은 최대 2가지** (primary + 1 상태색)
2. **강조 표면은 화면당 1~2개만** (과하면 강조 효과 소멸)
3. **아이콘에도 컬러를**: 모든 아이콘을 gray로 두지 않고, 주요 아이콘은 primary/accent로
4. **컬러 블록 전략**: 헤더나 CTA 영역은 과감한 컬러 배경 사용 가능
```

---

## 해결책 5: 타이포그래피 대비 강화

현재 타이포 시스템은 정확하지만, 시각적 극적(dramatic) 효과가 부족합니다.

### 개선 전략

```markdown
## 타이포그래피 강화

### 크기 대비 원칙
화면 내 가장 큰 텍스트와 가장 작은 텍스트의 비율이 최소 2:1 이상이어야 합니다.
- 현재: heading 30px / meta 12px = 2.5:1 ✓ (수치는 괜찮음)
- 문제: 실제 화면에서 heading을 거의 안 쓰고 body(16px)~caption(14px)만 사용

### 해결: 화면별 "타이포 히어로" 지정
각 화면 프롬프트에 가장 시각적으로 두드러져야 할 텍스트를 지정:
- 예: G1 홈 → 「진행 요약」 제목을 heading(30px)이 아닌 subheading(20px)으로 쓰되,
  **weight 700 + letter-spacing -0.4px**로 더 임팩트 있게
- 예: 숫자 데이터 → display sm(30px) + weight 700으로 강조

### 텍스트 컬러 대비 강화
| 현재 | 개선 |
|------|------|
| 제목: gray.900 / 본문: gray.900 | 제목: gray.900 bold / 본문: gray.700 regular |
| 보조: gray.500 | 보조: gray.400 (더 연하게 → 주요 텍스트와 대비 증가) |
```

---

## 해결책 6: 패턴 프롬프트에 "비주얼 레시피" 포함

`06-pattern-prompt.md`에서 패턴을 정의할 때, 단순 구조뿐 아니라 **비주얼 처리 레시피**를 포함합니다.

### 패턴 프롬프트 확장 구조

```markdown
## PAT-XXX 비주얼 레시피

### 표면 처리
- 배경: [surface 레벨] + [쉐도우 레벨]
- 특수 처리: [accent bar / gradient / 없음]

### 내부 리듬
- 요소 간 간격 변주: [제목↔본문: 8px / 본문↔메타: 4px / 섹션간: 16px]
  (동일한 12px가 아닌, 콘텐츠 관계에 따른 차등 간격)

### 아이콘 처리
- 스타일: [배경 원형 + 컬러 아이콘 / 아웃라인만 / 솔리드 채움]
- 크기: [상위 텍스트와 시각적 무게 균형]

### 상태 변화 시각화
- default → hover/press: [쉐도우 강화 / 배경색 변화 / 스케일 변화]
- 완료: [체크 오버레이 / opacity 변화 / 컬러 변화]
```

---

## 해결책 7: Audit 커맨드에 "비주얼 품질 체크리스트" 추가

`09-audit.md`에 기능 검증 외에 **시각적 품질 검증** 항목을 추가합니다.

### 추가 검증 항목

```markdown
## 비주얼 품질 감사 (Visual Quality Audit)

### 1. 깊이감 (Depth)
- [ ] 표면 레벨이 최소 2단계 이상 사용되었는가?
- [ ] 주요 카드에 쉐도우가 적용되었는가?
- [ ] 쉐도우 + 보더가 동시 적용된 곳은 없는가?

### 2. 시각적 위계 (Visual Hierarchy)
- [ ] 화면 내 포컬 포인트가 명확한가?
- [ ] 텍스트 크기가 3단계 이상 사용되었는가? (heading/body/caption)
- [ ] 주요 액션 버튼이 시각적으로 가장 두드러지는가?

### 3. 컬러 활용 (Color Usage)
- [ ] gray 외 컬러가 의미 있게 사용되었는가?
- [ ] 강조 표면(accent surface)이 1개 이상 있는가?
- [ ] 아이콘에 컬러가 적용되었는가? (전부 gray가 아닌가?)

### 4. 시각적 리듬 (Visual Rhythm)
- [ ] 모든 간격이 동일하지 않고, 관계에 따라 차등 적용되었는가?
- [ ] 카드 내부 패딩과 외부 간격이 구분되는가?
- [ ] 반복 요소에 시각적 변주가 있는가?

### 5. 장식 요소 (Decorative Elements)
- [ ] accent bar, 아이콘 배경, 그래디언트 중 1개 이상 사용되었는가?
- [ ] 장식 요소가 브랜드 컬러와 일관되는가?
- [ ] 장식 요소가 과하지 않은가? (화면당 2~3개 이내)

### 6. 전체 인상 (Overall Impression)
- [ ] 스크린샷을 5초간 봤을 때 "어디를 봐야 하는지" 즉시 알 수 있는가?
- [ ] 경쟁 앱과 나란히 놓았을 때 시각적으로 뒤지지 않는가?
- [ ] 빈 공간이 "허전함"이 아닌 "여유"로 느껴지는가?
```

---

## 해결책 8: 구체적 Figma MCP 비주얼 레시피

현재 프로젝트에서 **즉시 적용 가능한** Figma MCP 명령 패턴입니다.

### 레시피 1: 카드 좌측 Accent Bar

```
1. create_rectangle
   - name: "accent-bar"
   - width: 4, height: FILL
   - fillColor: primary #7f56d9 (r:0.498, g:0.337, b:0.851)
   - cornerRadius: 상좌 12, 하좌 12, 상우 0, 하우 0

2. 카드 frame의 set_auto_layout
   - layoutMode: HORIZONTAL
   - itemSpacing: 0
   - clipContent: true (accent bar가 카드 radius 안에 클리핑)

→ 효과: 단순한 카드가 즉시 개성 있어지고, 카테고리/상태별 색상 변경으로 확장 가능
```

### 레시피 2: 아이콘 배경 원형 (Icon Background Circle)

```
1. create_frame
   - name: "icon-container"
   - width: 40, height: 40
   - fillColor: primary-subtle #f9f5ff (r:0.976, g:0.961, b:1.0)
   - cornerRadius: 20 (완전한 원)

2. set_auto_layout
   - layoutMode: VERTICAL
   - primaryAxisAlignItems: CENTER
   - counterAxisAlignItems: CENTER

3. clone_node → 아이콘을 icon-container에 insert_child
4. set_fill_color → 아이콘 컬러를 primary #7f56d9

→ 효과: 아이콘이 배경 없이 떠있는 것보다 훨씬 완성도 높아 보임
```

### 레시피 3: Gradient Header Background

```
1. create_rectangle (헤더 frame 안 배경용)
   - name: "header-gradient-bg"
   - width: FILL, height: FILL
   - fill: LINEAR_GRADIENT
     - stops: [{color: {r:0.498,g:0.337,b:0.851,a:0.05}, position:0},
               {color: {r:0.498,g:0.337,b:0.851,a:0}, position:1}]

→ 효과: 헤더 영역이 미세하게 브랜드 컬러를 머금어 특별한 느낌
```

### 레시피 4: 상태별 카드 배경 차별화

```
- 진행 중: fillColor #ffffff, shadow.sm, 좌측 accent-bar primary #7f56d9
- 완료: fillColor #ecfdf3 (success.50), shadow.xs, 좌측 accent-bar success #039855
- 경고: fillColor #fffaeb (warning.50), shadow.xs, 좌측 accent-bar warning #f79009
- 오류: fillColor #fef3f2 (error.50), shadow.xs, 좌측 accent-bar error #d92d20

→ 효과: 동일한 카드 구조지만 상태에 따라 시각적으로 즉시 구분 가능
```

### 레시피 5: 숫자/핵심 데이터 강조 블록

```
1. create_frame
   - name: "stat-block"
   - fillColor: primary-subtle #f9f5ff
   - cornerRadius: radius.xl (12px)
   - padding: 16px

2. create_text (숫자)
   - fontSize: 30 (display sm), fontWeight: 700
   - color: primary #7f56d9

3. create_text (라벨)
   - fontSize: 12 (meta), fontWeight: 400
   - color: text-secondary #717680

→ 효과: 핵심 정보가 시각적으로 "팝"되어 데이터 중심 화면의 완성도 상승
```

---

## 해결책 9: 프롬프트 시스템 개선 — 단계별 적용 가이드

### Phase 1: 즉시 적용 (기존 파일 수정)

**`04-design-system.md` 수정사항:**
- "비주얼 방향성" 섹션 필수 추가 (무드 키워드 3개 + 표면 전략)
- "표면 깊이 시스템" (L0~L3) 필수 정의
- "컬러 악센트 전략" 섹션 추가
- "장식 토큰" (accent-bar, icon-bg, gradient 등) 정의

**`05-screen-prompt.md` 수정사항:**
- "비주얼 연출" 섹션 추가 (포컬 포인트, 시각적 리듬, 장식 요소)
- 각 카드/섹션에 표면 레벨(L0~L3) 명시
- 간격을 일률적이 아닌 콘텐츠 관계 기반 차등으로

**`06-pattern-prompt.md` 수정사항:**
- "비주얼 레시피" 섹션 추가 (표면 처리, 내부 리듬, 아이콘 처리)

**`09-audit.md` 수정사항:**
- "비주얼 품질 감사" 체크리스트 추가

### Phase 2: 디자인 시스템 확장

- foundation `core-visual-tokens.json`에 accent surface 컬러 추가
- 패턴 라이브러리에 장식 패턴(accent-bar 카드, stat-block 등) 추가
- 각 프로젝트 시작 시 "비주얼 레퍼런스 이미지" 수집 단계 추가

### Phase 3: 프로세스 고도화

- 화면별 "비주얼 스코어" 자동 채점 (audit 시)
- A/B 비교: 동일 화면의 기본 버전 vs 강화 버전 생성
- 외부 디자인 레퍼런스 분석 → 자동 비주얼 토큰 추출 파이프라인

---

## 핵심 원칙 요약

| 원칙 | 현재 | 개선 |
|------|------|------|
| 표면 | 모든 카드가 같은 스타일 | 3단계 깊이 시스템 (L0~L3) |
| 컬러 | gray + primary만 사용 | 상태별 subtle 배경 + accent 적극 활용 |
| 장식 | 없음 | accent bar, icon-bg, gradient 헤더 |
| 간격 | 모두 동일 (16px/24px) | 콘텐츠 관계 기반 차등 간격 |
| 타이포 | 크기 차이 적음 | 포컬 포인트에 극적 크기 대비 |
| 위계 | 평평한 구조 | 명확한 시각적 우선순위 |
| 프롬프트 | 구조만 지시 | 구조 + 비주얼 연출 + 폴리싱 |

**한 줄 요약**: 구조(Structure)는 이미 훌륭합니다. 이제 **표면(Surface) + 장식(Decoration) + 위계(Hierarchy)** 세 가지 레이어를 프롬프트 시스템에 추가하면, 동일한 MCP 도구로도 훨씬 세련되고 개성 있는 디자인이 나옵니다.

---

## 참고 리소스

- [NN/g - Prompt to Design Interfaces: Why Vague Prompts Fail](https://www.nngroup.com/articles/vague-prototyping/)
- [Figma Blog - Cooking with Constraints: Designer's Framework for Better AI Prompts](https://www.figma.com/blog/designer-framework-for-better-ai-prompts/)
- [Figma Blog - Design Systems And AI: Why MCP Servers Are The Unlock](https://www.figma.com/blog/design-systems-ai-mcp/)
- [Medium - Prompt Engineering for UI: Figma Make at Scale](https://medium.com/design-bootcamp/prompt-engineering-for-ui-how-i-made-figma-make-generate-real-screens-at-scale-6e997c6b691e)
- [UX Design - How to Prompt Figma Make's AI Better](https://uxdesign.cc/how-to-prompt-figma-makes-ai-better-for-product-design-627daf3f4036)
- [Index.dev - 12 UI/UX Design Trends 2026](https://www.index.dev/blog/ui-ux-design-trends)
- [MockFlow - 18 Common UI Design Mistakes](https://mockflow.com/blog/ui-design-mistakes)
- [Martin Fowler - Design Token-Based UI Architecture](https://martinfowler.com/articles/design-token-based-ui-architecture.html)
