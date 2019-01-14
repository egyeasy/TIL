### 1번

numbers.Number, numbers.Complex, numbers.Real, numbers.Rational, numbers.Integral



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
```

