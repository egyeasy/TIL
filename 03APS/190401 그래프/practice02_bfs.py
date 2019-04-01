N = 10
q = [0] * N
front = 0
rear = 0

def enqueue(item):
    global rear
    if isFull():
        print("is full")
    else:
        rear = (rear + 1) % N
        q[rear] = item

def dequeue():
    global front
    if isEmpty():
        print("is empty")
    else:
        front = (front + 1) % N
        de_item = q[front]
        q[front] = 0
        return de_item


def isFull():
    return (rear + 1) % N == front


def isEmpty():
    return rear == front


def bfs(s):
    enqueue(s)
    while not isEmpty():
        s = dequeue()
        if not visited[s]:
            visited[s] = 1
            print(s, end=" ")
        for i in range(1, N_node + 1):
            if not visited[i]:
                enqueue(i)
                print("s:", q, "front", front, "rear", rear)


N_node = 7
nums = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
mat = [[0] * (N_node + 1) for _ in range(N_node + 1)]

for i in range(0, len(nums), 2):
    mat[nums[i]][nums[i + 1]] = 1

visited = [0] * (N_node + 1)
bfs(1)