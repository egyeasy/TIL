# Project08 - 데이터베이스 seeding

기존의 데이터 - data seed

시드를 넣는 작업을 seeding이라고 함.

fixture - 1) 시드 데이터를 넣는 기능. 2) 테스트 코드의 인풋 데이터





# 190322 Model Form

## todo project에 이어서 만들기

현재는 익명의 유저가 홈(/home/)에 접속하면 에러 메시지 출력



### views.py

```python
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # todos에 있는 내용을 다 가져와 보여주기(id 기준 내림차순 정렬)
        # todos = Todo.objects.all().order_by('-id')
        # todos = Todo.objects.filter(user_id=request.user.id).all()
        todos = request.user.todo_set.all() # anonymous의 경우 todo_set이 없음 - 처리해줄 것
        context = {
            'todos': todos
        }
    else:
        context = {}
    return render(request, 'todos/home.html', context)
```







### users/base.html

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="{% url 'home' %}">TODO APP</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          {% if user.is_authenticated %}
              <li class="nav-item">
                <a class="nav-link" href="{% url 'logout' %}">Logout</a>
              </li>
          {% else %}
              <li class="nav-item">
                <a class="nav-link" href="{% url 'login' %}">Login</a>
              </li>
{#             회원가입 페이지 추가 #}
              <li class="nav-item">
                <a class="nav-link" href="#">Register</a>
              </li>
{#             고객센터 버튼 추가 #}
              <li class="nav-item">
                <a class="nav-link" href="#">고객센터</a>
              </li>
          {% endif %}
```






## 고객센터 앱 만들기

`$ python manage.py startapp shouts`

settings.py에 앱 추가



### models.py

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`

`urls.py` 만들기



### 메인 todo/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('todos.urls')),
    path('shouts/', include('shouts.urls')),
]
```





### shouts/urls.py

```python
from django.urls import path
from . import views

app_name = "shouts"

# /shouts/...
urlpatterns = [
    path('', views.home, name="home"),
]
```



### views.py

```python
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'shouts/home.html')
```



shouts/templates/shouts/home.html 만들기



### home.html

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>고객센터</h1>
    <form action="POST" action="{% url 'shouts:home' %}">
{#    <form action="POST"> 아무것도 안 적어줘도 자신으로 보낸다. but 명시해주는 게 convention #}
        {% csrf_token %}
        문의 제목 : <input type="text" name="title">
        문의 내용 : <input type="text" name="content">
        <input type="submit">
    </form>
{% endblock %}
```





### users/base.html

메뉴에서 고객센터 버튼 연결

```html
{#             고객센터 버튼 추가 #}
              <li class="nav-item">
                <a class="nav-link" href="{% url 'shouts:home' %}">고객센터</a>
              </li>
          {% endif %}
```





### views.py

```python
from django.shortcuts import render, redirect
from .models import Shout

# Create your views here.
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        title = request.POST.get('title')
        content = request.POST.get('content')
        Shout.objects.create(title=title, content=content)
        return redirect('shouts:home')
    # GET
    else:
        # form 보여주기
        return render(request, 'shouts/home.html')
```



GET 요청일 때 문의사항을 전부 보여주도록 만들어보자



```python
from django.shortcuts import render, redirect
from .models import Shout

# Create your views here.
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        title = request.POST.get('title')
        content = request.POST.get('content')
        Shout.objects.create(title=title, content=content)
        return redirect('shouts:home')
    # GET
    else:
        # form 보여주기 & 문의사항 전부 보여주기
        shouts = Shout.objects.all()
        context = {
            'shouts': shouts
        }
        return render(request, 'shouts/home.html', context)
```



### home.html

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>고객센터</h1>
    <form action="POST" action="{% url 'shouts:home' %}">
{#    <form action="POST"> 아무것도 안 적어줘도 자신으로 보낸다. but 명시해주는 게 convention #}
        {% csrf_token %}
        문의 제목 : <input type="text" name="title">
        문의 내용 : <input type="text" name="content">
        <input type="submit">
    </form>
    <hr>
    <h2>문의 내용</h2>
    {% for shout in shouts %}
        {{ shout.title }}
        {{ shout.content }}
    {% endfor %}

{% endblock %}
```





## Validation

데이터의 유효성 검증

방법 1. frontend validation

방법 2. model(server-side) validation : django 활용

방법 3. DBMS validation - sqlite 단에서 막는 것. 별로 믿음직하지 못함.



### 1. frontend validation - home.html

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>고객센터</h1>
    <form action="POST" action="{% url 'shouts:home' %}">
{#    <form action="POST"> 아무것도 안 적어줘도 자신으로 보낸다. but 명시해주는 게 convention #}
        {% csrf_token %}
        문의 제목 : <input required type="text" name="title">
        문의 내용 : <input required type="text" name="content">
        <input type="submit">
    </form>
    <hr>
    <h2>문의 내용</h2>
    {% for shout in shouts %}
        {{ shout.title }}
        {{ shout.content }}
    {% endfor %}

{% endblock %}
```



하지만 개발자 도구에서 html 열어서 소스에서 required 지우고 제출하면 된다.

방법 2를 통해 해결해야 함.



### 2. model validation - views.py

views 단에서 if 문이나 try except 사용할 수 있지만 번거롭다

```python
from django.shortcuts import render, redirect
from .models import Shout

# Create your views here.
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 직접 서버 단에서 검증해주기
        if title == "" and content == "":
            messages.success('마 내용입력해라')
            return redirect()
        Shout.objects.create(title=title, content=content)
        return redirect('shouts:home')
```



basic CRUD에서 두 단계로 업그레이드 할 것

1. form class
2. model form





## form class

1. data validation
2. input formation

장고에게 form을 만들어서 input 데이터를 핸들링하라고 시키는 것

데이터 검증 및 저장까지 하는 기능.

app(shouts) 아래에 `forms.py` 파일 만든다.



ShoutForm이라는 클래스를 만들 건데, 이 클래스가 장고의 내장 클래스를 상속 받아서 커스터마이징하는 것.

이 클래스에게 model의 구조를 알려준다.

github django form 검색 -> form 파이썬 소스를 볼 수 있다.



### forms.py

```python
from django import forms

class ShoutForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)

```



### views.py

cleand_data를 쓰면 string 양쪽의 space strip도 처리해줌.

```python
from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm

# Create your views here.
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        form = ShoutForm(request.POST)
        if form.is_vaild(): # 날아온 데이터가 제대로 돼있을 때를 검증
            # form이 필터링한 데이터를 쓴다
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # 직접 서버 단에서 검증해주기
            # if title == "" and content == "":
            #     messages.success('마 내용입력해라')
            #     return redirect()
            Shout.objects.create(title=title, content=content)
            return redirect('shouts:home')
    # GET
    else:
        # form 보여주기 & 문의사항 전부 보여주기
        shouts = Shout.objects.all()
        context = {
            'shouts': shouts
        }
        return render(request, 'shouts/home.html', context)
```



django 특유의 regular expression, image, url, email validator들이 존재한다. 



form class 활용해서 for 만들기



```python
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        form = ShoutForm(request.POST)
        if form.is_vaild(): # 날아온 데이터가 제대로 돼있을 때를 검증
            # form이 필터링한 데이터를 쓴다
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # 직접 서버 단에서 검증해주기
            # if title == "" and content == "":
            #     messages.success('마 내용입력해라')
            #     return redirect()
            Shout.objects.create(title=title, content=content)
            return redirect('shouts:home')
    # GET
    else:
        # form 보여주기 & 문의사항 전부 보여주기
        form = ShoutForm()  # initialize
        shouts = Shout.objects.all()
        context = {
            'shouts': shouts,
            'form': form,  # form을 html에서 쓰겠다
        }
        return render(request, 'shouts/home.html', context)
```





### base.html

form class는 input formation 기능도 제공한다. max_length, required(frontend validation) 기능도 제공한다.

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>고객센터</h1>
    <form method="POST" action="{% url 'shouts:home' %}">
{#    <form action="POST"> 아무것도 안 적어줘도 자신으로 보낸다. but 명시해주는 게 convention #}
        {% csrf_token %}
        {{ form.as_ul }}
{#        문의 제목 : <input required type="text" name="title">#}
{#        문의 내용 : <input required type="text" name="content">#}
        <input type="submit">
    </form>
    <hr>
    <h2>문의 내용</h2>
    {% for shout in shouts %}
        제목 : {{ shout.title }}
        내용 : {{ shout.content }}
    {% endfor %}

{% endblock %}
```





## FormClass

1. data validation

2. input formation

   +

3. data creation

'views.py' 코드는 여전히 길다. 이걸 줄여주도록 하자.



### forms.py

form을 만들 때 앞에서와 다른 클래스를 상속한다.

modelform은 우리가 갖고있는 model을 자동으로 form으로 만들어준다.

```python
from django import forms
from .models import Shout

class ShoutForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)

class ShoutModelForm(forms.ModelForm):
    class Meta:  # 메타 정보를 넣어줌
        model = Shout
        # form의 필드 중 어떤 것을 쓸지 얘기해준다
        fields = '__all__'  # 모든 필드 사용
```





### views.py

```python
from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm, ShoutModelForm

# Create your views here.
def home(request):
    # POST
    if request.method == "POST":
        # 고객센터 문의 작성하기
        form = ShoutModelForm(request.POST)
        # form = ShoutForm(request.POST)
        if form.is_valid(): # 날아온 데이터가 제대로 돼있을 때를 검증
            form.save() # 이 한 문장으로 해결!
            
            # # form이 필터링한 데이터를 쓴다
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # Shout.objects.create(title=title, content=content)
            
            # # title = request.POST.get('title')
            # # content = request.POST.get('content')
            # # 직접 서버 단에서 검증해주기
            # # if title == "" and content == "":
            # #     messages.success('마 내용입력해라')
            # #     return redirect()
            return redirect('shouts:home')
```



## update 만들기

ModelForm을 쓰면 create와 update 로직이 거의 비슷하게 된다. -> 한 곳에서 다 처리할 수 있다.

### home.html

```html
    {% for shout in shouts %}
        <p>
            제목 : {{ shout.title }}
            내용 : {{ shout.content }}
            <a href="{% url 'shouts:update' shout.id %}">[수정]</a>
        </p>
    {% endfor %}
```



### urls.py

```python
from django.urls import path
from . import views

app_name = "shouts"

# /shouts/...
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>/update/', views.update, name="update")
]
```



### views.py

edit과 update를 따로 만들 필요가 없다. GET, POST 방식에 따라 분기시켜서 처리하면 된다.

```python
def update(request, id):
    # 수정하기(update)
    if request.method == "POST":
        pass
    # 편집하기(edit)
    else:
        shout = Shout.objects.get(pk=id)
        form = ShoutModelForm()
        context = {
            'shout': shout,
            'form': form,
        }
        return render(request, 'shouts/update.html', context)
```



`update.html`을 만든다

### update.html

```html
<form action="{% url 'update' shout.id %}" method="POST">
    {{ form.as_p }}
</form>
```



views에서 default값을 받아서 넘겨주도록 하자.



### views.py

```python
def update(request, id):
    # 수정하기(update)
    if request.method == "POST":
        pass
    # 편집하기(edit)
    else:
        shout = Shout.objects.get(pk=id)
        form = ShoutModelForm(instance=shout)  # instance shout 지정해주면 form 안에 이 shout를 넣어서 html에 넣어줌
        # default 값을 여기서 넣어서 전달 가능하다.
        context = {
            'shout': shout,
            'form': form,
        }
        return render(request, 'shouts/update.html', context)
```



shout 어차피 한 번만 쓸 건데 넘길 필요 있을까? 없앨 수 있다.

form에 이미 들어가있는 데이터들이 있다.



```python
def update(request, id):
    # 수정하기(update)
    if request.method == "POST":
        pass
    # 편집하기(edit)
    else:
        shout = Shout.objects.get(pk=id)
        form = ShoutModelForm(instance=shout)  # instance shout 지정해주면 form 안에 이 shout를 넣어서 html에 넣어줌
        # default 값을 여기서 넣어서 전달 가능하다.
        context = {
            # 'shout': shout,
            'form': form,
        }
        return render(request, 'shouts/update.html', context)
```





### update.html

```html
<form action="{% url 'shouts:update' form.instance.id %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
</form>
```



자기자신에게 보내는 것이기 때문에 url 다 써줄 필요 없다.

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```



### views.py

update(수정 반영) 로직

```python
def update(request, id):
    shout = Shout.objects.get(pk=id) # 양쪽 공통이므로 맨 위에 써준다
    # 수정 반영하기(update)
    if request.method == "POST":
        # 인자 - 날아온 데이터, 수정할 인스턴스(생성에 비해 인자가 하나 더 필요) -> 알아서 update로 처리
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
        return redirect('shouts:home')

    # 편집하기(edit)
    else:
        form = ShoutModelForm(instance=shout)  # instance shout 지정해주면 form 안에 이 shout를 넣어서 html에 넣어줌
        # default 값을 여기서 넣어서 전달 가능하다.
        context = {
            # 'shout': shout,
            'form': form,
        }
        return render(request, 'shouts/update.html', context)
```





구조를 좀 더 정리해보자

### urls.py

```python
from django.urls import path
from . import views

app_name = "shouts"

# /shouts/...
urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('<int:id>/update/', views.update, name="update")
]
```





### home.html





### views.py

```python
# Create your views here.
def home(request):
    # form 보여주기 & 문의사항 전부 보여주기
    # form = ShoutForm()  # initialize
    shouts = Shout.objects.all()
    form = ShoutModelForm()
    context = {
        'shouts': shouts,
        # 'form': form,  # form을 html에서 쓰겠다
    }
    return render(request, 'shouts/home.html', context)


def create(request):
    # POST : 글을 DB에 저장
    if request.method == "POST":
        # home의 로직을 그대로 가져오면 됨
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')

    # GET : 글 작성할 수 있는 form
    else:
        form = ShoutModelForm()
        context = {
            'form': form
        }
        return render(request, 'shouts/create.html', context)
```





### create.html

새로 만들어서 home에서 form을 가져온다.

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```



create와 update html이 똑같이 생겨서, update를 없애도 된다.

update.html 삭제

create.html -> form.html 이름 수정





### forms.py

css 추가

```python
class ShoutModelForm(forms.ModelForm):
    class Meta:  # 메타 정보를 넣어줌
        model = Shout
        # form의 필드 중 어떤 것을 쓸지 얘기해준다
        fields = '__all__'  # 모든 필드 사용
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

```



## 이것은 작성 또는 수정페이집니다

어떻게 두 경우를 다르게 표현할 수 있을까? -> url이 다르다는 점을 이용

### form.html

django request object 내에도 수많은 attribute들이 있다. request.method, request.path 등등

템플릿 extends 없이 하면 form이 우선순위가 높아서 제일 위에 rendering 된다.

`{% if "create" in request.path %}`는 쓸 수 없다.

```html
{% extends 'users/base.html' %}

{% block content %}
    {% if request.resolver_match.url_name == 'create' %}
        <h1>문의 작성</h1>
    {% else %}
        <h1>수정하기</h1>
    {% endif %}
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock %}
```





## 회원가입 기능

### users/views.py

```python

from django.contrib.auth.forms import UserCreationForm  # 회원가입
```



### urls.py

```python
from django.urls import path
from . import views

# '/users/' => 홈페이지
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
]
```





### templates/users/register.html (만들기)

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>

```



### base.html

```html
{#             회원가입 버튼 추가 #}
              <li class="nav-item">
                <a class="nav-link" href="{% url 'register' %}">Register</a>
              </li>
```



이제 POST 받아서 처리하기 로직



### views.py

```python
def register(request):
    if request.method == "POST":
        # 회원가입 시키기(DB에 사용자 정보를 저장)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # 회원정보를 받는 form 보여주기
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)
```







## modelForm에서 foreign key 처리(todos app)

### todos/forms.py(만들기)

```python
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
```



### todos/views.py

instance를 지정해주면 기본적으로 값을 채워서 TodoForm으로 만들 수 있다()

```python
from .forms import TodoForm

def create(request):
    # todos 작성하기
    # content = request.POST.get('content')
    # user_id = User.objects.first().id # 이건 첫번째 유저만 가져온다!
    # current_user_id = request.user.id
    # # completed = request.POST.get('completed')
    # # 현재 접속해있는 유저의 아이디
    # Todo.objects.create(content=content, user_id=current_user_id)
    ### 방법 1
    user = request.user  # 유저 객체를 받아오고
    todo = Todo(user=user)  # todo를 만들어서 미리 user 칼럼을 채워줌
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()

    return redirect('todos:home')

```















