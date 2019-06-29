import sys
sys.stdin = open('6-1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f"#{tc} {nums[m % n]}")