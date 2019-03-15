# 07) Django - 데이터베이스 설계

## 1. 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- 데이터베이스 테이블 간 관계 설정(1:N)



## 2. 구현

1. 데이터베이스 설계

   - Genre(1) : Movie(N)

   - Movie(1) : Score(N)

   - Genre

     필드 : id, name

   - Movie

     필드 : id, title, audience, poster_url, description, genre_id_id

   - Score

     필드 : id, content, score, movie_id_id



2. `movies` App

   1) 제공된 csv 파일을 Database 탭을 활용해 migrate 한 후의 DB에 저장

   2) 영화 목록

   - bootstrap card component 활용

   3) 영화 정보 조회

   - 해당 영화의 모든 정보를 보여줌
   - 렌더할 html 파일을 `detail.html`과 그 안에 들어가는 `_create_score.html`(댓글 작성 및 표시)로 구분하여 구성

   4) 영화 정보 삭제

   - 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제
   - delete시 cascade 되도록 하여 해당 영화 하의 댓글도 모두 삭제

   5) 평점 생성

   - 영화 정보 조회 페이지 내의 `_create_score.html` 파일 내에 `form` 태그로 평점 생성 기능 구현

   6) 평점 목록

   - 영화 정보 조회 페이지 내의 `_create_score.html` 파일 내에, 평점 생성을 위한 form 태그 아래에 작성된 댓글 모두 표시

   7) 평점 삭제

   - 평점 목록의 `content`, `score` 옆에 `a` 태그를 활용하여 평점 삭제 기능 구현 