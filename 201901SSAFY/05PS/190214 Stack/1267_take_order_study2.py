# 짜다 말았음
import sys
sys.stdin = open('task.txt', 'r')

top = -1
def push(item):
    global top
    top += 1
    s[top] = item

def pop():
    global top
    if top == -1:
        return 0
    else:
        pop_item = s[top]
        top -= 1
        return pop_item

def find_next(v):
    for i in range(1, node_V + 1):
        if mat[v][i] and not visited[i]:
            return i

def dfs(v):
    visited[v] = 1
    while v:
        w = find_next(v)
        if w:
            push(v)
        while w:
            visited[w] = 1
            push(w)
            v = w
            w = find_next(v)
        v = pop()



for tc in range(1, 11):
    node_V, edge_E = map(int, input().split())
    # print(node_V, edge_E)
    mat = [[0] * (node_V + 1) for _ in range(node_V + 1)]
    aline = list(map(int, input().split()))
    for i in range(edge_E):
        mat[aline[2 * i + 1]][aline[2 * i]] = 1
    # for i in mat:
    #     print(i)
    # print()

    s = [0] * (node_V)
    top = -1
    visited = [0] * (node_V + 1)
    print("#{}".format(tc), end=" ")
    for i in range(1, node_V + 1):
        if not visited[i]:
            dfs(i)
    print()