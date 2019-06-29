# 05_detail

## 목표

- 영화 추천 사이트의 세부 페이지 구성
- Template Variable을 활용한 Template 제작



## 준비 사항

- Django Web Framework 사용
- C9



## 요구 사항

### 1. Django Setting

- project name : project5
- app name : detail
- django 언어 설정 : `ko`



### 2. base.html 구성

1. Bootstrap css, js 추가

   - CDN 경로로 추가
     

2. Nav Bar 구성

   - bootstrap component `navbar` 활용

   **05_detail\detail\urls.py**

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index),
       path('qna/', views.qna),
       path('mypage/', views.mypage),
       path('signup/', views.signup),
       path('<str:not_found>/', views.notfound),
   ]
   ```



3. Nav Bar 링크 위치

   `mr-auto`, `ml-auto` 활용



4. favicon 설정

   ```html
   <head>
       <link rel="icon" type="image/png" sizes="16x16" href="{% static 'img/favicon.png' %}">
   </head>
   ```



### 3. 페이지 구성

- `extends` base.html

  ```html
  <!-- base.html body -->
  {% block body %}
  {% endblock %}
  ```

  ```html
  <!-- other html -->
  {% extends 'base.html' %}
  {% block body %}
  	<!-- body content-->
  {% endblock %}
  ```

  

1. `/`

   1) Header

   - bootstrap component `jumbotron` 활용

   - 배경 이미지 : `jumbotron`의  `background-image` 속성으로 삽입

   - `display: flex` 활용하여 내부 텍스트 가운데 정렬


   
   2) Footer

   - bootstrap component `navbar` 활용

   - fixed가 아닌 페이지 최하단에 배치

     (참고 : http://qnrdlqkrwhdgns.canxan.com/prob/post/52)



2. `qna/`
   - 사용자의 질문을 받기 위한 페이지
   - bootstrap component `form` 활용
   - bootstrap grid system 활용



3. `mypage/`
   - 유저 정보를 출력하는 페이지
   - bootstrap component `card` 활용
   - bootstrap grid system 활용
   - `col-*-*` 클래스를 적용한 `div` 태그 내에 `card`를 삽입함으로써 margin 생성



4. `signup/`
   - 회원가입 페이지
   - bootstrap component `form` 활용
   - bootstrap grid system 활용
   - 이미지 넘쳐서 login form을 침범하는 것을 막기 위해 `img` 태그의 부모 태그 `div`에 `overflow: hidden` 속성 적용



5. `<str:not_found>/`

   - 위에서 만든 경로를 제외한 다른 요청이 들어오면 보여줄 404페이지
   - `variable routing` 활용
   - bootstrap component `jumbotron` 활용

   - 배경 이미지 : `jumbotron`의  `background-image` 속성으로 삽입

   - bootstrap grid systyem 활용 : `col-md-3` 활용하여 내부 텍스트 왼쪽 정렬