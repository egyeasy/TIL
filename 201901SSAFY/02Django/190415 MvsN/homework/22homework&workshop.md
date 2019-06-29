# 22homework

1. ```python
   class Post(models.Model):
       attachment = models.FileField(upload_to='uploads_files/')
   ```

2. ```python
   # 파일 주소에 접미사를 만들어줌
   MEDIA_URL = '/uploaded_files/'
   
   # root는 절대경로로 나타내기 때문에 os.path.join을 사용하여 주소를 합쳐서 MEDIA_ROOT로 지정해준다.
   MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
   ```

3. development 단계(debug = True)에서 프로젝트 최상단 폴더 하위의 static 폴더를 참조하려면 `STATICFILES_DIRS` 설정을 활용한다.

   ```python
   STATICFILES_DIRS = (os.path.join(BASE_DIR, "assets"),)
   ```

   

# 22workshop

1. bootstrap 홈페이지에서 compiled CSS and JS 다운로드

   <https://getbootstrap.com/docs/4.3/getting-started/download/>

2. 해당 폴더의 압축을 해제한 후 하위 폴더의 css, js 폴더를 프로젝트 폴더 하위의 assets 폴더 내부로 이동

3. `base.html` 수정

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
       
   
       <title>INSTAGRAM</title>
     </head>
     <body>
       {% include 'nav.html' %}
       <div class="container">
         {% block body %}
       
         {% endblock %}
       </div>
       <!-- Optional JavaScript -->
       <!-- jQuery first, then Popper.js, then Bootstrap JS -->
       <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
       <script src="{% static 'js/bootstrap.js' %}"></script>
     </body>
   </html>
   ```

   

