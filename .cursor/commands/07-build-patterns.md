# /build-patterns

## ⚙️ 프로젝트 설정 (실행 전 여기를 먼저 채운다)

```
채널명:        ysm85zx5
부모 프레임 nodeId:  42-4415
```

> 채널명과 nodeId는 프로젝트마다 다르다. 실행 전 반드시 확인하고 위 값을 수정한다.

---

## 목적
`patterns/patterns-prompt.md`를 읽고 위에서 지정한 부모 프레임 하위에 패턴 frame을 생성한다.
생성된 nodeId를 `patterns/_index.md`에 기록하고,
해당 패턴을 사용하는 모든 화면 프롬프트(`prompt/*-prompt.md`)의 노드 ID를 실제 값으로 업데이트한다.

## 실행 전 읽기
1. `projects/{nn}.{project-name}/design-system/patterns/patterns-prompt.md` — 실행 지시 전체
2. `projects/{nn}.{project-name}/design-system/patterns/_index.md` — 현재 패턴 목록
3. `.cursor/context/figma-tools.md` — 필요한 도구 확인

design-system, screen-spec은 이미 patterns-prompt.md에 반영되어 있으므로 재읽기 금지.

---

## 실행 원칙
- 모든 패턴은 **frame으로만 생성한다** (`create_frame` 사용, `create_component` 절대 금지)
- 부모 프레임 하위에 모아서 생성한다. 페이지 생성/전환 금지
- 각 패턴 frame 생성 직후 반환된 nodeId를 반드시 기록한다
- 패턴 간 간격: x축 40px 이상 떨어뜨려 배치한다
- x, y는 **부모 프레임 내부 좌표** 기준이다. 캔버스 절대 좌표로 지정하지 않는다
- 수치는 patterns-prompt.md에 명시된 값만 사용한다

---

## 실행 흐름

### Step 1. 사전 확인
이 파일 상단 **⚙️ 프로젝트 설정**의 값을 사용한다.

```
join_channel → channel: "{채널명}"
get_node_info → nodeId: "{부모 프레임 nodeId}"
```

응답에서 다음 두 가지를 확인한다:
1. 프레임이 존재하는지
2. **기존 children의 배치 현황** — children 배열에서 각 child의 x, width를 읽어 현재 가장 오른쪽 끝 x 좌표(`nextX`)를 계산한다

```
nextX = max(child.x + child.width) + 40   // 기존 child가 없으면 nextX = 0
```

> ⚠️ 프레임이 존재하지 않거나 오류가 나면 즉시 중단하고 사용자에게 nodeId 재확인을 요청한다.
> 페이지를 새로 생성하거나 `set_current_page`를 호출하지 않는다.

### Step 2. 패턴 순서대로 실행
`patterns-prompt.md`의 PAT-001부터 순서대로 실행한다.

각 패턴마다:
```
create_frame
  → name: "PAT-XXX-{패턴명}"
  → parentId: {부모 프레임 nodeId}  ← 반드시 지정
  → x: {nextX}, y: 0               ← 부모 내부 좌표 기준
set_auto_layout → 레이아웃 설정
(내부 요소 생성 — create_frame / create_text / create_rectangle 등)
get_node_info → 생성 결과 확인 + nodeId, width 메모
```

패턴 배치 — 생성할 때마다 nextX를 갱신한다:
```
nextX = nextX + (생성된 패턴 width) + 40
```
다음 패턴은 갱신된 nextX에 배치한다.

### Step 3. _index.md 노드 ID 기록
모든 패턴 생성 완료 후 `design-system/patterns/_index.md`의 "Figma 노드 ID" 열을 실제 nodeId로 채운다.

```markdown
| PAT-001 | top-bar | 상단 내비게이션 바 | G1, G2, L1 | 1234:5678 |
| PAT-002 | cta-button | 주요 행동 버튼 | G1, L1, L2 | 1234:5690 |
```

### Step 4. 화면 프롬프트 업데이트
`_index.md`의 "사용 화면" 열을 기준으로
각 화면의 `prompt/{screen-id}-*-prompt.md`를 열어
"사용 패턴" 표의 "Figma 노드 ID" 열을 실제 nodeId로 채운다.

업데이트 전:
```markdown
| PAT-001 | top-bar | 화면 상단 | (노드ID) |
```

업데이트 후:
```markdown
| PAT-001 | top-bar | 화면 상단 | 1234:5678 |
```

---

## 완료 보고
```
완료: 패턴 {n}개 생성

| PAT ID | 패턴명 | 노드 ID |
|--------|--------|--------|
| PAT-001 | ... | ... |

업데이트된 화면 프롬프트: {screen-id 목록}
이슈: {있다면 구체적으로}
```

## 실패 시
- 오류 내용을 그대로 보고한다
- 부분 완료된 PAT ID와 nodeId를 명시한다
- 재시도는 1회. 동일 오류 반복 시 중단하고 보고한다
- 롤백(delete_node) 필요 시 사용자 확인 후 실행한다
