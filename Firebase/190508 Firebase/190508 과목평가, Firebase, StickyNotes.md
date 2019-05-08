# 190508 과목평가, Firebase

# 과목평가 풀이

- js object에서 가져올 때 get 메소드는 없다.

- `addEventListener` 두 번째 인자 함수를 기명으로 넣어도 제대로 동작한다. this는 클릭하든 button을 가리킨다. this : `function`일 때는 button(불리는 곳의 객체. 수동적), arrow일 때는 window/global(불리는 곳(button)의 bind를 풀어버리고 최상단(브라우저에서는 window, node에서는 global 객체)를 가리킨다.)

  python의 self는 주체적 -> 스스로를 가리킴. js는 수동적이어서 불리는 곳을 가리킴.

  vue에서는 항상 `function`을 써라 -> this가 Vue app을 가리켜야하기 때문에 bind를 풀면 안된다.

- Vue template에 표현할 때 `{{ const number = 1 }}`는 불가하다. **함수의 return 값**으로 쓸 수 있는 것들만 쓸 수 있다.

- `v-if` 는 false면 렌더링 자체가 되지 않는다. `v-show`는 렌더링 되고 `display: none`으로 처리됨.



# 오후 수업 Firebase

### IaaS(Infrastructure as a Service)

이와 비슷하게 PaaS(Platform as a Service)가 있다. 데이터베이스 등은 서비스 업체에 맡기는 개발 방식. ex) 구글의 firebase

cf. 마케팅 : 유입 -> 전환 -> 재구매. 추적대상 ex) 도착하고 다음 버튼을 누르기까지의 시간. 첫번째 버튼이 뭔지. 궁극적으로 구매 전환율. 실제로 회사 가서 보면 마케팅 스토리 상에서 어떤 데이터 포인트를 만들지를 결정하고 구현하게 되는데 이것을 js로 짜게 된다. 이걸 지원하는 곳이 생겼고 페이스북이 이걸 잘한다. 어떻게 **깔때기**처럼 고객들을 개미지옥에 빠지게 할 것인가의 문제. PM으로 갈 데 더 중요한 내용이기도 하다. 



## Firebase

홈페이지 접속 -> 구글 로그인 후 시작하기 -> 프로젝트 추가

우리는 Vue.js 앱의 데이터베이스로 firebase를 쓸 것

- 프로젝트 이름 : test

- 위치 : 대한민국, asia-northeast1(데이터를 놔둘 위치)

- 구글 애널리틱스 사용 V
- 약관 두 개 동의 후 프로젝트 생성

A/B testing : 페북에서는 자신의 앱을 계속해서 테스팅하는데, 사람들마다 버전을 다르게 해서 배포한다. 두 버전에 대해서 사람들의 이용 상황을 추적 -> 실제 배포 버전에 반영.

unified matrix : 처음 들어와서 2주동안 몇번을 탔는지(우버), 신규 유저가 몇명의 유저를 친추했는지(페북) 등 각종 메트릭을 설치해서 UI를 끝없이 바꿔간다.

오늘날의 개발은 일단 shipping하고, 무결한 완성품을 만들기보다는 유저들의 피드백을 만들면서 계속해서 발전시켜나감. -> 소프트웨어 방법론 최고의 수업 : 버클리 **Software as a Service** 

agile : 모든 게 불확실하다. 유저는 ㄸㄹㅇ + 자기도 원하는 게 뭔지 모른다. 문서화한 것을 진행한다고 해서 최선이 보장이 안된다. 소프트웨어는 자동체, 반도체와는 다르게 출시를 하더라도 업데이트를 할 수 있음 -> 첫 번째 버전을 작은 버전으로 shipping해도 크게 문제가 없다. 주로 2주의 주기로 뛰면서 업데이트. 2주 마다의 결과를 계속해서 확인. 



### DB

SQL -> ORM -> Firestore

중구난방이었던 초기 DB 시스템을 정리하고자, 그리고 개발자가 아닌 사람도 data에 접근할 수 있도록 SQL이 고안됨. ('~~에서 ~~를 주세요') 그걸 기반으로 DBMS가 등장. but 개발자들이 SQL을 배워야하는 부담이 생겨서 프로그래밍 언어로 DB를 짜는 방식이 ORM. 이것도 귀찮아서 다른 곳에 맡기는 것이 파이어베이스 DB service(Firestore)

개발 탭 -> Database -> Realtime database 테스트 모드로 시작

- 데이터 : 이건 결과물이 single file 같은 JSON인데 사용하기 쉽게 만들어놨다.

- 규칙 : js object. '읽고 쓸 수 있다.'

- 백업 : 알아서 백업해준다. 자주 백업할수록 돈을 더 내야함
- 사용량 : 얼마나 사용했는지 볼 수 있다. 이런 DB들은 대체로 사용량에 비례해서 돈을 지불하게 된다.

Firebase를 쓰면 우리 서비스의 데이터를 어디서든 접근할 수 있다.



### index.html

<https://firebase.google.com/docs/web/setup?hl=ko> (google firebase cdn)에서 복붙.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Firebase TODO</title>
</head>
<body>
    
    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
    <script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    var config = {
        apiKey: "<API_KEY>",
        authDomain: "<PROJECT_ID>.firebaseapp.com",
        databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
        projectId: "<PROJECT_ID>",
        storageBucket: "<BUCKET>.appspot.com",
        messagingSenderId: "<SENDER_ID>",
    };
    firebase.initializeApp(config);
    </script>
</body>
</html>
```



API_KEY 등을 채워줘야한다.

Firebase 사이트 -> 데이터 -> 나와있는 주소가 우리가 쓸 DB의 주소(https://test-4bfbb.firebaseio.com/)

`test-4bfbb`를 복사 -> <DATABASE_NAME>, projectId 자리에 복붙.

지금 당장 안 쓰는 것들은 지우기.

좌상단 설정 들어가서 API 키 복붙



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Firebase TODO</title>
</head>
<body>

    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
    <script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    const config = {  // var 안쓰기로 했으므로 const로 바꿔줌
        apiKey: "*************************",
        // authDomain: "<PROJECT_ID>.firebaseapp.com",  // 일단 지금은 안쓴다.
        databaseURL: "https://test-4bfbb.firebaseio.com",
        projectId: "test-4bfbb",
        // storageBucket: "<BUCKET>.appspot.com",
        // messagingSenderId: "<SENDER_ID>",
    };
    firebase.initializeApp(config);

    const db = firebase.database()  // 데이터베이스를 쓰기 위해 객체를 만들어쓴다.
    </script>
</body>
</html>
```



Vuejs 설치하고,

Vue + FIrebase를 연결해주는 Vuefire를 설치해야.

Vuefire cdn으로 검색해서 `min.js` 버전 복사(minified된, 못 생긴 작은 버전 -> 속도 빠름)



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Firebase TODO</title>
</head>
<body>
    <div id="app">

    </div>

    <!-- Vue js -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Firebase database -->
    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>

    <!-- Vue Fire -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vuefire/1.4.5/vuefire.min.js"></script>
    <script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    const config = {  // var 안쓰기로 했으므로 const로 바꿔줌
        apiKey: "AIzaSyDTo76Oi1NTWog6kLGRjX4nfADjYe60WjM",
        // authDomain: "<PROJECT_ID>.firebaseapp.com",  // 일단 지금은 안쓴다.
        databaseURL: "https://test-4bfbb.firebaseio.com",
        projectId: "test-4bfbb",
        // storageBucket: "<BUCKET>.appspot.com",
        // messagingSenderId: "<SENDER_ID>",
    };
    firebase.initializeApp(config);

    const db = firebase.database()  // 데이터베이스를 쓰기 위해 객체를 만들어쓴다.
    
    const app = new Vue({
        el: "#app",
        data: {
            newTodo: ''
        }
    })
    </script>
</body>
</html>
```



이전엔 data에 `todos`를 만들고 `addTodo`를 통해 todos를 업데이트 시키는 방식. 이번에는 파이어베이스 Database를 활용할 것이다.



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Firebase TODO</title>
</head>
<body>
    <div id="app">
        <div>
            <input v-model="newTodo" @keyup.enter="addTodo">
        </div>
        <ul>
            <li v-for="todo in todos">{{ todo }}</li>
        </ul>
    </div>

    <!-- Vue js -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Firebase database -->
    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>

    <!-- Vue Fire -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vuefire/1.4.5/vuefire.min.js"></script>
    <script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    const config = {  // var 안쓰기로 했으므로 const로 바꿔줌
        apiKey: "AIzaSyDTo76Oi1NTWog6kLGRjX4nfADjYe60WjM",
        // authDomain: "<PROJECT_ID>.firebaseapp.com",  // 일단 지금은 안쓴다.
        databaseURL: "https://test-4bfbb.firebaseio.com",
        projectId: "test-4bfbb",
        // storageBucket: "<BUCKET>.appspot.com",
        // messagingSenderId: "<SENDER_ID>",
    };
    firebase.initializeApp(config);

    const db = firebase.database()  // 데이터베이스를 쓰기 위해 객체를 만들어쓴다.
    
    const app = new Vue({
        el: "#app",
        data: {
            newTodo: '',
            todos: [],
        },
        methods: {
            addTodo: function() {
                this.todos.push(this.newTodo)
                this.newTodo = ''
            }
        }
    })
    </script>
</body>
</html>
```



글 쓰고 엔터치면 저장됨. 이제 이걸 DB에 저장해보자.

이제 Vue와 Firebase를 연결해보자. 그러려면 firebase를 코드에 추가해줘야 함.

ref를 통해 바로가기(reference)를 만들고, 원본의 todos를 없앨 것.

- 그럼 템플릿에서 어떻게 DB의 todos를 불러올까?

  일단 data 내에 `status`를 새로 만든다.

  `computed`를 통해 변경될 때마다 계산된 결과물을 계속 뽑아내기



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Firebase TODO</title>
</head>
<body>
    <div id="app">
        <div>
            <input v-model="newTodo" @keyup.enter="addTodo">
        </div>
        <ul>
            <!-- <li v-for="todo in todos">{{ todo }}</li> -->
            <!-- 기존의 todos도 다르게 가져와야 한다: computed 소환 -->
            <li v-for="todo in current">{{ todo['.value'] }}</li> 
        </ul>
    </div>

    <!-- Vue js -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Firebase database -->
    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>

    <!-- Vue Fire -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vuefire/1.4.5/vuefire.min.js"></script>
    <script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    const config = {  // var 안쓰기로 했으므로 const로 바꿔줌
        apiKey: "AIzaSyDTo76Oi1NTWog6kLGRjX4nfADjYe60WjM",
        // authDomain: "<PROJECT_ID>.firebaseapp.com",  // 일단 지금은 안쓴다.
        databaseURL: "https://test-4bfbb.firebaseio.com",
        projectId: "test-4bfbb",
        // storageBucket: "<BUCKET>.appspot.com",
        // messagingSenderId: "<SENDER_ID>",
    };
    firebase.initializeApp(config);

    const db = firebase.database()  // 데이터베이스를 쓰기 위해 객체를 만들어쓴다.
    
    const app = new Vue({
        el: "#app",
        data: {
            newTodo: '',
            // todos: [],
            // status: 
        },
        methods: {
            addTodo: function() {
                // newTodo를 todos에 추가
                // this.todos.push(this.newTodo)
                this.$firebaseRefs.todos.push(this.newTodo)  // 아래의 todos에 접근
                // -> firebase의 reference(바로가기)에 접근하기 때문에 Vuefire에 의해 이렇게 접근 가능하게 되어있다.
                this.newTodo = ''
            }
        },
        firebase: {  // vue를 firebase와 연결시키는 역할
            todos: db.ref('todos')  // (객체의 키 이름): db.ref('테이블 이름')
        },
        computed: {
            current: function() {
                return this.todos  // 이렇게 써도 db todos에 접근이 가능하다.
            }
        }
    })
    </script>
</body>
</html>
```



- NoSQL은 기본적으로는 JSON의 형태.

  Django ORM은 RDBMS, Excel의 형태.

- Firebase는 js코드로 JSON 다루듯이 DB에 접근할 수 있게 하는 것. JSON parsing도 필요하지 않다.

  firebase realtime database source를 참고해볼 것

- vue fire는 orm의 역할, 즉 DB와 프론트엔드를 연결시켜주는 역할





# 늦은 오후 수업 Rest Framework with JSON

JSON을 던져주는 Django Rest Framework를 만든다.

클라이언트 어플리케이션

server로 데이터를 요청해서 받아온 것으로 Application을 구동하는 것.

서로 data만 통신하고 각자의 Application을 돌리는 시스템을 구축할 것이다.





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

































