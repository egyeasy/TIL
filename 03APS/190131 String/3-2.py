import sys
sys.stdin = open("2.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    grid = [0 for i in range(N)]
    for i in range(N):
        grid[i] = list(input())

    print(grid)

    for i in len(grid):
        for j in len(grid[0]):
