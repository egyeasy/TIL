# import sys
# sys.stdin = open("input1-4.txt", "r")

T = int(input())
for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    maxx = sum(alist[:m])
    minn = sum(alist[:m])
    i = 1
    while i < n - m + 1:
        value = sum(alist[i:i+m])
        if value > maxx:
            maxx = value
        elif value < minn:
            minn = value
        i += 1

    print(f"#{t} {maxx-minn}")