import sys
sys.stdin = open('6-2.txt', 'r')

def dfs(s, go):
    global found, min_go
    row = s[0]
    col = s[1]
    if matrix[row][col] == 3:
        found = True
        if go - 1 < min_go:
            min_go = go - 1
        return
    if not matrix[row][col] == 1 and not visited[row][col]:
        visited[row][col] = 1
        dfs([row - 1, col], go + 1)
        dfs([row, col + 1], go + 1)
        dfs([row + 1, col], go + 1)
        dfs([row, col - 1], go + 1)


T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    matrix = [[1] * (m + 2) for i in range(m + 2)]
    visited = [[0] * (m + 2) for i in range(m + 2)]
    start = [0, 0]
    found = False
    min_go = m ** 2
    for i in range(m):
        aline = list(input())
        for j in range(m):
            num = int(aline[j])
            matrix[i + 1][j + 1] = num
            if num == 2:
                start = [i + 1, j + 1]

    # for i in matrix:
    #     print(i)
    #
    # print(start)

    dfs(start, 0)
    if found:
        print(f"#{tc} {min_go}")
    else:
        print(f"#{tc} 0")
