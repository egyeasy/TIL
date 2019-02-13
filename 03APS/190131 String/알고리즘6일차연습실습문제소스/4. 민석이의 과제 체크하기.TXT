import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N, S = list(map(int, input().split()))
    scores = list(map(int, input().split()))

    cnt = [0] * N
    for i in range(S):
        cnt[ scores[i]-1 ] += 1

    res = "#%d "%tc
    for i in range(N):
        if cnt[i] == 0:
            res += "%d "%(i+1)
    print(res)
