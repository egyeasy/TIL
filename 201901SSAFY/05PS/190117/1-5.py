import sys
sys.stdin = open("input1-5.txt", "r")

for tc in range(1, 11):
    total_dt = int(input())
    alist = list(map(int, input().split()))
    print(f"#{tc}")