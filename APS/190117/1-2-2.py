import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    start = 0
    result = 0
    for idx, m in enumerate(mlist):
        if n - m > k:
            if k >= m - start:
                if k >= mlist[idx+1] - start:
                    continue
                result += 1
                start = m
            else:
                result = 0
                break
        else:
            result += 1
            break

    print(f"#{t} {result}")





