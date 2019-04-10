# 190410 Create Delete Update



### instagram/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]

```



### posts/urls.py

```python
from django.urls import path

app_name = "posts"

urlpatterns = [
    #
]
```



`$ cd INSTAGRAM`

`$ git status`

`$ git add .`

`$ git commit -m "posts 앱의 urls.py 생성 및 메인 urls.py에 posts.urls 추가"`





## Create

### urls.py

```python
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    
]
```





### views.py

```python
from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'posts/create.html')
```



강사님은 코드에 있는 파일들은 되도록 commit 당시에 존재하게 만드는 편.



### posts/templates/posts/create.html 생성

git은 폴더 안에 파일이 없는 경우 tracking을 하지 않는 기능이 있다. 그래서 tracking 되게 하려면 파일을 넣어줘야함.

```html
{% extends 'base.html' %}

{% block body %}
{% endblock %}
```



`$ git add .`

`$ git commit -m "/posts/create/ url 설정 & template 파일 생성"`





## Navbar - Nav(unordered)

base.html에 navbar를 넣으면 너무 난잡해진다. 파일을 분리하자.

### INSTAGRAM/templates/nav.html 생성

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
```



### base.html

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>INSTAGRAM</title>
  </head>
  <body>
    {% include 'nav.html' %}
    {% block body %}
    
    {% endblock %}
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```



`$ python manage.py runserver $IP:$PORT`

`https://last-pang-egyeasy.c9users.io/posts/create/`로 이동하면 화면 확인 가능





## font awesome

<https://fontawesome.com/start>

복사

### base.html

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <!-- Font Awesome-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

    <title>INSTAGRAM</title>
  </head>
  <body>
    {% include 'nav.html' %}
    {% block body %}
    
    {% endblock %}
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```



<https://fontawesome.com/icons/instagram?style=brands>

태그 복사

### nav.html

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <i class="fab fa-instagram"></i>
    Intagram
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
```





`$ git add .`

`$ git commit -m "Navbar 수정 & FA추가 및 인스타그램 아이콘 추가"`





## ModelForm

### posts/forms.py 생성

Meta 클래스를 가지고 해당 modelform이 어떤 model이고, 어떤 필드를 가져올지

`fields = '__all__'`을 쓰면 필요하지 않은 컬럼까지도 가져오게 됨

```python
from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label="content")
    
    class Meta:
        model = Post
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = ['content',]
```



### views.py

```python
from django.shortcuts import render
from .forms import PostModelForm

# Create your views here.
def create(request):
    # post를 작성하는 폼을 가져와 template에서 보여줌.
    form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)
```





### create.html

```html
{% extends 'base.html' %}

{% block body %}

{{ form }}

{% endblock %}
```

되는지 확인

`$ python manage.py runserver $IP:$PORT`



구체화.

```html
{% extends 'base.html' %}

{% block body %}
<h1>새로운 Post 작성하기</h1>
<form method="POST">
  {% csrf_token %}
  {{ form }}
</form>
{% endblock %}
```

action을 구체적으로 적어줄 필요가 없다. POST로 들어올 때, GET으로 들어올 때를 view 단에서 다르게 처리해서 해결할 것



### views.py

```python
from django.shortcuts import render
from .forms import PostModelForm

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        pass
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
```



`$ git add .`

`$ git commit -m "posts/create 템플릿 파일에 form 추가"`





## form에 bootstrap 적용

`$ pip install django-bootstrap4`

### settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'bootstrap4',
]
```



### create.html

bootstrap이 들어간 button을 만드려면 아래와 같이 buttons를 활용해야 한다.

```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
<h1>새로운 Post 작성하기</h1>
<form method="POST">
  {% csrf_token %}
  <!--부트스트랩 form을 쓰겠다는 의미. 함수 실행할 때처럼 %괄호 필요-->
  {% bootstrap_form form %}
  <!--django에서 지원하는 button-->
  {% buttons %}
    <button type="submit" class="btn btn-primary">업로드</button>
  {% endbuttons %}
</form>
{% endblock %}
```



### forms.py

html 태그 Textarea를 쓰고, attributes를 설정. placehoder도 바꿀 수 있다.

```python
from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label="content", widget=forms.Textarea())
    
    class Meta:
        model = Post
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = ['content',]
        # widget - 특정한 필드에 대해 옵션을 주기(기본 옵션을 override하게 됨)
        widget = {
            'content': forms.Textarea(attrs={
                'class': '',
                'rows': 5,
                'cols': 50,
                'placeholder': '지금 뭘 하고 계신가요?',
            })
        }
```



이제 view에서 POST 요청을 처리해보자.

### views.py

```python
from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        # 여기서 form.save()로 끝내줘도 되나, validation을 넣도록 하자.
        if form.is_valid():
            form.save()
            return redirect('posts:create')
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
```



관리자 페이지를 만들어보자



### admin.py

```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

superuser를 만들ㅈ다



`$ python manage.py createsuperuser`

Jack

dz@dz.kr

12341234



### models.py

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    
    def __str__(self):
        return self.content
```



<https://last-pang-egyeasy.c9users.io/admin> 에서 업로드 내역 확인

`$ git add instagram/settings.py posts/admin.py posts/forms.py posts/models.py posts/templates/posts/create.html posts/views.py`

`$ git commit -m "bootstrap4 설치 및 form에 적용 & post 작성 view 추가"`

`$ git push origin master`

git에서 add하면 staging area에 올라가게 되고, staging area의 내용들을 commit할 수 있게 된다. staging area에서 특정 파일을 제외하는 것도 가능(추후 공개)

`git add posts/*` : 와일드카드, posts 아래의 모든 것들을 다 add



### base.html

컨테이너로 감싸주기

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <!-- Font Awesome-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

    <title>INSTAGRAM</title>
  </head>
  <body>
    {% include 'nav.html' %}
    <div class="container">
      {% block body %}
    
      {% endblock %}
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```



placeholder가 안 나와서 수정

### forms.py

```python
from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(
        label="content",
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 50,
            'placeholder': '지금 뭘 하고 계신가요?',
    }))
    
    class Meta:
        model = Post
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = ['content',]
```







## 리스트로 보여주기(posts/)

### urls.py

```python
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list"),
]
```



### views.py

```python
from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)
```



### posts/list.html 생성

bootstrap - card component

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  {% for post in posts %}
    <div class="card" style="width: 18rem;">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <p class="card-text">{{ post.content }}</p>
      </div>
    </div>
  {% endfor %}
{% endblock %}
```





## lorempicsum 사진 추가

picsum.photos

https://picsum.photos/300/300/?random 복사

### list.html

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <img src="https://picsum.photos/300/300/?random" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```





create 후에 list로 오도록 설정

### views.py

```python
from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        # 여기서 form.save()로 끝내줘도 되나, validation을 넣도록 하자.
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
        
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)
```

`$ git status`

`$ git add templates/base.html`

`$ git commit -m "레이아웃 조정(body 컨텐트 container에 추가)"`	



`$ git add posts/forms.py posts/templates/posts/create.html`

`$ git commit -m "posts/create"의 textfield 수정`



`$ git add .`

`$ git commit -m "list.html 생성 및 url 정의`



## 삭제 기능

### urls.py

```python
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list"),
    path('<int:post_id>/delete/', views.delete, name="delete")
]
```



### list.html

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <img src="https://picsum.photos/300/300/?random" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```



### views.py

```python
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:list')

```

`$ git add .`

`$ git commit -m "Post 삭제 기능 추가"`



## update 기능

### urls.py

```python
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/update/', views.update, name="update"),
]
```



### views.py

```python
def update(request, post_id):
    if request.method == 'POST':
        # 수정내용 DB에 반영
        pass
    else:
        # 수정내용 편집 가능한 페이지 보여주기
        return render(request, 'posts/update.html')
```



### posts/update.html 생성

```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
<h1>Post 수정하기</h1>
<form method="POST">
    {% csrf_token %}
    
    {% bootstrap_form form %}
    
    {% buttons %}
        <button type="submit" class="btn btn-primary">수정하기</button>
    {% endbuttons %}
    
</form>
{% endblock %}
```





### list.html

수정 버튼 생성

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <img src="https://picsum.photos/300/300/?random" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <a href="{% url 'posts:update' post.id %}" class="btn btn-success">수정</a>
          <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```





### views.py

instance 인자에 수정할 내용을 넣어줘야 한다. POST라면 request의 내용을 instance에 담아줘야 한다. POST 시에 instance 안 쓰면 아예 새로운 데이터가 추가되어버림

```python
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # 수정내용 DB에 반영
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        # 수정내용 편집 가능한 페이지 보여주기
        form = PostModelForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'posts/update.html', context)
```



`$ git add .`

`$ git commit -m "Post 편집 기능 추가"`

`$ git push`







































