def dfs(x, y):
    global ans
    if x < 0 or x >= N or y < 0 or y >= N : return
    if not mat[x][y] : return
    if max_height < mat[x][y] : max_height = mat[x][y]

    # 0으로 바꿔줘서 다음번에 왔을 때 dfs 진입하지 않도록!
    mat[x][y] = 0

    # 이웃처리
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

for i in range(N):
    for j in range(N):
        if mat[i][j]:
            dfs(i, j)
            cnt += 1

