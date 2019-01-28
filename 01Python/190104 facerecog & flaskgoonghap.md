# Naver API #2 - Face Recognition

`res.json` 은 json 형식으로 받은 response를 파이썬 dictionary 형태로 바꾸어줌



#### dictionary를 보기 좋게 프린트하는 방법

```python
from pprint import pprint as pp
pp(result)
```



#### dictionary 다른 출력 방법

```python
doc = {'message': {'@service': 'naverservice.nmt.proxy',
             '@type': 'response',
             '@version': '1.0.0',
             'result': {'srcLangType': 'en',
                        'tarLangType': 'ko',
                        'translatedText': '야호'}}}
# 아래 형식을 더 많이 쓰게 됨 - 찾는 데이터가 없을 경우 에러메시지 대신 None 타입을 출력
pp(doc.get('message').get('result').get('translatedText'))
```





## Face Recognition

### CFR API 사용하기

```
// 유명인 얼굴 인식 API
https://openapi.naver.com/v1/vision/celebrity

// 얼굴 감지 API - 사진에서 얼굴인 부분을 감지
https://openapi.naver.com/v1/vision/face
```



### API 요청 메시지 예시

```
[HTTP Request Header]
POST /v1/vision/celebrity HTTP/1.1
Host: openapi.naver.com
Content-Type: multipart/form-data; boundary={boundary-text}
X-Naver-Client-Id: {앱 등록 시 발급받은 Client ID}
X-Naver-Client-Secret: {앱 등록 시 발급 받은 Client Secret}
Content-Length: 96703

--{boundary-text}
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

{image binary data}
--{boundary-text}--
```

요청 시 files 파라미터에 content와 관련한 정보를 대체하여 사진 url이 들어가게 된다.



### string 출력

1. 합체 : concatenation

   ```python
   "PP" + "AP"
   ```

2. 수술 : interpolation(보간법) - pythonic한 방법

   ```python
   name = "john"
   greeting = "Hello  {}".format(name)
   ```

3. 자르기 : slice

   ```python
   greeting = "hello"
   print(hello[1:5])
   # 다음은 불가(immutable)
   # "hello"[4] = "s"
   # 대신
   "hello".replace("o", "s")
   ```


### 얼굴인식 연습1

```python
# 인식시킬 사진을 clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req (파일)

# 1. requests를 통해 clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다

import requests
from pprint import pprint as pp

naver_id = ""
naver_secret = ""

url = "https://openapi.naver.com/v1/vision/celebrity"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# open함수는 파일을 열 때 씀. 파일을 연 결과물을 image에 넣어준다.
# rb는 read binary : 바이너리 형식으로 연다.
files = {
    'image': open('lim.jpg', 'rb')
}

# 파일을 보내는 것이라서 files 파라미터로 보내줌
res = requests.post(url, headers=headers, files=files)
pp(res.json())

name = res.json().get('faces')[0].get('celebrity').get('value')
conf = res.json().get('faces')[0].get('celebrity').get('confidence')

# XXX입니다. XX% 확신할 수 있습니다.
print("{}입니다. {}% 확신할 수 있습니다.".format(name, round(float(conf)*100)))
```



파일은 텍스트 데이터가 오고 갈 때와는 느낌이 다르다. file stream을 가져오는 거라는 표시가 필요함(streaming requests)

`dir(class, 변수명)` : class, 변수에서 사용할 수 있는 메소드 표시 ex) `dir("hello")`

`image_res.raw` : 이미지를 날 것 그대로(이진수) 만들어서 줌.

`read` or `read()` : 그냥 read 쓰면 'method'라고 나온다 -> ()써야 함 <bound method HTTPResponse.read of <urllib3.response.HTTPResponse object at 0x7faeb1232be0>> 



### 이미지 url 그대로 가져와서 요청하기

```python
import requests
from pprint import pprint as pp

naver_id = "d00SP7JEdZRtLTS28EmG"
naver_secret = "Xt0R1rmu7w"

url = "https://openapi.naver.com/v1/vision/celebrity"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# 이미지 주소 복사 해서 .jpg로 끝나는 이미지들만 가능
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Kang_Seul-gi_at_Hello_Counselor_on_November_11%2C_2018_%284%29.jpg/250px-Kang_Seul-gi_at_Hello_Counselor_on_November_11%2C_2018_%284%29.jpg"

# 1. 해당하는 image_url에 요청을 보내서,
image_res = requests.get(image_url, stream=True) # file stream을 가져올 것이다

# 2. 파일데이터를 받아 저장해 둔다.
# print(image_res.raw.read())


# open함수는 파일을 열 때 씀. 파일을 연 결과물을 image에 넣어준다.
# rb는 read binary : 바이너리 형식으로 연다.
files = {
    'image': image_res.raw.read()   #open('lim.jpg', 'rb') # 저장된 사진 쓰기
}

# 파일을 보내는 것이라서 files 파라미터로 보내줌
res = requests.post(url, headers=headers, files=files)
pp(res.json())

name = res.json().get('faces')[0].get('celebrity').get('value')
conf = res.json().get('faces')[0].get('celebrity').get('confidence')

# XXX입니다. XX% 확신할 수 있습니다.
print("{}입니다. {}% 확신할 수 있습니다.".format(name, round(float(conf)*100)))
```





# FLASK

`$ sudo pip3 install flask`

`$ flask run --host 0.0.0.0 --port 8080`

`$ app.run(debug=True)`로 저장 할 때마다 리프레쉬 되는 기능 활용할 수도 있지만, 나중에 장고 서버 등 이용하 때 로드가 안 되는 경우가 발생할 수 있어서 안 쓰도록 한다!

### 예제 서버 돌리기

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```



![flask](C:\Users\student\Desktop\flask.png)





```python
from flask import Flask
app = Flask(__name__)

from datetime import datetime as dt

@app.route("/") # 주문 받는 방법(요청을 받는 방법)
def index():
    return "Hello" # 서비스 주는 방법(응답을 보내는 방법)

# 가변 주소(variable routing)
@app.route("/hello/<name>")
# 꺽쇠 안의 변수를 쓰겠다고 함수에 선언해줘야 함
def hello(name):
    return "hello," + name

# /cube/4 => 64
@app.route("/cube/<int:num>") # type을 미리 강제해서 지정해줄 수도 있다.
def cub(num):
    return num + "^3 = "+ str(int(num)**3)

# /reverse/hello => olleh
@app.route("/reverse/<word>")
def reverse(word):
    # ::로 두번째 인자까지 무시하고 세번째 인자에 -1을 넣는다.
    return word[::-1]

# /ispal/racecar => true
# /ispal/john => false
@app.route("/ispal/<pal>")
def ispal(pal):
    # 내가 작성한 것
    # for i in range(len(pal)//2):
    #     if pal[i] != pal[-i-1]:
    #         return "false"
    #     else:
    #         return "true"

    # 강사 예시
    # if pal == pal[::-1]:
    #     return str(True)
    # else:
    #     return str(False)

    # 삼항연산자로 표현
    return "True" if pal == pal[::-1] else str(False)


# /isitnewyear => 1월 1일이면 "예" 아니면 "아니요"
@app.route("/isitnewyear")
def newyear():
    if dt.now().month == 1 and dt.now().day == 1:
        return "<h1>예</h1>"
    else:
        return "<h1>아니요</h1>"

```



/isitnewyear 에서 html 값을 return할 수도 있지만 큰 html 문서라면 따로 두는 것이 좋다. 이 때 템플릿 엔진이 필요하다. flask에서는 render_template을 쓴다. 해당 위치에 templates라는 폴더를 만들고 하부에 html 파일을 만든 뒤 다음과 같이 사용한다.

```python
from flask import Flask, render_template, send_file
app = Flask(__name__)

from datetime import datetime as dt
import random

@app.route("/") # 주문 받는 방법(요청을 받는 방법)
def index():
    # return str(random.sample(range(1, 46), 6))
    # return send_file('home.html') # send_file의 디폴트 위치는 같은 폴더 내
    lotto = random.sample(range(1, 46), 6)
    return render_template('index.html', lucky=lotto) # 서비스 주는 방법(응답을 보내는 방법)
```

send_file로는 동적 렌더링이 불가하기 때문에 html에 파이썬으로 계산한 결과를 보내주는 역할이 불가하다. 그래서  render_template을 사용한다.





### fake 네이버 검색 엔진

- html 파일 작성할 때 느낌표+tab
- 사용자의 입력을 받는 태그는 <form>, <input>이다. 받을 입력의 type을 파라미터로 지정해줄 수 있다.
- 검색 엔진의 검색창 form 태그를 요소 검사 해보면 어떤 변수를 어디로 보내는지 파악할 수 있다.
- 검색 결과 url에서 q=ssafy는 ''입력받는 변수의 이름=입력내용''이다. 이걸 form 태그에서 넘겨줄 수 있다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Naver</title>
</head>
<body>
    <h1>Naver</h1>
    <!-- action에는 받은 값을 어디로 보낼지 입력(그냥 '/'는 홈을 가리킨다) -->
    <form action="https://search.naver.com/search.naver">
        <!-- 받을 입력의 이름과 타입을 지정할 수 있다 -->
        <input name="query" type="text"></input>
    </form>
</body>
</html>
```





### 궁합 예제

- html form으로 입력받은 이름을 app.py에서 처리하기 위해 flask의 `request`를 import 한다.

```python
from flask import Flask, render_template, send_file, request
app = Flask(__name__)

from datetime import datetime as dt
import random

@app.route("/") # 주문 받는 방법(요청을 받는 방법)
def index():
    # return str(random.sample(range(1, 46), 6))
    # return send_file('home.html') # send_file의 디폴트 위치는 같은 폴더 내
    lotto = random.sample(range(1, 46), 6)
    return render_template('index.html', lucky=lotto) # 서비스 주는 방법(응답을 보내는 방법)

# /gonghap => 입력받은 값을 그대로 출력한다.
@app.route("/goonghap")
def goonghap():
    # request : 사용자의 요청 정보
    # request.full_path : 요청을 받은 url의 전체 정보(/goonghap?me=강동주)
    # request.args : 물음표 뒤의 정보들을 dictionary로 받아온다. -> get()으로 indexing 할 수 있다.
    return str(request.args.get('me'))
```







## 페이크 궁합

### app.py

```python
from flask import Flask, render_template, send_file, request
app = Flask(__name__)

from datetime import datetime as dt
import random

hogu = []

@app.route("/") # 주문 받는 방법(요청을 받는 방법)
def index():
    # return str(random.sample(range(1, 46), 6))
    # return send_file('home.html') # send_file의 디폴트 위치는 같은 폴더 내
    lotto = random.sample(range(1, 46), 6)
    return render_template('index.html', lucky=lotto) # 서비스 주는 방법(응답을 보내는 방법)

# /goonghap => 나와 상대방의 이름 + 페이크 궁합값(60-99).
@app.route("/goonghap")
def goonghap():
    me = request.args.get('me')
    you = request.args.get('you')
    hogu.append([me, you])
    num = random.randint(60, 99)
    return render_template('goonghap.html', me=me, you=you, rating=num)

@app.route("/god")
def god():
    return str(hogu)
```



### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>궁합</h1>
    <p>궁합을 알려드립니다 !</p>
    <form action="/goonghap">
        <p>당신의 이름</p>
        <input name="me" type="text"></input>
        <p>그분의 이름</p>
        <input name="you" type="text"></input>
        <input type="submit">
    </form>
</body>
</html>
```



### goonghap.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>궁합</title>
</head>
<body>
    <h1>{{ me }}님과 {{ you }}님의 궁합은 {{ rating }}%입니다.</h1>
</body>
</html>
```











