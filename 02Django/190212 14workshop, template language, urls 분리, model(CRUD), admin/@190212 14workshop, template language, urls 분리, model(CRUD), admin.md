# 14workshop review(c9: first_django)

c9  first-django

### 버전

django 2.1.7

Breaking.Feature.Fix

incompatible.하위호완(backwards-compatible).bug-fix

breaking-change.new-feature.bug-fix



# pjt: 1ST_WORKSHOP

### 이름 변경 -> 지운 다음 다시 만들면 됨

```bash
rm -rf first_project/
rm manage.py
ls -al
```



### lint

py_lint를 좀 빡세게 쓰면 4 space나 style(변수 이름 등)도 강제하게 된다.



### isval.html - django template language 조건문

```html
{% if month == 2 and day == 14 %}
    <h1>예</h1>
{% else %}
    <h1>아니요</h1>
{% endif %}

<p>{% lorem %}</p>
<p>{% lorem 3 p %}</p> <!-- 문단 3개 -->
<p>{% lorem 3 w %}</p> <!-- 단어 3개 -->

<h1>{% now "SHORT_DATETIME_FORMAT" %}</h1>
```

django built-in template tag 찾아보면 이런 것들 볼 수 있다. 나중에 프론트엔드/퍼블리셔/백엔드 등으로 업무 분장해서 일한다면 가급적 template tag는 지양할 것. 정말 필요할 때만 써라.

cf. css파일 경로는 root/static/ 안에 배치할 것!





### 이미지 가져오기 - lorem pixel, lorem picsum



# urls 분리하기

### urls.py

views 안의 것들만 포장하기

```python
from django.contrib import admin
from django.urls import path, include #inclue 추가
# from solution import views # 없어도 됨

urlpatterns = [
    path('admin/', admin.site.urls),
    # include('앱이름.urls')
    path('', include('solution.urls')), # 아무것도 안들어왔을 때 솔루션에 있는 urls.py를 쓰겠다.
]
```



### solution(app name) 폴더 밑에 파일 하나 만들기 = urls.py

솔루션이라는 앱 안에만 있는 기능들 모아주기

```python
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>/', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
    path('translate/', views.translate),
    path('result/', views.result),
]
```





# django html 복붙

### base.html

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
    <title>First Django!</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```



```python
{% extends 'base.html' %}

{% block body %}
<h1>환영합니다!</h1>

<form action="/catch"> <!-- 받을 자리에 넣어줌 -->
    <input type="text" name="message"/>
    <input type="submit" value="Sub던지기"/>
</form>
{% endblock%}
```





# catch - 입력 텍스트 아스키 art로 만들기

### 아스키 art

http://artii.herokuapp.com/make?text=ssafy

http://artii.herokuapp.com/make?text=ssafy&font=cosmic

http://artii.herokuapp.com/fonts_list



서버 돌리던거 끝내고

`pip install requests`



### views.py

requests를 통해 request 보내기

```python
def catch(request):
    msg = request.GET.get('message')
    styles= ['rounded', 'cosmic', 'gothic', 'alligator', 'avatar']
    style = random.choice(styles)
    url = f"http://artii.herokuapp.com/make?text={msg}&font={style}"
    result = requests.get(url).text #url에 요청을 보내서 받은 결과물을 text만 뽑아내서 result에 넣는다
    return render(request, 'catch.html', {'msg': result})
```





### catch.html

```html
{% extends 'base.html' %}


{% block body %}
<pre>{{ mseg }}</pre> <!-- preformatted tag. 입력한 문장 형태 그대로 브라우저에 표현 -->
{% endblock %}
```





# 네이버 파파고 API

### 명세

/translate

-> 한글 단어를 입력 받아

/result

-> (Papago NMT API) 번역 결과를 출력함



### views.py

```python
def translate(request):
    
    return render(request, 'translate.html')
    

def result(request):
    text = request.GET.get('message')
    
    naver_id = os.getenv("NAVER_ID")
    naver_secret = os.getenv("NAVER_PW")
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    
    data = {
        'source': 'ko',
        'target': 'en',
        'text': text
    }
    
    res = requests.post(url, headers=headers, data=data)
    doc = res.json()
    
    result = doc['message']['result']['translatedText']
    
    return render(request, 'result.html', {'result': result})
```



### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>/', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
    path('translate/', views.translate),
    path('result/', views.result),
]
```



### translate.html

```python
{% extends 'base.html' %}

{% block body %}
<h1>영어로 번역할 말을 입력하세요.</h1>

<form action="/result"> <!-- 받을 자리에 넣어줌 -->
    <input type="text" name="message"/>
    <input type="submit" value="번역하기"/>
</form>
{% endblock%}
```



### result.html

```python
{% extends 'base.html' %}

{% block body %}
<h1>{{ result }}</h1>
{% endblock %}
```





# Django Model(pjt:  ORM)

ORM 폴더 만들어서 project 만들고, articles 앱 만듦



### orm\settings.py - 앱 연결

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles.apps.ArticlesConfig', # 'articles'만 넣어도 돌아가긴 함
]
```



### articles\models.py

sqlAlchemy와 비슷하게 테이블을 만든다.

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    # 테이블 이름은 알아서 articles로 잡아줌
    # id 정의 안해도 알아서 만들어줌
    title = models.TextField() # title = models.CharField() 보다 명확함
    content = models.TextField()
```

Article이라는 모델을 이런 방식으로 쓰겠다.

이 blueprint를 실제 DB에 적용하는 작업이 **migration**



### migration

1. migration 파일을 생성
   `\ORM $ python manage.py makemigrations`
   migrations 폴더 하에 테이블이 정의된 것을 볼 수 있다.



2. DB에 적용
   `$ python manage.py migrate`



### 데이터베이스 테스트 -> shell을 통해서 한다.

`$ python manage.py shell`



### InteractiveConsole

```python
# articles안의models에다가 Article을 불러와서 쓰겠다.
from articles.models import Article

# 첫번째 글 쓰기
article = Article(title="Happy", content="Hacking")

# 저장
article.save()
```

SQLAlchemy에서 db.session.add -> db.session.commit() 해야 했던 것에 비해 간단



### READ

```python
# SQLAl - Article.query.all()
articles = Article.objects.all() #list를 강력하게 만든 QuerySet이 반환
a = articles[0]

a.title # 'Happy'
a.content # 'Hacking'

a = Article(title="하하하 두번째 글이다.", content="냉무")
a.save()
```



### filter

```python
a = Article.objects.filter(title="Happy").first()
a.title
a.content
```



### get

```python
a = Article.objects.get(pk=1) #primary key
a.title
```



### delete

pk는 1에서부터 시작. 2개를 넣었는데 2개를 삭제해서 최종적으로 0개 남음.

```python
a1 = Article.objects.get(pk=1)
a1.title
a1.content
a1.delete()

a2 = Article.objects.get(pk=2)
a2.title
a2.content
a2.delete()

articles = Article.objects.all()
len(articles) # 0
```



### CRU

```python
article = Article(title="이제 곧 수업 끝남", content="좀만 더 화이팅")
article.save()
article = Article(title="hey", content="it's done")
article.save()

articles = Article.objects.all()
a = articles[0]
a.title

Article.objects.get(pk=1)
article = Article.objects.get(title="hey")
article.title = "dong"
article.save() # 수정하면 save해줘야함
```





# 관리자 설정

### admin.py

```python
from django.contrib import admin
# 현재 폴더에 models라는 파일이 있는데 여기서 Article을 가져와서 쓸래
from .models import Article

# Register your models here.
admin.site.register(Article) # 여기에 등록만 하면 django가 관리를 쉽게 할 수 있도록 만들어줌
```

`/ORM $ python manage.py createsuperuser`

Username : admin

Password : 12341234



https://first-django190211-egyeasy.c9users.io/admin

으로 들어가서 로그인 하면 관리자 창이 뜸

- DB에 CRUD 가능



### customizing

```python
from django.contrib import admin
# 현재 폴더에 models라는 파일이 있는데 여기서 Article을 가져와서 쓸래
from .models import Article

## customizing ##
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',) # trailing comma

# Register your models here.
admin.site.register(Article, ArticleAdmin) #ArticleAdmin도 등록
```

서버 껐다 켠다.

DB 들어가면 title과 content를 바로 볼 수 있게 됨.