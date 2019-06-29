def push(item):
    global top
    stack[top + 1] = item
    top += 1

def pop():
    global top
    if top == -1:
        return 0
    pop_item = stack[top]
    stack[top] = 0
    top -= 1

    return pop_item

def find_next(v):
    for i in range(m + 1):
        if matrix[v][i] and not visited[i]:
            return i
    return 0

def DFSs(v):
    print(v)
    visited[v] = True
    while v:
        w = find_next(v)
        if w:
            push(v)
        while w:
            print(stack)
            print(w)
            visited[w] = True
            push(w)
            v = w
            w = find_next(v)
        v = pop()

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
m = 7
matrix = [[0] * (m + 1) for i in range(m + 1)]
visited = [0] * (m + 1)
stack = [0] * m
top = -1

for i in range(len(edges)//2):
    matrix[edges[2*i]][edges[2*i+1]] = 1
    matrix[edges[2*i+1]][edges[2*i]] = 1
for i in matrix:
    print(i)

DFSs(1)