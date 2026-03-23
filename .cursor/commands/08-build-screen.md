# /build-screen {screen-id}

## ⚙️ 프로젝트 설정 (실행 전 여기를 먼저 채운다)

```
채널명:        ysm85zx5
부모 프레임 nodeId:  42-4415
```

> 채널명과 nodeId는 프로젝트마다 다르다. 실행 전 반드시 확인하고 위 값을 수정한다.

---

## 목적
`prompt/{screen-id}-*-prompt.md`를 읽고 위에서 지정한 부모 프레임 하위에 화면을 실행한다.
프롬프트 파일이 없으면 먼저 `/screen-prompt {screen-id}`를 실행한다.

## 실행 전 읽기
1. `projects/{nn}.{project-name}/prompt/{screen-id}-*-prompt.md` — 실행 지시 전체
2. `.cursor/context/figma-tools.md` — 필요한 도구 확인

design-system, screen-spec은 이미 프롬프트에 반영되어 있으므로 재읽기 금지.

---

## 실행 원칙
- 프롬프트 파일의 순서를 그대로 따른다. 임의 변경 금지
- 수치는 프롬프트 파일에 명시된 값만 사용한다
- 단계마다 생성된 nodeId를 기록하여 다음 단계에서 parentId로 활용한다

---

## 실행 흐름

### Step 1. 사전 확인
이 파일 상단 **⚙️ 프로젝트 설정**의 값을 사용한다.

```
join_channel → channel: "{ysm85zx5}"
get_node_info → nodeId: "{65:4639}"
```

응답에서 다음 두 가지를 확인한다:
1. 프레임이 존재하는지
2. **기존 children의 배치 현황** — children 배열에서 각 child의 x, width를 읽어 현재 가장 오른쪽 끝 x 좌표(`nextX`)를 계산한다

```
nextX = max(child.x + child.width) + 40   // 기존 child가 없으면 nextX = 0
```

화면 최상위 `create_frame`의 `parentId`는 부모 프레임 nodeId로, x는 `nextX`로 지정한다.
x, y는 **부모 프레임 내부 좌표** 기준이다. 캔버스 절대 좌표로 지정하지 않는다.

> ⚠️ 프레임이 존재하지 않거나 오류가 나면 즉시 중단하고 사용자에게 nodeId 재확인을 요청한다.
> 페이지를 새로 생성하거나 `set_current_page`를 호출하지 않는다.

대상 화면 frame이 이미 존재하는 경우:
```
get_node_info → 기존 frame 확인
```
→ 기존 frame이 있으면 사용자에게 확인: "덮어쓸까요, 새로 만들까요?"

### Step 2. 프롬프트 순서대로 실행
프롬프트 파일의 "실행 순서" 섹션을 위에서 아래로 순서대로 실행한다.

각 create 작업 후:
- 반환된 nodeId를 메모
- 다음 단계의 parentId에 사용

### Step 3. 패턴 적용
프롬프트의 "사용 패턴" 표에 명시된 패턴 처리:
```
get_node_info → 패턴 노드 존재 확인
clone_node → 복사
insert_child → 대상 frame에 삽입
move_node → 위치 조정 (필요 시)
set_text_content → 실제 데이터로 텍스트 교체
```

패턴 노드 ID가 _index.md에 비어있는 경우:
→ `/build-patterns`가 먼저 실행되어야 한다. 사용자에게 알리고 중단한다.
(패턴은 frame이므로 get_local_components로 검색 불가)

### Step 4. 검증
```
get_node_info → 최상위 frame 구조 확인
```

선택:
```
export_node_as_image → 시각적 확인
```

---

## 완료 보고
```
완료: {screen-id} — {화면명}
생성된 frame nodeId: {id}
사용된 패턴: {PAT-번호 목록 또는 "없음"}
미사용 패턴: {있다면 PAT-번호, 사유}
이슈: {있다면 구체적으로}
```

## 실패 시
- 오류 내용을 그대로 보고한다
- 부분 완료된 노드 ID를 명시한다
- 재시도는 1회. 동일 오류 반복 시 중단하고 보고한다
- 롤백(delete_node) 필요 시 사용자 확인 후 실행한다
