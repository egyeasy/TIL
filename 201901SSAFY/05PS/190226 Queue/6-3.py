import sys
sys.stdin = open('6-3.txt', 'r')

q = []
front = 0
rear = 0

def enqueue(item):
    global rear
    if not isFull():
        rear = (rear + 1) % len(q)
        q[rear] = item

def dequeue():
    global front
    if not isEmpty():
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item

def isFull():
    return (rear + 1) % len(q) == front

def isEmpty():
    return front == rear

def peek():
    if not isEmpty():
        return q[(front +1) % len(q)]


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(zip(range(1, m + 1),map(int, input().split())))
    q = [0] * (n + 1)
    front = 0
    rear = 0
    input_idx = n

    for num in nums:
        if not isFull():
            enqueue(num)
        else:
            break

    # print(q)
    while not isEmpty():
        if peek()[1] == 0:
            item = dequeue()[0]
            if not input_idx == m:
                enqueue([nums[input_idx][0], nums[input_idx][1] // 2])
                input_idx += 1
            # print(f"out {q}")
        else:
            de_item = dequeue()
            enqueue((de_item[0], de_item[1] // 2))
            # print(f"아무일도 없었다: {q}")
    print(f"#{tc} {item}")
