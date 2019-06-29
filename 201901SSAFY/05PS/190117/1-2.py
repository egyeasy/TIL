# import sys
# sys.stdin = open("input1-2.txt", "r")

T = int(input())
for t in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    start = 0
    result = 0
    for idx, m in enumerate(mlist):
        if k >= m - start:
            if n - m <= k:
                result += 1
                break
            if idx == len(mlist) - 1 :
                result = 0
                break
            if k >= mlist[idx+1] - start:
                continue
            result += 1
            start = m
        else:
            result = 0
            break
    print(f"#{t} {result}")





