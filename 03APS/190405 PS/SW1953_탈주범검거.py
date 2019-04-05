import sys
sys.stdin = open('1953.txt', 'r')

from collections import deque
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(s):
    global total_cnt
    dq.append(s)
    while dq:
        s_row, s_col, dir, curr_time = dq.popleft()
        # 방문, count 처리
        pipe = mat[s_row][s_col]
        if not visited[s_row][s_col] and ((pipe == 1) or (pipe == 2 and (dir == 2 or dir == 3))\
            or (pipe == 3 and (dir == 0 or dir == 1)) or (pipe == 4 and (dir == 2 or dir == 1))\
            or (pipe == 5 and (dir == 1 or dir == 3)) or (pipe == 6 and (dir == 0 or dir == 3))\
            or (pipe == 7 and (dir == 0 or dir == 2))):
            visited[s_row][s_col] = 1
            total_cnt += 1
        if curr_time == max_time:
            continue
        if pipe == 1:
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                    dq.append([c_row, c_col, i, curr_time + 1])
        elif pipe == 2 and (dir == 2 or dir == 3):
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])
        elif pipe == 3 and (dir == 0 or dir == 1):
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])
        elif pipe == 4 and (dir == 1 or dir == 2):
            if dir == 1:
                dir = 3
            else:
                dir = 0
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])
        elif pipe == 5 and (dir == 1 or dir == 3): # 서 또는 북
            # 남 또는 동으로 바꿈
            if dir == 1:
                dir = 2
            else:
                dir = 0
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])
        elif pipe == 6 and (dir == 0 or dir == 3): # 동 또는 북
            # 남 또는 서로 바꿈
            if dir == 0:
                dir = 2
            else:
                dir = 1
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])
        elif pipe == 7 and (dir == 0 or dir == 2): # 동 또는 남
            # 남 또는 동으로 바꿈
            if dir == 0:
                dir = 3
            else:
                dir = 1
            c_row = s_row + dx[dir]
            c_col = s_col + dy[dir]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col, dir, curr_time + 1])


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_row, M_col, start_row, start_col, max_time = map(int, input().split())
    mat = [0] * N_row
    for i in range(N_row):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)
    # print()

    dq = deque()
    visited = [[0] * M_col for _ in range(N_row)]
    total_cnt = 0
    for direction in range(4):
        bfs([start_row, start_col, direction, 1])

    print(f"#{tc} {total_cnt}")