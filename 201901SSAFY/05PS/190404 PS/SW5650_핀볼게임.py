from collections import deque

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def change_dir(block, dir):
    if block == 1:
        if dir == 0:
            return 2
        elif dir == 1:
            return 0
        elif dir == 2:
            return 3
        else:
            return 1
    elif block == 2:
        if dir == 0:
            return 2
        elif dir == 1:
            return 3
        elif dir == 2:
            return 1
        else:
            return 0
    elif block == 3:
        if dir == 0:
            return 1
        elif dir == 1:
            return 3
        elif dir == 2:
            return 0
        else:
            return 2
    elif block == 4:
        if dir == 0:
            return 3
        elif dir == 1:
            return 2
        elif dir == 2:
            return 0
        else:
            return 1
    else:
        if dir == 0:
            return 2
        elif dir == 1:
            return 3
        elif dir == 2:
            return 0
        else:
            return 1

def change_position(row, col):
    worm_num = mat[row][col] - 6
    if worms[worm_num][0] == [row, col]:
        return worms[worm_num][1]
    else:
        return worms[worm_num][0]


def bfs(s):
    global this_point
    dq.append(s)
    while dq:
        s_row, s_col, dir, curr_point = dq.popleft()
        c_row = s_row + dx[dir]
        c_col = s_col + dy[dir]
        if 0 <= c_row < N_side and 0 <= c_col < N_side and visited[c_row][c_col] != dir:
            # 지나간 길 또 안 지나가게 처리
            if visited[c_row][c_col] == -1:
                visited[c_row][c_col] = dir
            if mat[c_row][c_col] == 0:
                if c_row == i and c_col == j and curr_point > this_point:
                    this_point = curr_point
                else:
                    dq.append([c_row, c_col, dir, curr_point])
            elif 1 <= mat[c_row][c_col] <= 5:
                new_dir = change_dir(mat[c_row][c_col], dir)
                dq.append([c_row, c_col, new_dir, curr_point + 1])
            elif 6 <= mat[c_row][c_col] <= 10:
                new_row, new_col = change_position(c_row, c_col)
                new_row += dx[dir]
                new_col += dy[dir]
                dq.append([new_row, new_col, dir, curr_point])
            elif curr_point > this_point:
                this_point = curr_point


T = int(input())
for tc in range(1, T + 1):
    N_side = int(input())
    mat = [[0] * N_side for _ in range(N_side)]
    worms = [[0] * 2 for _ in range(5)]
    # print(worms)
    for i in range(N_side):
        aline = list(map(int, input().split()))
        for j in range(N_side):
            mat[i][j] = aline[j]
            value = mat[i][j]
            # 웜홀 기록
            if 6 <= value <= 10:
                if worms[value - 6][0]:
                    worms[value - 6][1] = [i, j]
                else:
                    worms[value - 6][0] = [i, j]

    # for i in mat:
    #     print(i)
    # print()

    max_point = 0
    for i in range(N_side):
        for j in range(N_side):
            if mat[i][j] == 0:
                for direction in range(4):
                    dq = deque()
                    visited = [[[-1] * 4 for _ in range(N_side)] for __ in range(N_side)]
                    this_point = 0
                    bfs([i, j, direction, 0])
                    if this_point > max_point:
                        # print(i, j)
                        max_point = this_point

    print(f"#{tc} {max_point}")