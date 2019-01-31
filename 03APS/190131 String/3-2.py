import sys
sys.stdin = open("2.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    grid = [0 for i in range(N)]
    for i in range(N):
        grid[i] = list(input())

    leng = len(grid)
    for i in range(leng):
        for k in range(leng - M + 1):
            row_result = ""
            col_result = ""
            if M % 2 == 1:
                row_result += grid[i][(M // 2) + k]
                col_result += grid[(M // 2) + k][i]
            for j in range(M):
                if j >= (M + 1) // 2:
                    if grid[i][j+k] == grid[i][M-j-1+k]:
                        row_result = grid[i][j+k] + row_result + grid[i][j+k]
                    else:
                        break

            for j in range(M):
                if j >= (M + 1) // 2:
                    if grid[j+k][i] == grid[M-j-1+k][i]:
                        col_result = grid[j+k][i] + col_result + grid[j+k][i]
                    else:
                        break

            if len(row_result) == M:
                print(f"#{tc}", row_result)
            if len(col_result) == M:
                print(f"#{tc}", col_result)
    