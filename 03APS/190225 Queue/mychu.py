class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def isEmpty():
    return front == None

def deQueue():
    global front, rear
    if isEmpty():
        return None
    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

m = 20
curr_m = m
idx = 1
front = None
rear = None

while curr_m > 0:
    new_one = [idx, 1]
    enQueue(new_one)
    print(f"{idx}번 학생 입장")
    out_one = deQueue()
    print(f"{out_one[0  ]}번 줄에서 나와")
    curr_m -= out_one[1]
    print(f"남은 사탕 개수: {curr_m}")
    print(f"{out_one[0]}번 학생 다시 줄 선다")
    out_one[1] += 1
    enQueue(out_one)
    idx += 1

print(out_one[0])
