# import sys
# sys.stdin = open("input.txt", "r")

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1 : return 0
    x = stack[top]
    top -= 1
    return x

def findnext(v):
    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            return i
    return 0

def DFS(v):
    print(v)
    visited[v] = True
    while v:
        w = findnext(v)
        if w : push(v)
        while w:
            print(w)
            visited[w] = True
            push(w)
            v = w
            w = findnext(v)
        v = pop()


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * (8)
G = [[0]* (8) for _ in range(8)]
stack = [0] * 10
top = -1

for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1

DFS(1)

# def DFSr(v):
#     print(v)
#     visited[v] = True
#
#     for i in range(1, 8):
#         if G[v][i] and not visited[i]:
#             DFSr(i)
#
#
# edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# visited = [0] * 8
# G = [[0] * 8 for _ in range(8)]
#
# for i in range(0, len(edges), 2):
#     G[edges[i]][edges[i+1]] = 1
#     G[edges[i+1]][edges[i]] = 1
#
# DFSr(1)