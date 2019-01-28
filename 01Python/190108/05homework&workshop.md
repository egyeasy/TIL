# 05workshop

### Problem

```python
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
```



### 강사님 답안

```python
def is_palindrome(word):
    list_word = list(word)
    for i in range(len(list_word) // 2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True

print(is_palindrome('level'))
print(is_palindrome('apple'))
```





# 05homework

### 1번

 List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
def printlist(my_list):
    for my in my_list:
        print(my)

printlist([1, 2, 3])
```





### 2번

위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.

```python
def printlist(my_list):
    for idx, my in enumerate(my_list):
        print("index: {} value: {}".format(idx,my))

printlist([1, 2, 3])
```



###  3번

딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.

```python
key: for key in my_dict:
value: for value in my_dict.values():
key, value: for key, value in my_dict.items():
```



### 4번

None을 출력한다. return 값을 지정해주지 않을 경우 디폴트로 None을 출력하기 때문.

```python
def my_func(a, b):
    c = a + b
    print(c)
    
result = my_func(1, 5)
print(result)
```

