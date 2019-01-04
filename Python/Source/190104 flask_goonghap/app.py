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

# /gonghap => 입력받은 값을 그대로 출력한다.
@app.route("/goonghap2")
def goonghap2():
    # request : 사용자의 요청 정보
    # request.full_path : 요청을 받은 url의 전체 정보(/goonghap?me=강동주)
    # request.args : 물음표 뒤의 정보들을 dictionary로 받아온다. -> get()으로 indexing 할 수 있다.
    return str(request.args.get('me'))

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







