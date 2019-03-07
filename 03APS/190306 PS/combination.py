import sys
sys.stdin = open('combination.txt', 'r')

def comb(n, r):
    if r == 0 or n == r:
        return 1
    elif n < r:
        return
    else:
        return comb(n - 1, r) + comb(n - 1, r - 1)

N = int(input())
nums = list(map(int, input().split()))
print(comb(5, 2))