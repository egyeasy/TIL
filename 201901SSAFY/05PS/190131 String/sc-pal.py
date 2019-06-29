import sys
sys.stdin = open("sc-palin.txt", "r")

for tc in range(1, 11):
    num = input()
    N = 100
    grid = [0 for i in range(N)]
    for i in range(N):
        grid[i] = list(input())
    maxx = 1
    for i in range(N):
        for M in range(N, maxx, -1):
            for k in range(N - M + 1):
                row_cnt = 0
                col_cnt = 0
                if M % 2 == 1:
                    row_cnt += 1
                    col_cnt += 1
                for j in range(M):
                    if j >= (M + 1) // 2:
                        if grid[i][j + k] == grid[i][M - j - 1 + k]:
                            row_cnt += 2
                        else:
                            break
                for j in range(M):
                    if j >= (M + 1) // 2:
                        if grid[j + k][i] == grid[M - j - 1 + k][i]:
                            col_cnt += 2
                        else:
                            break
                if row_cnt > maxx:
                    maxx = row_cnt
                if col_cnt > maxx:
                    maxx = col_cnt
    print(f"#{tc} {maxx}")