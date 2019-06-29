 # Django CRUD(c9: first-django)

## 폴더이름 : BONBON

가상환경 생성, 장고 설치



### faker python  - 페이크 데이터를 자동으로 만들어줌

사이트 들어가보면 설치법부터 볼 수 있음

`$ pip install faker`

fake name, fake 주소, fake text 만들 수 있다.



### faker example

```python
from faker import Faker
fake = Faker()
fake.name()
fake.name() # 매번 다른 이름이 리턴
fake.address()
fake.text()

# Localization : 한국어를 쓰고 싶다면
fake = Faker('ko_KR')
fake.name()
fake.name()
fake.address()
```



### 명세

**'/'** 

```html
<h1>전생앱</h1>
<p>전생을 알려드립니다.</p>
<form>사용자의 이름을 입력받아, => /pastlife</form>
```



**'/pastlife'** 

- 'XX님의 전생은 YY였습니다.'

- faker를 통해 가짜 직업을 보여줌



### view.py

context로 만들어서 넣어도 된다.

```python
def pastlife(request):
    # 1. index에서 넘어온 이름을 받고,
    name = request.GET.get('name')
    
    # 2. faker를 통해 가짜 전생(직업)을 생성하여
    fake = Faker('ko_KR')
    job = fake.job()
    
    # 3. pl.html에 뿌려준다.
    context = {
        'name': name,
        'job': job,
    }
    return render(request, 'pl.html', context)
```







## DB 만들기

한번 나왔던 값이라면 같은 결과가 나오도록 해보자.



### models.py

```python
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField()
    job = models.TextField()
```



`$ python manage.py makemigrations`

: `pastlife\migrations\0001_initial.py` 에 가면 요청한 대로 만들어진 걸 볼 수 있다.



`$ python manage.py sqlmigrate pastlife 0001`

: pastlife(앱 이름)의 0001 버전(migrations 파일의 id)을 만들기 위해 어떤 sql을 썼는지 볼 수 있음

id는 알아서 NOT NULL PRIMARY KEY AUTOINCREMENT. 다른 column들도 NOT NULL이 default.



`$ python manage.py migrate`

: migrate 시킨다.



`$ sqlite3 db.sqlite3`

`.tables` 보면 pastlife_job으로 table이 만들어져있음.(appname_tablename)

`.exit`



`$ python manage.py shell`

interactive shell 열기



```python
from pastlife.models import Job
Job.objects.all() # queryset이라는 list 안에 넣어서 줌
j = Job(name="강동주", job="셔터맨") # 인스턴스 만들기
j.save()
## 다음과 같이 만들어도 똑같다. ##
Job.objects.create(name="한동훈", job="아이돌") # 바로 만들기

Job.objects.all() # <QuerySet [<Job: Job object (1)>, <Job: Job object (2)>]>

Job.objects.first().name
Job.objects.first().job

Job.objects.all()[1].name # 모든 것 중에서 1번 index의 name
```



### models.py - `__repr__`

객체 보여주는 방식 변경하기(default: `<QuerySet [<Job: Job object (1)>, <Job: Job object (2)>]>`)

```python
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField()
    job = models.TextField()
    
    def __repr__(self):
        return f"{self.name}: {self.job}"
```

`__repr__`은 queryset에 담겨 있을 때 보여주고, print(object)를 통해서 보면 `__str__`이 보인다.



쉘을 껐다가(`exit()`) 켠다.

`$ python manage.py shell`

```python
from pastlife.models import Job
Job.objects.all()
print(Job.objects.first())
```

print 했을 땐 디폴트 대로 보임 => `__str__` 설정해줘야



### models.py - `__str__`

```python
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField()
    job = models.TextField()
    
    def __repr__(self):
        return f"{self.name}: {self.job}"
        
    def __str__(self):
        return f"<{self.name}: {self.job}>"
```



쉘 껐다가 켠다.

`$ python manage.py shell`

```python
from pastlife.models import Job
print(Job.objects.first())
```



이제 db를 조회해보자.

### views.py

```python
from django.shortcuts import render
from .models import Job # DB 쓰기 위해 import 해준다(같은 위치에 있는 model.py)
from faker import Faker
```



### Shell

```python
Job.objects.get(name="강동주")
Job.objects.get(name="김경태") # 에러
Job.objects.filter(name="김경태").first() # 없어도 아무 것도 출력하지 않음. None 반환.

person = Job.objects.filter(name="김경태").first()
print(person) # None

person2 = Job.objects.filter(name="한동훈").first()
print(person2) # 제대로 출력

person3 = Job.objects.get(name="박보윤") # get은 에러 출력
 
Job.objects.filter(name="한동훈") # object들을 queryset에 넣어줌. 두 명 이상이어도 괜춘
# <class 'django.db.models.query.QuerySet'>
Job.objects.get(name="한동훈") # object 하나만 반환(repr). "한동훈"이 두 명 이상이면 error 출력
# <class 'pastlife.models.Job'>
```





### GIPHY

움짤(.gif)에 직업 검색해서 넣어주기

https://developers.giphy.com/ -> 회원가입

create a new app -> Api key 생성됨



https://developers.giphy.com/docs/ -> get started documents

`Search`를 쓸 것

GET 방식 -> 브라우저로 URL 들어가봐도 바로 될 것

`http://api.giphy.com` (HOST) + `/v1/gifs/search` (PATH) + `?api_key=SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq` (Parameter) + `&q=의사` + `&limit=1` + `&lang=ko`

=> api.giphy.com/v1/gifs/search?api_key=SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq&q=의사&limit=1&lang=ko

주소창에 넣으면 json으로 보여줌(json viewer extension)

이 중에서 "original"의 url을 쓸 것이다!



- requests 요청 보내려면 `$ pip install requests` 해야!







## 게시판 만들기(app: articles)

여기서는 앱의 url을 분리하도록 한다.

articles\urls.py 생성



### 기존 urls.py

```python
from django.contrib import admin
from django.urls import path, include # inclue 추가
from pastlife import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pastlife/', views.pastlife),
    path('articles/', include('articles.urls')) # articles 요청이 들어오면 articles 안의 urls.py에게 넘겨줘
]
```





### articles\urls.py

```python
from django.urls import path # 기존 urls.py에서 복붙
from . import views # 같은 폴더에 있는 views.py를 가져오겠음

# articles를 일일이 써줄 필요가 없다!
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
]
```



### views.py

```python
from django.shortcuts import render

# Create your views here.
# 1. /articles -> 모든 글을 보여주는 곳(제목만)
# 2. /articles/1 -> 글 상세하게 보는 곳
# 3. /articles/new -> 새 글을 작성
# 4. /articles/create -> 새 글을 저장
# 5. /articles/1/edit -> 글을 편집
# 6. /articles/1/update -> 글을 수정
# 7. /articles/1/delete -> 글을 삭제

def index(request):
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')
```



articles 아래에 templates 폴더 생성

그 밑에 'index.html' 만들어도 이동되지 않는다. templates 폴더는 모두 동일한 걸로 취급되고, 이전에 만들었던 데서 index.html을 가져오기 때문. 두 개가 경쟁할 때는 settings.py에서 `INSTALLED_APPS`에 넣은 순으로 우선순위 부여.

-> pastlife\templates\pastlife 폴더를 만들고 그 안의 기존 pastlife html 파일들을 넣어준다.

-> pastlife\views.py 수정



### pastlife\view.py

```python
from django.shortcuts import render
from .models import Job # DB 쓰기 위해 import 해준다(같은 위치에 있는 model.py)
from faker import Faker
import requests, os

# Create your views here.
def index(request):
    return render(request, 'pastlife/index.html')
    
    
def pastlife(request):
    pass
```





### news.html

news.html 생성

```python
<h1>새 게시물 쓰기</h1>
<form action="/articles/create/"/> <!-- 앞뒤를 다 닫는다. django앱에서 뒤를 다 닫기 때문 -->
    <input type="text" name="title"/> <!-- />:self closing tag. react(있어야 함) 아닌 이상 있어도 없어도 됨 -->
    <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
</form>
```





### models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



cf. GET 쓸 때 'pk' 대신 'id'라고 써줘도 된다.



## 완성본

### views.py

```python
from django.shortcuts import render
from .models import Article
from django.shortcuts import redirect

# Create your views here.
# 1. /articles -> 모든 글을 보여주는 곳(제목만)
# 2. /articles/1 -> 글 상세하게 보는 곳
# 3. /articles/new -> 새 글을 작성
# 4. /articles/create -> 새 글을 저장
# 5. /articles/1/edit -> 글을 편집
# 6. /articles/1/update -> 글을 수정
# 7. /articles/1/delete -> 글을 삭제

def index(request):
    data = Article.objects.all()
    
    return render(request, 'articles/index.html', {'data': data})

def detail(request, num):
    a = Article.objects.get(pk=num)
    
    return render(request, 'articles/detail.html', {'article': a})

def new(request):
    return render(request, 'articles/new.html')
    
    
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    a = Article(title=title, content=content)
    a.save()
    
    return redirect('/articles/')
    

def edit(request, num):
    a = Article.objects.get(pk=num)
    
    return render(request, 'articles/edit.html', {'article': a})
    
    
def update(request, num):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    a = Article.objects.get(pk=num)
    a.title = title
    a.content = content
    a.save()
    
    return redirect('/articles/')
    
    
def delete(request, num):
    a = Article.objects.get(pk=num)
    a.delete()
    
    return redirect('/articles/')
```





### urls.py

```python
from django.urls import path # 기존 urls.py에서 복붙
from . import views # 같은 폴더에 있는 views.py를 가져오겠음

# articles를 일일이 써줄 필요가 없다!
urlpatterns = [
    path('', views.index),
    path('<int:num>/', views.detail),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:num>/edit/', views.edit),
    path('<int:num>/update/', views.update),
    path('<int:num>/delete/', views.delete),
]
```





### base.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
    <title>게시판</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```





### detail.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>제목: {{ article.title }}</h1>
<h1>내용: {{ article.content }}</h1>

{% endblock%}
```





### edit.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>게시물 수정하기</h1>
<form action="/articles/{{ article.id }}/update/"/> <!-- 앞뒤를 다 닫는다. django앱에서 뒤를 다 닫기 때문 -->
    <input type="text" name="title" value="{{ article.title }}"/> <!-- />:self closing tag. react(있어야 함) 아닌 이상 있어도 없어도 됨 -->
    <input type="text" name="content" value="{{ article.content }}"/>
    <input type="submit" value="Submit"/>
</form>
{% endblock%}
```





### index.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>게시판입니다.</h1>
<table class="table">
  <thead>
    <tr>
      <th scope="col">Title</th>
    </tr>
  </thead>
  <tbody>
    {% for row in data %}
    <tr>
      <td><a href="/articles/{{ row.id }}/">{{ row.title }}</a></td>
      <td><a href="/articles/{{ row.id }}/edit/">편집</a></td>
      <td><a href="/articles/{{ row.id }}/delete/">삭제</a></td>
    </tr>
    {% endfor %}
  </tbody>
</table>
<a href="/articles/new/">새 글 쓰기</a>

{% endblock%}
```



### new.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>새 게시물 쓰기</h1>
<form action="/articles/create/"/> <!-- 앞뒤를 다 닫는다. django앱에서 뒤를 다 닫기 때문 -->
    <input type="text" name="title"/> <!-- />:self closing tag. react(있어야 함) 아닌 이상 있어도 없어도 됨 -->
    <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
</form>
{% endblock%}
```





## View를 넘겨주는 url passing(redirect)

**name** parameter를 통해 이름을 붙여줄 수 있다.

### urls.py

```python
from django.urls import path # 기존 urls.py에서 복붙
from . import views # 같은 폴더에 있는 views.py를 가져오겠음

# articles를 일일이 써줄 필요가 없다!
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:num>/edit/', views.edit),
    path('<int:num>/update/', views.update),
    path('<int:num>/delete/', views.delete),
]
```



### views.py

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    a = Article(title=title, content=content)
    a.save()
    
    # return redirect('/articles/') ########## 이걸 바꾼다 ###########
    return redirect('index')
```





## app_name

### urls.py

```python
from django.urls import path # 기존 urls.py에서 복붙
from . import views # 같은 폴더에 있는 views.py를 가져오겠음

app_name = 'articles'

# articles를 일일이 써줄 필요가 없다!
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:num>/edit/', views.edit),
    path('<int:num>/update/', views.update),
    path('<int:num>/delete/', views.delete),
]
```

url을 얼마든지 바꿔도 name은 변하지 않는다 -> 편리하게 불러올 수 있음.

but 그냥 'index'을 쓰면 여기 앱 뿐만 아니라 전역에서 찾게 됨. 중복 우려.

=> 그래서 app_name 지정. articles 안의 index라는 표시

### views.py

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    a = Article(title=title, content=content)
    a.save()
    
    # return redirect('/articles/') ########## 이걸 바꾼다 ###########
    # return redirect('articles:index')
    # return redirect('/articles/1') # 이걸 바꾸려면(아래와 같음)
    return redirect('articles:detail', a.id) # 글 상세정보로 이동
```



### detail.html

html 파일에도 진자 형태로 view name 적용 가능!

```html
{% extends 'articles/base.html' %}

{% block body %}
<h1>제목: {{ article.title }}</h1>
<h1>내용: {{ article.content }}</h1>
<a href="{% url 'articles:index' %}">홈으로</a> <!-- url 중에 app_name=articles 중에 index라는 애를 가져와라 -->

{% endblock %}
```



### edit.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>게시물 수정하기</h1>
<!-- <form action="/articles/{{ article.id }}/update/"/> 앞뒤를 다 닫는다. django앱에서 뒤를 다 닫기 때문 -->
    <form action="{% url 'articles:update' article.id %}"/>
    <input type="text" name="title" value="{{ article.title }}"/> <!-- />:self closing tag. react(있어야 함) 아닌 이상 있어도 없어도 됨 -->
    <input type="text" name="content" value="{{ article.content }}"/>
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```

