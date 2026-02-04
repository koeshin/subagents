---
description: 새 프로젝트의 PDCA 개발 환경 초기화
---

# Starter Workflow

새 프로젝트에 PDCA 개발 환경을 설정합니다.

## 실행

```
/starter
```

## 수행 작업

### 1. 폴더 구조 생성

```
// turbo
mkdir -p docs/01-plan/features docs/02-design/features docs/03-analysis docs/04-report/features docs/archive
```

### 2. PDCA 상태 파일 생성

`docs/.pdca-status.json` 파일 생성:

```json
{
  "version": "1.0.0",
  "features": {},
  "activeFeature": null,
  "createdAt": "{현재 시간}"
}
```

### 3. 기본 .gitignore 추가 (docs 폴더용)

`docs/.gitignore` 파일:
```
# PDCA temporary files
.pdca-snapshots/
.bkit-memory.json
```

### 4. README 생성

`docs/README.md` 생성:

```markdown
# Project Documentation

PDCA 방법론을 사용한 개발 문서입니다.

## 구조

- `01-plan/` - 계획 문서
- `02-design/` - 설계 문서  
- `03-analysis/` - Gap 분석 결과
- `04-report/` - 완료 보고서
- `archive/` - 완료된 PDCA 문서 아카이브

## 사용법

1. `/pdca plan {feature}` - 새 기능 계획 시작
2. `/pdca status` - 현재 진행 상황 확인
3. `/pdca next` - 다음 단계 안내

자세한 사용법은 `.agent/workflows/pdca.md` 참조.
```

## 완료 후

초기화가 완료되면 다음 명령으로 PDCA 사이클을 시작할 수 있습니다:

```
/pdca plan {feature-name}
```
