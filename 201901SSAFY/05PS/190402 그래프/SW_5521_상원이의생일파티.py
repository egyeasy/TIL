import sys
sys.stdin = open('5521.txt', 'r')

from collections import deque


def bfs(s):
    global cnt
    dq.append(s)
    visited[s] = 1
    while dq:
        s = dq.popleft()
        if visited[s] == 2 or visited[s] == 3:
            cnt += 1
        elif visited[s] == 4:
            return
        for i in range(1, N_person + 1):
            if mat[s][i] and not visited[i]:
                dq.append(i)
                visited[i] = visited[s] + 1


T = int(input())
for tc in range(1, T + 1):
    N_person, M_edge = map(int, input().split())
    mat = [[0] * (N_person + 1) for _ in range(N_person + 1)]

    for i in range(M_edge):
        alist = list(map(int, input().split()))
        mat[alist[0]][alist[1]] = 1
        mat[alist[1]][alist[0]] = 1

    dq = deque()
    visited = [0] * (N_person + 1)
    cnt = 0
    bfs(1)
    print(f"#{tc} {cnt}")
