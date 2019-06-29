import sys
sys.stdin = open('7-1.txt', 'r')

class Node:
    def __init__(self, data, n=None):
        self.data = data
        self.link = n

def push(item):
    global head
    newNode = Node(item)
    if not head:
        head = newNode
    else:
        p = head
        while p.link:
            p = p.link
        p.link = newNode

def find(idx):
    if idx == 0:
        return head
    p = head
    result = 0
    while p.link:
        if result + 1 == idx:
            break
        result += 1
        p = p.link
    return p

def add(idx, item):
    global head
    if idx == 0:
        head = Node(item, head)
    else:
        prev = find(idx)
        prev.link = Node(item, prev.link)

def traverse():
    p = head
    while p:
        print(p.data)
        p = p.link



T = int(input())
# for tc in range(1, 2):
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    # print(nums)
    head = None
    for i in nums:
        push(i)
    for i in range(m):
        idx, item = map(int, input().split())
        add(idx, item)
    # traverse()
    print(f"#{tc} {find(l + 1).data}")
