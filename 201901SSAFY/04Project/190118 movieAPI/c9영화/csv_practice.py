import csv # 첫번째와 같은 방식으로 하면 쓰는 작업이 굉장히 불편하다.

lunch = {
    '김밥카페': '02-1234-5678',
    '양자강' : '02-2345-6789',
    '순남시래기': '02-9876-5432'
}

lunch2 = {
    '상호명': '양자강',
    '전화번호': '02-2345-6789'
}

# 보통은 이런 형태의 데이터로 저장될 것!
lunch3 = [
    {
        '상호명': '양자강',
        '전화번호': '02-2345-6789'        
    },
    {
        '상호명': '김밥카페',
        '전화번호': '02-1234-5678'        
    },
    {
        '상호명': '순남시래기',
        '전화번호': '02-9876-5432'        
    }
    
]

menu = ['김밥', '탕수육', '시래기']

# with open('lunch.csv', 'w') as f: # f에 open한 것을 담고 with context가 끝나면 닫는다
#     # f.write('김밥카페, 02-1234-5678')
#     for name in lunch:
#         # f.write("{}, {}\n".format(name, lunch[name]))
#         f.write(', '.join((name, lunch[name])) + '\n')

# 리스트를 가지고 csv를 만들 때
# with open('lunch.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(menu) # 인자로 리스트를 넣어주면 알아서 한 행에 ',' 구분자로 만들어준다
    
# dictionary를 가지고 csv 만들 때    
# with open('lunch.csv', 'w') as f:
#     field = ('상호명', '전화번호')
#     writer = csv.DictWriter(f, fieldnames=field) # 기본 라이터가 아닌 dict 라이터 소환(f, 필드네임(튜플형태))
#     writer.writeheader() # 헤더를 써줘야함
#     writer.writerow(lunch2)


# with open('lunch.csv', 'w') as f:
#     field = ('상호명', '전화번호')
#     writer = csv.DictWriter(f, fieldnames=field)
#     writer.writeheader()
#     for l in lunch3:
#         writer.writerow(l)

with open('lunch.csv', newline='') as f:
    reader = csv.reader(f) # 파이썬 리더('r')을 쓰는게 아니라 csv의 reader를 쓰겠다는 것
    # print(reader[0][0]) # 여기서는 일반 iterable로 구현돼서 안됨. 행렬처럼 저장했을 때 이렇게 호출할 수 있다.
    for row in reader:
        print(row) # row 별로 리스트화 돼서 출력될 것
        print(row[0])