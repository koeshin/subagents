---
name: pdca
description: PDCA (Plan-Design-Do-Check-Act) 방법론 핵심 지식
---

# PDCA Methodology Skill

PDCA 방법론의 핵심 개념과 원칙을 제공합니다.
각 단계의 실제 작업은 전문 에이전트가 담당합니다.

## PDCA 사이클

```
┌─────────────────────────────────────────────────────────────────┐
│                      PDCA Cycle                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Plan ──────► Design ──────► Do ──────► Check ──────► Act     │
│     │                                                    │      │
│     └────────────────── Improvement Cycle ◄──────────────┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 정의

| Phase | 담당 에이전트 | 역할 |
|-------|-------------|-----|
| Plan | plan-writer | 목표, 범위, 성공 기준 정의 |
| Design | design-writer | 아키텍처, API, 데이터 모델 설계 |
| Do | code-implementer | 설계 기반 구현 |
| Check | gap-analyzer | 설계-구현 Gap 분석 |
| Act | pdca-iterator | 자동 개선 반복 |
| Report | report-writer | 완료 보고서 작성 |

## Match Rate 기준

```
Match Rate = (매칭 항목 / 전체 항목) × 가중치 합계

가중치:
- API 엔드포인트: 40%
- 데이터 모델: 30%
- 컴포넌트 구조: 20%
- 에러 핸들링: 10%
```

| Match Rate | 판정 | 다음 단계 |
|-----------|-----|---------|
| >= 90% | Pass | report-writer |
| 70-89% | Partial | pdca-iterator 권장 |
| < 70% | Fail | pdca-iterator 필수 |

## 작업 분류

| 분류 | 라인 수 | PDCA 적용 |
|-----|--------|----------|
| Quick Fix | < 10 | 선택 |
| Minor Change | < 50 | 권장 |
| Feature | < 200 | 필수 |
| Major Feature | >= 200 | 필수 + 분할 |

## 문서 경로

```
docs/
├── 01-plan/features/{feature}.plan.md     # Plan 문서
├── 02-design/features/{feature}.design.md # Design 문서
├── 03-analysis/{feature}.analysis.md      # Gap 분석
├── 04-report/features/{feature}.report.md # 완료 보고서
├── archive/YYYY-MM/{feature}/             # 아카이브
└── .pdca-status.json                      # 상태 추적
```

## 상태 파일 구조

```json
{
  "version": "1.0.0",
  "features": {
    "{feature}": {
      "phase": "plan|design|do|check|act|completed|archived",
      "matchRate": 0-100,
      "iterationCount": 0-5,
      "startedAt": "ISO timestamp",
      "updatedAt": "ISO timestamp"
    }
  },
  "activeFeature": "{feature}"
}
```

## 에이전트 위치

모든 PDCA 에이전트는 `.skills/agents/` 폴더에 위치:
- `.skills/agents/plan-writer/SKILL.md`
- `.skills/agents/design-writer/SKILL.md`
- `.skills/agents/code-implementer/SKILL.md`
- `.skills/agents/gap-analyzer/SKILL.md`
- `.skills/agents/pdca-iterator/SKILL.md`
- `.skills/agents/report-writer/SKILL.md`
