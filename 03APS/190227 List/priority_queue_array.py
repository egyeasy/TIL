def enqueue(item):
    global rear
    if isfull():
        print("isfull")
    else:
        rear = (rear + 1) % len(q)
        q[rear] = item
        p = rear
        while q[p] < q[(p - 1) % len(q)]:
            if q[(p - 1) % len(q)] == 0:
                break
            q[p], q[(p - 1) % len(q)] = q[(p - 1) % len(q)], q[p]
            p = (p - 1) % len(q)

def dequeue():
    global front
    if isempty():
        print("isempty")
    else:
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return rear == front

nums = 1, 5, 2, 4, 3
q = [0] * (len(nums) + 1)
front = 0
rear = 0

for i in nums:
    enqueue(i)

for i in q:
    if i:
        print(i)