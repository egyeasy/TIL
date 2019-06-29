import sys
sys.stdin = open('contact.txt', 'r')

def enqueue(item):
    global rear
    if not isfull():
        rear = (rear + 1) % len(q)
        q[rear] = item
    else:
        print("it's full")

def dequeue():
    global front
    if not isempty():
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item
    else:
        print("empty")

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return front == rear

def bfs(s):
    enqueue(s)
    floor[s] = 1
    while not isempty():
        global max_floor
        s = dequeue()
        # 끝 도달 처리
        if not visited[s]:
            visited[s] = 1
            # print(f"visited {s}")
            if not floor[s]:
                floor[s] = floor[former[s]] + 1
                if floor[s] > max_floor:
                    max_floor = floor[s]
                    max_list = [0] * 100
                    max_idx = 0
                    max_list[max_idx] = s
                elif floor[s] == max_floor:
                    max_idx += 1
                    max_list[max_idx] = s
                # print(f"s: {s}, floor: {floor}")
            for i in range(101):
                if matrix[s][i] and not visited[i]:
                    # print(f"s: {s}, i: {i}")
                    if not former[i]:
                        former[i] = s
                    enqueue(i)
                    # print(f"q: {q}")
    return max_list

T = 10
for tc in range(1, T + 1):
# for tc in range(1, 2):
    num_line, start = map(int, input().split())
    lines = list(map(int, input().split()))
    len_line = len(lines)
    matrix = [[0] * 101 for i in range(101)]
    visited = [0] * 101
    former = [0] * 101
    floor = [0] * 101
    # print(lines)
    for i in range(len_line):
        if not i % 2:
            matrix[lines[i]][lines[i+1]] = 1

    # for i in matrix:
    #     print(i)

    q = [0] * 100
    front = 0
    rear = 0
    max_floor = 0
    max_list = bfs(start)
    # print(len_line)
    # print(floor)
    # print(max_list)

    maxx = 0
    for num in max_list:
        if num and num > maxx:
            maxx = num
    print(f"#{tc} {maxx}")