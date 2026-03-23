# Figma 실행 프롬프트 — M3 출동 종료 경고

## 사전 확인
- 문서: (`context/figma-target.json`의 `fileKey` — 저장소에 파일 없음, 사용자 제공값 사용)
- 페이지: (`context/figma-target.json`의 작업 페이지명)
- 화면 frame 이름: "M3-출동-종료-경고"
- 디바이스 기준: 390×844 모바일 (모달·스크림 포함 전체 캔버스)

## 사용 아이콘
| 위치 | 아이콘명 | figmaId | 크기 | 색상 |
|------|---------|---------|------|------|
| modal-alert-row 경고 아이콘 | icon.feedback.tokens.alertTriangle | 2:472 | 24×24 | warning color.warning.500 (#f79009) |

## 사용 패턴
| PAT ID | 패턴명 | 적용 위치 | Figma 노드 ID |
|--------|--------|----------|--------------|
| PAT-005 | 2버튼 확인 모달 | 스크림 위 중앙 `modal-card` — 제목·본문·하단 2버튼 골격 | 65:4624 |

## 미사용 패턴 및 사유
| PAT ID | 사유 |
|--------|------|
| PAT-001 | 케이스·동기화 헤더는 L1 등 본 화면용; M3는 상위 이탈 시 노출 모달 단독 구성 |
| PAT-002 | 동기화·네트워크 배너는 전역 한 줄 알림용; 미반영·대기는 본문 카피로 처리 |
| PAT-003 | 업무 단계 스텝퍼 없음 |
| PAT-004 | 화면 하단 단일 CTA 바가 아니라 모달 내부 2버튼 행(PAT-005) |

---

## 실행 순서

### 1. 문서 준비
- `get_document_info`
- `set_current_page` → "{figma-target.json의 페이지명}"

### 2. 화면 외부 frame
- `create_frame`
  - name: "M3-출동-종료-경고"
  - x: 0, y: 0, width: 390, height: 844
  - fillColor: background — `color.gray.25` (#fdfdfd)
- `set_auto_layout`
  - layoutMode: VERTICAL
  - paddingTop: 0, paddingBottom: 0, paddingLeft: 0, paddingRight: 0
  - itemSpacing: 0
  - primaryAxisAlignItems: CENTER
  - counterAxisAlignItems: CENTER

### 3. 스크림(배경 딤)
- `create_frame`
  - name: "scrim"
  - parentId: 화면 frame ID
  - width: 390, height: 844 (부모에 맞게 stretch / absolute로 전면 덮음)
  - fillColor: `color.gray.900` / text-primary (#181d27)
- Figma **Fill opacity**: foundation에 스크림 전용 토큰 없음 → 팀 모달 가이드값 적용(스크림만 투명도 조절, hex는 위 팔레트 유지)

### 4. 모달 카드 (`modal-card`)
- `create_frame`
  - name: "modal-card"
  - parentId: 화면 frame ID (스크림 **위** z-order)
  - width: 358 (390 − 2×`spacing.xl` 16px)
  - height: hug contents(콘텐츠 높이에 맞춤)
  - fillColor: surface-raised — `color.white` (#ffffff)
  - stroke: `border.width.default` (1px), 색상 border-default — `color.gray.300` (#d5d7da) *(필요 시 생략 가능, 카드만 surface로 구분)*
  - cornerRadius: `radius.2xl` (16px) — 모서리 전부 동일
- `set_auto_layout`
  - layoutMode: VERTICAL
  - paddingTop: `spacing.xl` (16px), paddingBottom: `spacing.xl` (16px)
  - paddingLeft: `spacing.xl` (16px), paddingRight: `spacing.xl` (16px)
  - itemSpacing: `spacing.3xl` (24px)

#### 4.1 패턴 적용 (PAT-005)
- `get_node_info` → PAT-005 노드 구조 확인
- `clone_node` → PAT-005 복사본을 `modal-card` 자식으로 배치(또는 `insert_child`)
- 다음을 **덮어써서** M3에 맞춤:
  - 모달 제목 텍스트: **"출동을 종료할까요?"** (또는 screen-spec과 동일한 헤더 카피)
  - 본문: 미반영·로컬 저장·동기화 대기 안내(아래 4.2 문구·필드 매핑 참고)
  - 좌측(보조) 버튼 라벨: **"계속 기록"** — 스타일: 채우기 surface-raised (#ffffff), 테두리 border-default (#d5d7da), 텍스트 text-primary (#181d27)
  - 우측(파괴적 확인) 버튼 라벨: **"출동 종료하고 나가기"** — 채우기 error — `color.error.600` (#d92d20), 텍스트 text-on-primary (#ffffff); PAT-005 기본이 primary(brand.600)면 fill을 error로 교체
- 버튼 타이포: `text md` · semibold — 16px / 24px line / fontWeight 600
- 버튼 행: layoutMode HORIZONTAL, `itemSpacing` `spacing.lg` (12px), `primaryAxisAlignItems` FILL 또는 SPACE_BETWEEN(두 버튼 동일 너비 권장 시 각 버튼 `layoutGrow: 1`)

#### 4.2 직접 구현 (PAT-005 미사용 시)
1. **경고 아이콘 + 한 줄 강조(선택)**  
   - `create_frame` name: "modal-alert-row", layoutMode HORIZONTAL, itemSpacing `spacing.lg` (12px), counterAxisAlignItems CENTER  
   - `icon.feedback.alertTriangle` 인스턴스 또는 벡터 복제, 색상 warning — `color.warning.500` (#f79009) (아이콘 단색 규칙에 맞게 적용)  
   - `create_text` name: "modal-title", text: "출동을 종료할까요?", fontSize **20px**, lineHeight **30px**, fontWeight **600** (`text xl` · semibold), fontColor text-primary (#181d27)  
   - *아이콘 행 없이 제목만 두려면 `modal-title`만 `modal-card` 첫 자식으로 배치.*

2. **본문**  
   - `create_text` name: "modal-body-primary", text: (예) "아직 서버에 반영되지 않은 기록이 있을 수 있습니다. 동기화가 끝나기 전에 나가면 일부 내용이 대기 상태로 남을 수 있어요."  
   - fontSize **16px**, lineHeight **24px**, fontWeight **400** (`text md` · regular), fontColor text-primary (#181d27)

3. **데이터 2줄(스펙 필드)**  
   - `create_text` name: "modal-meta-unsent", text: (예) "미전송 구간 · 3건" — 플레이스홀더 숫자는 스펙의 `미전송 구간 수`에 매핑  
   - fontSize **14px**, lineHeight **20px**, fontWeight **400** (`text sm` · regular), fontColor text-secondary (#717680)  
   - `create_text` name: "modal-meta-saved", text: (예) "마지막 저장 · 14:32" — `마지막 저장 시각`에 매핑  
   - 동일 타이포·색상(caption 계열, `text sm` / text-secondary)

4. **버튼 행**  
   - `create_frame` name: "modal-actions", width: fill, layoutMode HORIZONTAL, itemSpacing `spacing.lg` (12px), counterAxisAlignItems STRETCH  
   - **계속 기록**  
     - `create_frame` name: "btn-secondary", minHeight 권장 48px(터치), horizontal padding `spacing.xl` (16px), vertical padding `spacing.lg` (12px), fillColor surface-raised (#ffffff), stroke 1px border-default (#d5d7da), cornerRadius `radius.md` (8px)  
     - 내부 `create_text`: "계속 기록", `text md` semibold 16/24, text-primary (#181d27)  
   - **출동 종료하고 나가기**  
     - `create_frame` name: "btn-destructive", 동일 높이·패딩 규칙, fillColor error (#d92d20), cornerRadius `radius.md` (8px), stroke 없음  
     - 내부 `create_text`: "출동 종료하고 나가기", `text md` semibold, text-on-primary (#ffffff)  
   - 두 버튼 동일 너비: 각각 `layoutGrow: 1` 또는 고정 width = (358 − 16 − 12) / 2 = 165px (카드 패딩 제외 시 내부 너비 326 기준으로 재계산)

### 5. 하단 고정 영역
- 없음 — 액션은 모달 카드 내부 `modal-actions`에만 둠(screen-spec의 "하단 고정"은 모달 카드 하단 UI로 해석).

### 6. 검증
- `get_node_info` → 최상위 "M3-출동-종료-경고", `modal-card`, 스크림 z-order 확인
- (선택) `export_node_as_image` — 스크림·카드 대비 확인
- **상태 참고**: 종료 처리 중일 때 주 버튼 로딩·비활성은 screen-spec 상태 정의에 맞춰 동일 프레임 변형 또는 별도 variant로 표현 가능

---

## 데이터 매핑
| 필드명 | 표시 위치 | 표시 방식 | 색상 |
|--------|----------|----------|------|
| (헤더 카피) | `modal-title` 또는 PAT-005 제목 슬롯 | `text xl` semibold 20px | text-primary #181d27 |
| 미전송 구간 수 | `modal-meta-unsent` | `text sm` regular, "미전송 구간 · N건" 형식 | text-secondary #717680 |
| 마지막 저장 시각 | `modal-meta-saved` | `text sm` regular, 시각 포맷은 제품 정책 | text-secondary #717680 |
| 경고 요약 본문 | `modal-body-primary` | `text md` regular | text-primary #181d27 |

**엣지**: 미전송 0건이면 `modal-meta-unsent` 문구 완화 또는 숨김(screen-spec 엣지케이스).
