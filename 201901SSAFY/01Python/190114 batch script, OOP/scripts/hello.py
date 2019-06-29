# 자동화할 기능들을 파이썬으로 구현
import webbrowser
import sys

# url = "https://search.naver.com/search.naver?query=미세먼지"

# webbrowser.open(url)

# sys.argv 우리가 입력한 명령어들이 다 들어가 있음(띄어쓰기로 split돼서 들어감)
# => hello john
# => ["hello 파일 전체 경로", "john"]

print(sys.argv)
# hello 입력받은 사람의 이름을 출력해 보세요.
# => hello john 입력
# => hello john 출력

print("hello", ' '.join(sys.argv[1:]))
