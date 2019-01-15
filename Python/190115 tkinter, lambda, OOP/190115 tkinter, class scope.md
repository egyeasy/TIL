# 위젯 만들기

### Tkinter

파이썬 GUI 위젯 구현 가능

`$ python widget.py`로 파일 실행하면 창이 열림

pack()의 순서에 따라 정렬 순서가 결정된다.

tkinter 강좌도 있으니 구글링 통해서 속성들 찾아보면 됨.





# 파이썬

### 함수 객체

```python
# high order function - 함수를 (괄호 없는 형태로) 인자로 넣어서 쓸 수 있다.
def ahnyung():
    print("ahnyung")

def ohiyou():
    print("ohiyou")
    
def hello():
    print("hello")

def greeter(func):
    func()

greeter(ohiyou)
```



### 선언, Instantiate, Initiate

```python
# 클래스 선언
class Person:
    def __init__(self, name):
        self.name = name
        
# instantiate
a = Person()

# 초기화(initialize)
a = Person("john")

# instantiate는 initialize를 포함한다!
```



### 함수를 변수처럼

```python
def hello():
    print("hello")

hi = hello

print(hi()) # hello() 실행 출력
print(hello) # 주소값 도출

def greeter(func):
    func()
    
greeter(hello)
```

python tutor에서 살펴볼 것. hello 값에 hi가 binding 된다. 결과적으로 hello와 hi라는 이름에 함수가 할당된 것이다. 함수를 호출(call)한다는 것은 ( )라는 호출 연산자를 통해서 가능하다.



```python
def hello():
    return "hello"

def greeter(func):
    func() # 이거 대신 return func()를 써야 출력됨
    
print(greeter(hello))
```

이렇게는 출력이 되지 않는다.



```python
print(sum([1, 2, 3, 4]))

sum = "하하하 너는 이제 sum을 쓰지 못한다"

print(sum)

print(sum([1, 2, 3, 4]))

print = "print도 못씀"

print()
```

합을 도출하는 내장함수의 네임스페이스에 string 값이 바인딩 돼서 sum() 함수를 쓸 수 없게 됨.



```javascript
# 변수에 함수 할당하는 방식으로 함수 정의 가능
hi = function() {
    return "hi"
}

# 또는
function hi() {
    return "hi"
}
```

python, javascript => 일급 객체로서의 함수를 이용할 수 있는 언어. 변수처럼 할당 및 연산 가능.



### 함수와 클래스의 Scope

- 함수 1 안에 정의된 함수 2가 있을 때 1에서 2의 변수를 접근할 수 없다.
- 클래스 변수는 바깥에서 클래스.변수명으로 타고 들어갈 수 있다. but `def __init()__`과 같은 함수 내의 변수는 함수 scope 룰의 적용을 받으므로 바깥에서 접근할 수 없다.