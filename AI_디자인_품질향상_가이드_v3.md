# AI 디자인 품질 향상 가이드 v3
> **Figma MCP 자동 디자인 시스템 — "허한 느낌" 탈출 완전 가이드**
> Chrome 직접 리서치 기반: NN/g · Sergei Chyrkov · UI Collective · 레이지코딩 · 피튜브 · 빌더 조쉬 수파노바

---

## 핵심 진단: 왜 AI 디자인은 허해 보이는가?

> **"AI 디자인이 구린 이유는 단 하나 — 기준이 없기 때문이다."**
> — 레이지코딩, "AI 냄새 안 나게 디자인 하는 방법" (2026.02)

AI는 무엇을 만들지(What)는 알지만 어떻게 느껴야 하는지(How it feels)는 모른다. 색상, 폰트, 버튼, 간격의 **기준(=디자인 시스템)** 을 명시적으로 제공하지 않으면 AI는 매번 다른 결정을 내린다. 그 결과가 "Frankenstein Layout" — 각 요소는 맞는데 전체가 어색한 화면이다.

이 가이드는 **현재 프로젝트의 `.cursor/commands/` 시스템에 직접 적용**할 수 있는 6가지 솔루션을 제공한다.

---

## 솔루션 1: 디자인 방향성(Visual Direction) 선언 — 04-design-system.md 개선

### 문제
현재 `04-design-system.md`는 색상 Hex와 px 수치만 있다. AI는 이 값들이 *왜* 존재하고 *어떤 분위기*를 내야 하는지 모른다.

### 해결: Visual Direction 섹션 추가

```markdown
## Visual Direction (브랜드 방향성)

**무드**: Professional Emergency · Calm Authority · Field-Ready
**키워드**: 신뢰감, 명료함, 현장 가독성, 절제된 긴장감
**금지**: 과도한 장식, 지나친 그라디언트, 소비자 앱 같은 발랄함

### 색상 사용 철학
- primary(#7f56d9 violet) = 선택·진행·주요 액션 — 화면당 1~2곳만
- surface-raised(#ffffff) = 카드·모달 — 항상 shadow.sm 적용 (border만 쓰지 말 것)
- background(#fdfdfd) = 페이지 배경 — 카드와 미세 대비 유지
- success/warning/error = 아이콘+문구 항상 병행 (색만으로 상태 표현 금지)

### 타이포그래피 철학
- 화면 내 텍스트 크기는 최대 3단계 (heading/body/caption)
- 같은 위계 내에서는 bold 대신 color로 강조
- 14px(caption) 이하는 보조 정보만 — 주요 정보는 최소 16px

### 컴포넌트 개성 포인트
- 카드: white + shadow.sm (테두리 없음) — 깊이감으로 구분
- 버튼: radius.md(8px) + 충분한 패딩(상하 12~16px) — 터치 타깃 확보
- 상태 배지: 아이콘 + 색 + 텍스트 3요소 항상 함께
```

---

## 솔루션 2: Surface Depth 시스템 — 카드가 허한 이유

### 문제 (현재 프로젝트의 실제 버그)

`G1-구급-홈-prompt.md`의 `summary-card`:
```
fillColor: #fafafa + stroke 1px gray.300
```
→ **결과**: 배경과 거의 같은 색 + 얇은 선 = 존재감 없는 카드

### 해결: Surface Depth 4단계

| 레이어 | 배경 | 효과 | 용도 |
|--------|------|------|------|
| L0 배경 | `color.gray.25` #fdfdfd | 없음 | 페이지 |
| L1 카드 | `color.white` #ffffff | `shadow.sm` | 모든 카드 |
| L2 입력/배지 | `color.gray.50` #fafafa | `border 1px gray.200` | 입력 필드, 상태칩 |
| L3 호버/선택 | `color.brand.50` #f9f5ff | `border 1px brand.300` | 선택 상태 |

### Figma MCP 적용 코드

```python
# summary-card를 L1 카드로 수정
set_fill_color(nodeId="summary-card", r=1.0, g=1.0, b=1.0)  # #ffffff
set_effects(nodeId="summary-card", effects=[
  {"type": "DROP_SHADOW", "color": {"r":0.039,"g":0.051,"b":0.071,"a":0.059},
   "offset": {"x":0,"y":1}, "radius":2, "spread":0, "visible":True},
  {"type": "DROP_SHADOW", "color": {"r":0.039,"g":0.051,"b":0.071,"a":0.102},
   "offset": {"x":0,"y":1}, "radius":3, "spread":0, "visible":True}
])
# stroke 제거 (white 카드는 테두리 불필요)
set_stroke_weight(nodeId="summary-card", weight=0)
```

---

## 솔루션 3: 레퍼런스 기반 워크플로 — 첫번째 방법 (레이지코딩 검증)

### 원리
말보다 이미지. AI는 스크린샷으로 디자인 기준을 파악할 때 훨씬 정확하다.

### 워크플로

1. **레퍼런스 수집**: Mobbin(해외) 또는 GD(국내)에서 목표 품질 앱 스크린샷 5~10장
2. **분석 요청**:
   ```
   첨부한 이미지들의 디자인 기준을 분석하고
   design-analysis.md 파일로 정리해 줘.
   (레이아웃 패턴, 타이포그래피 스케일, 색상 역할, 간격 패턴, 컴포넌트 스타일)
   ```
3. **화면 생성**: design-analysis.md를 컨텍스트로 유지한 채 작업
4. **일관성 체크**: 새 섹션 추가 시 "지금까지의 기준과 어울리는지 분석 후 작업"

### 현재 프로젝트 적용 — 05-screen-prompt.md에 추가

```markdown
## 레퍼런스 분석 섹션 (화면 프롬프트 시작 전)

사전 작업:
1. `design-system.md` 읽기
2. 유사 의료/현장 앱 레퍼런스 1~3장 분석
3. 분석 결과를 바탕으로 `visual-direction.md` 확인/보완
4. 이후 화면 구현 시 이 기준만 사용
```

---

## 솔루션 4: CLAUDE.md 디자인 규칙 — 피튜브 검증

### 원리 (피튜브: "클로드 코드+피그마로 일관된 디자인")

> "CLAUDE.md에 규칙을 명시하고, 하드코딩하지 말고 토큰/컴포넌트에 없는 요소가 있으면 **무조건 물어보고 진행**하라고 명시하라."

### 현재 프로젝트에 추가할 CLAUDE.md 규칙

```markdown
# 디자인 시스템 규칙 (AI 필독)

## 절대 규칙
1. 색상은 반드시 design-system.md의 팔레트 키 사용 (Hex 직접 입력 금지)
2. 간격은 spacing 토큰만 사용 (px 직접 입력 금지)
3. 그림자는 shadow 토큰만 사용 (직접 수치 입력 금지)
4. 카드는 반드시 white + shadow.sm (gray.50 + border 조합 사용 금지)
5. 디자인 시스템에 없는 새 컴포넌트가 필요하면 반드시 먼저 물어볼 것

## 화면당 시각적 계층
- Dominant(1개): 주요 CTA 또는 핵심 정보 — primary color 사용
- Sub-dominant(2~3개): 보조 액션 또는 섹션 제목
- Subordinate(나머지): 보조 텍스트, 메타 정보

## 금지 패턴
- 같은 화면에 진한 색 배경 섹션 2개 이상
- 텍스트 크기 4단계 이상 혼용
- 버튼 스타일 3종 이상 혼용
- border만으로 카드 구분 (항상 shadow 또는 배경색 차이 사용)
```

---

## 솔루션 5: 디자인 키트 / 스킬 활용 — 두번째 방법 (레이지코딩 + 빌더 조쉬 검증)

### 원리
개인이 만든 디자인보다 수년간 검증된 디자인 키트가 AI에게 더 강력한 기준이 된다.

### 선택지별 적용

#### A. shadcn/ui (웹 개발 기반 프로젝트)
```
전체 디자인을 shadcn/ui 컴포넌트 기반으로 재구성해 줘.
단, 색상은 우리 design-system.md의 primary(#7f56d9)를 유지할 것.
```

#### B. 수파노바 디자인 스킬 (빌더 조쉬 추천, GitHub: uxjoseph/supanova-design-skill)
- Claude Code 스킬로 설치
- 레퍼런스 기반 + 템플릿 코드 결합 방식
- 추상 애니메이션 요소로 시각적 개성 추가 가능

#### C. Figma 커뮤니티 소스 (피그마 MCP 기반 프로젝트 — 현재 프로젝트 해당)
```
Figma 커뮤니티에서 "medical app design system" 검색
→ 라이센스 확인 후 토큰/컴포넌트 추출
→ 우리 design-system.md 토큰과 매핑
```

### 현재 프로젝트 권장 접근
현재 프로젝트는 **Figma MCP 직접 조작** 방식이므로:
1. `design-system.md`의 토큰 정의 강화 (용도 설명 추가)
2. `07-build-patterns.md`에서 패턴 빌드 시 shadow.sm 기본 적용 규칙 추가
3. PAT-001~005 각각에 "Visual Recipe" 섹션 추가 (아래 솔루션 6 참고)

---

## 솔루션 6: Visual Recipe — 각 패턴에 시각적 레시피 추가

### 원리 (NN/g + Sergei Chyrkov 검증)

AI는 구조적 지시는 잘 따르지만 시각적 완성도 지시는 놓친다. 각 패턴 프롬프트에 **시각적 레시피** 섹션을 추가하면 AI가 의도한 시각적 결과를 만든다.

### 06-pattern-prompt.md 개선 — Visual Recipe 섹션 추가

```markdown
## Visual Recipe (각 PAT 파일에 추가)

### PAT-001 케이스·동기화 헤더
- 배경: white + shadow.xs (subtle 구분)
- 케이스 식별자: body 16px bold + text-primary
- 시각적 무게 중심: 동기화 상태 배지 (아이콘+색+텍스트)
- 액센트 포인트: 동기화 성공 시 success dot (#039855) 좌측 배치

### PAT-002 동기화 배너
- 배경: error-subtle(#fef3f2) + border-left 3px error(#d92d20)
- 핵심: 얇은 테두리보다 왼쪽 컬러 바가 시선을 더 끔
- 텍스트: caption 14px regular + 짧은 한 줄 메시지

### PAT-003 업무 단계 스텝퍼
- 완료 단계: 마커 success 채움 + 아이콘 white
- 현재 단계: 마커 brand 테두리 2px + 아이콘 brand color + 라벨 bold
- 미시작 단계: 마커 gray.200 테두리 + 아이콘 gray.400 + 라벨 gray.500
- 연결선: gray.200 1px — 완료 구간은 success.600으로 채움

### PAT-004 하단 고정 CTA 바
- 배경: white + shadow.md (상단으로 올라오는 느낌)
- 버튼: FILL width + primary(#7f56d9) + text-on-primary(#ffffff)
- 안전 영역: paddingBottom = 34px (노치 기기 대응)
- 인터랙션: pressed 시 primary-pressed(#6941c6)

### summary-card (G1 전용)
- 배경: white + shadow.sm (gray.50+border 절대 금지)
- pre-KTAS 칩: primary-subtle(#f9f5ff) + border-focus(#7f56d9) 1px + label 14px medium
- 진행 요약 제목: subheading 20px semibold text-primary
- 이송 상태 링크: accent(#1570ef) underline — body와 명확히 구분
```

---

## 솔루션 7: 히어로 섹션 교체 꿀팁 (레이지코딩 · 숨겨진 꿀팁)

전체 화면이 완성된 후 허한 느낌이 남을 때:

### 프로세스
1. **Mobbin 또는 GD**에서 유사 분위기 스크린샷 캡처
2. AI에게 먼저 물어봄:
   ```
   이 스크린샷이 현재 우리 디자인 기준(첨부: design-system.md)과
   어울리는지 분석해 줘. 색상, 타이포, 간격 측면에서.
   ```
3. "어울린다" 답변 받은 후:
   ```
   기존 버튼/폰트/컴포넌트 기준을 유지하면서
   이 섹션만 이미지 스타일로 재작업해 줘.
   ```
4. **주의**: 레퍼런스를 무작정 적용하면 기준이 흔들림 — 반드시 2번 단계 거칠 것

---

## 솔루션 8: 4단계 프롬프트 체이닝 — 05-screen-prompt.md 구조 개선

### 현재 문제
프롬프트가 구조 → 콘텐츠 → 끝. Visual Polish 단계 없음.

### 개선된 4단계 구조

```markdown
## Phase 1: 구조 (Structure)
create_frame / set_auto_layout — 레이아웃만, 색상 없음

## Phase 2: 콘텐츠 (Content)
clone_node(PAT 적용) / set_text_content — 데이터 매핑

## Phase 3: 시각 품질 (Visual Polish) ← 현재 빠진 단계
- 카드에 shadow.sm 적용 확인
- 타이포그래피 계층 3단계 확인 (heading/body/caption)
- primary color 사용 빈도 확인 (화면당 1~2곳)
- 여백 일관성 확인 (spacing 토큰 준수)
- focal point 1개 명확한지 확인

## Phase 4: 검증 (Consistency Check)
- export_node_as_image → 시각 확인
- design-system.md 대비 토큰 준수 여부 체크
- 이전 화면과의 일관성 확인
```

---

## 솔루션 9: 09-audit.md 시각 품질 감사 추가

### 현재 문제
감사 항목이 기능/구조 중심. 시각 품질 체크 없음.

### 추가할 Visual Quality Audit

```markdown
## Visual Quality Audit (09-audit.md 추가)

### 깊이감 (Depth)
- [ ] 모든 카드가 white + shadow 사용 (gray.50+border 없음)
- [ ] 배경(#fdfdfd) vs 카드(#ffffff) 대비 명확
- [ ] 하단 CTA 바에 shadow.md 적용

### 시각적 계층 (Hierarchy)
- [ ] 화면당 focal point 1개 명확
- [ ] 텍스트 계층 3단계 이하 (heading/body/caption)
- [ ] primary color 화면당 1~2곳 이하

### 색상 일관성 (Color)
- [ ] 상태 표현 시 아이콘+색+텍스트 3요소 병행
- [ ] 모든 색상이 design-system.md 팔레트 키 사용
- [ ] 링크/강조는 accent(#1570ef) 또는 primary(#7f56d9) 둘 중 하나만

### 리듬감 (Rhythm)
- [ ] 섹션 간격 spacing.3xl(24px) 일관 적용
- [ ] 카드 내부 padding spacing.xl(16px) 일관 적용
- [ ] 버튼 상하 padding 최소 spacing.lg(12px)

### 완성도 포인트 (Polish)
- [ ] pre-KTAS 칩: primary-subtle 배경 + border-focus 테두리
- [ ] 스텝퍼 현재 단계: 마커 테두리 bold + 라벨 semibold
- [ ] 동기화 배너: 왼쪽 컬러 바 강조
```

---

## 피그마 MCP 특화 팁 — Figma DevMode MCP vs Talk-to-Figma MCP

피튜브 영상에서 확인된 실전 구분법:

| | DevMode MCP | Talk-to-Figma MCP |
|--|-------------|-------------------|
| 강점 | 디자인→코드 추출, 변수/토큰 읽기 | 피그마 파일 내 요소 수정, 주석, 인스턴스 교체 |
| 용도 | 현재 프로젝트처럼 코드로 디자인 시스템 추출 | 이미 만든 피그마 파일 수정 자동화 |
| 한계 | 직접 수정 불가 | 변수 읽기 정확도 낮음 |

→ **현재 프로젝트**: DevMode MCP로 토큰/컴포넌트 추출 → Claude Code에서 Figma MCP로 조작

---

## 즉시 적용 우선순위

### 🔴 즉시 (가장 효과 큼)
1. `summary-card` → `white + shadow.sm` 변경 (gray.50+border 제거)
2. `design-system.md`에 Visual Direction 섹션 추가
3. `CLAUDE.md` (또는 각 커맨드 파일) 에 디자인 규칙 추가

### 🟡 이번 스프린트
4. 각 PAT 프롬프트 파일에 Visual Recipe 섹션 추가
5. `05-screen-prompt.md`에 Phase 3 (Visual Polish) 추가
6. `09-audit.md`에 Visual Quality Audit 체크리스트 추가

### 🟢 다음 단계
7. Figma 커뮤니티에서 의료 앱 디자인 시스템 레퍼런스 수집
8. Mobbin에서 현장 업무 앱 스크린샷 수집 → design-analysis.md 작성
9. 수파노바 디자인 스킬 검토 (웹 출력 필요 시)

---

## 핵심 요약

> AI 디자인의 핵심 문제는 **기준 부재**다.
> 해결은 단 하나: **AI에게 명확한 기준을 먼저 심어라.**

기준을 심는 3가지 방법:
1. **명문화**: design-system.md + CLAUDE.md에 규칙 명시 (what, why, how)
2. **시각화**: 레퍼런스 스크린샷 제공 → AI가 분석 → design-analysis.md 생성
3. **구조화**: 화면 프롬프트에 Visual Polish 단계 추가 → 감사 단계에서 확인

이 세 가지가 갖춰지면 AI는 허한 디자인이 아니라, 디자이너가 의도한 품질의 화면을 일관되게 만들어낼 수 있다.

---

*리서치 출처: NN/g "5 Ways to Make AI-Generated UIs Not Look AI-Generated" · Sergei Chyrkov Blog · UI Collective YouTube · 레이지코딩 "AI 냄새 안 나게 디자인 하는 방법" · 피튜브 "클로드 코드+피그마로 일관된 디자인 하는 방법" · 빌더 조쉬 "수파노바 디자인 스킬" · 2026.03 기준*
