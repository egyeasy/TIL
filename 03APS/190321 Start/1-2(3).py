# 정수로 만들어줘서 작업하는 방식 - 따라가기가 더 수월하다
import sys
sys.stdin = open('1-2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = input()
    float_num = float(num)
    index = -1
    for i in range(0, 13):
        if float_num * 2**i == int(float_num * 2**i):
            int_num = int(float_num * 2**i)
            index = i
            break
    # print(int_num, index)

    if index == -1:
        print(f"#{tc} overflow")
    else:
        result = [0] * index
        while index > 0:
            index -= 1
            result[index] = int_num % 2
            int_num //= 2
        print(f"#{tc} ", end="")
        for i in range(len(result)):
            print(result[i], end="")
        print()