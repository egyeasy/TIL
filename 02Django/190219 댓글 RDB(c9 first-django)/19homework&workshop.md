# 19homework

1. Cross Site Request Forgery

2. ```python
   def create(request):
   	title = request.POST.get('title')
   ```

3. ```html
   <form action="/posts/{{post.id}}/update/" method="POST">
       {% csrf_token %}
       <input type="text" name="title" value="{{post.title}}">
       <input type="text" name="content" value="{{post.content}}">
       <input type="submit" value="Submit">
   </form>
   ```





# 19workshop

### models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
```



### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]
```



### students/urls.py

```python
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:student_id>/edit/', views.edit, name='edit'),
    path('<int:student_id>/update/', views.update, name='update'),
    path('<int:student_id>/delete/', views.delete, name='delete'),
]
```



### views.py

```python
from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)
    
def detail(request, student_id):
    s = Student.objects.get(pk=student_id)
    context = {
        'student': s,
    }
    return render(request, 'detail.html', context)
    

def new(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    s = Student(name=name, email=email, birthday=birthday, age=age)
    s.save()
    
    return redirect('students:index')
    

def edit(request, student_id):
    s = Student.objects.get(pk=student_id)
    context = {
        'student': s,
    }
    return render(request, 'edit.html', context)
    

def update(request, student_id):
    s = Student.objects.get(pk=student_id)
    
    s.name = request.GET.get('name')
    s.email = request.GET.get('email')
    s.birthday = request.GET.get('birthday')
    s.age = request.GET.get('age')
    
    s.save()
    
    return redirect('students:index')
    
    
def delete(request, student_id):
    s = Student.objects.get(pk=student_id)
    s.delete()
    
    return redirect('students:index')
```



### index.html

```html
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
    <title>Document</title>
</head>
<body>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">번호</th>
                <th scope="col">이름</th>
            </tr>
        </thead>
        <tbody>
            {% for stu in students %}
            <tr>
                <th scope="row">{{ stu.id }}</th>
                <td><a href="{% url 'students:detail' stu.id %}">{{ stu.name }}</a></td>
                <td><a href="{% url 'students:edit' stu.id %}">편집</a></td>
                <td><a href="{% url 'students:delete' stu.id %}">삭제</a></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <h2>새 학생 추가</h2>
    <form action="{% url 'students:new' %}">
        <input type="text" name="name" placeholder="이름"/><br>
        <input type="text" name="email" placeholder="이메일"/><br>
        <input type="text" name="birthday" placeholder="생년월일 YYYY-MM-DD"/><br>
        <input type="text" name="age" placeholder="나이"/><br>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



### detail.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{ student.id }}번</h1>
    <h1>{{ student.name }}</h1>
    <h1>{{ student.email }}</h1>
    <h1>{{ student.birthday|date:"Y-m-d" }}</h1>
    <h1>{{ student.age }}</h1>
    <h1><a href="{% url 'students:edit' student.id %}">편집</a></h1>
    <h1><a href="{% url 'students:delete' student.id %}">삭제</a></h1>
</body>
</html>
```





### edit.html

```html
<form action="{% url 'students:update' student.id %}">
    <input type="text" name="name" placeholder="이름" value="{{ student.name }}"/><br>
    <input type="text" name="email" placeholder="이메일" value="{{ student.email }}"/><br>
    <input type="text" name="birthday" placeholder="생년월일 YYYY-MM-DD" value="{{ student.birthday|date:'Y-m-d' }}"/><br>
    <input type="text" name="age" placeholder="나이" value="{{ student.age }}"/><br>
    <input type="submit" value="Submit"/>
</form>
```

