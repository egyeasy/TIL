import sys
sys.stdin = open('6-2.txt', 'r')

m = 1
q = [0] * m ** 2
front = -1
rear = -1

def enqueue(item):
    global rear
    if not isFull():
        rear += 1
        q[rear] = item

def dequeue():
    global front
    if not isEmpty():
        front += 1
        de_item = q[front]
        q[front] = 0
        return de_item

def isFull():
    return rear == len(q) - 1

def isEmpty():
    return front == rear

def peek():
    if not isEmpty():
        return q[front + 1]


def bfs(s):
    global result
    enqueue(s)
    floor[s[0]][s[1]] = 1
    while not isEmpty():
        s = dequeue()
        row = s[0]
        col = s[1]
        if not visited[row][col]:
            visited[row][col] = 1
            if not floor[row][col]:
                floor[row][col] = floor[former[row][col][0]][former[row][col][1]] + 1
            if matrix[row][col] == 3:
                result = floor[row][col] - 2
            # print(f"visited {s}")
            for i in range(4):
                cand_x = row + dx[i]
                cand_y = col + dy[i]
                if (not matrix[cand_x][cand_y] or matrix[cand_x][cand_y] == 3) and not visited[cand_x][cand_y]:
                    if not former[cand_x][cand_y]:
                        former[cand_x][cand_y] = s
                    enqueue([cand_x, cand_y])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    matrix = [[1] * (m + 2) for i in range(m + 2)]
    visited = [[0] * (m + 2) for i in range(m + 2)]
    floor = [[0] * (m + 2) for i in range(m + 2)]
    former = [[0] * (m + 2) for i in range(m + 2)]
    for i in range(m):
        aline = list(input())
        for j in range(m):
            num = int(aline[j])
            matrix[i + 1][j + 1] = num
            if num == 2:
                start = [i + 1, j + 1]

    # for i in matrix:
    #     print(i)
    # print(start)

    q = [0] * m ** 2
    front = -1
    rear = -1
    result = 0
    bfs(start)
    print(f"#{tc} {result}")

    # print()