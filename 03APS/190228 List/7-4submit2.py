import sys
sys.stdin = open('7-4.txt', 'r')
# 처음, 끝에 추가, 삭제할 경우 head, tail

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
    else:
        # 0번 index에 insert할 경우 대비해 head와 tail을 연결
        newNode = Node(item, tail)
        tail.next = newNode
        tail = newNode

def find(idx):
    curr_idx = 0
    p = head
    # if 시간 초과 => p = tail로 두는 방법도 생각해볼 것
    while p != tail:
        if curr_idx == idx:
            break
        # print(f"curr_idx: {curr_idx}, idx: {idx}, p: {p.data}")
        curr_idx += 1
        p = p.next
    if curr_idx == idx:
        # print(f"found {p.data}")
        return p
    # else:
    #     print("not found")


def insert(idx, item):
    global head
    post = find(idx)
    if idx == 0:
        newNode = Node(item, next=post)
        post.prev = newNode
        head = newNode
    else:
        newNode = Node(item, post.prev, post)
        post.prev.next = newNode
        post.prev = newNode

def delete(idx):
    global tail, head
    p = find(idx)
    if idx == 0:
        post = p.next
        p.next = None
        post.prev = None
        head = post
    elif idx == length:
        prev = p.prev
        p.prev = None
        prev.next = None
        tail = prev
    else:
        prev = p.prev
        post = p.next
        prev.next = post
        post.prev = prev
        p.prev = None
        p.post = None

def change(idx, item):
    p = find(idx)
    p.data = item


def traverse():
    global length
    p = head
    print(f"head: {head.data} tail: {tail.data}")
    while p != tail:
        print(p.data, length, end=" ")
        p = p.next
    print(p.data)
    print()


T = int(input())
for tc in range(1, T + 1):
    n, times_m, print_l = map(int, input().split())
    nums = list(map(int, input().split()))

    head = None
    tail = None

    length = -1

    for num in nums:
        push(num)
        length += 1

    # traverse()

    for _ in range(times_m):
        command = input().split()
        if command[0] == 'I':
            # print("insert", command[1], command[2])
            insert(int(command[1]), int(command[2]))
            length += 1
            # traverse()
        elif command[0] == 'D':
            # print("delete", command[1])
            delete(int(command[1]))
            length -= 1
            # traverse()
        else:
            # print("change", command[1], command[2])
            change(int(command[1]), int(command[2]))
            # traverse()
    
    result = find(print_l)
    
    if result:
        print(f"#{tc} {result.data}")
    else:
        print(f"#{tc} -1")

