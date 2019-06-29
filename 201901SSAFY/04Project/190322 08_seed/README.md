# 08) Django - Seed Data

## 1. 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Seed Data를 활용한 DB 설계
- Django Form을 통해 입력받은 데이터 유효성 검증



## 2. 구현 사항

1. 데이터베이스 설계

   - Genre - Movie와 1:N 관계, Movie의 foreign key
   - Movie - Score와 1:N 관계, Score의 foreign key
   - Score

2. Seed Data 반영

   `movie.json`과 `genre.json`을 `movies/fixtures/` 디렉토리로 옮긴 후, 명령어를 통해 DB로 가져옴

3. movie App

   1. 영화 생성을 위한 사용자 Form
      - a 태그 활용
      - 영화 수정 페이지와 템플릿 파일 공유(`form.html`)
   2. 영화 생성
      - 입력된 데이터 유효성 검증
      - 데이터가 유효하지 않은 경우 bootstrap alert component를 통해 오류 메시지를 출력하고 `form.html` 반환
      - 데이터가 유효한 경우 데이터를 DB에 저장하고 영화 정보 조회 페이지로 redirect
   3. 영화 수정을 위한 사용자 Form
      - 영화 정보 조회 페이지에서 a 태그 활용
      - 영화 생성 페이지와 템플릿 파일 공유(`form.html`)
      - 수정되기 이전의 데이터를 input 내에 채워서 제공
   4. 영화 수정
      - 입력된 데이터 유효성 검증
      - 데이터가 유효하지 않은 경우 bootstrap alert component를 통해 오류 메시지를 출력하고 `form.html` 반환
      - 데이터가 유효한 경우 데이터를 DB에 저장하고 영화 정보 조회 페이지로 redirect
   5. 평점 생성
      - 영화 정보 조회 페이지에서 form 태그 활용
      - 입력된 데이터 유효성 검증
      - 데이터가 유효하지 않은 경우 bootstrap alert component를 통해 오류 메시지를 출력하고 영화 정보 조회 페이지로 redirect
      - 데이터가 유효한 경우 데이터를 DB에 저장하고 해당 영화의 영화 정보 조회 페이지로 redirect