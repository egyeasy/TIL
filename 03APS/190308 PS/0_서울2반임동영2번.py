# import sys
# sys.stdin = open('2.txt', 'r')

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(s):
    global max_height
    dq.append(s)
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        if not visited[s_row][s_col]:
            visited[s_row][s_col] = 1
            if mat[s_row][s_col] > max_height:
                max_height = mat[s_row][s_col]
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if 0 <= c_row < side_N and 0 <= c_col < side_N and mat[c_row][c_col] and not visited[c_row][c_col]:
                    dq.append([c_row, c_col])



T = int(input())
for tc in range(1, T + 1):
    side_N = int(input())
    mat  = [0] * side_N
    for i in range(side_N):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)

    visited = [[0] * side_N for _ in range(side_N)]
    dq = deque()
    sum_cnt = 0
    max_height = 0

    for i in range(side_N):
        for j in range(side_N):
            if mat[i][j] and not visited[i][j]:
                bfs([i, j])
                sum_cnt += 1

    print("#{}".format(tc), sum_cnt, max_height)



