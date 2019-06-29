import sys
sys.stdin = open('find.txt', 'r')

front = 0
rear = 0

def enqueue(item):
    global rear
    if isFull():
        pass
        # print("Queue_Full")
    else:
        rear = rear + 1
        q[rear] = item

def dequeue():
    global front
    if isEmpty():
        pass
        # print("Queue_Empty")
    else:
        front += 1
        return q[front]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(q) - 1

def peek():
    if isEmpty():
        pass
        # print("Queue_Empty")
    else:
        return q[front + 1]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global m, minn, maxx
    while not isEmpty():
        s = dequeue()
        row = s[0]
        col = s[1]
        if not visited[row][col]:
            visited[row][col] = 1
            # print(f"visited {s}")
            if row <= minn[0] and col <= minn[1]:
                minn = s
            elif row >= maxx[0] and col >= maxx[1]:
                maxx = s
            for i in range(4):
                cand = matrix[row + dx[i]][col + dy[i]]
                if cand and not visited[row + dx[i]][col + dy[i]]:
                    next_point = [row + dx[i], col + dy[i]]
                    enqueue([row + dx[i], col + dy[i]])
                    # print(q)

def align_list(idx, item):
    for i in range(len(max_list) - 2, idx - 1, -1):
        max_list[i + 1] = max_list[i]
    max_list[idx] = item


T = int(input())

for tc in range(1, T + 1):
    m = int(input())
    matrix = [[0] * (m + 2) for i in range(m + 2)]
    visited = [[0] * (m + 2) for i in range(m + 2)]
    max_list = [[0, 0] for i in range((m + 2))]
    max_list[0] = 0
    max_idx = 0

    for i in range(m):
        aline = list(map(int, input().split()))
        for j in range(m):
            if aline[j]:
                matrix[i + 1][j + 1] = aline[j]
    
    # if tc != 7:
    #     continue

    # for i in matrix:
    #     print(i)

    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if matrix[i][j] and not visited[i][j]:
                q = [0] * m**2
                front = -1
                rear = -1
                enqueue([i, j])
                minn = [i, j]
                maxx = [i, j]
                bfs()
                # print(minn, maxx)
                # print(f"{maxx[0] - minn[0] + 1} X {maxx[1] - minn[1] + 1}")
                len_row = maxx[0] - minn[0] + 1
                len_col = maxx[1] - minn[1] + 1
                square = len_row * len_col
                for i in range(1, len(max_list)):
                    # print(max_list)
                    if max_list[i] != [0, 0]:
                        if square == max_list[i][0] * max_list[i][1]:
                            if len_row < max_list[i][0]:
                                align_list(i, [len_row, len_col])
                                break
                            else:
                                align_list(i + 1, [len_row, len_col])
                                break
                        elif square < max_list[i][0] * max_list[i][1]:
                            # print(square, i, max_list)
                            align_list(i, [len_row, len_col])
                            break
                    else:
                        max_list[i] = [len_row, len_col]
                        break
                max_list[0] += 1

    print(f"#{tc} {max_list[0]}", end=" ")
    for i in range(1, len(max_list)):
        if max_list[i] == [0, 0]:
            break
        print(f"{max_list[i][0]} {max_list[i][1]}", end=" ")
    print()

