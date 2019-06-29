from flask import Flask, render_template, send_file, request
import csv
from datetime import datetime

app = Flask(__name__) # 생성함수 초기값으로 __name__ : execution contenxt

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ask")
def ask():
    question = request.args.get('question')
    with open('question.csv', 'a') as f:
        writer = csv.writer(f) # f를 쓸 수 있게 만들어줘
        # [index, 질문, 날짜+시간 ]
        former_idx = 0 # 파이썬은 안에서도 바깥을 볼 수 있지만 실수 방지를 위해 미리 정의
        with open('question.csv', 'r') as f2:
            reader = csv.reader(f2)
            former_idx = len(list(reader)) # 형변환(type casting) 가능
        new_idx = former_idx + 1
        dt = datetime.now()
        # writer.writerow([question, datetime.today().strftime("%Y/%m/%d %H:%M:%S")]) # writerow 안에는 무조건 리스트가 들어가야 한다.
        # writer.writerow([question, '{}년 {}월 {}일 {}시 {}분'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute)])
        writer.writerow([new_idx, question, datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")])
    return render_template('ask.html', question=question)


@app.route("/quest")
def quest():
    result = []
    with open('question.csv', 'r') as f:
        reader = csv.reader(f) # f를 읽을 수 있게 만들어줘. 파이썬 리더('r')을 쓰는게 아니라 csv의 reader를 쓰겠다는 것.
        # print(list(reader)) # [['dididid야야ㅑ'], ['질무짐룬']] 출력. 이 작업을 하면 reader의 내용이 모두 사라짐
        for row in reader:
            result.append(row)
    return render_template('quest.html', questions=reversed(result)) # 최근 질문이 맨 위로 오도록