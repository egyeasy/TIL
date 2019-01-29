import sqlite3

# 1. $ sqlite3 [데이터베이스] [파일명]
#      => 데이터베이스에 접속
# 2. SQL 쿼리 사용
#      => SELECT * FROM users;
#      => 결과를 가져다 줌
# 3. $ .exit
#       => 작업이 끝나면 콘솔 종료

# db = sqlite3.connect('test.sqlite3') # 데이터베이스 파일명
# cur = db.cursor() # DB 조작을 할 수 있는 커서를 만든다.
# cur.execute('SELECT * FROM users LIMIT 10') # 실행할 SQL query 문을 cursur에 넣어줌
# # cur.fetchone()
# data = cur.fetchall() # cursor에 저장한 모든 sql문 실행(가져옴) 
# 한 줄이 하나의 튜플로 됨. 2차원 리스트+튜플로 데이터들이 담긴다.

# for row in data:
#     print(row)


db = sqlite3.connect('test.sqlite3') # 데이터베이스 파일명
word = input("검색할 성(씨)을 입력해 주세요: ")

def search(keyword):
    """
    DB에서 검색어를 받아 검색을 해주는 친구
    """
    cur = db.cursor()
    cur.execute('SELECT * FROM users WHERE last_name == "{}"'.format(keyword)) # 따옴표 넣어줘야함!(바깥이랑 겹치지 않게 조심)
    data = cur.fetchall() # all 해야 모든 '이'씨의 데이터 받아볼 수 있다.
    cur.execute('SELECT COUNT(*) FROM users WHERE last_name == "{}"'.format(keyword))
    total = cur.fetchone()
    
    # 1. 해당 검색 결과의 '수'를 출력하고,
    
    # 2. 데이터들을 출력한다.
    
    # => '박'씨 성을 가지 ㄴ사람은 XX명입니다. 명단은 다음과 같습니다.
    # => (박, 010)
    
    return data, total[0]
    
data, total = search(word)
print("{}씨 성을 가진 사람은 {}명입니다. 명단은 다음과 같습니다.".format(word, total))

for row in data:
    print(row)

# for row in result:
#     print(row)