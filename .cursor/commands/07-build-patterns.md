# /build-patterns [PAT-ID]

## 인수
- `[PAT-ID]` 생략 시: `_index.md` 전체 패턴을 순서대로 생성
- `[PAT-ID]` 지정 시: 해당 패턴 1개만 생성 (PAT-001, pat001, pat01 → PAT-001로 정규화)

## 목적
패턴 **디자인 명세서**(patterns/PAT-*-prompt.md)를 읽고 Figma에 패턴 frame을 생성한다.
**명세서에는 MCP 명령이 없다.** agent가 디자인 의도를 해석하고 `figma-tools.md`를 참조하여 실행 계획을 스스로 수립한다.

## 실행 전 읽기
0. `.cursor/context/figma-project-config.md` — 프로젝트 설정 확인 (채널명, 부모 프레임 nodeId)
1. `{프로젝트}/design-system/patterns/_index.md` — 대상 패턴 확인
2. 대상 패턴의 `PAT-{ID}-{패턴명}-prompt.md` — **디자인 명세** (핵심 입력)
3. `{프로젝트}/design-system/design-system.md` — 이펙트 토큰(shadow) 구체 값, 타이포 세밀값 확인
4. `{프로젝트}/design-system/visual-direction.mdc` — 시각적 판단 기준
5. `.cursor/context/figma-tools.md` — **사용 가능한 MCP 도구, 파라미터, 제약 사항, 실행 패턴**

---

## 핵심 원칙: 디자인 명세 → 빌드 계획

패턴 디자인 명세는 **디자인 의도와 토큰 값**으로 작성되어 있다. MCP 명령은 없다.
agent는 다음 순서로 실행 계획을 수립한다:

### 1단계: 시각적 의도 파악
명세의 "시각적 의도" 섹션을 읽고 **완성된 결과물의 모습**을 머릿속에 그린다.
- 어디에 시선이 먼저 가는가?
- 요소 간 시각적 무게 비율은?
- 이 패턴을 "잘 만들었다"고 느끼게 하는 포인트는?

### 2단계: 레이아웃 분석
명세의 "레이아웃 구조" 섹션에서 frame 계층을 도출한다:
- 표의 "배치" → auto-layout 방향 (수직=VERTICAL, 수평=HORIZONTAL)
- 표의 "주축 정렬" → primaryAxisAlignItems 값
- 표의 "교차축 정렬" → counterAxisAlignItems 값
- 표의 "내부 여백" → padding 값
- 표의 "요소 간격" → itemSpacing 값
- 표의 "깊이" → shadow 토큰 → `design-system.md` 이펙트 토큰 표에서 구체 값 확인

### 3단계: 토큰 매핑
각 요소의 색상·타이포·간격·깊이를 design-system.md 토큰으로 확인한다:
- 색상: 명세의 "(rgba)" → `set_fill_color`/`set_stroke_color` 파라미터
- 타이포: 명세의 "{크기}/{행간}/{자간} {굵기}" → `create_text` + `set_font_name` + `set_line_height` + `set_letter_spacing`
- shadow: 명세의 "shadow.sm" 등 → `design-system.md` 이펙트 토큰 표에서 `set_effects` 파라미터 구성

### 4단계: MCP 도구 선택
`figma-tools.md`에서 적합한 도구를 매칭한다. 반드시 확인할 섹션:
- **생성 도구** — create_frame, create_text 파라미터
- **수정 도구** — set_fill_color, set_auto_layout, set_effects 파라미터
- **텍스트 스타일** — set_font_name, set_line_height, set_letter_spacing
- **MCP 미지원 항목** — STRETCH/fill/hug/transparent 등 대체 방법
- **실행 계획 패턴** — 아이콘 복제, 카드 elevation 등 참고 시퀀스

---

## 실행 흐름

### Step 1. 사전 확인

```
join_channel → channel: "{채널명}"
get_node_info → nodeId: "{부모 프레임 nodeId}"
```

- 프레임 존재 여부 확인
- children에서 nextX 계산: `max(child.x + child.width) + 40` (children 없으면 0)
- 오류 시 즉시 중단, 사용자에게 nodeId 재확인 요청

### Step 2. 빌드 계획 수립

디자인 명세를 해석하고 **실행 전에** 아래 형식으로 계획을 정리한다:

```
빌드 계획 — PAT-{ID} {패턴명}

1. 외부 frame "{패턴명}" — {크기}, {배경}, {배치}
2. 하위 frame "{영역명}" — {크기}, {배경}, {배치}
3. 텍스트 "{요소명}" — {타이포 역할}, {색상}
4. 아이콘 "{아이콘명}" — figmaId:{id}, {크기}, {색상}
5. elevation — {대상}, {shadow 토큰}
6. 시각 검증
```

### Step 3. 실행

계획 순서대로 MCP 도구를 호출한다. 기본 순서:
외부 frame 생성 → auto-layout → 하위 frame → 텍스트 → 아이콘 → elevation → 검증

#### 투명 fill 처리
- `create_frame(fillColor: {r:0, g:0, b:0, a:0})` 직후 **무조건** `set_fill_color r:0 g:0 b:0 a:0` 재적용
- `get_node_info`로 fill 확인하는 중간 단계 생략 (무조건 재적용이 더 빠르고 안전)

#### 텍스트 생성 (모든 텍스트 노드에 필수)
1. `create_text` — fontSize, fontWeight, fontColor 지정
2. `set_font_name` — fontFamily + style (400→Regular, 500→Medium, 600→SemiBold, 700→Bold)
3. `set_line_height` — 명세의 행간 값 (unit: PIXELS)
4. `set_letter_spacing` — 명세의 자간 값 (unit: PIXELS)

> set_font_name, set_line_height, set_letter_spacing 중 하나라도 빠지면 타이포가 어긋난다. 절대 생략하지 않는다.

#### 아이콘 배치
1. `get_node_info` → figmaId 원본 구조 확인 (COMPONENT / INSTANCE / VECTOR / GROUP / FRAME)
2. `clone_node` → nodeId: {figmaId}, x:0, y:0 (원본 근처 절대 좌표에 복제됨)
3. `insert_child` → parentId: {아이콘 컨테이너 nodeId}, childId: {clonedId}
4. `move_node` → nodeId: {clonedId}, x:0, y:0 (**필수** — 생략 시 원본 위치에 남아 컨테이너 밖에 렌더)
5. `resize_node` → 명세 크기 적용
6. 색상 적용 — **원본 구조에 따라 방법이 다르다**:
   - **단일 VECTOR 노드**: `set_fill_color` 직접 적용
   - **GROUP / FRAME (다층 path)**: `get_node_info`로 children 탐색 → 각 child vector에 `set_fill_color` 개별 적용
   - **COMPONENT / INSTANCE**: 색상 변경이 제한될 수 있음. `flatten_node` 후 `set_fill_color` 시도
   - **색상 적용 실패 시**: 원본 색상 유지하고 보고
7. `get_node_info` → 아이콘 컨테이너에서 위치·크기 검증

#### Elevation (shadow) 적용
디자인 명세의 "Elevation" 검증 표에 shadow 토큰이 명시된 요소에 적용한다.
`design-system.md`의 이펙트 토큰 표에서 구체적인 `set_effects` 파라미터를 확인한다.

#### MCP 미지원 값 변환 (`figma-tools.md` 참조)
- "양끝 정렬" → `primaryAxisAlignItems: SPACE_BETWEEN`
- 투명 배경 → `fillColor: {r:0, g:0, b:0, a:0}` (문자열 "transparent" 금지)
- 부모 폭 채움 → 부모 width − paddingLeft − paddingRight 계산하여 숫자 입력
- `counterAxisAlignItems: STRETCH` 미지원 → `MIN` + 자식에 `resize_node`

### Step 4. 검증 (선별적)

#### 4-a. 구조 검증 [선택]
조건: 복잡한 레이아웃(3개 이상 영역) 또는 새로운 구조
실행: export_node_as_image → 배치, 계층 확인
체크:
- [ ] 전체 레이아웃이 명세 다이어그램과 일치?
- [ ] 요소 배치 순서가 맞는가?
- [ ] 여백이 극단적이지 않은가?

#### 4-b. 스타일 검증 [선택]
조건: 색상/shadow 여러 개 적용 또는 변경 많은 경우
실행: export_node_as_image → 색상 톤, 깊이감 확인
체크:
- [ ] 배경색이 명세 토큰과 일치?
- [ ] 텍스트 색상이 올바른 역할?
- [ ] shadow 적용 여부 (필요한 경우)?

#### 4-c. 최종 검증 [필수]
조건: 모든 경우
실행: export_node_as_image → 전체 시각 확인
체크:
- [ ] Visual Recipe 시각적 의도와 일치?
- [ ] 색상 톤: 설계된 분위기가 나는가?
- [ ] 초점(focal point) 명확한가?
- [ ] 완성되었다는 느낌이 드는가?

## 검증 생략 규칙

다음 경우 구조/스타일 검증 스킵 가능:
- 1줄 텍스트 + 아이콘 같은 극도로 단순한 경우
- 이미 검증된 패턴의 색상/텍스트만 변경
- 명세가 매우 상세한 경우 (레이아웃 동일)

최종 검증은 항상 필수.

### Step 5. _index.md 노드 ID 기록

생성된 패턴의 nodeId를 `_index.md`의 "Figma 노드 ID" 열에 기입한다.

### Step 6. 화면 프롬프트 업데이트

`_index.md`의 "사용 화면" 열을 기준으로 `prompt/*-prompt.md`의 패턴 노드 ID를 실제 값으로 채운다.

---

## 실행 규칙
- `create_component` 절대 금지. `create_frame`만 사용
- 패턴 간 x축 40px 이상 간격
- x, y는 부모 프레임 내부 좌표 기준 (캔버스 절대 좌표 아님)
- 디자인 명세에 없는 시각적 선택이 필요하면 임의 결정하지 않고 사용자에게 확인

---

## 완료 보고
```
완료: 패턴 {n}개 생성

| PAT ID | 패턴명 | 노드 ID |
|--------|--------|--------|
| PAT-001 | ... | ... |

업데이트된 화면 프롬프트: {screen-id 목록}
시각 검증: {통과 / 수정 사항}
이슈: {있다면 구체적으로}
```

## 실패 시
- 오류 내용을 그대로 보고한다
- 부분 완료된 PAT ID와 nodeId를 명시한다
- 재시도는 1회. 동일 오류 반복 시 중단하고 보고한다
- 롤백(delete_node) 필요 시 사용자 확인 후 실행한다
