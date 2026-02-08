# 🛠️ Antigravity 스킬 및 에이전트 가이드

Antigravity 시스템에 등록된 스킬(Skills)과 에이전트(Agents), 그리고 워크플로우의 기능과 사용법 정리 문서입니다.

## 1. 개발 및 코드 품질 (Development & Quality)

| 이름 | 기능 (Features) | 사용법 (Usage) |
| :--- | :--- | :--- |
| **Code Reviewer**<br>(`code-reviewer`) | 코드 품질, 보안, 아키텍처, 스타일을 선제적으로 검토하고 개선안을 제안합니다. | "이 코드 리뷰해줘", "방금 짠 코드 점검해줘"<br>*(코드 변경 후 자동 제안되기도 함)* |
| **Debugger**<br>(`debugger`) | 에러 로그와 스택 트레이스를 분석하여 근본 원인(RCA)을 찾고 수정을 제안합니다. | "이 에러 고쳐줘", "테스트가 실패하는 이유가 뭐야?" |
| **API Client Generator**<br>(`api-client-generator`) | Base URL이나 JSON 스키마를 입력받아 Python(`requests`) 또는 TS 클라이언트 코드를 생성합니다. | "https://api.example.com용 파이썬 클라이언트 만들어줘" |

## 2. 데이터 및 콘텐츠 (Data & Content)

| 이름 | 기능 (Features) | 사용법 (Usage) |
| :--- | :--- | :--- |
| **Data Scientist**<br>(`data-scientist`) | SQL 쿼리 작성, 데이터 분석, BigQuery 연동 등을 수행하여 인사이트를 도출합니다. | "이 데이터에서 월별 매출 추이 뽑아줘", "SQL 쿼리 최적화해줘" |
| **YouTube Collector**<br>(`youtube-collector`) | 유튜브 채널을 등록하고, 새 영상과 자막을 수집하여 요약본을 생성합니다. | **채널 등록**: "유튜브 채널 @침착맨 등록해줘"<br>**수집**: "새 영상 수집해줘"<br>**확인**: ".reference 폴더 확인해줘" |
| **Brand Logo Finder**<br>(`brand-logo-finder`) | Brandfetch를 통해 브랜드의 공식 로고, 색상, 아이콘 에셋을 찾습니다. | "보스(Bose) 로고 찾아줘", "Spotify 브랜드 컬러 알려줘" |

## 3. 크리에이터 도구 (Meta-Tools)
*시스템 자체를 확장하는 도구들입니다.*

| 이름 | 기능 (Features) | 사용법 (Usage) |
| :--- | :--- | :--- |
| **Skill Creator**<br>(`skill-creator`) | 새로운 스킬을 생성하기 위한 템플릿과 가이드를 제공합니다. | "이미지 리사이징 스킬 만들어줘", "새 스킬 만드는 법 알려줘" |
| **Sub-agent Creator**<br>(`subagent-creator`) | 특정 역할(페르소나)과 툴을 가진 전용 서브 에이전트를 만듭니다. | "기술 문서 작성 전용 에이전트 만들어줘" |
| **Slash Command Creator**<br>(`slash-command-creator`) | 자주 쓰는 프롬프트를 `/command` 형태로 만듭니다. | "자주 쓰는 배포 명령어를 슬래시 커맨드로 등록해줘" |
| **Hook Creator**<br>(`hook-creator`) | 특정 이벤트(파일 저장 등) 발생 시 실행될 자동화 훅을 만듭니다. | "저장할 때마다 포맷팅하는 훅 만들어줘" |

---

# ⚡ 워크플로우 (Slash Commands)

자주 사용하는 복합 작업을 단축키처럼 실행합니다.

| 명령어 | 설명 | 실행 방법 |
| :--- | :--- | :--- |
| **/optimize** | 코드를 분석하여 성능 병목을 찾고 최적화된 코드를 제안합니다. | 채팅창에 `/optimize` 입력 |
| **/security-review** | 코드의 보안 취약점(SQLi, 비밀키 노출 등)을 점검합니다. | 채팅창에 `/security-review` 입력 |
| **/framer-clone** | 디자인 파이프라인. Framer 사이트를 분석하여 React 코드로 변환합니다. | 채팅창에 `/framer-clone` 입력 |
| **/daily** | 오늘 진행한 작업을 수집, 요약하여 일일 보고서를 작성합니다. | 채팅창에 `/daily` 입력 |
| **/pdca** | Plan-Design-Do-Check-Act 방법론에 따른 구조화된 개발을 진행합니다. | 채팅창에 `/pdca` 입력 |
| **/starter** | 새 프로젝트를 위한 PDCA 개발 환경을 초기화합니다. | 채팅창에 `/starter` 입력 |

---

### 💡 팁
- 스킬들은 **필요할 때 자연어로 요청**하면 자동으로 호출됩니다.
- 워크플로우는 **채팅창에 `/`를 입력**하여 직접 호출하는 것이 정확합니다.
- `youtube-collector`와 같이 설정이 필요한 스킬은 **최초 1회 설정**(API 키 등)이 필요할 수 있습니다.
