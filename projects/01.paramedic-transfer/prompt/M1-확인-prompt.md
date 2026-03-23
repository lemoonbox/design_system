# Figma 실행 프롬프트 — M1 확인

## 사전 확인
- 문서: `context/figma-target.json`의 `fileKey`(프로젝트에 파일이 없으면 생성·기입 후 사용)
- 페이지: Figma 문서 내 **M1·모달 작업용 페이지명**을 확인한 뒤 동일 이름으로 `set_current_page`
- 화면 frame 이름: `M1-확인`
- 디바이스 기준: **390×844** 모바일 캔버스 위에 **딤 오버레이 + 확인 모달**을 올린 상태(풀스크린 단일 화면이 아님)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| PAT-005 모달 제목 앞 (출발 확인) | icon.feedback.tokens.checkCircle | 2:588 | 24×24 | primary color.brand.600 (#7f56d9) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-005 | 2버튼 확인 모달 | 딤 위 중앙(또는 하단 시트) 모달 카드 전체 — 제목·본문 컨테이너·취소·출발 확정 | 65:4624 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-001 | M1은 L4 위 레이어 모달이며 케이스·동기화 앱 바가 없음 |
| PAT-002 | 동기화·네트워크 배너는 풀스크린 업무 화면 전용 |
| PAT-003 | 업무 단계 스텝퍼는 G1·L2·L4 본문용 |
| PAT-004 | 하단 **단일** 주요 CTA 바가 아니라 **취소+주요 확인 2버튼** 구조이므로 PAT-005에 해당 |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{작업 페이지명}"

### 2. 화면 외부 frame(모달 상태 캔버스)
- `create_frame`
  - name: `M1-확인`
  - x: 0, y: 0, width: **390**, height: **844**
  - fillColor: **background** `color.gray.25` (**#fdfdfd**)(캔버스 기준면; 실제로는 바로 아래 딤이 전면을 덮음)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - paddingTop: **0**, paddingBottom: **0**, paddingLeft: **0**, paddingRight: **0**
  - itemSpacing: **0**
  - primaryAxisAlignItems: **CENTER**, counterAxisAlignItems: **CENTER**(중앙 다이얼로그 기준. **바텀시트**로 그릴 경우 `primaryAxisAlignItems: **MAX**`로 바꾸고 모달을 하단 정렬)

### 3. 딤(배경)
- `create_frame`
  - name: `overlay-dim`
  - parentId: `M1-확인` frame ID
  - width: **390**, height: **844**(캔버스와 동일)
  - position: **절대 배치**로 전체 덮음(오토레이아웃 자식이면 **FILL**에 가깝게 맞춤)
  - fillColor: **text-primary** `color.gray.900` (**#181d27**)에 **불투명도 약 50%**(딤; 정확한 %는 시각적으로 L4가 읽힐 정도로 조정)
- (선택) L4 맥락 목업이 필요하면 딤 **아래**에 흐릿한 L4 플레이스홀더를 별도 레이어로 두되, 본 작업 범위는 **M1 모달**에 한정

### 4. 모달 카드 — PAT-005 적용
- `get_node_info` → PAT-005 노드 확인(제목·본문 영역·좌우 버튼 구조·패딩)
- `clone_node` → PAT-005 복사
- `insert_child` → `overlay-dim` **위**(또는 `M1-확인`의 형제로 딤 다음)에 삽입해 **항상 딤보다 앞**에 오도록 함
- 모달 카드 컨테이너 권장값(패턴과 충돌 시 **패턴 수치 우선**):
  - 가로: **358**(`390 − spacing.xl`×2 = **16**×2)
  - 배경: **surface-raised** `color.white` (**#ffffff**)
  - 모서리: **radius.2xl** (**16px**)(중앙 다이얼로그면 사각 전부; 하단 시트면 상단만 **16px**·하단 **0** 등 패턴과 동일하게)
  - 테두리(선택): **border.width.default** (**1px**), **border-default** `color.gray.300` (**#d5d7da**)
- `set_auto_layout`(패턴이 고정 프레임이면 생략·패턴 유지)
  - 내부 세로 간격은 **spacing.3xl** (**24px**)급으로 맞춤

#### 4a. 제목
- `set_text_content`(또는 해당 텍스트 노드 편집)
  - text: **「이송 출발 확인」**(screen-spec 헤더 예시)
  - 타이포: **subheading** `text xl` · semibold **20px** / line **30px** / weight **600**, **text-primary** `color.gray.900` (**#181d27**)(모달 제목은 한 줄 위주라 전역 화면 제목 **display sm 30px** 대신 **text xl** 사용)

#### 4b. 본문(출발 병원명 + 자동 취소 안내 + 선택 법적 고지)
- PAT-005 본문이 **단일 텍스트**면: 줄바꿈으로 (1) 병원명 한 줄 (2) 안내 문장 (3) 불릿 목록을 표현
- **프레임 분리 구조**면 다음 순서로 자식 배치:

**4b-1. 출발 병원명**
- `create_text` 또는 기존 슬롯
  - name: `departure-hospital-name`
  - text: `{출발 병원명}`(placeholder 예: 「서울○○병원」)
  - **body-strong** `text lg` · medium **18px** / line **28px** / weight **500**, **text-primary** `color.gray.900` (**#181d27**)

**4b-2. 안내·불릿 블록**
- `create_frame`
  - name: `auto-cancel-copy`
  - width: **FILL**
  - height: **HUG**
  - fill: 없음(투명)
- `set_auto_layout`
  - layoutMode: **VERTICAL**
  - itemSpacing: **spacing.lg** (**12px**)
  - paddingLeft: **0**, paddingRight: **0**, paddingTop: **0**, paddingBottom: **0**
- 안내 한 줄(예: 「아래 병원에 걸린 이송 신청은 출발 확정과 함께 자동으로 취소됩니다.」) — **body** `text md` · regular **16px** / line **24px** / weight **400**, **text-primary** (**#181d27**)
- `자동 취소 대상 병원 목록`이 있을 때: 각 항목을 가로 행으로
  - `bullet-row`: layoutMode **HORIZONTAL**, itemSpacing **spacing.lg** (**12px**), counterAxisAlignItems **CENTER**
  - 불릿 기호(소형 원 또는 「•」) — **caption** `text sm` · regular **14px**, **text-secondary** `color.gray.500` (**#717680**)
  - 병원명 — **body** `text md` · regular **16px**, **text-primary** (**#181d27**)
- 목록이 **없을 때**(N): 안내 문구만 표시하거나 「다른 신청 병원 없음」 등 스펙 문구로 대체(구현 시 데이터 조건 반영)

**4b-3. 법적·안전 고지(선택, N)**
- `create_text`
  - name: `legal-footnote`
  - text: `{법적·안전 고지 한 줄}` 또는 생략 시 노드 숨김
  - **meta** `text xs` · regular **12px** / line **18px** / weight **400**, **text-secondary** `color.gray.500` (**#717680**)
  - 본문 블록과 간격 **spacing.lg** (**12px**) 이상

#### 4c. 하단 2버튼(PAT-005 유지)
- **취소**(보조): 테두리 **border.width.default** (**1px**) **border-default** (**#d5d7da**), 채우기 **surface-raised** (**#ffffff**), 라벨 **button** `text md` · semibold **16px** / line **24px** / weight **600**, 글자색 **text-primary** (**#181d27**), 모서리 **radius.md** (**8px**), 내부 패딩 좌우 **spacing.xl** (**16px**) 이상
- **출발 확정**(주요): 채우기 **primary** `color.brand.600` (**#7f56d9**), 라벨 **button** 동일 스케일, 글자색 **text-on-primary** `color.white` (**#ffffff**), 모서리 **radius.md** (**8px**)
- 두 버튼 사이 간격 **spacing.lg** (**12px**); 행은 **HORIZONTAL**, `primaryAxisAlignItems`: **SPACE_BETWEEN** 또는 동일 폭 **FILL** 1:1(터치 영역 확보)

#### 4d. 상태 참고(스펙 반영, 디자인 시안용)
- **전송 중**: 주요 버튼 라벨을 「확인 중…」 등으로 바꾸고 중복 탭 방지(시각적 비활성: **text-disabled** `color.gray.300` (**#d5d7da**) 또는 투명도)
- **실패·오프라인**: 본 프롬프트는 기본 오픈 상태 중심; 상세는 **M2** 스펙·프롬프트와 연계

### 5. 검증
- `get_node_info` → `M1-확인` 최상위 및 모달 카드 계층 확인(딤 위 z-order, 가로 **358**·좌우 **16** 여백)
- `export_node_as_image` → 시각적 확인(선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| 출발 병원명 | 모달 본문 상단 | **body-strong** `text lg` medium **18px**, 한 줄 강조 | **text-primary** `color.gray.900` (**#181d27**) |
| 자동 취소 대상 병원 목록 | 안내 문구 아래 | 불릿 행 목록(병원명 **body** 16px) | 본문 **#181d27**, 불릿 기호 **text-secondary** **#717680** |
| 법적·안전 고지 한 줄 | 본문 최하단(있을 때만) | **meta** `text xs` 12px | **text-secondary** **#717680** |
| (액션) 취소 | 모달 하단 좌측(또는 보조측) | 보조 버튼 라벨 「취소」 | 테두리·글자 **text-primary** **#181d27** |
| (액션) 출발 확정 | 모달 하단 주요측 | 주요 버튼 라벨 「출발 확정」 | 배경 **primary** **#7f56d9**, 글자 **text-on-primary** **#ffffff** |
