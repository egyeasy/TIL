# 190507 RESTful Django

## c9 last workspace 열어볼 것

지금까지 API 접해왔었고, 앞으로도 수많은 api 접할 것이다. 이전에 Restful하게 짜는 것이 무엇인지 설명했었다. GIPHY에 들어가보면, 이전에는 url들이 제멋대로였는데 이제 이걸 통일해보자는 생각에서 restful한 것이 등장. giphy에서 url에 /gifs/라고 돼있음. 영진위 api에도 open api > 제공 서비스 들어가보면 url을 확인할 수 있는데, 우리가 이 api를 던져주는 서버를 만들어볼 것. 영진위 API에 요청하면 json을 던져준다. 우리도 json을 던져주는 서버를 만들어보도록 하자.



## new project

궁극적으로 API 서버 만들기 

폴더 이름 `API` 만들기

`$ cd API`

`$ pyenv virtualenv 3.6.7 api-venv`

`$ pyenv local api-venv`

`$ pip install  django==2.1.8`

버전을 잘못 설치했다면? : `$ pip uninstall django` -> `$ y ` -> `$ pip list`로 삭제됐는지 확인

`$ django-admin startproject api .`

`$ python manage.py startapp musics`

특정 테이블 또는 모델의 복수형으로 앱 이름을 씀(music은 불가산(셀 수 없는)명사이긴 한데 일단 이렇게 쓰자)



이번에는 http response 중에서도 json을 주는 서버로 만들어볼 것이다.

google에 django json object 검색해보면 -> 'Serializeing django object' 문서가 나오는데 이건 어렵고,

`djanogo-rest-framework.org` 가보면 굉장히 편리하게 rest 서버를 만들어주는 pip가 있다.

`$ pip install djangorestframework`



### settings.py

```python
ALLOWED_HOSTS = ['*']  # 이렇게 쓰면 어디서든 돌아가게 돼서 편리하긴 하지만 위험하다.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'musics',
    'rest_framework',
]
```



이제 rest framework를 써보자.

restframework를 쓰는 것은 ModelForm을 쓰는 것과 굉장히 비슷함. 거의 완전 똑같다고 해도 무방할 정도



### musics/models.py

restframework의 모델을 정의해보자.

Artist **has many** Music

Music **belongs to** Artist

=> Artist : Music = 1 : N

```python
from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# 음악에 대한 평 남기기
class Comment(models.Model):
    content = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



잘 만들어졌는지 확인해보자.

`$ python manage.py createsuperuser`



### amdin.py

```python
from django.contrib import admin
from .models import Artist, Music, Comment

# Register your models here.
admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)
```



여기까진 평범한 django 앱이랑 똑같다!

`$ python manage.py runserver $IP:$PORT`

admin 들어가서 model 잘 만들어졌는지 확인





## api url 만들기

api url을 보면 version이 있다. ex. /lol/champion-mastery/**v4**/...

버전이 몇인지 명시되어있고 바뀔 때마다 바꿔주는 것이 관례.

`도메인/api/버전명/모델|데이터명`

=> `/api/v1/musics` 와 같은 식이 될 것

이제 url 문지기한테 가서 만들어주자.



### api/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('musics.urls')),
]
```





### musics/urls.py 생성

music에 대해 restful한 api를 만든다는 것은 Music/GET, Music/POST, Music/PUT(또는 Patch), Music/DELETE 와 같은 방식으로 짜게 된다는 것.

Read : GET
1) listing `/posts` 사실 이렇게 슬래시를 때는 것이 맞지만 django 관례상 붙여줘야함(`/posts/`) 그래서 강사님은 rest API 짤 때 django 안 쓴다고 함
2) 한 개 : `/posts/1`

Create : POST `/posts`

Update : PUT/PATCH `/posts/1`

Delete : DELETE `/posts/1`

Read의 최종적인 url은 `xxx.com/api/v1/musics`

```python
from django.urls import path
from . import views

urlpatterns = [
    # /api/v1/musics
    path('musics/', views.music_list)
]
```





## Serialize

이전 django project에서 html에 뭔가를 보여줄 때 form을 만들어서 했었는데,

이번엔 **serialize**해서 볼 것.

selrialize란? 우선 parsing을 보자. parsing은 string을 object로 만들어주는 것. 이것의 반대(= stringify) 작업의 정식 명칭이 serializing이다.



### musics/serializer.py 생성

serializer을 만들어줘야한다. modelform을 만드는 것과 유사함

```python
from rest_framework import serializers  # from django import forms 와 비슷
from .models import Music


class MusicSerializer(serializers.ModelSerializer):  # class MusicForm(forms.ModelForm)
    class Meta:  # ModelForm과 똑같은 방식으로 만든다.
        model = Music
        fields = ['id', 'title', 'artist',]  # API 응답은 id도 같이 넘겨줘야 한다.
```





### views.py

우리가 javascript에서 한 것은 `JSON.stringify`를 serializer로 쓴 것.

여기서의 시리얼라이저는 쿼리셋도 알아서 처리해준다.

여러개인지 여부(`many`)는 default는 False. True로 지정하면 배열 안에 있는 형태로 넣어준다.

rest framework import 소스가 궁금하다면 googling : "github django rest framework"

상위의 객체들의 소스를 따라가다보면 django의 기본적인 reponse class를 상속하고 있음을 알 수 있다.

더 상위에는 `HttpResponse`, `HttpResponseBase`가 있다. 진짜 바닥부터 짜려면 얘네를 직접 만들어야 한다.

```python
from django.shortcuts import render
from .serializer import MusicSerializer
from rest_framework.response import Response
from .models import Music

# Create your views here.
def music_list(request):
    # 여기서 쓰는 ORM 작업 정의 : 모든 음악들을 가져온다.
    musics = Music.objects.all()
    
    # 예전의 html 버전 같았으면
        # return render(request, 'list.html', {'musics': musics})
    # 여기서는 json을 만들어서 던져줄 것
    serializer = MusicSerializer(musics, many=True)  # 인자(무엇을시리얼라이즈할지, 여러개인지한개인지)
    return Response(data=serializer.data)  # 시리얼라이저 안의 데이터를 인자로 넣어준다.
    
    
```

이렇게 서버 돌리면 에러메시지 발생.

api_view라는 걸 써야함 : rest framework를 썼을 때 어떤 method를 쓸지 명시해줘야 함. 아쉽게도 django는 PUT/PATCH/DELETE를 구분할 기본 능력이 없음. 이걸 쓰기 위해서는 django-restframework가 지원하는 기능을 써야하는데 이것이 api_view.

api_view의 인자로 리스트를 넘기는데, 어떤 http method를 허용하게 할지 써주는 것.



```python
from django.shortcuts import render
from .serializer import MusicSerializer
from rest_framework.response import Response
from .models import Music
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def music_list(request):
    # 여기서 쓰는 ORM 작업 정의 : 모든 음악들을 가져온다.
    musics = Music.objects.all()
    
    # 예전의 html 버전 같았으면
        # return render(request, 'list.html', {'musics': musics})
    # 여기서는 json을 만들어서 던져줄 것
    serializer = MusicSerializer(musics, many=True)  # 인자(무엇을시리얼라이즈할지, 여러개인지한개인지)
    return Response(data=serializer.data)  # 시리얼라이저 안의 데이터를 인자로 넣어준다.
```



서버를 돌려보면, 우리가 html 렌더하지 않아도 알아서 페이지를 만들어서 보여줌.

admin에서 artist와 music을 추가해보자.

그러고 보면 잘 받아지는 것을 볼 수 있다.



2. postman에서도 보내보자.

   GET 요청으로 `https://last-pang-egyeasy.c9users.io/api/v1/musics/`로 보내면 json을 보내줌.



3. requests를 써보자.

   ### myapi.py

   ```python
   import requests
   
   response = requests.get('https://last-pang-egyeasy.c9users.io/api/v1/musics/')
   print(response.json())
   ```

   서버를 켠 상태에서 다른 터미널로 돌릴 것. 



 4. curl : postman의 cli 버전. 고수 느낌남. but 불편한 점이 많음.

    `$ curl -X GET "https://last-pang-egyeasy.c9users.io/api/v1/musics/"`



위의 여러 방법 중에서 우리는 postman을 쓸 것이다.



지금까지 Read의 listing이 끝남. 나머지 작업들을 처리해보자.



## 하나만 GET 해오는 것 짜기

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # /api/v1/musics
    path('musics/', views.music_list),
    # /api/v1/musics/1
    path('musics/<int:music_id>/', views.music_detail),
]
```



### views.py

```python
from django.shortcuts import render, get_object_or_404
from .serializer import MusicSerializer
from rest_framework.response import Response
from .models import Music
from rest_framework.decorators import api_view

# 생략 #

@api_view(['GET'])
def music_detail(request, music_id):
    # music_id에 있는 값으로 music을 찾아 가져온다.
    music = get_object_or_404(Music, pk=music_id)
    serializer = MusicSerializer(music)  # many=False가 default
    return Response(data=serializer.data)
```



앞의 listing과의 차이점은 json object를 리스트 안에 담지 않고 하나의 object만 반환해준다는 것.



이와 같은 방식이 restful한 django API를 만드는 일반적인 방식.



