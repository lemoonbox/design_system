# Figma 실행 프롬프트 — M2 동기화·오류

## 사전 확인
- 문서: (`context/figma-target.json`의 `fileKey` — 저장 후 기입)
- 페이지: (팀 규약상 모달 전용 페이지명 또는 `figma-target.json`의 대상 페이지)
- 화면 frame 이름: "M2-동기화·오류"
- 디바이스 기준: 390×844 모바일(모달은 동일 폭 기준, 카드 폭은 좌우 안전영역 반영)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| PAT-005 모달 제목 앞 (오류·오프라인) | icon.feedback.tokens.alertCircle | 2:467 | 24×24 | error color.error.600 (#d92d20) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-005 | 2버튼 확인 모달 | 스크림 위 중앙 모달 카드(제목·본문·메타·닫기+다시 시도) | 65:4624 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-001 | 케이스·동기화 헤더는 본 화면이 전역 헤더가 아닌 오류 모달이라 미적용 |
| PAT-002 | 인라인 동기화 배너가 아니라 동기화 상세·재시도가 목적인 전면 모달이라 미적용 |
| PAT-003 | 업무 단계 스텝퍼는 G1/L2/L4 맥락용이며 오류 모달과 무관 |
| PAT-004 | 하단 고정 단일 CTA 바는 본 화면이 카드 내부 2버튼(닫기·다시 시도) 구조라 미적용 |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: "M2-동기화·오류"
  - x: 0, y: 0, width: 390, height: 844
  - fillColor: `text-primary` / `color.gray.900` (**#181d27**) — 스크림 역할, **opacity 약 50%** (foundation에 스크림 토큰 없음; 동일 팔레트 키 + 불투명도로 표현)
- `set_auto_layout`
  - layoutMode: VERTICAL
  - paddingTop: 0, paddingBottom: 0, paddingLeft: 0, paddingRight: 0
  - itemSpacing: 0
  - primaryAxisAlignItems: CENTER
  - counterAxisAlignItems: CENTER

### 3. 모달 카드 컨테이너
- `create_frame`
  - name: "modal-card"
  - parentId: {화면 frame ID}
  - width: 358 (390 − `spacing.xl` 16 × 2)
  - height: hug contents (또는 Figma에서 세로 hug)
  - fillColor: `surface-raised` (**#ffffff**)
  - cornerRadius: `radius.2xl` (**16px**) — 모달·시트 상단 규칙과 동일하게 카드 전체에 적용
  - stroke: `border.width.default` (**1px**), 색 `border-default` (**#d5d7da**)
- `set_auto_layout`
  - layoutMode: VERTICAL
  - paddingTop: `spacing.xl` (**16px**), paddingBottom: `spacing.xl` (**16px**)
  - paddingLeft: `spacing.xl` (**16px**), paddingRight: `spacing.xl` (**16px**)
  - itemSpacing: `spacing.lg` (**12px**)

### 4. 패턴 적용 (PAT-005)
- `get_node_info` → PAT-005(2버튼 확인 모달) 노드 구조 확인
- `clone_node` → PAT-005 복사본 생성
- `insert_child` → `modal-card`의 첫 자식으로 삽입(또는 PAT-005가 카드 단위면 `modal-card`와 병합 가능한지 확인 후, **내부 제목·본문·버튼 영역만** 카드 안으로 맞춤)
- 구조 맞춤 원칙: **제목 1줄 + 본문(사용자 메시지) + (선택) 대기 건수·마지막 시도 시각 + 가로 2버튼 행**이 되도록 프레임 계층 정리
- `set_text_content` / 텍스트 노드 교체:
  - 제목 예: "연결할 수 없습니다" 또는 "동기화 대기 중" (상황별)
  - 본문: 사용자 메시지(기술 스택·에러코드 노출 없음)
  - 보조 버튼 라벨: "닫기"
  - 주요 버튼 라벨: "다시 시도"

#### PAT-005와 스펙 불일치 시 직접 보정
- 제목 텍스트: `typography.text xl` · semibold — **20px**, lineHeight **30px**, fontWeight **600**, fontFamily **Inter**, 색 `text-primary` (**#181d27**)
- 본문: `typography.text md` · regular — **16px**, lineHeight **24px**, fontWeight **400**, 색 `text-primary` (**#181d27**)
- (선택) 대기 건수 줄: `typography.text sm` · regular — **14px**, lineHeight **20px**, 색 `text-secondary` (**#717680**), 예시 문구: "전송 대기 3건"
- (선택) 마지막 시도 시각: `typography.text xs` · regular — **12px**, lineHeight **18px**, 색 `text-secondary` (**#717680**)
- 영향 안내 문구(예: "일지는 기기에 저장됨"): 본문과 동일 타이포 또는 `text sm`으로 위계 구분(본문이 길면 `text sm`·`text-secondary`로 보조 문장 처리)

### 5. 버튼 행 (PAT-005에 없거나 변형 필요 시)
- `create_frame` name: "modal-actions", parentId: `modal-card`
  - width: fill (358 − 좌우 패딩 반영된 hug/fill)
  - height: hug
  - fill: none
- `set_auto_layout`
  - layoutMode: HORIZONTAL
  - itemSpacing: `spacing.lg` (**12px**)
  - primaryAxisAlignItems: SPACE_BETWEEN 또는 FILL 균등 배분
  - counterAxisAlignItems: CENTER
- **보조 버튼 "닫기"**
  - 높이 최소 **48px** 권장(터치 타깃), `radius.md` (**8px**)
  - fill: `surface-raised` (**#ffffff**) 또는 `surface` (**#fafafa**)
  - stroke: `border.width.default` (**1px**), `border-default` (**#d5d7da**)
  - 라벨: `typography.text md` · semibold — **16px**, **600**, 색 `text-primary` (**#181d27**)
- **주요 버튼 "다시 시도"**
  - 동일 높이·`radius.md` (**8px**)
  - fill: `primary` / `color.brand.600` (**#7f56d9**)
  - 라벨: `typography.text md` · semibold — **16px**, **600**, 색 `text-on-primary` (**#ffffff**)
  - pressed 시 시각: `primary-pressed` / `color.brand.700` (**#6941c6**) (모바일 pressed)

### 6. 상태 변형(재시도 중)
- "다시 시도" 탭 직후: 주요 버튼에 로딩 인디케이터 표시·라벨 유지 또는 "다시 시도 중" 등 — 버튼 `disabled` 시 라벨 색 `text-disabled` (**#d5d7da**) + 배경 `primary` 유지 시 대비 저하 방지를 위해 **비활성 스타일은 제품 가이드에 맞춰** 조정(중복 탭 방지)
- 실패 지속 시 본문 텍스트만 `set_text_content`로 갱신, 모달 프레임 유지

### 7. 검증
- `get_node_info` → 최상위 "M2-동기화·오류" frame 및 `modal-card` 자식 순서 확인
- `export_node_as_image` → 시각적 확인 (선택)

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| 오류 유형 (offline / timeout / server_error) | UI 비노출 | 내부·카피 분기만 | — |
| 사용자 메시지 | 모달 본문 | `text md` regular, `text-primary` | **#181d27** |
| 대기 중 작업 수 | 본문 아래 한 줄(선택) | `text sm`, `text-secondary`, 예: "전송 대기 N건" | **#717680** |
| 마지막 시도 시각 | 카드 하단 메타(선택) | `text xs`, `text-secondary` | **#717680** |
| (고정 안내) 영향 예시 | 본문 또는 본문 직후 | "일지는 기기에 저장됨" 등 — 스펙의 사용자 친화 문구 | 본문과 동일 또는 `text sm`/`text-secondary`로 위계 |
