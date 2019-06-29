import sys
sys.stdin = open("1.txt", "r")

T = int(input())


def rec(n):
    if n < 30 or memo[n//10] != 0:
        return memo[n//10]
    memo[n//10] = rec(n-10) + 2*rec(n-20)
    return memo[n//10]

for tc in range(1, T+1):
    N = int(input())
    memo = [0] * ((N//10) + 1)
    memo[1], memo[2] = 1, 3
    print(f"#{tc} {rec(N)}")