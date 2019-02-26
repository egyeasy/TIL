import sys
sys.stdin = open('6-1.txt', 'r')

m = 20
q = [0] * m
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

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    q = [0] * (n + m)
    front = -1
    rear = -1
    for num in nums:
        enqueue(num)
    for i in range(m):
        enqueue(dequeue())
    # print(q)

    print(f"#{tc} {peek()}")
