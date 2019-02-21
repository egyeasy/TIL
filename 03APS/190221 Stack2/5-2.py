import sys
sys.stdin = open('5-2.txt', 'r')

def DFS(start):
    global RESULT
    # print(start)
    visited[start[0]][start[1]] = 1
    go_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in go_list:
        if matrix[start[0] + i[0]][start[1] + i[1]] == 3:
            # print("found")
            # print(start, [start[0] + i[0], start[1] + i[1]])
            RESULT = 1
            return
        elif matrix[start[0] + i[0]][start[1] + i[1]] == 0 and not visited[start[0] + i[0]][start[1] + i[1]]:
            DFS([start[0] + i[0], start[1] + i[1]])


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    m = int(input())
    matrix = [[1] * (m + 2) for i in range(m + 2)]
    cnt_zero = 0
    cnt_visit = 0
    RESULT = 0
    for i in range(m):
        aline = input()
        for j in range(m):
            matrix[i + 1][j + 1] = int(aline[j])
            if aline[j] == '2':
                start = [i + 1, j + 1]
            if aline[j] == '0':
                cnt_zero += 1
    # for i in matrix:
        # print(i)
    # print(start)

    # visited matrix
    visited = [[0] * (m + 2) for i in range(m + 2)]

    DFS(start)

    print(f"#{tc} {RESULT}")




