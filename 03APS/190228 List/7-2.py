import sys
sys.stdin = open('7-2.txt', 'r')

class Node:
    def __init__(self, item, link=None):
        self.data = item
        self.link = link

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            p = self.head
            # while p.link != None:
            #     p = p.link
            # p.link = Node(item)
            # print(item)
            self.tail.link = Node(item)
            self.tail = self.tail.link

    def traverse(self):
        p = self.head
        print(p.data, end=" ")
        while p.link:
            p = p.link
            print(p.data, end=" ")
        print(p.data)

def merge(a, b):
    global globalhead, globaltail
    value = b.head.data
    p = globalhead
    # b의 기준값이 head보다 작을 경우
    if value < p.data:
        # q = b.head
        # while q.link:
        #     q = q.link
        # print(f"q.data: {q}, p: {p}")
        b.tail.link = p
        globalhead = b.head
    else:
        # b의 기준값이 a의 모든 값보다 클 경우
        if value >= maxes[0]:
            globaltail.link = b.head
            globaltail = b.tail
        else:
            # b의 기준값이 p.link.data보다 작을 경우
            while p.link:
                if value < p.link.data:
                    break
                p = p.link
            if p.link:
                q = b.head
                while q.link:
                    q = q.link
                q.link = p.link
                p.link = b.head

def total_traverse():
    p = globalhead
    print(p.data)
    while p.link:
        p = p.link
        print(p.data)

def make_result():
    p = globalhead
    result = []
    remains = n * m
    while remains:
        if remains <= 10:
            result = [p.data] + result
        p = p.link
        remains -= 1
    print(f"#{tc} {' '.join(map(str, result))}")

T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    head = None
    n, m = map(int, input().split())
    lists = [0] * m
    maxes = [0] * m
    for i in range(m):
        alist = list(map(int, input().split()))
        a = Linked()
        for j in alist:
            if j > maxes[i]:
                maxes[i] = j
            a.push(j)
        # a.traverse()
        # print()
        lists[i] = a

    globalhead = lists[0].head
    globaltail = lists[0].tail
    # print(maxes)
    for i in range(1, m):
        merge(lists[0], lists[i])
        if maxes[i] > maxes[0]:
            maxes[0] = maxes[i]
        # print(maxes)
        # lists[0].traverse()
        # print(f"global head: {globalhead.data}")
        # print()

    # print(f"traverse:")
    # total_traverse()

    make_result()
