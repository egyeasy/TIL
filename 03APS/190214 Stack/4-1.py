import sys
sys.stdin = open("1.txt", "r")

T = int(input())


def rec(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return 2*rec(n-20) + rec(n-10)

for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc} {rec(N)}")