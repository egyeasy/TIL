# homework

1. ALLOWED_HOSTS

2. ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('ssafy/', views.ssafy)
   ]
   ```

3. `python manage.py runserver $IP:$PORT`

4. Model, Template, View





# workshop

### views.py

```python
from django.shortcuts import render
import random

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
    
def student(request, name):
    age = random.choice(range(24, 30))
    return render(request, 'student.html', {'name': name, 'age': age})
```



### info.html

```html
<h1>우리반정보</h1>
<h3>Teacher</h3>
<ul>
    <li>NAME</li>
</ul>
<h3>Student</h3>
<ul>
    <li>홍길동</li>
    <li>김길동</li>
    <li>박길동</li>
</ul>
```



### student.html

```html
<h1>이름 : {{ name }}</h1>
<h2>나이 : {{ age }}</h2>
```



### urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
    path('student/<str:name>/', views.student)
]
```

