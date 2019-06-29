from flask import Flask, render_template, send_file, request, redirect
from flask_sqlalchemy import SQLAlchemy # import csv
from datetime import datetime
    
app = Flask(__name__) # 생성함수 초기값으로 __name__ : execution contenxt


# ORM 버전
# 초기 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// : 상대경로, //// : 절대경로
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.init_app(app) # init app에 app을 넣어주면 flask app과 orm이 하나가 됨

class Quest(db.Model): # 상속 받아야
    __tablename__ = "questions" # table 이름
    id = db.Column(db.Integer, primary_key=True) # schema 정의
    content = db.Column(db.String, nullable=False)

db.create_all() #초기설정 끝



@app.route("/")
def index():
    # DB에 저장된 모든 질문들을 불러온다.
    quests = Quest.query.all() # Quest에 담겨있는 모든 애들에게 query를 날려 가져오겠다.
    # print(quests) # [<Quest 1>, <Quest 2>, <Quest 3>, <Quest 4>] 객체가 담겨있다.
    # print(quests[0].content) 객체 내용 출력
    
    return render_template('index.html', quests=quests)


@app.route("/ask")
def ask():
    # 데이터베이스에 저장
    # print(request.args)
    q = request.args.get('question')
    
    # ORM 통해 DB에 데이터를 저장하는 방법
    # SQL - INSERT INTO questions (id, content) VALUES (1, 사용자가 입력한 값)
    quest = Quest(content=q) # 인스턴스 생성
    db.session.add(quest) # db야 방금 만들어놓은 quest 친구를 추가좀 해주렴
    db.session.commit() # db야 추가한 걸 실제로 저장해주렴
    
    return redirect('/') # 다시 index 페이지로 보내겠다.(import redirect)
    

@app.route('/delete/<int:id>') # 들어오는 임의의 숫자 지정
def delete(id): # 위에서 받은 id를 아래에서 쓸 수 있게 함.
    # 특정 데이터 레코드를 지워준다.
    # SQL - DELETE FROM questions WHERE id == id
    q = Quest.query.get(id) # 일단 제거할 것을 찾는다. id == id인 객체가 q에 들어감(input = primary key)
    db.session.delete(q) # db야 q에 담긴 친구를 지워줘.
    db.session.commit()
    
    return redirect('/')



# csv 버전

# @app.route("/")
# def index():
#     return render_template('index.html')
    
# @app.route("/ask")
# def ask():
#     question = request.args.get('question')
#     with open('question.csv', 'a') as f:
#         writer = csv.writer(f) # f를 쓸 수 있게 만들어줘
#         # [index, 질문, 날짜+시간 ]
#         former_idx = 0 # 파이썬은 안에서도 바깥을 볼 수 있지만 실수 방지를 위해 미리 정의
#         with open('question.csv', 'r') as f2:
#             reader = csv.reader(f2)
#             former_idx = len(list(reader)) # 형변환(type casting) 가능
#         new_idx = former_idx + 1
#         dt = datetime.now()
#         # writer.writerow([question, datetime.today().strftime("%Y/%m/%d %H:%M:%S")]) # writerow 안에는 무조건 리스트가 들어가야 한다.
#         # writer.writerow([question, '{}년 {}월 {}일 {}시 {}분'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute)])
#         writer.writerow([new_idx, question, datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")])
#     return render_template('ask.html', question=question)  
    

# @app.route("/quest")
# def quest():
#     result = []
#     with open('question.csv', 'r') as f:
#         reader = csv.reader(f) # f를 읽을 수 있게 만들어줘. 파이썬 리더('r')을 쓰는게 아니라 csv의 reader를 쓰겠다는 것.
#         # print(list(reader)) # [['dididid야야ㅑ'], ['질무짐룬']] 출력. 이 작업을 하면 reader의 내용이 모두 사라짐
#         for row in reader:
#             result.append(row)
#     return render_template('quest.html', questions=reversed(result)) # 최근 질문이 맨 위로 오도록