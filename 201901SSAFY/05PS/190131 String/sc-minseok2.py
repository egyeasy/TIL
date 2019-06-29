import sys
sys.stdin = open("sc-ms.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n,k = map(int,input().split())
    sb = list(map(int,input().split()))
    total = list(range(1, n+1))

    for i in sb:
        total[i-1] = -1

    print(f"#{tc}", end=" ")

    for i in total:
        if i != -1:
            print(i, end=" ")

    print()