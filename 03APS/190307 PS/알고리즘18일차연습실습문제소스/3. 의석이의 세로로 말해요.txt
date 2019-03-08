import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    arr = [0] * 5

    maxLen = 0
    for i in range(5):
        arr[i] = input()
        if maxLen < len(arr[i]) :
            maxLen = len(arr[i])

    print("#%d"%tc, end=' ')
    for j in range(maxLen):
        for i in range(5):
            if j >= len(arr[i]) : continue
            print(arr[i][j], end='')
    print()
