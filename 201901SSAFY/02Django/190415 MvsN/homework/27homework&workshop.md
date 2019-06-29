# 27homework



1. 

```python
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
```

2. 

1. ```python
   from django.db import models
   from django.conf import settings
   
   class Question(models.Model):
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       title = models.CharField(max_length=50)
       
   	def __str__(self):
           return self.title
   ```





# 27workshop

프로젝트 생성 후

`$ python manage.py startapp accounts`

`settings.py`에 app 추가

### settings.py

```python
ALLOWED_HOSTS = ['last-pang-egyeasy.c9users.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'accounts',
]
```



###  _nav.html

navbar에 회원가입 버튼 생성

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="{% url 'posts:list' %}">홈</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <!--좌측 버튼-->
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="{% url 'posts:create' %}">글 작성</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <!--우측 버튼-->
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:signup' %}">회원가입</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
```





### <project_name>/urls.py

`accounts`  앱의 `urls.py`로 url 처리하도록 설정

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('accounts/', include('accounts.urls'))
]
```



### accounts/urls.py

`signup` 처리를 위한 url 설정

```python
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```



### accounts/views.py

`signup` 기능 구현

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
```



### accounts/templates/accounts/signup.html

`signup` 페이지 구현

```html
{% extends 'base.html' %}

{% block body %}

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>

{% endblock %}
```


