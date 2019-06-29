import sys
sys.stdin = open('7-3.txt', 'r')

head = None
tail = None

class Node:
    def __init__(self, item, prev=None, next=None):
        self.data = item
        self.prev = prev
        self.next = next


def push(item):
    global head, tail
    if not head:
        head = Node(item)
        tail = head
        # head, tail 연결
        tail.next = head
        head.prev = tail
    else:
        tail.next = Node(item, tail, head)
        tail = tail.next
        # head, tail 연결
        head.prev = tail

def add(idx, times):
    global head, tail
    p = head
    for tim in range(times):
        remains = idx
        for i in range(idx):
            if remains == 1 and p == tail:
                new_item = p.data + head.data
                new_node = Node(new_item, p, head)
                p.next = new_node
                head.prev = new_node
                tail = new_node
                p = tail
                break
            p = p.next
            remains -= 1
        else:
            new_item = p.prev.data + p.data
            new_node = Node(new_item, p.prev, p)
            p.prev.next = new_node
            p.prev = new_node
            if p == head:
                head = new_node
            p = p.prev
        # print(f"put {new_node.data}")
        # print(f"traverse:")
        # traverse_front()
        # print(f"head: {head.data}")
        # print()
        
def traverse():
    p = tail
    for i in range(10):
        print(p.data, end=" ")
        if p == head:
            break
        p = p.prev
    print()

def traverse_front():
    p = head
    # for i in range(10):
    while p != tail:
        print(p.data, end=" ")
        p = p.next
    print(p.data)

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    head = None
    tail = None

    for num in nums:
        push(num)

    # print(f"first:")
    # traverse_front()

    add(m, k)
    print(f"#{tc} ", end="")
    traverse()