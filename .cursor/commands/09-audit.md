# /audit {screen-id}

## 목적
Figma에 구현된 화면을 검토하고 위반 사항과 개선점을 구체적으로 보고한다.

## 실행 전 읽기
1. `projects/{nn}.{project-name}/design-system/design-system.md` — 기준 색상/타이포/간격값
2. `projects/{nn}.{project-name}/context/screen-specs/{screen-id}-*.md` — 데이터 필드, 액션, 상태 기준
3. `projects/{nn}.{project-name}/prompt/{screen-id}-*-prompt.md` — 의도한 실행 계획

---

## Figma 조회
```
join_channel → channel: "{08-build-screen 설정값}"
get_node_info → {부모 프레임 nodeId} — 화면 frame 위치 확인
get_node_info → {screen-id} frame 전체 구조
scan_text_nodes → 텍스트 노드 전체 조회
get_styles → 적용된 스타일 목록
```

---

## 검토 항목

### 1. 기능 완전성 (screen-spec 기준)
- 데이터 필드가 모두 화면에 표시되는가?
- 정의된 액션(버튼 등)이 모두 구현되어 있는가?
- 빈 상태, 오류 상태 등 정의된 상태가 반영되어 있는가?

### 2. 디자인 시스템 준수 (design-system.md 기준)
- 사용된 색상이 design-system 역할 색상과 일치하는가?
- 텍스트 크기/굵기가 타이포그래피 스케일을 따르는가?
- **행간(line-height)·자간(letter-spacing)이 타이포 세밀값 표와 일치하는가?**
- 간격이 기준 spacing값을 따르는가?
- 반경(corner radius)이 기준값을 따르는가?
- **카드·입력창·플로팅 요소에 shadow 토큰이 적용되어 있는가? (elevation 검토)**
- **shadow와 stroke가 동시에 적용된 요소가 있는가? (중복 금지)**
- **인접한 두 요소가 동일한 fill color를 갖지 않는가? (색상 계층 검토)**

### 3. 패턴 일관성
- 동일한 사용자 목적의 UI가 다른 방식으로 구현되어 있는가?
- 프롬프트에서 사용하기로 한 패턴이 실제로 적용되었는가?

### 4. 시각적 위계
- 화면에 focal point가 명확히 있는가?
- 주요 액션이 시각적으로 가장 우선순위가 높은가?
- 텍스트 계층(크기/색상/굵기)이 정보 위계와 일치하는가?

### 5. 밀도 & 여백
- 빈 영역이 의도된 여백인가, 누락된 콘텐츠인가?
- 간격이 일관된 rhythm을 따르는가?

---

## 출력 형식

**위반 사항은 노드 위치와 구체적 수정 방법까지 명시한다.**

```
## 검토 결과 — {screen-id} {화면명}

### 위반 사항
| 번호 | 항목 | 위치 | 문제 | 수정 방법 |
|------|------|------|------|----------|
| 1 | 색상 | 헤더 배경 | raw hex #1a1a1a — design-system 미준수 | gray.900(#101828)으로 교체 |
| 2 | 기능 누락 | 하단 영역 | screen-spec의 '저장' 버튼 없음 | 하단 고정 bar 추가, primary(#{hex}) 버튼 배치 |
| 3 | 타이포 | 섹션 제목 | fontSize 18px — subheading 기준 20px 불일치 | set_font_size → 20 |

### 개선 제안 (선택)
(위반은 아니지만 개선 시 품질 향상)

### 양호
(잘 구현된 부분 간략히)
```

---

## 수정 실행 여부
보고 후 사용자에게 확인한다:
- "위반 사항을 바로 수정할까요?"
- 수정 요청 시: 위반 목록 순서대로 노드별 수정 실행
  ```
  get_node_info → 대상 노드 확인
  set_fill_color / set_font_size / create_frame 등 해당 도구 실행
  get_node_info → 수정 결과 확인
  ```
- 수정 완료 후 재검토 여부 사용자에게 확인
