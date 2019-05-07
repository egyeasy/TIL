# Project10 API

## 1. 목표

- RESTful API 서버 구축



## 2. 준비 사항

- Django 2.1.8
- Python 3.6.7
- c9 workspace(ruby on rails)



## 3. 구현 사항

### 프로젝트, 앱 스타트

c9 터미널에서

`$ mkdir PROJECT10`

`$ cd PROJECT10`

`$ pyenv virtualenv 3.6.7 pjt10-venv`

`$ pyenv local pjt10-venv`

`$ pip install django==2.1.8`

`$ django-admin startproject pjt10 .`

`$ python manage.py startapp movies`



### django-rest-framework 설치

`$ pip install djangorestframework`



### settings.py

```python
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'movies',
]
```



### movies/models.py

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=500)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Score(models.Model):
    content = models.CharField(max_length=50)
    score = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content, self.score
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



`movies` 앱 폴더 내에 `fixtures` 폴더를 생성하고 안에 `genre.json`, `movie.json`을 넣어준다.

`$ python manage.py loaddata genre.json`

`$ python manage.py loaddata movie.json`



### movies/admin.py

```python
from django.contrib import admin
from .models import Genre, Movie, Score

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Score)
```



`$ python manage.py createsuperuser`

슈퍼유저 생성



`$ python manage.py runserver $IP:$PORT`

`/admin`으로 가서 실제 데이터베이스에 migration 및 loaddata 작업이 잘 수행되었는지 확인.



### pjt10/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
]
```



### movies/urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_id>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('scores/<int:score_id>/', views.score_detail),
]
```



### movies/serializer.py

```python
from rest_framework import serializers
from .models import Genre, Movie, Score


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience',
                'poster_url', 'description', 'genre']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score', 'movie']
```



### movies/views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Score
from .serializer import GenreSerializer, MovieSerializer, ScoreSerializer

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    serializer = GenreSerializer(genre)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def score_detail(request, score_id):
    score = Score.objects.get(pk=score_id)
    serializer = ScoreSerializer(score)
    return Response(data=serializer.data)
```



기본적인 정보들이 그대로 나오는 것을 확인할 수 있다.

단, 특정 genre를 요청하였을 때 그에 해당되는 movie_set을 담아서 보내주는 등의 기능은 아직 미구현.





























