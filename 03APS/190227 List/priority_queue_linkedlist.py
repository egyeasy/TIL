class Node:
    def __init__(self, item, prev=None, next=None):
        self.data = item
        self.prev = prev
        self.next = next

head = None

def addfirst(item):
    global head
    head = Node(item, next=head)

def add(item):
    global head
    if head == None:
        head = Node(item, next=head)
    else:
        p = head
        # print(head.data)
        while item > p.data:
            if p.next == None:
                p.next = Node(item, p, None)
                # print(f"put first {p.next.data}")
                break
            p = p.next
        else:
            p.prev = Node(item, p.prev, p)
            p.prev.prev.next = p.prev

def dequeue():
    global head
    de_item = head.data
    head = head.next
    return de_item

def traverse():
    p = head
    while p.next != None:
        print(p)
        print(p.data)
        p = p.next

nums = [1, 5, 2, 4, 3]
for i in nums:
    add(i)

# traverse()

for i in range(5):
    print(dequeue())





