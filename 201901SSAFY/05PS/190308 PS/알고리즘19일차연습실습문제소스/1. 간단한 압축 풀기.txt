import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    data = [[0] * 2 for i in range(N)]

    for i in range(N):
        data[i][0], cnt = input().split()
        data[i][1] = int(cnt)

    print("#%d"%tc)

    cnt = 0
    for i in range(N):
        for j in range(data[i][1]):
            print(data[i][0], end='')
            cnt += 1
            if cnt % 10 == 0:  print()

    print()












