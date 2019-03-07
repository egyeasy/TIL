import sys
sys.stdin = open('4.txt', 'r')

from collections import deque

def bfs(s):
    global go_cnt
    dq.append(s)
    go_cnt = 0
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        judge = False
        if s_row == 99:
            return
        # print(s_row, s_col)
        if not visited[s_row][s_col]:
            visited[s_row][s_col] = 1
            go_cnt += 1
            for i in range(-1, 2, 2):
                c_col = s_col + i
                if 0 <= c_col < 100 and mat[s_row][c_col] and not visited[s_row][c_col]:
                    dq.append([s_row, c_col])
                    break
            else:
                dq.append([s_row + 1, s_col])


for tc in range(1, 11):
    tc = int(input())
    mat = [0] * 100
    for i in range(100):
        mat[i] = list(map(int, input().split()))
    starts = []
    for i in range(100):
        if mat[0][i]:
            starts.append(i)
    min_cnt = 10000
    min_idx = 0
    # for i in mat:
    #     print(i)
    for start in starts:
        go_cnt = 0
        visited = [[0] * 100 for _ in range(100)]
        dq = deque()
        bfs([0, start])
        if go_cnt < min_cnt:
            min_idx = start
            min_cnt = go_cnt

    print("#{}".format(tc), min_idx)
