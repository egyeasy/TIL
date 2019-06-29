# pf 코드 참조 - visited에 거리를 넣으면 다른 변수 만들어서 중복 체크할 필요도 없음!

import sys
sys.stdin = open('6-4.txt', 'r')

q = []
front = 0
rear = 0

def enqueue(item):
    global rear
    if not isfull():
        rear = (rear + 1) % len(q)
        q[rear] = item

def dequeue():
    global front
    if not isempty():
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return front == rear

def bfs(s):
    global end, tc, found
    enqueue(s)
    while not isempty():
        # print(f"q: {q}")
        s = dequeue()
        if s == end:
            found = True
            print(f"#{tc} {matrix[former[s]][s]}")
            break
        if not visited[s]:
            visited[s] = 1
            # print(f"visited {s}")
            for i in range(v + 1):
                if matrix[s][i] and not visited[i]:
                    if former[s]:
                        matrix[s][i] = matrix[former[s]][s] + 1
                    if not former[i]:
                        former[i] = s
                    # print(f"former: {former}, s: {s}, i: {i}")
                    enqueue(i)


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    matrix = [[0] * (v + 1) for i in range(v + 1)]
    visited = [0] * (v + 1)
    former = [0] * (v + 1)
    q = [0] * v
    front = 0
    rear = 0
    found = False
    for i in range(e):
        ad_start, ad_end = map(int, input().split())
        matrix[ad_start][ad_end] = 1
        matrix[ad_end][ad_start] = 1

    # for i in matrix:
    #     print(i)

    start, end = map(int, input().split())

    depth = 0
    bfs(start)

    if not found:
        print(f"#{tc} 0")

    # for i in matrix:
    #     print(i)


    # print()