### 1번

int, str, dictinary, list, set 등 대부분의 자료형



### 2번

5번. `print(type(5))`를 통해 int class에 속함을 알 수 있다.



### 3번

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def greeting(self):
        return f'안녕하세요. {self.name}입니다. {self.age}살입니다.'
    
p1 = Person('홍길동', 20)
p1.greeting()

p2 = Person('둘리')
p2.greeting()
```

