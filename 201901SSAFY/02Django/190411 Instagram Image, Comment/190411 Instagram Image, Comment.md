# 190411 Instagram Image, Comment



### backlog

개발할 제품에 대한 요구사항 목록





## update

- 사용자에 대한 두 가지 가정

1. 사용자는 게으르다.
2. 사용자는 ㄸㄹㅇ밖에 없다.



`$ git add .`

`$ git commit -m "Post Update 기능 추가"`





## 사진 업로드

사진을 올리는 패키지인 pillow를 설치해야함

`$ pip install pillow`

-> models.py의 imagefield를 사용할 수 있게 함. Python Image Library의 뒤를 이은 후계자



### models.py

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # 사진 없는 것도 가능하게 설정
    
    def __str__(self):
        return self.content
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



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
        fields = ['content', 'image'] # 이미지 추가
```



파일을 전달하는 것은 텍스트를 전달하는 것과 굉장히 다른 종류의 액션. 이미지도 전달될 때는 비트로 이루어져있다. 파일을 넘길 때는 '스트림'이라고 해서 파일에 대한 정보를 함께 넘겨줘야 한다.(enctype - encoding type 설정)



### create.html

```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
<h1>새로운 Post 작성하기</h1>
<form method="POST" enctype="multipart/form-data">
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



### settings.py

맨 아래에 다음 코드 삽입

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 파일 주소에 접미사를 만들어줌
MEDIA_URL = '/media/'

# 절대경로로 나타내기 때문에 os.path.join 사용
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

이 설정을 하지 않으면 파일이 BASE_DIR, 즉 프로젝트 최상단 폴더에 쌓이게 된다.





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
        form = PostModelForm(request.POST, request.FILES) # 이미지 파일도 함께 받아온다.
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
```



but admin 사이트에서 개별 포스트 이미지에 접근하면 not found가 뜬다.

문지기가 이미지가 어디있는지 모르는 것

메인 urls.py에서 설정을 해줘야한다.



### instagram/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from . import settings #라고 쓸 수도 있지만
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

데이터 은닉 - 사용자가 내부에 대해서 모르도록 하는 것. 함수나 OOP에서 많이 구현되어있다. 경로를 통해 직접 접근하는 것보다는, wrapping이 되어있는 함수에 접근하는 것이 더 좋다.

settings에 접근하는 방법으로 django.conf에서 들어가는 방법이 있다.



### AWS

AWS 쓰면 나중에는 이미지 파일 등 파일을 amazon s3에 저장하게 될 것이다. 여기는 데이터 보관하는 구글 드라이브 같은 곳.

초반 설정이 좀 귀찮지만 하고 나면 하나로 하는 것과 크게 다르지 않다.

django의 경우,

컴퓨팅(기본) - ec2 or eb

파일(스태틱, 미디어) - s3

DB - RDS



js의 경우,

DB - MongoDB(Javascript) -> NoSQL(Key-Value 데이터베이스)

MongoDB 호스팅은 MLab이라는 서비스를 쓰게 될 것



### list.html

이제 이미지를 보여줄 수 있도록 하자.

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
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



이렇게 서버 돌리면 이미지가 없는 파일들 때문에 에러가 나게 된다.

1차적으로 이미지가 있을 때만 이미지 보여주는 방법(if문) - 이것도 파일을 넘겨줄 때부터 문제가 발생하는거라 에러



```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        {% if post.image.url %}
          <img src="{{ post.image.url }}" class="card-img-top" alt="...">
        {% endif %}
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



그냥 admin에서 이미지 없는 포스트를 삭제하도록 하자.



`$ git status`

media 폴더는 .gitignore에 포함되어 있어서 track하지 않는다. 이게 장고의 관례이다. media 다 올려버리면 github 속도를 느리게 함.

`$ git add .`

`$ git commit -m "Pillow 설치 & Post 모델에 이미지 추가 & 사진 업로드 기능 추가"`





## 회원가입

유저 시스템은 settings.py를 보면 auth를 통해 이미 깔려있음을 알 수 있다.

ORM도 데이터 은닉의 개념을 반영하기도 함. SQL을 쓰지 않고 django에게 해달라고 요청할 뿐 DB에 직접 접근해서 할 일은 없기 때문이다.



먼저 user와 Post를 연결시켜주도록 하자.

### models.py

```python
from django.db import models
# from django.auth 써도 되는데 아래는 다른 방법
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # 사진 없는 것도 가능하게 설정
    # User와의 연결고리 필요
    # user = models.ForeignKey(User, ) 이렇게 하지 않고
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
```

사실은 프로젝트 폴더 아래에 auth라는 앱(폴더)이 숨겨져 있을 것이고, 그 안에 model로 User가 정리되어 있을 것. 여기서는 그 모델의 포장을 뜯지 않고 접근하는 은닉적인 방법을 사용.



`$ python manage.py makemigrations`

터미널에서 이전에 만들었던 포스트들을 어떻게 처리할지 묻는다. 

1. 원래 있던 거 삭제
2. 임시값들로 채워주기(이번 한번만 쓰는 디폴트 값. one-off default)
3. 있던 것들 무시하고 넘어가기 -> 절대 쓰지 말 것(비어있는 데이터를 놔두지 말아야 한다)

보통 쓸 데 없는 유저(ghost user)를 만들어놓고 걔한테 다 가리키게 한다. 우리는 admin(pk=1)이 만들었다고 처리하게 할 것이다. 



### 터미널

`1` : 1번 선택지

`1` : 다 1로 채워준다(admin 계정의 pk)

migrate 파일 가보면 default 값이 1로 되어있음을 볼 수 있다.



`$ python manage.py migrate`



### views.py

request를 날린 사람의 정보를 추가해줘야 해서, save를 바로 하지 않는다.

post 객체에는 form.save()를 통해 user 빼고 다른 칼럼 값들이 다 들어가게 된다.

```python
# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST, request.FILES) # 이미지 파일도 함께 받아온다.
        # 여기서 form.save()로 끝내줘도 되나, validation을 넣도록 하자.
        if form.is_valid():
            post = form.save(commit=False) # form을 객체로 만들긴 하지만 DB에 넣지는 마라
            post.user = request.user
            post.save()
            return redirect('posts:list')
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
```



예전 수업에서 다른 방법을 제시해주었을 것. 참고 바람.



## Username 표시해주기

bootstrap card header를 쓸 것이다.(bootstrap 문서 참고)

username까지 써주지 않아도 str 메소드 덕분에 username을 출력 가능.

### list.html

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <div class="card-header">
          <span>{{ post.user.username }}</span>
        </div>
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
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



`$ git status`

`$ git add .`

`$ git commit -m "User와 Post를 1:N으로 연결 & Post 작성 시 User 정보 포함 & list 템플릿에서 작성자 보여줌"`





## 작성자에게만 수정/삭제 권한 부여

### list.html

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <div class="card-header">
          <span>{{ post.user.username }}</span>
        </div>
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <!--본인의 글만 삭제, 수정 버튼이 보이도록-->
          {% if request.user == post.user %}
            <a href="{% url 'posts:update' post.id %}" class="btn btn-success">수정</a>
            <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```

admin에서 로그아웃 한 뒤 /posts로 들어가보면 수정/삭제 버튼이 보이지 않는 것을 확인할 수 있다.

but 이렇게 해도 수정/삭제 url을 안다면 requests를 날려서 작업할 수 있다.

이걸 view 단에서 막아보자.



### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')
    
    
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('posts:list')
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



`$ git status`

`$ git add .`

`$ git commit -m "Update와 Delete에 대한 권한 설정"`





## Comment - 댓글 기능 추가

comment라는 모델을 만들어야 한다.



### models.py

```python
from django.db import models
# from django.auth 써도 되는데 아래는 다른 방법
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # 사진 없는 것도 가능하게 설정
    # User와의 연결고리 필요
    # user = models.ForeignKey(User, ) 이렇게 하지 않고
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
        
        
class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



댓글 작성 form을 만들기 위해 form 생성

### forms.py

여기서 comments를 자세하게 정의해주지 않아도, model을 참고해서 알아서 form을 정의해준다.

```python
from django import forms
from .models import Post, Comment

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
        fields = ['content', 'image'] # 이미지 추가
        

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
```



### urls.py

나중에 like 등 기능도 추가할거라 comment/create로 분리해서 만든다

```python
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/update/', views.update, name="update"),
    path('<int:post_id>/comments/create/', views.create_comments, name="create_comments")
]
```



### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment

def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    
    comment_form = CommentForm()
    
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/list.html', context)

def create_comments(request, post_id):
    pass
```





### list.html

comment_form 추가

```html
{% extends 'base.html' %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <div class="card-header">
          <span>{{ post.user.username }}</span>
        </div>
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <!--본인의 글만 삭제, 수정 버튼이 보이도록-->
          {% if request.user == post.user %}
            <a href="{% url 'posts:update' post.id %}" class="btn btn-success">수정</a>
            <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
          {% endif %}
          
          <!--Comment form-->
          <form>
            {{ comment_form }}
          </form>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```



bootstrap을 적용해보자.



```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <div class="card-header">
          <span>{{ post.user.username }}</span>
        </div>
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <!--본인의 글만 삭제, 수정 버튼이 보이도록-->
          {% if request.user == post.user %}
            <a href="{% url 'posts:update' post.id %}" class="btn btn-success">수정</a>
            <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
          {% endif %}
          
          <!--Comment form-->
          <form method="POST" action="{% url 'posts:create_comments' post.id %}">
            {% csrf_token %}
            {% bootstrap_form comment_form %}
            <button type="submit" class="btn btn-warning">댓글</button>
          </form>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```



buttons를 쓰지 않아도 돌아간다. 장고 표준 문서에서는 쓰는 것을 권장.



### views.py

```python
def create_comments(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id # 객체를 갖다 쓸 수 없어서 id를 넣어준다
        comment.save()
    return redirect('posts:list')
```





### list.html

```html
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}
  <!--모든 post를 보여줌-->
  <div class="row justify-content-center"> <!-- row는 포함된 것을 flex로 만든다 -->
    {% for post in posts %}
      <!--width 조정하면 가로폭 달라짐-->
      <div class="card" style="width: 40rem;">
        <div class="card-header">
          <span>{{ post.user.username }}</span>
        </div>
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
          <!--본인의 글만 삭제, 수정 버튼이 보이도록-->
          {% if request.user == post.user %}
            <a href="{% url 'posts:update' post.id %}" class="btn btn-success">수정</a>
            <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
          {% endif %}
          
          <!--Comment form-->
          <form method="POST" action="{% url 'posts:create_comments' post.id %}">
            {% csrf_token %}
            {% bootstrap_form comment_form %}
            <button type="submit" class="btn btn-warning">댓글</button>
          </form>
          {% for comment in post.comment_set.all %}
            <p>{{ comment.content }}</p>
          {% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```



















