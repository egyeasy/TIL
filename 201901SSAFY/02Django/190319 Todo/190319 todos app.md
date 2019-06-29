# 190319 todos app



## todos 초기 세팅

`$ django-admin startapp todos`

settings.py todos 추가



### todo/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('todos.urls')),
]
```



todos/templates/todos 폴더 만들기

그 안에 home.html 만들기



### todos/urls.py

```python
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('home/', views.home, name='home'),
]
```





### home.html

users의 base.html extends 해서 써도 되고,

프로젝트 폴더 최상단의 templates 폴더에 base.html을 넣어서 불러와도 된다

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>Todo List</h1>
{% endblock %}
```



### views.py

```python
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'todos/home.html')
```



## Create 만들기

### home.html

bootstrap forms를 직접 만드려면 form-group, form-control을 활용해야 한다.

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>Todo List</h1>
    <form action="/create/" method="POST">
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="todo" class="form-control">
        </div>
        <div class="form-group">
            <button class="btn btn-primary">만들기</button>
        </div>
    </form>
{% endblock %}
```



### models.py

```python
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



### admin.py

```python
from django.contrib import admin
from .models import Todo

# Register your models here.
admin.site.register(Todo)
```



어드민 들어가서 todo 추가가 잘 되는지 확인해본다.



## listing in home

### views.py

```python
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기(id 기준 내림차순 정렬)
    todos = Todo.objects.all().order_by('-id')
    context = {
        'todos': todos
    }
    return render(request, 'todos/home.html', context)

```


### home.html

```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>Todo List</h1>
    <form action="/create/" method="POST">
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="todo" class="form-control">
        </div>
        <div class="form-group">
            <button class="btn btn-primary">만들기</button>
        </div>
    </form>
    {% for todo in todos %}
        {{ todo }}
    {% endfor %}

{% endblock %}
```



bootstrap form을 활용하여 좀 더 이쁘게 만들어준다.



```html
{% extends 'users/base.html' %}

{% block content %}
    <h1>Todo List</h1>
    <form action="/create/" method="POST">
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="content" class="form-control">
        </div>
        <div class="form-group">
            <button class="btn btn-primary">만들기</button>
        </div>
    </form>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">체크</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody>
        {% for todo in todos %}
            <tr>
              <th scope="row">{{ todo.id }}</th>
              <td>{{ todo.content }}</td>
              <td>{{ todo.completed }}</td>
              <td>삭제</td>
            </tr>
        {% endfor %}
      </tbody>
    </table>
{% endblock %}
```





## create 기능

### views.py

```python
def create(request):
    # todos 작성하기
    content = request.POST.get('content')
    # completed = request.POST.get('completed')
    Todo.objects.create(content=content)

    return redirect('todos:home')
```



### urls.py

```python
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
]
```



create의 기능을 home에서 post로 request를 받았을 때 처리하도록 하여 동일 url 내에서 처리하게 할 수도 있지만,

restful하게 짜기 위해서는 이렇게 create url을 따로 두는 것이 좋다.





## check 누를 시 completed로 만들기

### urls.py

```python
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('check/<int:id>', views.check, name='check'),
]
```



### views.py

```python
def check(request, id):
    # 특정 id를 가진 todo를 뽑아 completed = True 로 만들어주기
    todo = Todo.objects.get(pk=id)
    todo.completed = True
    todo.save()
    return redirect('todos:home')
```



### home.html

```html

    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">체크</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody>
        {% for todo in todos %}
            <tr>
              <th scope="row">{{ todo.id }}</th>
              <td>{{ todo.content }}</td>
              <td>{{ todo.completed }}</td>
                <td><a href="{% url 'todos:check' todo.id %}">체크</a></td>
              <td>삭제</td>
            </tr>
        {% endfor %}
      </tbody>
    </table>
```



1. if문 활용하여 check 된 경우에 취소선 보여주기
2. check를 버튼으로 바꿔주기

```html

    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">체크</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody>
        {% for todo in todos %}
            <tr>
              <th scope="row">{{ todo.id }}</th>
              {% if todo.completed %}
                  <td><strike>{{ todo.content }}</strike></td>
              {% else %}
                  <td>{{ todo.content }}</td>
              {% endif %}
              <td>{{ todo.completed }}</td>
              <td><button class="btn btn-dark"><a href="{% url 'todos:check' todo.id %}">체크</a></button></td>
              <td>삭제</td>
            </tr>
        {% endfor %}
      </tbody>
    </table>
```

1. check 해제하는 기능 추가
2. 위에는 완료 안된 일, 아래는 완료 된 일 보여주기
3. 삭제 기능 추가

html 단에서 분류하지 말고, db에게 completed에 따른 분류를 맡겨놓고 views 단에서 받아와서 html로 넘겨주는 것이 좋다 -> 잘하는 놈한테 맡겨라

```html
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">완료 여부</th>
          <th scope="col">체크</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody>
        {% for todo in todos %}
            {% if not todo.completed %}
            <tr>
              <th scope="row">{{ todo.id }}</th>
              <td>{{ todo.content }}</td>
              <td>{{ todo.completed }}</td>
              <td><button class="btn btn-dark"><a href="{% url 'todos:check' todo.id %}">체크</a></button></td>
              <td><button class="btn btn-dark"><a href="{% url 'todos:delete' todo.id %}">삭제</a></button></td>
            </tr>
            {% endif %}
        {% endfor %}
        {% for todo in todos %}
            {% if todo.completed %}
                <tr>
                  <th scope="row">{{ todo.id }}</th>
                  <td><strike>{{ todo.content }}</strike></td>
                  <td>{{ todo.completed }}</td>
                  <td><button class="btn btn-dark"><a href="{% url 'todos:check' todo.id %}">체크</a></button></td>
                  <td><button class="btn btn-dark"><a href="{% url 'todos:delete' todo.id %}">삭제</a></button></td>
                </tr>
            {% endif %}
        {% endfor %}
      </tbody>
    </table>
```



### urls.py

```python
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('check/<int:id>', views.check, name='check'),
    path('delete/<int:id>', views.delete, name='delete'),
]
```



### views.py

```python
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기(id 기준 내림차순 정렬)
    todos = Todo.objects.all().order_by('-id')
    context = {
        'todos': todos
    }
    return render(request, 'todos/home.html', context)


def create(request):
    # todos 작성하기
    content = request.POST.get('content')
    # completed = request.POST.get('completed')
    Todo.objects.create(content=content)

    return redirect('todos:home')


def check(request, id):
    # 특정 id를 가진 todo를 뽑아 completed = True 로 만들어주기
    todo = Todo.objects.get(pk=id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:home')


def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todos:home')
```





## 사용자와 Todo 매칭(1:N)

### models.py

`on_delete=models.CASCADE` : DB의 무결성을 보장하기 위해 table(model)이 사라졌을 때 안에 소속된 애들을 삭제

django에 이미 탑재된 User가 있으므로 가져와서 1:N 매칭해준다.

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



`$ python manage.py makemigrateions`

이미 todo로 만들어진 데이터들이 있다. 그래서 todo의 user 필드를 non-nullable로 만들 수가 없음. 따라서 이미 만들어진 것들을 어떻게 처리할 것인지 django가 물어본다.(1 - 한번 사용된 default값 사용하기, 2 - quit)

1) 1 선택 -> 이렇게 하지 말고

2) DB 다 날려버리기 : `db.sqlite3`를 삭제, migrations 폴더 내의 0001 파일 삭제

2) 를 선택

`$ python manage.py makemigrations`

`$ python manage.py migrate`



슈퍼유저도 다시 만들어줘야 한다.

`$ python manage.py createsuperuser`

애초에 이런 상황을 만들지 않도록 DB설계를 배우는 것. 망라적(exhaustive)으로 짜야한다!



### views.py

runserver 해서  todo를 만들려고 하면 안된다. create logic에서 user를 설정해줘야 함!

현재 유저의 아이디를 넣어줘야 한다.

```python
from django.contrib.auth.models import User

# ... #

def create(request):
    # todos 작성하기
    content = request.POST.get('content')
    # completed = request.POST.get('completed')
    # 현재 접속해있는 유저의 아이디
    user_id = User.objects.first().id # 이건 첫번째 유저만 가져온다!
    current_user_id = request.user.id
    Todo.objects.create(content=content, user_id=current_user_id)

    return redirect('todos:home')
```



### home.html

```html

    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">완료 여부</th>
          <th scope="col">체크</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody>
        {% for todo in todos %}
            {% if not todo.completed %}
            <tr>
              <th scope="row">{{ todo.user }}</th>
              <td>{{ todo.content }}</td>
              <td>{{ todo.completed }}</td>
              <td><button class="btn btn-dark"><a href="{% url 'todos:check' todo.id %}">체크</a></button></td>
              <td><button class="btn btn-dark"><a href="{% url 'todos:delete' todo.id %}">삭제</a></button></td>
            </tr>
            {% endif %}
        {% endfor %}
        {% for todo in todos %}
            {% if todo.completed %}
                <tr>
                  <th scope="row">{{ todo.user }}</th>
                  <td><strike>{{ todo.content }}</strike></td>
                  <td>{{ todo.completed }}</td>
                  <td><button class="btn btn-dark"><a href="{% url 'todos:check' todo.id %}">체크</a></button></td>
                  <td><button class="btn btn-dark"><a href="{% url 'todos:delete' todo.id %}">삭제</a></button></td>
                </tr>
            {% endif %}
        {% endfor %}
      </tbody>
    </table>
```





## 해당 사용자의 todo만 보여주기

admin 창에서 일반 권한 계정 하나 더 만들기(bakbak)



### views.py

```python
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기(id 기준 내림차순 정렬)
    # todos = Todo.objects.all().order_by('-id')
    # todos = Todo.objects.filter(user_id=request.user.id).all()
    todos = request.user.todo_set.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/home.html', context)
```



### users/views.py

로그인 시에 todos 리스트로 이동

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# '/users/' => 홈페이지
# '/users/login' => 로그인 화면


def home(request):
    return render(request, 'todos/home.html')


def login_user(request):
    # /users/login POST
    # -> 로그인(유저 검증)
    if request.method == "POST":
        # 만약에 username, password로 넘어온 값이 DB에 저장된 값과 같다면,
        #   로그인
        # 아니면
        #   꺼지셈
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # 1. 사용자가 로그인 되었을 때
            messages.success(request, "성공적으로 로그인 되었습니다.")
            return redirect('todos:home')
        else:
            # Return an 'invalid login' error message.
            # 2. 사용자가 로그인이 되지 않았을 때
            messages.success(request, "로그인이 되지 않았습니다. 다시 시도해 주세요.")
            return redirect('login')
```



커스마이징할 것 - anonymous 유저 들어왔을 때 에러메시지.