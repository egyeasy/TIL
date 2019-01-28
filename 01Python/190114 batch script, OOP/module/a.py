# 두 개의 함수를 정의한다.
# cube(num) => num 세제곱 해주는 함수
def cube(num):
    return num ** 3

# squar(num) => num 제곱해주는 함수
def square(num):
    return num ** 2

if __name__ == "__main__":
    print(cube(3))
    print(square(23))

# 파일이 직접 실행되면 => "__main__"
# 파일이 불려오게 되면(import) => "파일이름"
# print(__name__)