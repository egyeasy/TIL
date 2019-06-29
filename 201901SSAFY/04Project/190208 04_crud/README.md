# 영화 DB 만들기

## 1. 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- 영화 추천 사이트의 영화 정보 데이터 관리



## 2. 준비 사항

1. Flask Framework 사용을 위한 환경 설정
   - C9 개발 가능 환경
2. SQLAlchemy 사용



## 3. 요구 사항

1. 데이터베이스
   - `movie.sqlite3` : 데이터베이스 파일
   - `movies` : 테이블 이름
   - 필드명 : 내용, 자료형
     - the_id : Integer id(Primary Key)
     - title : String 영화명
     - title_en : String 영화명(영문)
     - audience : Interger 누적 관객수
     - open_date : String(기본) / DateTime(선택) 개봉일
     - genre  : String 장르
     - watch_grade : String 관람등급
     - score : Float 평점
     - poster_url  : TEXT 포스터 이미지 URL
     - description : TEXT 영화소개



2. 페이지

   1. 영화 목록 - DB 내에 존재하는 모든 영화의 목록 표시(각 영화의 `title`, `score`, `genre`, `open_date` 표시)
      - URL : /movies/
      - SQL : `movies = Movie.query.all()`
      - bootstrap button - '새 영화 등록' 버튼 클릭 시 '영화 정보 생성 Form' 페이지로 이동
      - a 태그 - `title` 클릭을 통한 '영화 정보 조회' 페이지 이동 링크

   

   2. 영화 정보 생성 Form - 영화 정보를 작성하는 Form을 보여주는 페이지
      - URL : /movies/new/
      - input, textarea 태그 :  id를 제외한 모든 정보 수정(입력)
      - Submit 버튼 누를 시 '영화 정보 생성' 페이지로 request 전송

   

   3. 영화 정보 생성 - 이전 페이지로부터 전송 받은 데이터를 데이터베이스에 저장

      - URL : /movies/create/

      - flask.request : '영화 정보 생성 Form' 페이지로부터 받은 요청을 처리

      - 데이터 입력 SQL : 

        ```python
        m = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
        db.session.add(m)
        db.session.commit()
        ```

      - redirection을 위한 DB 조회 SQL : `idx = Movie.query.order_by(Movie.the_id.desc()).first().the_id`

      - 작성한 영화 정보 페이지로 redirect : `return redirect('/movies/{}'.format(idx))`

   

   4. 영화 정보 조회 페이지 - 특정 Primary key를 가진 영화의 모든 정보 표시
      - URL : /movies/<movie_id>
      - SQL : `'m = Movie.query.get(movie_id)`
      - render_template 시에 SQL을 통해 받아온 정보를 함께 넘김
      - a 태그 : 영화 목록, 수정, 삭제 페이지 이동 링크

   

   5. 영화 정보 수정 Form - 특정 Primery key를 가진 영화 정보를 수정할 수 있는 Form이 표시되며, 정보가 입력된 채로 다음과 같은 input들을 가지고 있음
      - `description` - textarea
        `input text` - id, textarea를 제외한 나머지
      - URL : /movies/<movie_id>/edit
      - submit : '영화 정보 수정' 페이지로 수정 요청

   

   6. 영화 정보 수정 - 해당 Primary key를 가진 영화 정보를 이전 페이지로부터 전송 받은 데이터로 변경하여 데이터베이스에 저장

      - URL : /movies/<movie_id>/update

      - flask.request : 이전 페이지로부터 받은 데이터 처리

      - 데이터 수정 SQL :

        ```python
            title = request.args.get('title')
            title_en = request.args.get('title_en')
            audience = request.args.get('audience')
            open_date = request.args.get('open_date')
            genre = request.args.get('genre')
            watch_grade = request.args.get('watch_grade')
            score = request.args.get('score')
            poster_url = request.args.get('poster_url')
            description = request.args.get('description')
            
            m = Movie.query.get(movie_id)
            m.title = title
            m.title_en = title_en
            m.audience = audience
            m.open_date = open_date
            m.genre = genre
            m.watch_grade = watch_grade
            m.score = score
            m.poster_url = poster_url
            m.description = description
            db.session.commit()
        ```

      - 수정한 영화 정보 조회 페이지로 redirect : ` return redirect('/movies/{}'.format(movie_id))`

   

   7. 영화 정보 삭제 - 해당 Primery key를 가진 영화 정보를 데이터베이스에서 삭제

      - URL : /movies/<movie_id>/delete

      - 데이터 삭제 SQL :

        ```python
        m = Movie.query.get(movie_id)
            db.session.delete(m)
            db.session.commit()
        ```

      - 영화 목록 페이지로 redirect : `return redirect('/movies')`