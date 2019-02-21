# import sys
# sys.stdin = open("input.txt", "r")

def findnext(v):
    for i in range(1, V+1):
        if G[v][i] and not visited[i]:
            return i
    return 0

def DFS(v, end):
    global top
    visited[v] = True
    while v:
        w = findnext(v)
        if w : top += 1;  stack[top] = v
        while w:
            if w == end: return 1
            visited[w] = True
            top += 1; stack[top] = w
            w = findnext(w)

        if top == -1 : return 0
        v = stack[top] ; top -= 1

stack = [0] * 50
top = -1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    G = [[0] * (V+1) for _ in range(V + 1)]

    for _ in range(E):
        s, t = map(int, input().split())
        G[s][t] = 1
    start, end = map(int, input().split())

    print('#%d'%tc, DFS(start, end))
    top = -1


# def DFSr(v):
#     global found
#     if v == end : found = 1; return
#     visited[v] = True
# 
#     for i in range(1, V + 1):
#         if G[v][i] and not visited[i] and not found:
#             DFSr(i)
# 
# 
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     visited = [0] * (V + 1)
#     G = [[0] * (V + 1) for _ in range(V + 1)]
# 
#     for _ in range(E):
#         s, t = map(int, input().split())
#         G[s][t] = 1
#     start, end = map(int, input().split())
# 
#     found = 0
#     DFSr(start)
#     print('#%d'%tc, found)
# 
