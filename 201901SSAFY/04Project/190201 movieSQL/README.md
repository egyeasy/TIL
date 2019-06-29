# 박스오피스 데이터베이스 생성 및 조회



### 소스

boxoffice.csv 내의 영화 정보 데이터



### 환경

- c9 workspace
- DB : sqlite3



### 1. 테이블 구성하기 (파일명 : 01_create_table.sql )

git bash 창에서 `sqlite3 pjt.sqlite3` 명령어로 DB 생성 후 sqlite3 쉘 접속

`CREATE TABLE` 쿼리로 테이블 생성

`.mode csv`, `.import boxoffice.csv movies` 명령어로 csv 파일 import

`SELECT * FROM` 쿼리로 테이블 조회





### 2. 기본 CRUD 조작하기 (파일명: 02_crud.sql )

1) 극한직업 데이터 `INSERT INTO` 쿼리로 추가.

2) 데이터 삭제
`WHERE`, `DELETE` 쿼리 활용

3) NULL 존재하는 레이블 처리
`UPDATE` 쿼리 활용



### 3. 원하는 데이터 찾기 (파일명: 03_select.sql )

다중 조건 검색, 범위 검색, 중복 제외 검색 등을 위해 다음의 조건 연산자 활용:
`WHERE`, `>=`, `==`, `AND`, `BETWEEN`, `SELECT DISTINCT`



### 4. Expression 활용하기 (파일명: 04_expression.sql )

칼럼 총계 및 평균 도출, 정렬, 조건별 레이블 수 검색을 위해 다음의 쿼리 활용:
`SUM()`, `ORDER BY`, `DESC`, `ASC`, `LIMIT`



### 5. 정렬하기 (파일명: 05_order.sql )

특정 칼럼 기준 정렬 및 상(하)위 레이블 검색을 위해 다음 쿼리 활용:
`ORDER BY`, `DESC`, `ASC`, `LIMIT`