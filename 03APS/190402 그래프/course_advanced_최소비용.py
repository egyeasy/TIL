import sys
sys.stdin = open('5250.txt', 'r')

from collections import deque

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(s):
    global min_sobi
    dq.append(s)
    visited[0][0] = 1
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        for i in range(4):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < N_side and 0 <= c_col < N_side:
                added_value = 1
                if mat[c_row][c_col] > mat[s_row][s_col]:
                    added_value += mat[c_row][c_col] - mat[s_row][s_col]
                if not visited[c_row][c_col]:
                    dq.append([c_row, c_col])
                    visited[c_row][c_col] = visited[s_row][s_col] + added_value
                elif visited[s_row][s_col] + added_value < visited[c_row][c_col]:
                    dq.append([c_row, c_col])
                    visited[c_row][c_col] = visited[s_row][s_col] + added_value


T = int(input())
for tc in range(1, T + 1):
    N_side = int(input())
    mat = [0] * N_side
    for i in range(N_side):
        mat[i] = list(map(int, input().split()))

    dq = deque()
    visited = [[0] * N_side for _ in range(N_side)]
    min_sobi = 100000000000
    bfs([0, 0])
    # print("visited")
    # for i in visited:
    #     print(i)
    print(f"#{tc} {visited[N_side - 1][N_side - 1] - 1}")