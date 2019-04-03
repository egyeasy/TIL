import sys
sys.stdin = open('2819.txt', 'r')

from collections import deque

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(s):
    global total_cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        s_row, s_col, curr_num = s
        for i in range(4):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < 4 and 0 <= c_col < 4 and curr_num not in visited[c_row][c_col]:
                visited[c_row][c_col].append(curr_num)
                next_num = curr_num + mat[c_row][c_col]
                if len(next_num) == 7:
                    counted.append(next_num)
                else:
                    dq.append([c_row, c_col, next_num])




T = int(input())
for tc in range(1, T + 1):
    mat = [0] * 4
    for i in range(4):
        mat[i] = list(input().split())

    visited = [[[] for __ in range(4)] for _ in range(4)]
    counted = []
    # total_cnt = 0
    # for i in visited:
    #     print(i)

    for i in range(4):
        for j in range(4):
            dq = deque()
            # [i, j, 지금까지 만든 숫자]
            bfs([i, j, ''])

    print(f"#{tc} {len(set(counted))}")