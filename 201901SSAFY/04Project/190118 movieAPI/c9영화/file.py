# '파일'의 형태는 영구저장 방식
movies = ['말모이', '랄프', '짱구', '물괴']


# 쓰기
# f = open('a.txt', 'a') # 'w' : 쓰기 모드로 새로 만들기 -> a.txt가 없을 때 file.py를 실행하면 생성됨
# f.write("wow this is file!" + "\n") # 파일에 쓸말을 적는다. w모드는 덮어쓰기이므로 있던 내용은 삭제된다. a모드를 통해 append 가능
# f.close()

# 읽기
# f = open('a.txt', 'r') # read로 열기 위해서는 r모드로 열어야
# # print(dir(f)) # read가 있다
# print(f.read())
# f.close()

# content = "this is content"

# f = open('b.txt', 'w')
# f.write(content)
# f.close() # close는 꼭 해야한다. 안하면 뒤에서 접근할 수가 없음. 이게 귀찮아서 with를 씀


# f = open('movies.txt', 'w')
# for movie in movies:
#     f.write(movie + ',')
# f.close()

# 파일 읽어오기
f = open('movies.txt', 'r')
print(f.read(), type(f.read())) # 인자 필요 없음
f.close()

# 파이썬 리스트로 만들어주기
movies = []

f = open('movies.txt', 'r')
movies = f.read().split(",")
f.close()

print(movies[0])