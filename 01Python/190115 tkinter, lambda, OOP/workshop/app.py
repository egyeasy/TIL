from flask import Flask
app = Flask(__name__)


@app.route("/") # 주문 받는 방법(요청을 받는 방법)
def index():
    return 'hi'


# 가변 주소(variable routing)
@app.route("/dictionary/<string:word>")
# 꺽쇠 안의 변수를 쓰겠다고 함수에 선언해줘야 함
def hello(word):
    dic = {'apple': '사과', 'banana': '바나나', 'burger': '햄버거',
    'kiwi': '키위'}
    if word in dic.keys():
        return f"{word}은(는) {dic[word]}"
    else:
        return f"{word}은(는) 나만의 단어장에 없는 단어입니다!"





