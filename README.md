# gmp_lite
GMP lite

웹페이지 제작 관련 프로젝트

## 사용 기술스택

|분야|라이브러리 명|상세|
|----|-------------|----|
|Front-end|Vue.js 2.x|.|
|Web framework|Django 3.2|.|

+ 나머지는 TBD

## 브랜치 전략


|브랜치명|상세설명|
|--------|--------|
|`main`|프로덕션 브랜치|
|`rc/x.y.z`|베타 테스트 브랜치|
|`dev/issue_{issue 번호}`|개발 브랜치|

### 머지 조건
+ 1인 이상 리뷰 후 머지

## 권장 라이브러리

+ [autoenv](https://github.com/hyperupcall/autoenv) (링크 참고)
+ EnvFile (PyCharm 서드파티 플러그인)

## 개발환경 설정

### Python 설치

1. Pipenv 를 통해 설치
2. virtualenv 를 통해 설치

### DB, 캐싱 등
1. 로컬 개발 시 `local.yml` 파일을 `docker-compose`로 구동
2. 아래와 같은 방식으로 `.env` 파일 추가

```dotenv
DATABASE_URL=postgres://debug:debug@localhost:5432/gmp
POSTGRES_HOST=192.168.0.17
POSTGRES_PORT=5432
POSTGRES_DB=gmp
POSTGRES_USER=debug
POSTGRES_PASSWORD=debug

REDIS_URL=redis://localhost:6379/0

USE_DOCKER=yes
```

3. `python manage.py migrate`
4. 서버 구동
