# /pattern-prompt [PAT-ID]

## 목적
`design-system.md`에 확정된 패턴을 바탕으로 **패턴 1개 = 파일 1개** 형태로 Figma 실행 프롬프트를 작성한다.
`PAT-ID`를 지정하면 해당 패턴만, 생략하면 `_index.md`의 모든 패턴을 순서대로 생성한다.
Figma는 건드리지 않는다. 프롬프트 파일만 작성한다.

## 실행 전 읽기 (이 순서로)
1. `projects/{nn}.{project-name}/design-system/patterns/_index.md` — 패턴 목록·ID 확인
2. `projects/{nn}.{project-name}/design-system/design-system.md` — 색상·타이포·간격·**이펙트 토큰**·**타이포 세밀값(행간/자간)** 전체
3. `projects/{nn}.{project-name}/context/foundation/icon-tokens.json` — **아이콘 figmaId 조회**
   패턴 내 아이콘 슬롯마다 맥락에 맞는 아이콘을 찾아 figmaId를 확인한다
4. 해당 패턴의 등장 화면 screen-spec에서 **"패턴 후보" 섹션만** 읽기 (필요 시)

읽기 후 Figma는 실행하지 않는다. 프롬프트 파일만 작성한다.

---

## 파일 구조

패턴별 파일은 `design-system/patterns/` 아래에 독립 파일로 저장한다.

```
design-system/patterns/
├── _index.md                            ← 패턴 목록 + nodeId (빌드 후 기입)
├── PAT-001-{패턴명}-prompt.md
├── PAT-002-{패턴명}-prompt.md
├── PAT-003-{패턴명}-prompt.md
...
```

---

## 패턴 빌드 기준

### 포함 대상
`_index.md`에 등록된 패턴만 생성한다.
새 후보 발견 시: 사용자 확인 → 확정 후 `_index.md` 추가 → 파일 생성.

### 패턴 단위 원칙
- 패턴 1개 = frame 1개 = 파일 1개
- 변형: 색상·텍스트·간격 조정만 허용 → 동일 PAT ID, 변형 상태 표로 정리
- 레이아웃 구조 변경 = 새 PAT ID

### 패턴화 금지 조건
- 2개 미만 화면에서 반복
- 복사 후 텍스트·색상 외 구조 변경 필요
- 화면 전체 단위

---

## 작성 원칙
- 수치는 `design-system.md` 값만. 팔레트 키 + hex + r/g/b/a 함께 표기
- `create_component` 절대 금지. `create_frame`만 사용
- **elevation 필수**: 카드·모달·플로팅은 design-system 이펙트 토큰의 `set_effects` 적용
- **타이포 세밀값 필수**: 모든 텍스트에 `set_line_height` + `set_letter_spacing` 적용 (생략 금지)
- **아이콘 원칙**:
  - 아이콘 슬롯을 빈 placeholder frame으로 두지 않는다
  - `icon-tokens.json`에서 맥락에 맞는 아이콘을 찾아 `figmaId`를 확인한다
    - 상태·피드백 아이콘: `icon.feedback.tokens` (alertCircle, alertTriangle, checkCircle, zap)
    - 일반 UI 아이콘: `icon.baseicon.tokens` (cloud, cloudOff, chevronLeft, clock, check 등)
  - 프롬프트에 아이콘 이름·figmaId를 명시하고 아래 시퀀스로 작성한다:
    ```
    clone_node   → nodeId: "{figmaId}"
    insert_child → parentId: {아이콘 컨테이너 nodeId}
    resize_node  → width: {size}, height: {size}   ← 20 또는 24
    set_fill_color → {맥락 색상 r/g/b/a}
    ```
  - 적합한 아이콘이 없을 때만 빈 frame으로 남기고 이유를 명시한다
- 패턴 간 종속성 없이 각 패턴이 독립 실행 가능하도록 작성

---

## 출력: PAT-{ID}-{패턴명}-prompt.md 1개

```markdown
# PAT-{ID} — {패턴명}

## 메타
- 등장 화면: {화면 ID 목록}
- 구조: (이 패턴이 어디서 어떻게 반복되는지 한 문장)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| {슬롯명} | {icon-tokens.json의 키} | {figmaId} | 20×20 또는 24×24 | {색상 토큰} |

---

## Figma 실행 지시

### 외부 frame
\```
create_frame
  name: "PAT-{ID}-{패턴명}"
  parentId: {부모 프레임 nodeId — 07-build-patterns 설정값}
  x: {nextX}, y: 0
  width: {값}, height: {값}
  fillColor: {팔레트키} — {색상명} (r:{} g:{} b:{} a:1)
\```
\```
set_auto_layout
  layoutMode: HORIZONTAL / VERTICAL
  paddingTop: {값}, paddingBottom: {값}
  paddingLeft: {값}, paddingRight: {값}
  itemSpacing: {값}
  counterAxisAlignItems: CENTER / MIN / MAX
\```

elevation (카드·모달·플로팅인 경우):
\```
set_corner_radius → radius: {값}
set_effects
  effects: [
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:{alpha}}, offset:{x:0,y:{y}}, radius:{r}, spread:{s}, visible:true },
    { type:"DROP_SHADOW", color:{r:0.039,g:0.051,b:0.071,a:{alpha}}, offset:{x:0,y:{y}}, radius:{r}, spread:{s}, visible:true }
  ]
\```
> shadow 토큰 기준: design-system.md 이펙트 토큰 표 참조

---

### {내부 요소명}
\```
create_frame / create_text / create_rectangle
  name: "{이름}"
  parentId: 외부 frame nodeId
  ...
\```

텍스트 노드마다:
\```
set_line_height    → lineHeight: {값}, unit: PIXELS
set_letter_spacing → letterSpacing: {값}, unit: PIXELS
\```

아이콘 노드 ("사용 아이콘" 표 참조):
\```
clone_node   → nodeId: "{figmaId}"             ← icon-tokens.json figmaId
insert_child → parentId: {아이콘 컨테이너 nodeId}
resize_node  → width: {size}, height: {size}
set_fill_color → r:{} g:{} b:{} a:1            ← 맥락 색상 토큰 값
\```

---

## 변형 상태

| 상태명 | 변경 항목 | 값 |
|--------|----------|-----|
| 상태1 | fillColor | {팔레트키} (r:{} g:{} b:{} a:1) |
| 상태2 | fontColor + opacity | {값} |
(레이아웃·구조 변경은 변형 아님 → 새 PAT ID)

---

## 주의
- create_component 금지
- 생성 후 반환된 nodeId를 `_index.md`에 기입
```

저장 위치: `projects/{nn}.{project-name}/design-system/patterns/PAT-{ID}-{패턴명}-prompt.md`

---

## 출력 2: _index.md 업데이트 (신규 패턴 추가 시만)

```markdown
| PAT-{ID} | {이름} | {한 줄 설명} | {화면 ID 목록} | (build 후 기입) |
```

저장 위치: `projects/{nn}.{project-name}/design-system/patterns/_index.md`
