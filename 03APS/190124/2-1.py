import sys
sys.stdin = open("2-1.txt", "r")


T = int(input())

for tc in range(1, T+1):

    grid = [[0 for i in range(10)] for j in range(10)]

    N = int(input())
    for n in range(N):
        input_ = list(map(int, input().split()))
        a1 = input_[:2]
        a2 = input_[2:4]
        color = input_[4]

        min_r = min(a1[0], a2[0])
        max_r = max(a1[0], a2[0])
        min_c = min(a1[1], a2[1])
        max_c = max(a1[1], a2[1])

        for i in range(min_r, max_r+1):
            for j in range(min_c, max_c+1):
                if grid[i][j] != color:
                    grid[i][j] += color

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 3:
                cnt += 1

    print(f"#{tc} {cnt}")