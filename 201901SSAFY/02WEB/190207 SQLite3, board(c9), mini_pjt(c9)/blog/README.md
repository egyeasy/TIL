# 블로그 만들기

## 1. 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- sqlite3를 통한 데이터 조작



## 2. 준비 사항

1. Flask Framework 사용을 위한 환경 설정
   - C9 개발 가능 환경
2. sqlite3 사용



## 3. 요구 사항

1. 데이터베이스
   - `blog.db` : 데이터베이스 파일
   - `articles` : 테이블 이름
   - 필드명 : 내용, 자료형
     - `title` : 제목, String
     - `content` : 내용, String
     - `created_at` : 작성일자, String
     - `author` : 글쓴이(이메일), String



2. 페이지

   1. 글 목록 - DB 내에 존재하는 모든 블로그 글의 목록 표시(각 블로그 글의 `title` 표시)
      - URL : /articles/
      - SQL : `SELECT * FROM articles`
      -  a 태그 - 새 글 등록 링크, `title` 클릭을 통한 글 상세 정보 페이지 이동 링크

   

   2. 새 글 생성 Form - 새 글의 정보를 입력하는 Form을 보여주는 페이지
      - URL : /articles/new/
      - input, textarea 태그 : `title`, `content`, `author` 정보 입력
      - Submit 버튼 누를 시 새 글 생성 페이지로 request 전송

   

   3. 새 글 생성 - 이전 페이지로부터 전송 받은 데이터를 데이터베이스에 저장
      - URL : /articles/create/
      - flask.request : 새 글 생성 Form 페이지로부터 받은 요청을 처리
      - datetime : Submit 당시의 시각(`created_at`) 기록
      - 데이터 입력 SQL : `INSERT INTO articles (title, content, author, created_at) VALUES ("{}", "{}", "{}", "{}")'.format(title, content, author, created_at)`
      - redirection을 위한 DB 조회 SQL : `SELECT id FROM articles ORDER BY id DESC LIMIT 1`
      - 작성한 글 상세 페이지로 redirect : `return redirect('/articles/{}'.format(article_id))`

   

   4. 글 상세 페이지 - 특정 Primary key를 가진 글의 모든 정보 표시
      - URL : /articles/<article_id>
      - SQL : `'SELECT * FROM articles WHERE id == {}'.format(article_id)`
      - render_template 시에 SQL을 통해 받아온 정보를 함께 넘김
      - a 태그 : 글 목록, 수정, 삭제 페이지 이동 링크

   

   5. 글 수정 Form - 특정 Primery key를 가진 글 정보를 수정할 수 있는 Form이 표시되며, 정보가 입력된 채로 다음과 같은 input들을 가지고 있음
      - `title` - input text
        `content` - textarea
        `author` - input text
      - URL : /articles/<article_id>/edit
      - submit : 글 수정 페이지로 수정 요청

   

   6. 글 수정 - 해당 Primary key를 가진 글 정보를 이전 페이지로부터 전송 받은 데이터로 변경하여 데이터베이스에 저장
      - URL : /articles/<article_id>/update
      - flask.request : 이전 페이지로부터 받은 데이터 처리
      - datetime : `created_at` 업데이트
      - 데이터 수정 SQL : `'UPDATE articles SET title = "{}", content = "{}", author = "{}", created_at = "{}" WHERE id == {}'.format(edits.get('title'), edits.get('content'), edits.get('author'), created_at, article_id)`
      - 수정한 글 상세 페이지로 redirect : ` return redirect('/articles/{}'.format(article_id))`

   

   7. 글 삭제 - 해당 Primery key를 가진 글 정보를 데이터베이스에서 삭제
      - URL : /articles/<article_id>/delete
      - 데이터 삭제 SQL : `'DELETE FROM articles WHERE id == {}'.format(article_id)`
      - 글 목록 페이지로 redirect : `return redirect('/articles')`