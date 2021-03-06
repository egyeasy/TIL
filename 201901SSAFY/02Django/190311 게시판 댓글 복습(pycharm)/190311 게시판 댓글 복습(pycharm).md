### 머신러닝, 데이터분석

conda를 설치하면 머신러닝에 필요한 패키지 포함해서 깔아준다. but 기존에 설치한 파이썬 버전이랑 충돌할 수 있으므로 원래 있던 건 삭제할 것



### 64비트

```python
import sys
sys.maxsize # 64비트 컴퓨터에서는 아래와 같이 나온다
9223372036854775807
2 ** 63 - 1
9223372036854775807
```





# Django local project

파이썬 3.7.2 설치

windows는 virtualenv를 지원하지 않음.



### new project - Django

![1](.\1.PNG)



pycharm project 경로 : C:\Users\student\PycharmProjects



### settings

ctrl + alt + s : settings



1. plugin 검색 - 다음 3개 설치

- csv plugin

- .ignore

- material theme UI



2. terminal 검색 - Git bash 디폴트 설정

- Shell path: C:\Program Files\Git\bin\bash.exe



### 시작

- templates는 c9에서 만든 templates폴더와 다른 기능
- venv에는 파일이 3-4천 개. 파이썬 버전 쉽게 쓸 수 있도록 c9에서 한 발 더 나간 기능. => git에 올리면 안된다.



### git ignore

프로젝트 최상단 디렉토리에서

`$ touch .gitignore`

```.gitignore
# 가상환경 파일/디렉토리
venv/

# Python auto generated cache
__pychache__/

# Jetbrain auto generated cache
.idea/

# Default django DB - git에 올리는 것이 부적절하다고 판단
*.sqlite3
```

cf. git 지우기 : `$ rm -rf .git`



### git bash

~/PycharmProjects/first_local

```bash
git init
```

`git status` 했을 때 빨간색으로 뜨는 것은 git이 처음으로 발견한 요소들. ignore 설정해준 것은 뜨지 않는 것을 볼 수 있다.0





# 진짜 시작 - 1:n mapping(댓글)

`$ django-admin startapp board`

강사님은 django-admin으로 startapp, startproject 한다고 한다.

`$ pip install django-extensions ipython`

여기서 안 되면 pycharm 껐다 켜볼 것



### settings.py

c9에서와는 달리 ALLOWED_HOST 안써줘도 됨

```python
INSTALLED_APPS = [
    'django_extensions', # 패키지, 모듈은 여기다 쓰신다고 함
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board', # 앱 추가
]

# ... #

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False
```



### first_local/urls.py

`$ mkdir -p board/templates/board` : 경로에 폴더가 없을 때 폴더를 만들면서 감

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls'))
]
```



cf. shift 두번눌러서 파일 찾아서 들어갈 수 있다



### board/urls.py

```python
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('new/', views.new_article, name='new_article'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
]
```



### board/views.py

```python
from django.shortcuts import render


# Create your views here.
def article_list(request):
    pass


def article_detail(request, article_id):
    pass


def new_article(request):
    pass


def create_article(request):
    pass


def edit_article(request, article_id):
    pass


def update_article(request, article_id):
    pass


def delete_article(reques, article_id):
    pass


```



`$ cd board/templates/board/`

`$ touch base.html list.html detail.html new.html edit.html`

`$ cd - ` : 뒤로가기(`$ cd ..`와는 다르게 한번에 여러 디렉토리 이동 가능)



### models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(default='')
    content = models.TextField(default='')
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.id}: {self.title[:20]}' # title 20글자만 보여주기
```



### admin.py

```python
from django.contrib import admin
from .models import Article ## 추가

# Register your models here.
admin.site.register(Article)
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`

비번 : 생일

cf. shift + insert : bash 붙여넣기



### manage.py 명령어 빠르게 쓰기

alt + ctrl + r

```django bash
runserver
```

http://127.0.0.1:8000/admin/ : 관리자 페이지



### 맨 우측 Database 탭

1. +버튼 > driver > SQLite > Download > 확인

2. 왼쪽 db.sqlite3을 database 탭으로 끌고 오기

- 스키마를 볼 수 있다.
- 여기서 레이블을 직접 만드는 것은 위험. password hashing도 되지 않는다.





### base.html

cf. block + tab -> 자동완성

```html
<!doctype html>
<html lang= "ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {% block  %}
    {% endblock %}
</body>
</html>
```





## List 페이지

### views.py

```python
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })
```



### list.html

block + tab -> 자동완성

for + tab -> 자동완성

```html
{% extends 'board/base.html' %}

{% block body %}
    {% if articles %}
    <ul>
        {% for article in articles %}
            <li><a href="{%  url 'board:article_detail' article.id %}">
                {{  article.title }}
            </a></li>
        {% endfor %}
    </ul>
    {% endif %}
{% endblock %}
```

article이 없을 때 ul태그가 나오지 않도록 if문 삽입





## detail 페이지

### views.py

```python
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/detail.html', {
        'article': article,
    })
```



### detail.html

cf. ctrl + g : 원하는 줄(line)의 칸(column)으로 이동할 수 있음.

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
{% endblock %}
```





## cf. 없는 id의 detail 페이지를 요청했을 때 500 에러 페이지를 404페이지로 바꿔주기

### settings.py

```python
DEBUG = False
ALLOWED_HOSTS = ['*'] # Debug False시 이거 써줘야 함
```

이렇게 하면 페이지 렌더링 시 에러 났을 때 친절하게 설명해주지 않는다.

- 4xx : 요청 오류
- 5xx : 서버 오류



### views.py - detail

```python
from django.shortcuts import render, get_object_or_404

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'board/detail.html', {
        'article': article,
    })
```





## 새 글 페이지

### views.py

```python
from IPython import embed

def new_article(request):
    print(request.method) # request가 GET과 POST 중 어느 것을 사용하는지 보여줌
    return render(request, 'board/new.html')

def create_article(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # embed() 해당 url 들어갔을 때 시간을 멈추고 bash에 ipython이 떠야 함
    article.save()

    return redirect('board:article_detail', article.id)
```

embed() 시점의 코드에서 테스트, 디버그를 해볼 수 있다. `article.title`, `article.content` 등 쳐볼 수 있음.

ctrl + d : ipython shell 탈출



### new.html

```html
{% extends 'board/base.html' %}

{% block body %}
<h1>New article</h1>

<form action="{% url 'board:create_article' %}" method="POST">
    {% csrf_token %}
    <div>
{#        input에는 꼭 label이 따라와야한다 - id를 써줘야하는듯#}
        <label for="title">Title</label>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}
```

cf. ctrl + alt + enter : 현재줄 아래로 밀어내고 위로 커서 이동



그냥 url 접근으로 /board/create 를 들어가면 GET 요청으로 파라미터 없이 create를 호출하고, 그래서 에러 페이지가 뜨게 된다. models.py에서 다 null=True로 바꿔줘도 되지만 그렇게 하면 에러페이지는 없어지는 대신 새로운 빈 내용의 데이터들이 막 생겨나게 됨.

방법 : GET 요청 -> 새로운 페이지로 이동시킴



### views.py

```python
# def new_article(request):
#     print(request.method) # request가 GET과 POST 중 어느 것을 사용하는지 보여줌
#     return render(request, 'board/new.html')

def create_article(request):
    if request.method == 'GET':
        return render(request, 'board/new.html')
    else:
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        # embed()
        article.save()
        return redirect('board:article_detail', article.id)
```



### urls.py

```python
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('new/', views.new_article, name='new_article'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
]
```





### new.html

form 태그에 action을 써주지 않아도 됨. 제자리로 POST로 다시 이동.

```html
{% extends 'board/base.html' %}

{% block body %}
<h1>New article</h1>

<form method="POST">
    {% csrf_token %}
    <div>
{#        input에는 꼭 label이 따라와야한다 - id를 써줘야하는듯#}
        <label for="title">Title</label>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}
```





## 편집

### views.py

일단 해당 id가 있는지 찾아보고(없으면 404 에러), 그 다음 request method 로직 분기

```python
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        return render(request, 'board/edit.html', {
            'article': article,
        })
    else:
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)
```



### edit.html

```html
{% extends 'board/base.html' %}

{% block body %}
<h1>Edit article</h1>

<form method="POST">
    {% csrf_token %}
    <div>
{#        input에는 꼭 label이 따라와야한다 - id를 써줘야하는듯#}
        <label for="title">Title</label>
        <input type="text" name="title" id="title" value="{{ article.title }}">
    </div>
    <div>
        <label for="content">Content</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
{% endblock %}
```



### urls.py

```python
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('new/', views.new_article, name='new_article'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    # path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
]
```





## 삭제

POST 방식으로 요청 보냈을 때만 삭제하도록 만든다.

### detail.html

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}">
        <button>목록으로 가기</button>
    </a>
    <a href="{% url 'board:update_article' article.id %}">
        <button>수정하러 가기</button>
    </a>
    <form action="{% url 'board:delete_article' article.id %}" method="POST">
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>
{% endblock %}
```



### views.py

```python
def delete_article(request, article_id):
    if request.method == 'GET':
        return redirect('board:article_detail', article_id)
    else:
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('board:article_list')
```





## 댓글 기능 - 보여주기

### models.py

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.article.title}: {self.content}'
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`

오른쪽 DB탭에서 새로고침 눌러주면 업데이트 된 결과 볼 수 있음



### views.py

```python
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()
    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
    })
```



### admin.py

```python
from django.contrib import admin
from .models import Article, Comment ## 추가


# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```



### detail.html

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}">
        <button>목록으로 가기</button>
    </a>
    <a href="{% url 'board:update_article' article.id %}">
        <button>수정하러 가기</button>
    </a>
    <form action="{% url 'board:delete_article' article.id %}" method="POST">
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>

    <form action="">
        <label for="comment">comment</label>
        <input type="text" name="comment" id="comment"> <!-- form 안의 input은 엔터치면 자동 submit -->
    </form>

    {% if comments %}
        <ul>
            {% for comment in comments %}
                <li>{{ comment.content }}</li>
            {% endfor %}
        </ul>
    {% endif %}
```





## 댓글 기능 - 수정, 삭제

### urls.py

```python
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('new/', views.new_article, name='new_article'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    # path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),

    path('<int:article_id>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:article_id>/delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
]
```





### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

def create_comment(request, article_id):
    # article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment = Comment()
        # comment.article_id = article.id # 아래와 같은 기능
        # comment.article = article
        comment.article = get_object_or_404(Article, id=article_id)
        comment.content = request.POST.get('comment')
        comment.save()
    return redirect('board:article_detail', article_id)


def delete_comment(request, article_id, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
    return redirect('board:article_detail', article_id)
```



### detail.html

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}">
        <button>목록으로 가기</button>
    </a>
    <a href="{% url 'board:update_article' article.id %}">
        <button>수정하러 가기</button>
    </a>
    <form action="{% url 'board:delete_article' article.id %}" method="POST">
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>

    <form action="{% url 'board:create_comment' article.id %}" method="POST">
        {% csrf_token %}
        <label for="comment">comment</label>
        <input type="text" name="comment" id="comment"> <!-- form 안의 input은 엔터치면 자동 submit -->
    </form>

    {% if comments %}
        <ul>
            {% for comment in comments %}
                <li>{{ comment.content }}</li>
            {% endfor %}
        </ul>
    {% endif %}

{% endblock %}
```





## html refactoring

return render에서 쓰지 않는 html들은 이름 제일 앞에 '_'가 붙고, 부품처럼 다른 html에 들어가게 된다. 

### templates/board/_comment.html

```html
<form action="{% url 'board:create_comment' article.id %}" method="POST">
    {% csrf_token %}
    <label for="comment">comment</label>
    <input type="text" name="comment" id="comment" autofocus> <!-- form 안의 input은 엔터치면 자동 submit. autofocus 기능 추가 -->
<!-- autofocus는 댓글 생성하고 난 뒤에도 계속 커서가 댓글 폼에 있게 한다 -->
</form>

{% if comments %}
    <ul>
        {% for comment in comments %}
            <li>{{ comment.content }}</li>
        {% endfor %}
    </ul>
{% endif %}
```



### detail.html

부품을 넣을 지점을 `include`로 표시

```html
{% extends 'board/base.html' %}
{% block body %}
    <h1>{{ article.title }}</h1>
    <p>
        {{ article.content }}
    </p>
    <p>
        {{ article.like }}
    </p>
    <a href="{% url 'board:article_list' %}">
        <button>목록으로 가기</button>
    </a>
    <a href="{% url 'board:update_article' article.id %}">
        <button>수정하러 가기</button>
    </a>
    <form action="{% url 'board:delete_article' article.id %}" method="POST">
        {% csrf_token %}
        <button type="submit">삭제하러 가기</button>
    </form>
{% include 'board/_comment.html' %} <!-- 여기에 include 추가 -->
{% endblock %}
```



### list.html

```html
{% extends 'board/base.html' %}

{% block body %}
    {% if articles %}
    <ul>
        {% for article in articles %}
            <li><a href="{%  url 'board:article_detail' article.id %}">
                {{ article.title }} - ({{ article.comment_set.count }}) <!-- html에서는 sql 괄호 쓰지 않는다 -->
            </a></li>
        {% endfor %}
    </ul>
    {% endif %}
{% endblock %}
```





## cf. version control, TODO

- 아랫단 version control > log 들어가면 변경사항 확인 가능
- 아랫단 TODO > 해야할 일 리스트 확인 가능

### _comment.html

todo는 주석 태그 안에 작성. python 파일에서도 사용 가능.

```html
<form action="{% url 'board:create_comment' article.id %}" method="POST">
    {% csrf_token %}
    <label for="comment">comment</label>
    <input type="text" name="comment" id="comment" autofocus> <!-- form 안의 input은 엔터치면 자동 submit -->
<!-- autofocus는 댓글 생성하고 난 뒤에도 계속 커서가 댓글 폼에 있게 한다 -->
</form>

{% if comments %}
    <ul>
        {% for comment in comments %}
            <li>{{ comment.content }}</li>
            {# TODO: implement comment delete UI #}
        {% endfor %}
    </ul>
{% endif %}
```







