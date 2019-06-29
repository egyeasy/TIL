# Python 기초
파이썬 기초 문법

## I. 입출력
### (1) 입력
파이썬에서 입력 받기

- `input()` : 사용자의 입력을 받는 함수
```python
n = input()
```


```python
# map(적용할 함수, 리스트 튜플 딕셔너리 등 literable)
a, b = list(map(int, input().split()))

a, b = [int(x) for x in input().split()]

print(a+b)
```

적용할 함수는 int(), str(), list(), set() 등



```python
print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')
```

따옴표 내의 \\는 디폴트로 하나 그대로 출력
but 조건 만족 시 보이는 대로 출력되지 않는다 -> 보이는 대로 하면 셋째 줄 마지막의 \는 줄바꿔도 이어진다는 기능으로 작동, 다섯번째 줄 \\\\는 \\ 하나만 출력하는 기능 수행.





### 입출력 더 빠르게

```python
import sys

for i in sys.stdin:
    print(i, end="") # end 파라미터를 통해 프린트문 뒤에 붙은 줄바꿈을 다르게 설정 가능
```


