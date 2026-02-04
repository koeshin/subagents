---
description: PDCA 방법론을 사용한 구조화된 개발 워크플로우 (Plan-Design-Do-Check-Act)
---

# PDCA Workflow

PDCA 사이클을 통해 체계적인 개발을 진행합니다.
각 단계는 전문 에이전트가 담당합니다.

## 명령어

```
/pdca plan {feature}     # Plan 에이전트 호출
/pdca design {feature}   # Design 에이전트 호출
/pdca do {feature}       # Do 에이전트 호출
/pdca analyze {feature}  # Check 에이전트 호출 (Gap 분석)
/pdca iterate {feature}  # Act 에이전트 호출 (반복 개선)
/pdca report {feature}   # Report 에이전트 호출
/pdca status             # 현재 상태 확인
/pdca next               # 다음 단계 안내
/pdca archive {feature}  # 완료 문서 아카이브
```

---

## 에이전트 호출 맵

| 명령어 | 호출 에이전트 | 위치 |
|-------|-------------|-----|
| `/pdca plan` | plan-writer | `.skills/agents/plan-writer/SKILL.md` |
| `/pdca design` | design-writer | `.skills/agents/design-writer/SKILL.md` |
| `/pdca do` | code-implementer | `.skills/agents/code-implementer/SKILL.md` |
| `/pdca analyze` | gap-analyzer | `.skills/agents/gap-analyzer/SKILL.md` |
| `/pdca iterate` | pdca-iterator | `.skills/agents/pdca-iterator/SKILL.md` |
| `/pdca report` | report-writer | `.skills/agents/report-writer/SKILL.md` |

---

## /pdca plan {feature}

**호출 에이전트**: plan-writer

**수행 작업**:
1. 사용자 요구사항 파악
2. 목표와 범위 정의
3. 성공 기준 수립
4. 리스크 분석
5. `docs/01-plan/features/{feature}.plan.md` 생성
6. `.pdca-status.json` 업데이트: phase="plan"

**다음 단계**: `/pdca design {feature}`

---

## /pdca design {feature}

**호출 에이전트**: design-writer

**전제 조건**: Plan 문서 존재

**수행 작업**:
1. Plan 문서 로드
2. 아키텍처 설계
3. 데이터 모델 정의
4. API 설계
5. 컴포넌트 구조 정의
6. 구현 순서 결정
7. `docs/02-design/features/{feature}.design.md` 생성
8. `.pdca-status.json` 업데이트: phase="design"

**다음 단계**: `/pdca do {feature}`

---

## /pdca do {feature}

**호출 에이전트**: code-implementer

**전제 조건**: Design 문서 존재

**수행 작업**:
1. Design 문서 로드
2. 구현 체크리스트 생성
3. 단계별 구현 가이드 제공
4. 코드 작성 지원
5. 진행 상황 추적
6. `.pdca-status.json` 업데이트: phase="do"

**다음 단계**: `/pdca analyze {feature}`

---

## /pdca analyze {feature}

**호출 에이전트**: gap-analyzer

**전제 조건**: 구현 코드 존재

**수행 작업**:
1. Design 문서 로드
2. 구현 코드 스캔
3. 항목별 비교 (API, 모델, 컴포넌트, 에러)
4. Match Rate 계산
5. `docs/03-analysis/{feature}.analysis.md` 생성
6. `.pdca-status.json` 업데이트: phase="check", matchRate=N

**다음 단계**:
- Match Rate >= 90%: `/pdca report {feature}`
- Match Rate < 90%: `/pdca iterate {feature}`

---

## /pdca iterate {feature}

**호출 에이전트**: pdca-iterator

**조건**: Match Rate < 90%

**수행 작업**:
1. Gap 분석 결과 로드
2. Gap 항목 우선순위화
3. 코드 수정 적용
4. gap-analyzer 재호출
5. 반복 (최대 5회)
6. `.pdca-status.json` 업데이트: phase="act", iterationCount=N

**종료 조건**:
- Match Rate >= 90%: 성공 → `/pdca report`
- 최대 반복 도달: 실패 → 수동 개입 필요

---

## /pdca report {feature}

**호출 에이전트**: report-writer

**조건**: Match Rate >= 90% 권장

**수행 작업**:
1. PDCA 문서 종합
2. 변경 내역 정리
3. 교훈 정리
4. `docs/04-report/features/{feature}.report.md` 생성
5. `.pdca-status.json` 업데이트: phase="completed"

**다음 단계**: `/pdca archive {feature}`

---

## /pdca status

**수행 작업**:
1. `.pdca-status.json` 읽기
2. 현재 상태 표시

**출력 형식**:
```
PDCA Status
─────────────────────────────
Feature: {feature}
Phase: {current phase}
Match Rate: N%
Iteration: N/5
─────────────────────────────
[Plan] O → [Design] O → [Do] O → [Check] > → [Act] -
```

---

## /pdca next

**수행 작업**:
1. 현재 Phase 확인
2. 다음 단계 안내

| 현재 | 다음 | 명령어 |
|-----|-----|-------|
| 없음 | plan | `/pdca plan {feature}` |
| plan | design | `/pdca design {feature}` |
| design | do | `/pdca do {feature}` |
| do | check | `/pdca analyze {feature}` |
| check (<90%) | act | `/pdca iterate {feature}` |
| check (>=90%) | report | `/pdca report {feature}` |
| completed | archive | `/pdca archive {feature}` |

---

## /pdca archive {feature}

**조건**: phase = "completed"

**수행 작업**:
1. `docs/archive/YYYY-MM/{feature}/` 생성
2. Plan, Design, Analysis, Report 이동
3. `.pdca-status.json` 업데이트: phase="archived"
