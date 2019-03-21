import sys
sys.stdin = open('1-2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    num = float(input())
    result = ""
    going_value = 0
    overflowed = False
    for exp in range(-1, -13, -1):
        two_exp = 2 ** exp
        if going_value + two_exp <= num:
            going_value += two_exp
            result += "1"
        else:
            result += "0"
        # print('going', going_value)
        # print(num)
        if going_value == num:
            break
    else:
        overflowed = True
    # print(result)
    if overflowed:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {result}")
