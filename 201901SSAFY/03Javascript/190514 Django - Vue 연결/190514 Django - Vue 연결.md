# 190514 Django - Vue 연결

## c9 Instagram 프로젝트

현재 좋아요 누를 때 페이지 리로드가 일어남.

이걸 Vue.js로 고쳐보자.



## 시작

Vuejs, Axios CDN 복사

### base.html

주의 : CDN을 body 태그 하단에 붙이면 안됨! block에서 부를 때 vue가 불러지지 않았기 때문.

html의 모든 것이 load 되고 js 코드를 사용하는 것은 문제가 없다.

bootstrap - css를 가져와서 쓰는 것. css는 페이지가 다 렌더된 다음에 쓰기 때문에 문제가 되지 않음.

```html
{% load staticfiles %}

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <!-- Bootstrap downloaded css -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">

    <!-- Bootstrap CSS -->
    <!--<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">-->
    
    <!-- Font Awesome-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
    <!-- Vuejs -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!--Axios-->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <title>INSTAGRAM</title>
  </head>
  <body>
```



### profile.html

`{{ text }}`라고 쓰게 되면 django template 문법으로 인식된다. 그렇기 때문에 하단의 Vue data에 접근할 수 없다. 그럼 어떻게 해야 될까?

문법(delimeters = 구분자)를 커스텀으로 바꿔서 쓸 수 있다.

+팔로우 버튼을 구현해보자.

```html
{% block body %}
  <div class="row">
    <div class="col-3">
      {% if profile.profile.image %}
        <img class="rounded-circle" src="{{ profile.profile.image.url }}">
      {% else %}
        <img class="rounded-circle" src="{% static 'defaultimage.jpg' %}">
      {% endif %}
      <h1>{{ profile.username }}
        {% if user != profile %}
          {% if user in profile.followers.all %}
            <a class="btn btn-primary" href="{% url 'accounts:follow' profile.id %}">언팔로우</a>
          {% else %}
            <a class="btn btn-info" href="{% url 'accounts:follow' profile.id %}">팔로우</a>
          {% endif %}
          <div id="app">
            <div>[[ text ]]</div>
            <!-- 버튼을 클릭하면 팔로우할 수 있는 버튼 -->
            <button @click="follow({{ profile.id }})" class="btn btn-info">팔로우</button>
          </div>
        {% endif %}
      </h1>
    </div>

      <!-- ... -->


  <script>
    const app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
        'text': '뷰 작동한다리',
      },
      methods: {
        follow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/follow/`)
          console.log(`${profile_id}번 유저 팔로우 했다리`)
        }
      }
    })
  </script>
{% endblock %}
```

#### 일반적인 django 렌더링

django 서버에 client가 browser로 접속.

url에 요청하면 view.profile을 통해 html 템플릿을 만들어서 전달.

#### Vue.js 렌더링

Vue는 html과 포함되어 client에 전달되면 browser가 해석해서 쓰는 것.