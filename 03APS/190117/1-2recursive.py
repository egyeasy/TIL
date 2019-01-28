import sys
sys.stdin = open("input.txt", "r")

def run(k, n, m, mlist, start=0, cnt_start=0, result=0):
    if n <= 0:
        return result
    go = 0
    for i in range(cnt_start, m):
        if k >= mlist[i] - start:
            if k >= mlist[i+1] - start:
                cnt_start += 1
                continue
            go = mlist[i] - start
            cnt_start += 1
        else:
            break
    if go == 0:
        return 0
    cnt_start -= 1
    start += go
    result += 1
    return run(k, n-go, m, mlist, start, cnt_start, result)

T = int(input())
for t in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    print(f"{t} {run(k, n, m, mlist)}")