# Project09

django-bootstrap4 설치

json 파일 로드

User, Movie, Genre에 대해 admin 설정 및 확인



3. 유저 목록(accounts:list)

   1. accounts/list 만들기

   2. accounts/detail 만들기
      1) `Score` model 만들기

      2) first_name, last_name 및 Follow 기능 설정하기

      ### accounts/forms.py

      ```python
      from django.db import models
      from django.contrib.auth.models import AbstractUser
      from django.conf import settings
      
      
      # Create your models here.
      class User(AbstractUser):
          first_name = models.CharField(max_length=30)
          last_name = models.CharField(max_length=20)
          followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
      ```

      makemigrations, migrate

      user.comment_set에서 작성한 comment 불러오기

      팔로우 버튼 구현

      작성한 평점 정보 출력 구현

      팔로워, 팔로잉 사람 수 출력 구현

      팔로워 및 팔로잉 리스트 구현 - url 생성, views.py에 해당 리스트 출력하는 함수 구현, 리스트에서 username 클릭 시 해당 user의 상세 정보 페이지로 이동하는 링크 구현

      

4. movie app

   1. 영화 목록

      영화 제목, 영화 이미지 출력

      영화 이미지 클릭시 영화 상세보기 페이지로 이동

   2. 영화 상세보기

      영화 관련 정보 모두 나열

      평점 생성 form 삽입, 그 아래에 평점 나열 및 평점 삭제 form 삽입

   3. 평점 생성

      로그인 한 유저만 평점 생성 탭을 볼 수 있도록 설정

      `ScoreForm` 생성 및 views.py 내에 `create_score` 함수 생성, 평점 작성 기능 구현

      생성 후 해당 영화의 상세보기 페이지로 redirect

   4. 평점 삭제

      본인만 가능하도록 설정

      삭제 후 해당 영화의 상세보기 페이지로 redirect

   5. 영화 기본 추천

      

   