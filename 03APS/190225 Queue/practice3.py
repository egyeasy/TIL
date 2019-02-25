graph = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

m = 7
matrix = [[0] * (m + 1) for i in range(m + 1)]
visited = [0] * (m + 1)

for i in range(len(graph)):
    if not i % 2:
        matrix[graph[i]][graph[i + 1]] = 1
        matrix[graph[i + 1]][graph[i]] = 1

for i in matrix:
    print(i)

queue = []
start = 1
queue.append(start)

while queue:
    start = queue.pop(0)
    if not visited[start]:
        visited[start] = 1
        print(start)
    for i in range(m + 1):
        # print(f"i {i}, {queue}")
        if matrix[start][i] and not visited[i]:
            queue.append(i)
