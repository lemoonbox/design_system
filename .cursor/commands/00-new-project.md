# /new-project

## 목적
새 프로젝트 폴더 구조를 생성한다.
이후 모든 커맨드가 올바른 경로에 산출물을 저장할 수 있도록 기반을 만든다.

## 실행 전 읽기
없음. 이 커맨드는 읽기 없이 바로 실행한다.

---

## Step 1. 프로젝트 정보 수집 (사용자에게)

아래 두 가지를 확인한다:

1. **프로젝트 번호 (nn)**: 기존 프로젝트가 있다면 다음 번호, 없으면 `01`
   - `projects/` 폴더 내 기존 프로젝트 목록을 확인하여 제안한다
2. **프로젝트 이름**: 영문 소문자, 하이픈 구분
   - 예: `ems-transport`, `food-delivery`, `admin-dashboard`

확인 후 생성될 경로를 보여주고 승인을 받는다:
```
생성될 폴더: projects/01.ems-transport/
맞으시면 진행하겠습니다.
```

---

## Step 2. 폴더 구조 생성

승인 후 아래 구조를 생성한다:

```bash
mkdir -p projects/{nn}.{project-name}/context/foundation
mkdir -p projects/{nn}.{project-name}/context/screen-specs
mkdir -p projects/{nn}.{project-name}/design-system/patterns
mkdir -p projects/{nn}.{project-name}/prompt
```

---

## Step 3. 사용자 안내

폴더 생성 완료 후 다음 안내를 제공한다:

```
✓ 프로젝트 폴더 생성 완료: projects/{nn}.{project-name}/

다음 파일을 직접 배치해 주세요:
  context/foundation/core-visual-tokens.json  ← 파운데이션 색상 토큰
  context/foundation/icon-tokens.json         ← 아이콘 토큰
  context/figma-target.json                   ← Figma 문서 정보

준비되면 /service-plan 으로 시작합니다.
```

---

## figma-target.json 형식 안내 (요청 시)

사용자가 figma-target.json 작성 방법을 묻는 경우 아래 형식을 안내한다:

```json
{
  "fileKey": "피그마 파일 URL의 키값",
  "pageName": "작업할 페이지 이름",
  "patternsPage": "패턴을 모아둘 페이지 이름"
}
```

Figma 파일 URL 예시:
`https://www.figma.com/file/AbCdEfGhIj/프로젝트명`
→ fileKey = `AbCdEfGhIj`

---

## 완료 후 다음 단계
```
프로젝트 루트: projects/{nn}.{project-name}/
다음 커맨드: /service-plan
```
