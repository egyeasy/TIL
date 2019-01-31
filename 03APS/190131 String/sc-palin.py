import sys
sys.stdin = open("sc-palin.txt", "r")

def is_pal(text):
    if text == text[::-1]:
        return True
    else:
        return False

for tc in range(1, 11):
    num = input()
    N = 100

    grid = [0 for i in range(N)]
    for i in range(N):
        grid[i] = list(input())

    maxx = 1

    leng = len(grid)
    max_col = ""
    max_row = ""
    max_point = ()
    max_point_col = ()

    for i in range(leng):
        for M in range(N, maxx, -1):
            for k in range(leng - M + 1):
                row_result = ""
                col_result = ""
                row_cnt = 0
                col_cnt = 0
                if M % 2 == 1:
                    row_result += grid[i][(M // 2) + k]
                    col_result += grid[(M // 2) + k][i]
                    row_cnt += 1
                    col_cnt += 1
                for j in range(M):
                    if j >= (M + 1) // 2:
                        if grid[i][j + k] == grid[i][M - j - 1 + k]:
                            row_result = grid[i][j + k] + row_result + grid[i][j + k]
                            row_cnt += 2
                            row_pointset = (i, j+k, M-j-1+k)
                        else:
                            break
                for j in range(M):
                    if j >= (M + 1) // 2:
                        if grid[j + k][i] == grid[M - j - 1 + k][i]:
                            col_pointset = (i, j+k, M-j-1+k)
                            col_result = grid[j + k][i] + col_result + grid[j + k][i]
                            col_cnt += 2
                        else:
                            break

                if row_cnt > maxx:
                    maxx = row_cnt
                    maxx = len(row_result)
                    max_row = row_result
                    max_point = row_pointset
                if len(col_result) > maxx:
                    maxx = col_cnt
                    maxx = len(col_result)
                    max_col = col_result
                    max_point_col = col_pointset

    print(f"#{tc} {maxx}", max_row, max_point, is_pal(max_row),  max_col, is_pal(max_col), max_point_col)
    # print(f"#{tc} {maxx}")