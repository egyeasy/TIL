# 190114 batch script, OOP

현재 디렉토리에 파이썬 파일 만든다.

win + r => 명령어 입력하면 미세먼지 등 정보를 알려주는 프로그램

python C:\Users\student\hello.py 하면 창이 잠깐 떴다가 사라진다!



### batch script (Windows)

: 윈도우의 여러 명령어를 모아서 한번에 실행할 수 있게 하는 코드(.bat)



`mkdir scripts`

파일 만들기 -> hello.bat



### 만들 것

윈도우즈 명령어 모음

1. python 파이썬
2. 잠시 멈춰라

```batch script
python c:\Users\student\scripts\hello.py %*
pause
```

pause는 bash 명령어가 아니라, cmd 커맨드. cmd 창에서도 사용할 수 있다.



### 실행

 c:\Users\student\scripts\hello.bat

.bat을 지우고 해도 실행된다(같은 이름 중에 최근에 실행한 것들 우선으로 실행해줌)



### 내 PC ->  속성 -> 고급 시스템 설정 -> 환경 변수

환경 변수는 윈도우 전체에서 공유하는 변수(alias jupyter notebook, API key)

cmd에서 경로 없이 'python'이라고만 쳐도 python이 실행 가능한 것이 환경 변수 설정 덕분임!



### 시스템 변수 -> Path -> 편집

새로 만들기 'C:\Users\student\scripts' -> 확인



### 실행

`hello` 라고 치면 간단하게 cmd 창 켜서 실행할 수 있음

hello.py를 편집해서 수행하고자 하는 기능을 추가



### 동적으로 만들 수는 없나요?

```batch script
@python c:\Users\student\scripts\hello.py %*
@pause
```

열리는 cmd창에 명령어가 출력되지 않게 만든다.

`%*` : 사용자로 하여금 hello.py에 다른 값을 같이 던져줄 수 있게 하는 것



```batch script
import webbrowser
import sys

print(sys.argv)
```

실행 `hello john` -> `john` 변수를 받아볼 수 있다.



### google.bat

구글 검색결과 창 열어주는 프로그램





# import, module

### a.py

```python
# 두 개의 함수를 정의한다.
# cube(num) => num 세제곱 해주는 함수
def cube(num):
    return num ** 3

# squar(num) => num 제곱해주는 함수
def square(num):
    return num ** 2

print(cube(2))
print(square(2))
```



### b.py (1)

```python
# a.py에서 정의한 걸 쓰고 싶어
import a

print(dir(a))

print(a.cube(2))
print(a.square(2))
```

`dir(a)` : a의 정체 알기





### b.py (1)

```python
# a.py에서 정의한 걸 쓰고 싶어
from a import cube, square

print(cube(2))
print(square(2))
```

b.py만 돌려도 a.py 내의 print가 실행된다.(a.py가 처음부터 끝까지 한번 실행된 후 가져와진다.)

그걸 방지하는 것이 아래 코드



### a.py 수정

```python
if __name__ == "__main__":
    print(cube(3))
    print(square(23))
```

`__name__`은 실행하는 맥락(execute context)
`print(__name__)`을 a에서 실행하면 `__main__`, b에서 실행하면 `a`(파일명)가 나온다.
`import requests`를 하면 requests.py 안에 정의된 get() 함수 등등이 불려와지는 것이다.

*파이썬은 파일이 실행되는 맥락을 직접 알려줘야 한다. 시작점을 명시해주어야 하는 것인데 그걸 `__name__`에 저장한다.



### 대문자는 뭐죠?

`bs4.BeautifulSoup()`,`from flask import Flask`

''클래스''는 항상 대문자로 쓰는 것이 Convention. BeautifulSoup이나 Flask는 클래스다.

bs4.py 파일 안에 `class Beautifulsoup:`이라는 class initializer가 있을 것.



- `from flask import *` : flask 안의 모든 것을 들고 오기. but 네임 스페이스 충돌이 일어날 수 있으므로 가급적 쓰지 말 것.







# OOP - 시험에 나옴!

https://lab.ssafy.com/seoul2/python2

git clone "clone https 주소"

폴더 들어가서 jupyter notebook -> oop.jpynb



### 프로그래밍의 3형식

1. 저장
2. 계산(조작)
   1) 조건
   2) 반복

##### Turing complete(튜링 완전 언어) : 저장, 조건, 반복 

하지만 이것만으로는 부족하고, 세상을 자연스럽게 인식하는 방식이 아니다.



### 세상을 요약하는 방법

##### - 주어와 동사

##### - 주부와 (서)술부

##### - Subject & Predicate

#### - Object & Method(행위)



### Object

- 세상에 존재하는 모든 물체, 사물, Thing

- 분류 체계 속의 예시
  예시) 나무 분류체계



### Object Oriented Programming

- 세상 모든 것을 인간이 인식하는 형태로 프로그래밍 하는 방법
- 상식적인 프로그래밍
- OOP





### 속성과 메소드

Class Car

- 속성 = Attribute = 멤버변수
  - self.brand
  - self.model
  - self.yunbi
  - self.color
- 메소드 = Method = 멤버함수
  - drive()
  - stop()