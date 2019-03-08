import sys
sys.stdin = open("input.txt", "r")


def cal(x, y):
    sum = 0
    for i in range(x, x+M):
        for j in range(y, y+M):
            sum += mat[i][j]
    return sum


TC = int(input())
for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    mat = [[0] * N for i in range(N)]
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    maxans = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ret = cal(i, j)
            if maxans < ret :
                maxans = ret

    print("#%d"%tc, maxans)



