# 06) Django Intro

## 1. 목표

- Django ORM을 활용하여 데이터를 생성, 조회, 삭제할 수 있는 Web Application 제작



## 2. 준비 사항

1. Python Web Framework
   - Django
   - Python
2. 샘플 영화 정보
   - `data.csv`



## 3. 구현

1. 데이터베이스

   1) Django 프로젝트 생성

   ### Git bash

   ```bash
   mkdir PROJECT06
   cd PROJECT06
   
   pyenv virtualenv 3.6.7 project06-venv
   pyenv local project06-venv
   
   pip install django django_extension ipython
   django-admin startproject project06 .
   
   python manage.py startapp movies
   ```

   `settings.py` 에서 앱과 url에 대해 초기 설정.

   

   2) 테이블 생성

   ### models.py

   ```python
   from django.db import models
   
   # Create your models here.
   class Movie(models.Model):
       title = models.TextField()
       audience = models.IntegerField()
       genre = models.TextField()
       score = models.FloatField()
       poster_url = models.TextField()
       description = models.TextField()
   ```

   

   3) `data.csv` 조회 및 정보 가져오기

   ### Git bash

   ```bash
   python manage.py makemigrations
   python manage.py sqlmigrate movies 0001
   python manage.py migrate
   python manage.py shell_plus
   ```

   

   ### shell plus

   ```python
   import csv
   with open('data.csv', 'r') as f:
       reader = csv.DictReader(f)
           for row in reader:
               movie = Movie(**row)
               movie.save()
   ```

   

2. 페이지

   프로젝트 폴더 아래의 `urls.py` 설정

   ### urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   from movies import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home)
     	path('movies/', include('movies.urls')),
   ]
   ```

   

   base 템플릿으로 `base.html` 생성

   ### base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       <title>영화 정보</title>
   </head>
   <body>
       {% block body %}
       {% endblock %}
   </body>
   </html>
   ```

   

   

   1. 영화 목록

      ### views.py

      ```python
      from django.shortcuts import render, redirect
      from .models import Movie
      
      def home(request):
          
          return redirect('movies:index')
      
      def index(request):
          movies = Movie.objects.all()
          context = {
              'movies': movies
          }
          return render(request, 'index.html', context)
      ```

      

      ### urls.py

      ```python
      from django.urls import path
      from . import views
      
      app_name = 'movies'
      
      urlpatterns = [
          path('', views.index, name='index'),
      ]
      ```

      

      ### index.html

      ```html
      {% extends 'base.html' %}
      
      {% block body %}
      <table class="table">
        <thead>
          <tr>
            <th scope="col">제목</th>
            <th scope="col">평점</th>
          </tr>
        </thead>
        <tbody>
          {% for movie in movies %}
          <tr>
            <th scope="row"><a href="{% url 'movies:detail' movie.id %}">{{ movie.title }}</a></th>
            <td>{{ movie.score }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
      {% endblock %}
      ```

   

   

   2. 영화 정보 조회

      ### views.py

      ```python
      def detail(request, movies.id):
          movie = Movie.objects.get(pk=moives.id)
          context = {
              'movie': movie
          }
          
          return render(request, 'detail.html', context)
      ```

      

      ### urls.py

      ```python
      from django.urls import path
      from . import views
      
      urlpatterns = [
          path('', views.index, name='index'),
          path('<int:movies.id>/', views.detail, name='detail'),
      ]
      ```

      

      ### detail.html

      ```html
      {% extends 'base.html' %}
      
      {% block body %}
          <h3>{{ movie.title }}</h3>
          <h3>{{ movie.adience }}</h3>
          <h3>{{ movie.genre }}</h3>
          <h3>{{ moive.score }}</h3>
          <h3>{{ movie.poster_url }}</h3>
          <h3>{{ movie.description }}</h3>
      
      	<a href="{% url 'movies:index' %}">목록</a>
      	<a href="{% url 'movies:edit' movie.id %}">수정</a>
      	<a href="{% url 'movies:delete' movie.id %}">삭제</a>
      {% endblock %}
      ```

      

      

   3. 영화 정보 삭제

      ### views.py

      ```python
      def delete(request, movies_id):
          movie = Movie.objects.get(pk=movies_id)
          movie.delete()
          
          return redirect('movies:index')
      ```

      

      ### urls.py

      ```python
      from django.urls import path
      from . import views
      
      app_name = 'movies'
      
      urlpatterns = [
          path('', views.index, name='index'),
          path('<int:movies_id>/', views.detail, name='detail'),
          path('<int:movies_id>/delete', views.delete, name='delete'),
      ]
      ```

