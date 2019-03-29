import sys
sys.stdin = open('1test.txt', 'r')

from collections import deque

dx = [2, -2, -3, -3, -2, 2, 3, 3]
dy = [3, 3, 2, -2, -3, -3, -2, 2]

def bfs(s):
    dq.append(s)
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        if s_row == end[0] and s_col == end[1]:
            return
        for i in range(8):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < N and 0 <= c_col < N and not visited[c_row][c_col]:
                visited[c_row][c_col] = visited[s_row][s_col] + 1
                dq.append([c_row, c_col])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    start = nums[:2]
    end = nums[2:]
    dq = deque()
    visited = [[0] * N for _ in range(N)]
    bfs(start)
    print(f"#{tc} {visited[end[0]][end[1]]}")