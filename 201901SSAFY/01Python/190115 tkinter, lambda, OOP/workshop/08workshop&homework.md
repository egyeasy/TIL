# workshop

### app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'hi'

@app.route("/dictionary/<string:word>")
def hello(word):
    dic = {'apple': '사과', 'banana': '바나나', 'burger': '햄버거',
    'kiwi': '키위'}
    if word in dic.keys():
        return f"{word}은(는) {dic[word]}"
    else:
        return f"{word}은(는) 나만의 단어장에 없는 단어입니다!"
```





# homework

### 1번

(a) request

(b) response



### 2번

`pip install flask`



### 3번

(a) `from flask import Flask`

flask라는 모듈에서 Flask 클래스와 명령어 모음을 불러온다. flask.Flask라고 입력하지 않고 Flask라고 입력함으로써 Flask 클래스 내의 속성과 메소드에 대한 접근이 가능해진다.

### 4번

`flask run`

