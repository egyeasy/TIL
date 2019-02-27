# 댓글 만들기(c9: first-django)

- 다른 테이블을 만들어서 댓글들을 저장하도록 한다.
- 기존의 DB에 붙이려면 댓글 개수 당 칼럼 1개가 필요해서 부적절



## 데이터베이스의 관계 - 테이블 간의 관계

### 1. 1:1의 관계

- 개인 - 주민등록증
- 법적인 부부



### 2. 1:N의 관계 

has_many, belongs_to

- 게시글 - 댓글
- ssafy반 - 학생

=> N(학생)쪽에서 자신이 어느 1(학년)의 소속인지 밝힌다(명찰 색깔).

| id   | content               | article_id(Foreign Key) |
| ---- | --------------------- | ----------------------- |
| 1    | 와 첫댓글이다.        | 1                       |
| 2    | 두번째 댓글           | 1                       |
| 3    | 야 순서놀이 하지마    | 1                       |
| 4    | ㅎㅏ하하 내가 첫 댓글 | 2                       |

댓글의 입장에서 article_id는 외부를 참조하는 foreign key(혹은 참조 키)



### 3. M:N

- 수강신청



### 4. 관계없음

- 지나가는 사람들 - 나





## comment table 만들기

### models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # foreign으로 연결된 글이 지워진 시점에 댓글들도 다 지움
```

`on_delete=models.CASCADE` : foreign으로 연결된 글이 지워진 시점에 댓글들도 다 지움



`$ python manage.py makemigrations`

: migrations 폴더 밑에 0002_comment.py가 생긴 것을 볼 수 있다.



`$ python manage.py migrate`



`$ python manage.py sqlmigrate articles 0002`

: SQL문 볼 수 있다. `"article_id" integer NOT NULL REFERENCES` 가 중요. 이름을 자동으로 만들어낸다.



`$ python manage.py dbshell`

: 그냥 shell이라 치면 장고 orm을 쓸 수 있는 python shell이 뜨고, 여기서는 sqlite 콘솔을 띄울 수 있다.



`.tables`

`.schema articles_comment` : 스키마 볼 수 있다.



==================================================================

`$ python manage.py shell`

```python
from articles.models import Article
```

=============이렇게 썼던 것을 jupyter notebook 비슷하게 만들기(iPython)=====

### (앞으로 Django 설치할 때 같이 설치해줄 것)

`$ pip install django_extensions ipython` # 2개 동시에 깔기



### settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pastlife',
    'articles',
    'django_extensions',
]
```



`$ python manage.py shell` : jn과 비슷한 방식으로 작동. syntax highlight 지원

```python
from articles.models import Article, Comment
Article.objects.all()
exit()
```



`$ python manage.py shell_plus` : import 안 해도 다 import 되게 바뀜. 모든 환경 자동 로드

```python
Article.objects.all()
```



### models.py - repr

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"<{self.id}번 글, {self.title}: {self.content}>"
    
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # foreign으로 연결된 글이 지워진 시점에 댓글들도 다 지움
    
    def __repr__(self):
        return f"<{self.content}>"
```



`$ python manage.py shell_plus`

```python
Comment.objects.all()

article1 = Article.objects.get(id=5)
article1

comment = Comment(content="첫번째 댓글이다!", article=article1) # 속할 글(객체)을 그대로 넣어주면 됨
comment.save()

Comment.objects.all()
Comment.objects.first()
Comment.objects.first().content
```



### 연결해서 조회하기

```python
Comment.objects.first().article # 첫번째 댓글이 속해있는 article
Comment.objects.first().article.content

Article.objects.first().comment_set.all() # 게시글에 속한 댓글 모두 조회. 클래스이름.lower()_set
```



```python
comment2 = Comment(content="두번째 글의 첫번째 ㄷㅅ글!", article=Article.objects.all()[1])
# article_id = 2 라고 해도 된다.
comment2.save()
Comment.objects.all()[1]
Comment.objects.all()[1].article # 자동으로 article property를 만들어준 것
Comment.objects.all()[1].article_id # Comment 객체에서 article_id 조회
Comment.objects.all()[1].article.id # Article 객체에서 id 조회
```

article이 property로 자동 추가됨으로써 굉장히 편리해짐.



```python
Comment.objects.all()[1].article # 아래를 축약할 수 있음
Article.objects.get(pk=Comment.objects.all()[1].article_id) # 라고 쓰지 않아도 된다.
```



```python
Article.objects.first().comment_set.all() # 아래를 축약해서 표현할 수 있게 됨
Comment.objects.filter(article_id=Article.objects.first().id).all()
```



더 쉽게 쓸 수 있다.

### models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"<{self.id}번 글, {self.title}: {self.content}>"
    
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") ########## 여기 related_name 추가 ####
    
    def __repr__(self):
        return f"<{self.content}>"
```



models.py 는 콘티, 대략적인 스케치. makemigrations는 스케치. 



`exit()`

`$ python manage.py makemigrations`

: 변경을 알아차려서 알아서 0003의 migration 파일 만들어 냄.

`$ python manage.py migrate`

`$ python python manage.py sqlmigrate articles 0003`

: SQL 문으로 하면 엄청나게 복잡한 과정을 간단하게 해결한 것임을 볼 수 있다.



`$ python manage.py shell_plus`

```python
Article.objects.first().comment_set.all() # 이것도 귀찮다면 이제 더 쉽게 쓸 수 있다
Article.objects.first().comments.all() # related_name의 default가 'comment_set'이어서 'comment_set'은 더이상 못 씀
```





## 댓글 Application 만들기

### detail.html

```html
{% extends 'articles/base.html' %}

{% block body %}
<h1>제목: {{ article.title }}</h1>
<h1>내용: {{ article.content }}</h1>
<a href="{% url 'articles:index' %}">홈으로</a>
<hr>
<h3>댓글들</h3>
<form action="/articles/{{ article.id }}/comment/">
    <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
</form>

{% endblock %}
```



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
    path('<int:num>/edit/', views.edit, name='edit'),
    path('<int:num>/update/', views.update, name='update'),
    path('<int:num>/delete/', views.delete, name='delete'),
    path('<int:article_id>/comment/', views.comment, name='comment'), ### 추가 ###
]
```



### views.py

```python
from django.shortcuts import render, redirect # redirect 쓰려면 import
from .models import Article, Comment

# ... #


def detail(request, num):
    a = Article.objects.get(pk=num) # pk 대신 id를 써도 된다.
    # comments = Comment.objects.filter(article_id=num) # 이걸 써서 다시 DB를 조회하지 않아도 됨!
    context = {
        'article': a,
 		# 'comments': comments # 안 넘겨줘도 됨
    }
    
    
    return render(request, 'articles/detail.html', context)

# ... #


def comment(request, article_id):
    # 댓글을 DB에 저장한다
    content = request.GET.get('content')
    comment = Comment(content=content, article_id=article_id)
    comment.save()
    
    return redirect('articles:detail', article_id)
```



### detail.html

```html
{% extends 'articles/base.html' %}

{% block body %}
<h1>제목: {{ article.title }}</h1>
<h1>내용: {{ article.content }}</h1>
<a href="{% url 'articles:index' %}">홈으로</a>
<hr>
<h3>댓글들</h3>
<form action="/articles/{{ article.id }}/comment/">
    <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
</form>

{% for comment in article.comments.all %} <!-- 템플릿 엔진에선 all괄호 안 씀! -->
    <p>{{ comment.content }}</p>
{% endfor %}

{% endblock %}
```

연결이 되어있기 때문에 views.py 조정할 필요 없이 html단에서 바로 조회해서 출력할 수 있다.





## GET을 POST로 바꾸기

### detail.html

```python
{% extends 'articles/base.html' %}

{% block body %}
<h1>제목: {{ article.title }}</h1>
<h1>내용: {{ article.content }}</h1>
<a href="{% url 'articles:index' %}">홈으로</a>
<hr>
<h3>댓글들</h3>
<!--<form action="/articles/{{ article.id }}/comment/">-->
<form action="/articles/{{ article.id }}/comment/" method="POST">
    <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
    {% csrf_token %} <!--토큰 보내기 : form 안에 어느 곳에든 써주면 됨-->
</form>

{% for comment in article.comments.all %} <!-- 템플릿 엔진에선 all괄호 안 씀! -->
    <p>{{ comment.content }}</p>
{% endfor %}

{% endblock %}
```

detail.html 파일의 form 태그 요소 검사하면 type="hidden"으로 토큰이 담기는 걸 볼 수 있다.



### views.py

```python
# ... #
def comment(request, article_id):
    # 댓글을 DB에 저장한다
    content = request.POST.get('content')
    comment = Comment(content=content, article_id=article_id)
    comment.save()
    
    return redirect('articles:detail', article_id)
```



### CSRF(Cross Site Request Forgery)

client와 server 사이에서 request와 response를 가로채서 위조.

이것을 막기 위해 client가 보내는 정보에 token을 담는다. 

- 글을 보러 와서 요청할 때 client에게 token을 주고, 댓글을 작성해서 요청할 때 받은 token을 내도록 한다.
- token = 도장
- token도 뚫릴 수 있지만, 최소한의 방어라고 할 수 있음
- 페이지 들어올 때마다 다른 토큰을 주면 hack.py는 막을 수 있음

위키피디아 영문판에 가장 잘 정리되어 있음.



### 무엇으로부터 방어?(GET방식일 경우)

프로젝트 제일 바깥 디렉토리에 `hack.py`생성

### hack.py

```python
import requests
from time import sleep

# 사이트에 접속하지 않고, 댓글을 죠오올라 많이 남기기
content = "싸이트에 가지도 않고 댓글 남길 수 있지롱"
url = f'https://first-django190211-egyeasy.c9users.io/articles/5/comment/?content={content}'

while True:
    sleep(10) # 10초 쉬고 가는 지점.
    # token을 받아오는 절차를 추가하면 POST도 뚫을 수 있다.
	request.get(url) # 10초마다 댓글을 하나 만들게 된다.
```