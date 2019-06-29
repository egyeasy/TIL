import sys
sys.stdin = open('1.txt', 'r')
# 북 북동 동 ...
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def find_change(row, col, color):
    global brake
    mat[row][col] = color
    for j in range(8):
        c_row = row + dx[j]
        c_col = col + dy[j]
        # print([row, col], c_row, c_col)
        while (0 < c_row + dx[j] <= side_N) and (0 < c_col + dy[j] <= side_N):
            # if [c_row, c_col] == [1, 3]:
            #     brake = True
            #     break
            # print(c_row, c_col)
            c_color = mat[c_row][c_col]
            if c_color and c_color != color:
                if mat[c_row + dx[j]][c_col + dy[j]] == c_color:
                    # print(1)
                    c_row += dx[j]
                    c_col += dy[j]
                elif mat[c_row + dx[j]][c_col + dy[j]] == color:
                    # print(2)
                    while c_row != row or c_col != col:
                        # print(c_row, c_col)
                        mat[c_row][c_col] = color
                        c_row -= dx[j]
                        c_col -= dy[j]
                    break
                else:
                    # print(3)
                    break
            else:
                break
        # if brake:
        #     break

T = int(input())
for tc in range(1, T + 1):
    side_N, M = map(int, input().split())
    mat = [[0] * (side_N + 1) for _ in range(side_N + 1)]
    half = side_N // 2
    mat[half][half: half + 2] = 2, 1
    mat[half + 1][half: half + 2] = 1, 2

    # for i in mat:
    #     print(i)
    # print()
    for i in range(M):
        row, col, color = map(int, input().split())
        # print("#", i)
        brake = False
        find_change(row, col, color)
        # if brake:
        #     break
        # for i in mat:
        #     print(i)
        # print()


    # for i in mat:
    #     print(i)

    black = 0
    white = 0
    for i in range(1, side_N + 1):
        for j in range(1, side_N + 1):
            if mat[i][j] == 1:
                black += 1
            elif mat[i][j] == 2:
                white += 1

    print("#{}".format(tc), black, white)

