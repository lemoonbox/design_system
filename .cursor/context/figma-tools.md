# Figma MCP 도구 레퍼런스

실행 계획 수립 시 이 목록을 참조한다. 실행 전 사용할 도구를 미리 선택하고 순서를 계획한다.

---

## 문서 조회 (읽기 전용)

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `get_document_info` | 현재 문서 전체 정보 | - |
| `get_pages` | 모든 페이지 목록 | - |
| `get_selection` | 현재 선택된 노드 | - |
| `get_node_info` | 단일 노드 상세 정보 | nodeId |
| `get_nodes_info` | 복수 노드 정보 | nodeIds[] |
| `get_styles` | 문서의 모든 스타일 | - |
| `get_local_components` | 로컬 컴포넌트 목록 | - |
| `get_remote_components` | 팀 라이브러리 컴포넌트 | - |
| `scan_text_nodes` | 노드 내 텍스트 전체 스캔 | nodeId |
| `get_styled_text_segments` | 텍스트 스타일 세그먼트 조회 | nodeId, property |
| `export_node_as_image` | 노드를 이미지로 내보내기 | nodeId, format(PNG/JPG/SVG/PDF), scale |

---

## 페이지 관리

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `set_current_page` | 작업 페이지 전환 | pageId |
| `create_page` | 새 페이지 생성 | name |
| `rename_page` | 페이지 이름 변경 | pageId, name |
| `delete_page` | 페이지 삭제 | pageId |

---

## 생성

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `create_frame` | 프레임 생성 (**레이아웃 기본 단위**) | x, y, width, height, name, parentId, fillColor{r,g,b,a} |
| `create_rectangle` | 사각형 생성 | x, y, width, height, name, parentId |
| `create_text` | 텍스트 생성 | x, y, text, fontSize, fontWeight, fontColor{r,g,b,a}, name, parentId |
| `create_ellipse` | 원형 생성 | x, y, width, height, name, parentId, fillColor |
| `clone_node` | 노드 복사 (**패턴 복사에 사용**) | nodeId, x, y |
| `group_nodes` | 노드 그룹화 | nodeIds[], name |
| `ungroup_nodes` | 그룹 해제 | nodeId |
| `insert_child` | 자식 노드 삽입 | parentId, childId, index |
| `flatten_node` | 노드 평탄화 | nodeId |
| `create_polygon` | 다각형 생성 | x, y, width, height, name, parentId, sides |
| `create_star` | 별 모양 생성 | x, y, width, height, name, parentId, points |

---

## 수정

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `set_fill_color` | 배경/채우기 색상 | nodeId, r(0-1), g(0-1), b(0-1), a(0-1) |
| `set_stroke_color` | 테두리 색상 | nodeId, r, g, b, a, strokeWeight |
| `set_corner_radius` | 모서리 둥글기 | nodeId, radius, corners[4] |
| `set_auto_layout` | Auto Layout 설정 (**레이아웃 핵심**) | nodeId, layoutMode(HORIZONTAL/VERTICAL/NONE), paddingTop/Bottom/Left/Right, itemSpacing, primaryAxisAlignItems(MIN/CENTER/MAX/SPACE_BETWEEN), counterAxisAlignItems(MIN/CENTER/MAX), layoutWrap(WRAP/NO_WRAP) |
| `set_effects` | 그림자/블러 등 효과 | nodeId, effects[] |
| `set_effect_style_id` | 스타일 효과 적용 | nodeId, effectStyleId |
| `move_node` | 노드 위치 이동 | nodeId, x, y |
| `resize_node` | 노드 크기 변경 | nodeId, width, height |
| `rename_node` | 노드 이름 변경 | nodeId, name |
| `delete_node` | 노드 삭제 | nodeId |

---

## 텍스트 스타일

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `set_text_content` | 텍스트 내용 변경 | nodeId, text |
| `set_multiple_text_contents` | 복수 텍스트 일괄 변경 | nodeId, text[{nodeId, text}] |
| `set_font_name` | 폰트 패밀리/스타일 | nodeId, family, style |
| `set_font_size` | 폰트 크기 | nodeId, fontSize |
| `set_font_weight` | 폰트 굵기 (100~900) | nodeId, weight |
| `set_letter_spacing` | 자간 | nodeId, letterSpacing, unit(PIXELS/PERCENT) |
| `set_line_height` | 줄 높이 | nodeId, lineHeight, unit(PIXELS/PERCENT/AUTO) |
| `set_paragraph_spacing` | 단락 간격 | nodeId, paragraphSpacing |
| `set_text_case` | 대소문자 | nodeId, textCase(ORIGINAL/UPPER/LOWER/TITLE) |
| `set_text_decoration` | 밑줄/취소선 | nodeId, textDecoration(NONE/UNDERLINE/STRIKETHROUGH) |
| `set_text_style_id` | 텍스트 스타일 적용 | nodeId, textStyleId |
| `load_font_async` | 폰트 로드 | family, style |

---

## 컴포넌트 (제한적 사용)

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `create_component_instance` | 컴포넌트 인스턴스 생성 | componentKey, x, y |
| `create_component_from_node` | 노드를 컴포넌트로 변환 | nodeId, name |
| `create_component_set` | 컴포넌트 세트(variant) 생성 | componentIds[], name |

> ⚠️ 패턴은 컴포넌트로 만들지 않는다. `create_component_*` 도구는 사용자가 명시적으로 컴포넌트를 요청할 때만 사용.

---

## 채널 연결

| 도구 | 용도 | 주요 파라미터 |
|------|------|--------------|
| `join_channel` | Figma 플러그인 채널 연결 | channel |

---

## 색상 변환 참고

Figma 도구의 색상 파라미터는 0~1 범위 RGB를 사용한다.
hex → RGB 변환: `r = R/255, g = G/255, b = B/255`

예시:
- `#ffffff` → r:1, g:1, b:1
- `#1d2939` → r:0.114, g:0.161, b:0.224
- `#6941c6` → r:0.412, g:0.255, b:0.776

---

## 실행 계획 패턴 (자주 쓰는 시퀀스)

### 카드 레이아웃 만들기
```
create_frame (카드 외부)
set_corner_radius
set_fill_color
set_auto_layout (VERTICAL, padding 16, gap 12)
create_text (타이틀)
create_text (본문)
set_fill_color (각 텍스트)
```

### 리스트 행 만들기
```
create_frame (행 컨테이너)
set_auto_layout (HORIZONTAL, padding 16, gap 12, counterAxisAlignItems: CENTER)
create_rectangle (아이콘 placeholder)
create_frame (텍스트 그룹)
  set_auto_layout (VERTICAL, gap 2)
  create_text (label)
  create_text (value)
create_text (우측 액션)
```

### 패턴 복사 후 삽입
```
get_node_info (패턴 노드 확인)
clone_node (복사)
insert_child (대상 frame에 삽입)
move_node (위치 조정)
set_text_content (텍스트 교체)
```

### 카드에 elevation 적용 (shadow-sm 예시)
```
set_effects
  nodeId: {카드 frame nodeId}
  effects: [
    {
      type: "DROP_SHADOW",
      color: { r: 0, g: 0, b: 0, a: 0.06 },
      offset: { x: 0, y: 1 },
      radius: 4,
      spread: 0,
      visible: true
    }
  ]
```

### shadow-md (모달/드롭다운)
```
effects: [{ type:"DROP_SHADOW", color:{r:0,g:0,b:0,a:0.12}, offset:{x:0,y:4}, radius:12, spread:-2, visible:true }]
```

### shadow-lg (플로팅 버튼/알림)
```
effects: [{ type:"DROP_SHADOW", color:{r:0,g:0,b:0,a:0.18}, offset:{x:0,y:8}, radius:24, spread:-4, visible:true }]
```

> 그림자와 border(`set_stroke_color`)를 동시에 쓰지 않는다. 둘 중 하나만 선택.
