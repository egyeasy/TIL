import sys
sys.stdin = open('5247.txt', 'r')

from collections import deque


def bfs(s):
    global result_cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        if s == M_target:
            return
        if s + 1 <= 1000000 and not visited[s + 1]:
            dq.append(s + 1)
            visited[s + 1] = visited[s] + 1
        if 0 < s - 1 and not visited[s - 1]:
            dq.append(s - 1)
            visited[s - 1] = visited[s] + 1
        if s * 2 <= 1000000 and not visited[s * 2]:
            dq.append(s * 2)
            visited[s * 2] = visited[s] + 1
        if 0 < s - 10 and not visited[s - 10]:
            dq.append(s - 10)
            visited[s - 10] = visited[s] + 1


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_start, M_target = map(int, input().split())
    dq = deque()
    visited = [0] * 1000000
    bfs(N_start)
    # print(visited)
    print(f"#{tc} {visited[M_target]}")