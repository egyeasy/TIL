# Stick Notes

## Django Rest Framework

1. Django rest framework 로 api 서버를 만든다
2. `content` 필드 1개를 가지고 있는 `Memo` 모델을 만든다.
3. POST 요청으로 Memo 를 create 할 수 있다.
   - POST http://localhost:8000/api/v1/memos/
4. GET 요청으로 모든 Memo 를 read 할 수 있다.
   - GET http://localhost:8000/api/v1/memos/

## Vue.js

1. textarea 태그와 Vue 의 data 인 `content` 를 양방향 바인딩한다.
2. `created` life cycle 에서 axios 로 위 api 서버에서 memos 를 불러온 뒤 Vue 의 data 인 memos 에 바인딩한다.
3. submit 버튼이 눌리면 axios 로 위 api 서버로 `content` 의 내용을 작성한뒤 응답받은 memo 를 Vue 의 memos 에 push 한다.
4. memo 가 작성될때마다 textarea 의 값은 초기화된다.





## 구현

### start project

`$ mkdir STICKYNOTES`

`$ cd STICKYNOTES`

`$ pyenv virtualenv 3.6.7 sticky-venv`

`$ pyenv local sticky-venv`

`$ pip install django==2.1.8`

`$ pip install djangorestframework`

`$ django-admin startproject stickynotes .`

`$ python manage.py startapp memos`



### settings.py

```python
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'memos',
]
```



### models.py

```python
from django.db import models

# Create your models here.
class Memo(models.model):
    content = models.TextField()
    
    def __str__(self):
        return self.content
```



`$ python manage.py makemigrations`

`$ python manage.py migrate`



### serializers.py

```python
from rest_framework import serializers
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'content']
```



### stickynotes/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('memos.urls')),
]
```



### memos/urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path('memos/', views.create_and_list),
]
```



### admin.py

```python
from django.contrib import admin
from .models import Memo

# Register your models here.
admin.site.register(Memo)
```



### views.py

```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Memo
from .serializers import MemoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def create_and_list(request):
    if request.method == 'POST':
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # 사용자가 잘못된 값 입력했을 때 알아서 400에러 출력 -> 다른 에러 핸들링 할 필요X
            serializer.save()
            # return Response(serializer.data)
    else:
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
    return Response(data=serializer.data)
```



<https://last-pang-egyeasy.c9users.io/api/v1/memos/> 로 들어가서 content에 json 형식으로 memo 만들어서 넣어주면 post 되는 것을 확인할 수 있다.



## Vue

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <link rel="stylesheet" href="./style.css">
</head>
<body>
  <div id="main">
    <h1>Sticky Notes</h1>
    <textarea></textarea>
    <button>Write!</button>
    <div id="memo-container">
      <div class="memo" v-for="memo in memos">
        <div class="memo-delete-button"></div>
        {{ memo.content }}
      </div>
    </div>
  </div>
  <script>
  const app = new Vue({
    el: '#main',
    data: {
      url: 'https://last-pang-egyeasy.c9users.io/api/v1/memos',  // 여러분의 c9 주소
      content: '',
      memos: [],
    },
    methods: {
      // 서버로 요청을 보내서 memo를 작성하고 응답받은 memo 데이터를 this.memos에 푸쉬
      writeMemo: function() {
      },
    },
    // 서버로 요청을 보내서 memos를 불러온 뒤 this.memos에 할당
    created: function() {  // created : 뷰 인스턴스가 새로 생성되면 한번 실행하고 끝남
      axios.get(this.url)
        .then(response => {
          console.log(response.data)
        })
    }
  })
  </script>
</body>
</html>
```



이렇게 하면 CORS 에러가 난다. 어떻게 해결할까?



### Cross-Origin Resource Sharing(CORS)

서버가 있는 도메인과는 다른 도메인에서 서버 도메인으로 AJAX call을 요청하는 것은 기본적으로 막혀있다.

서버에서 다른 도메인에서 오는 걸 허락해줘야 응답을 해줄 수 있다.

현재 5500 포트에서 다른 곳으로 요청을 하는 중 -> Cross Origin 상태

REST framework에서 허락을 해주도록 만들어보자.



구글에 `django rest framework cors`를 검색해보자.

맨 위 https://www.django-rest-framework.org/topics/ajax-csrf-cors/로 들어가보면 패키지를 어떻게 적용하는지 볼 수 있다.



`$ pip install django-cors-headers`



### settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'memos',
    'corsheaders',
]

```



미들웨어를 추가해줘야 한다.

그리고 어떤 곳에서 접근을 할 것인지를 허락해줘야한다 -> 그냥 모든 곳에서 허락하자

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS 대응
    # 'django.middleware.common.CommonMiddleware',  # 위에 있으므로 지워도됨
]

CORS_ORIGIN_ALLOW_ALL = True
```





### GET 응답 보여주기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <link rel="stylesheet" href="./style.css">
</head>
<body>
  <div id="main">
    <h1>Sticky Notes</h1>
    <textarea></textarea>
    <button>Write!</button>
    <div id="memo-container">
      <div class="memo" v-for="memo in memos">
        <div class="memo-delete-button"></div>
        {{ memo.content }}
      </div>
    </div>
  </div>
  <script>
  const app = new Vue({
    el: '#main',
    data: {
      url: 'https://last-pang-egyeasy.c9users.io/api/v1/memos/',  // 여러분의 c9 주소
      content: '',
      memos: [],
    },
    methods: {
      // 서버로 요청을 보내서 memo를 작성하고 응답받은 memo 데이터를 this.memos에 푸쉬
      writeMemo: function() {
      },
    },
    // 서버로 요청을 보내서 memos를 불러온 뒤 this.memos에 할당
    created: function() {  // created : 뷰 인스턴스가 새로 생성되면 한번 실행하고 끝남
      axios.get(this.url)
        .then(response => {
          // console.log(response.data)
          this.memos = response.data
        })
    }
  })
  </script>
</body>
</html>
```



이제 POST form 입력받아서 서버에 POST 요청 해보자.

```html

<body>
  <div id="main">
    <h1>Sticky Notes</h1>
    <textarea v-model="content"></textarea>
    <button @click="writeMemo">Write!</button>
      
      <!-- 생략 -->
    
    <script>
  const app = new Vue({
    el: '#main',
    data: {
      url: 'https://last-pang-egyeasy.c9users.io/api/v1/memos/',  // 여러분의 c9 주소
      content: '',
      memos: [],
    },
    methods: {
      // 서버로 요청을 보내서 memo를 작성하고 응답받은 memo 데이터를 this.memos에 푸쉬
      writeMemo: function() {
        axios.post(this.url, { content: this.content })
          .then(response => {
            // console.log(response.data)
            this.memos.push(response.data)  // 방법 1(방법 2는 완전히 새롭게 모든 memo를 호출하는 로직)
            this.content = ''
          })
      },
    },
    // 서버로 요청을 보내서 memos를 불러온 뒤 this.memos에 할당
    created: function() {  // created : 뷰 인스턴스가 새로 생성되면 한번 실행하고 끝남
      axios.get(this.url)
        .then(response => {
          // console.log(response.data)
          this.memos = response.data
        })
    }
  })
  </script>
```



코드를 리팩토링 해보자 -> memo를 다시 전부 가져오는 로직

```html
  <script>
  const app = new Vue({
    el: '#main',
    data: {
      url: 'https://last-pang-egyeasy.c9users.io/api/v1/memos/',  // 여러분의 c9 주소
      content: '',
      memos: [],
    },
    methods: {
      // 서버로 요청을 보내서 memo를 작성하고 응답받은 memo 데이터를 this.memos에 푸쉬
      writeMemo: function() {
        axios.post(this.url, { content: this.content })
          .then(response => {
            // console.log(response.data)
            // this.memos.push(response.data)  // 방법 1
            this.getMemos() // 방법 2 - 완전히 새롭게 모든 memo를 호출하는 로직
            this.content = ''
          })
      },
      getMemos: function() {
        axios.get(this.url)
          .then(response => {
            // console.log(response.data)
            this.memos = response.data
          })
      }
    },
    // 서버로 요청을 보내서 memos를 불러온 뒤 this.memos에 할당
    created: function() {  // created : 뷰 인스턴스가 새로 생성되면 한번 실행하고 끝남
      this.getMemos()
    }
  })
  </script>
```





## DELETE

추가로 해본다면, `memo-delete-button`이 있다. 이것에 대한 삭제 로직을 서버 단에서 DELETE method로 구현해볼 것.

### urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path('memos/', views.create_and_list),
    path('memos/<int:memo_id>/', views.delete),
]
```



### views.py

```python
@api_view(['DELETE'])
def delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return Response({ "message" : "삭제되었습니다!"})
```



### index.html

```html
      <div class="memo" v-for="memo in memos">
        <div @click="deleteMemo(memo.id)" class="memo-delete-button"></div>
        {{ memo.content }}
      </div>


  <script>
  const app = new Vue({
    el: '#main',
    data: {
      url: 'https://last-pang-egyeasy.c9users.io/api/v1/memos/',  // 여러분의 c9 주소
      content: '',
      memos: [],
    },
    methods: {
      deleteMemo: function(memo_id) {
        // console.log(this.url + memo_id.toString() + '/')
        // console.log(`${this.url}${memo_id}/`)
        // axios.delete(this.url + memo_id + '/')
        axios.delete(`${this.url}${memo_id}/`)
          .then(response => {
            console.log(response.data)
            this.getMemos()
          })
      }
    },
  </script>

```





















