import sys
sys.stdin = open("sc-ms.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n,k=map(int,input().split())
    sb=set(map(int,input().split()))
    s=set(range(1,n+1))
    print(f"#{tc} {' '.join(map(str, s-sb))}")
    # for i in (s-sb):
    #     print(i,end=" ")
    # print()