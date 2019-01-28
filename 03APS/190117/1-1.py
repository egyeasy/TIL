# import sys
# sys.stdin = open("input1-1.txt", "r")

TC = int(input())

def maxmin(alist):
    maxx = alist[0]
    minn = alist[0]
    for a in alist:
        if a > maxx:
            maxx = a
        elif a < minn:
            minn = a
    return maxx - minn

for tc in range(1, TC + 1):
    n = int(input())
    alist = [int(i) for i in input().split()]
    print(f"#{tc} {maxmin(alist)}")