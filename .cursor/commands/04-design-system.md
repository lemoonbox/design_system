# /design-system

## 목적
프로젝트가 제공한 foundation 파일을 읽고, 이 프로젝트에서 실제로 사용할
디자인 시스템을 정의한다. 이후 모든 화면 프롬프트의 색상/타이포/간격 기준이 된다.

> ⚠️ **파운데이션 원칙**
> 모든 색상·타이포·간격·이펙트 값은 반드시 `foundation/core-visual-tokens.json`에서 읽어온 값을 사용한다.
> 이 커맨드가 값을 임의로 생성하거나 예시값을 그대로 쓰는 것은 금지다.
> foundation 파일에 없는 값은 사용자와 협의 후 별도 추가한다.

## 실행 전 읽기
1. `projects/{nn}.{project-name}/context/foundation/core-visual-tokens.json` — 팔레트 전체
2. `projects/{nn}.{project-name}/context/foundation/icon-tokens.json` — 아이콘 카테고리
3. `projects/{nn}.{project-name}/context/service-plan.md` — 서비스 성격, 사용자 맥락
4. `projects/{nn}.{project-name}/context/screen-specs/` — 파일명만 훑기 (어떤 화면들이 있는지 파악)

## 진행 방식
사용자와 함께 결정한다. 시스템이 임의로 선택하지 않는다.
각 항목을 제안하고 사용자 확인 후 확정한다.

---

## Step 1. 색상 역할 배정
foundation 팔레트에서 각 역할에 사용할 색상을 결정한다.

논의 항목:
- 브랜드 컬러 방향 (어느 팔레트를 primary로 쓸 것인가)
- 배경색 / 표면색 (surface, background)
- 텍스트 색상 계층 (primary, secondary, disabled)
- 경계선 / 구분선 색상
- 상태 색상 (success, warning, error)
- 강조색 (accent, 있다면)

## Step 2. 타이포그래피 스케일
foundation의 텍스트 스케일에서 이 프로젝트에서 사용할 것만 선택한다.

논의 항목:
- 화면 제목 (heading)
- 섹션 제목 (subheading)
- 본문 (body)
- 보조 텍스트 (caption)
- 레이블, 버튼 텍스트
- 폰트 패밀리 (있다면)

## Step 3. 간격 & 반경 기준
- 기본 padding 단위 (내부 여백 기준값)
- 섹션 간 spacing 기준값
- 카드/컨테이너 corner radius
- 버튼 corner radius

## Step 3-b. 이펙트 토큰 (elevation & border)
시각적 깊이감을 만드는 값을 결정한다. 이 값은 patterns-prompt와 screen-prompt에서 반드시 참조된다.

**그림자 (shadow)** — 3단계 elevation 기준으로 논의:
- `shadow-sm`: 카드, 입력창 (subtle — offset y:1~2, blur:4, spread:0, alpha:0.06)
- `shadow-md`: 모달, 드롭다운 (mid — offset y:4, blur:12, spread:-2, alpha:0.12)
- `shadow-lg`: 플로팅 버튼, 알림 (strong — offset y:8, blur:24, spread:-4, alpha:0.18)

**테두리 (border)**:
- 기본 테두리 두께 (1px 또는 0px)
- 테두리 색상 역할 (border 토큰 사용)

**타이포그래피 세밀값** (폰트 크기/굵기 외):
- 행간(line-height): heading / body / caption 각각
- 자간(letter-spacing): heading / button / caption 각각

## Step 4. 공통 패턴 목록 결정
screen-specs를 참조하되, **구조(chrome) 요소만** 패턴 후보로 선정한다.

패턴 대상 (일관성 영역):
- 헤더/앱 바, 하단 CTA 바, 상태 배너, 탭/스텝퍼 등 내비게이션
- 2개 이상 화면에서 **동일한 구조와 동일한 역할**로 반복

패턴 비대상 (창의 영역):
- 콘텐츠 카드, 리스트 아이템, 데이터 표시 영역
- 데이터 구조가 같더라도 화면 목적이 다르면 별도 디자인
- "비슷하게 생긴 카드"는 패턴이 아니라 화면별 창의적 결과

> 패턴은 **최소한으로** 유지한다. 패턴이 많을수록 디자인이 획일화된다.
> 사용자에게 "이 요소를 패턴화할까요, 화면별로 자유롭게 디자인할까요?" 질문한다.

---

## 출력 1: design-system.md

> ⚠️ 아래 템플릿의 `{…}` 자리는 반드시 foundation 파일에서 읽은 실제 값으로 채운다.
> 예시값(brand.600, gray.50, 30px 등)을 그대로 복사하지 않는다.

```markdown
# Design System — {서비스명}

## 색상 역할
| 역할 | 팔레트 키 | Hex | 용도 |
|------|----------|-----|------|
| primary | {foundation 팔레트 키} | {hex} | 주요 버튼, 강조 |
| primary-hover | {foundation 팔레트 키} | {hex} | 버튼 hover |
| surface | {foundation 팔레트 키} | {hex} | 카드 배경 |
| background | {foundation 팔레트 키} | {hex} | 페이지 배경 |
| text-primary | {foundation 팔레트 키} | {hex} | 본문 텍스트 |
| text-secondary | {foundation 팔레트 키} | {hex} | 보조 텍스트 |
| text-disabled | {foundation 팔레트 키} | {hex} | 비활성 텍스트 |
| border | {foundation 팔레트 키} | {hex} | 구분선, 테두리 |
| success | {foundation 팔레트 키} | {hex} | 성공 상태 |
| warning | {foundation 팔레트 키} | {hex} | 경고 상태 |
| error | {foundation 팔레트 키} | {hex} | 오류 상태 |

## 타이포그래피
| 역할 | foundation 스케일 | 크기 | 굵기 | 용도 |
|------|-----------------|------|------|------|
| heading | {foundation 스케일 키} | {px} | {weight} | 화면 제목 |
| subheading | {foundation 스케일 키} | {px} | {weight} | 섹션 제목 |
| body | {foundation 스케일 키} | {px} | {weight} | 본문 |
| caption | {foundation 스케일 키} | {px} | {weight} | 보조, 메타 |
| label | {foundation 스케일 키} | {px} | {weight} | 폼 레이블 |
| button | {foundation 스케일 키} | {px} | {weight} | 버튼 텍스트 |

## 간격 & 반경
- 기본 내부 padding: {spacing값} ({px})
- 섹션 간 gap: {spacing값} ({px})
- 카드 radius: {radius값} ({px})
- 버튼 radius: {radius값} ({px})

## 이펙트 토큰
| 이름 | type | offset | blur | spread | color | alpha | 용도 |
|------|------|--------|------|--------|-------|-------|------|
| shadow-sm | DROP_SHADOW | x:0 y:1 | 4 | 0 | #000 | 0.06 | 카드, 입력창 |
| shadow-md | DROP_SHADOW | x:0 y:4 | 12 | -2 | #000 | 0.12 | 모달, 드롭다운 |
| shadow-lg | DROP_SHADOW | x:0 y:8 | 24 | -4 | #000 | 0.18 | 플로팅 요소, 알림 |

## 타이포그래피 세밀값
| 역할 | line-height | letter-spacing |
|------|------------|----------------|
| heading | {값px 또는 %} | {값px 또는 %} |
| body | {값px 또는 %} | {값px 또는 %} |
| caption | {값px 또는 %} | {값px 또는 %} |
| button | {값px 또는 %} | {값px 또는 %} |

## 테두리
- 기본 두께: {0 또는 1px}
- 색상: border 토큰 (#{hex})

## 아이콘
- 기본 크기: {sm/md/lg}
- 주요 사용 카테고리: baseicon, feedback

## 공통 패턴 목록
| ID | 패턴명 | 설명 | 등장 화면 |
|----|--------|------|----------|
| PAT-001 | ... | ... | G1, L1 |
```

## 출력 2: patterns/_index.md

```markdown
# 패턴 인덱스

| ID | 이름 | 설명 | 사용 화면 | Figma 노드 ID |
|----|------|------|----------|--------------|
| PAT-001 | ... | ... | G1, L1 | (build 후 기입) |
```

저장 위치:
- `projects/{nn}.{project-name}/design-system/design-system.md`
- `projects/{nn}.{project-name}/design-system/patterns/_index.md`

---

## 다음 단계
`design-system.md` 저장 완료 후 아래 안내를 출력한다:

```
✅ design-system.md 저장 완료.

다음 단계: /visual-direction 을 실행하세요.
이 프로젝트의 비주얼 방향(톤, 레이아웃 스타일, 강조 방식 등)을 정의합니다.
/visual-direction 을 실행하기 전까지 05~09 커맨드는 비주얼 기준 없이 진행됩니다.
```
