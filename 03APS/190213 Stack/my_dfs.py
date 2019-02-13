ad_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
stack = [0]*100
top = -1

def push(item):
    global top
    stack[top+1] = item
    top += 1

def isEmpty():
    for i in stack:
        if i != 0:
            return False
    return True

def pop():
    global top
    if top != -1:
        result = stack[top]
        stack[top] = 0
        top -= 1
        return result
    else:
        return 0

def peek():
    global top
    if top == -1:
        return -1
    else:
        return stack[top]

maxx = 0
for i in ad_list:
    if i > maxx:
        maxx = i

visited = [0] * (maxx + 1)

# matrix = [[0] * (maxx + 1) for i in range(maxx + 1)]

matrix = [0] * (maxx + 1)
for i in range(maxx + 1):
    matrix[i] = [0] * (maxx + 1)

print(matrix)

for i in range(1, len(ad_list) + 1):
    if i % 2:
        a = ad_list[i-1]
        b = ad_list[i]
        matrix[a][b] = 1
        matrix[b][a] = 1

print(matrix)



v = 1
visited[v] = 1
w = 0

result = [0]*(len(visited)-1)
result_idx = 0
result[result_idx] = v
result_idx += 1

while True:
    for find_w in range(1, len(matrix[v])):
        if matrix[v][find_w] == 1 and visited[find_w] == 0:
            w = find_w
            push(v)
            break
    while w:
        visited[w] = 1
        push(w)
        result[result_idx] = w
        result_idx += 1
        print(stack, top, w)
        v = w
        for find_w in range(1, len(matrix[v])):
            if matrix[v][find_w] == 1 and visited[find_w] == 0:
                w = find_w
                break
        w = 0
    v = pop()
    if isEmpty():
        break

print(result)

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(result[i], end="-")