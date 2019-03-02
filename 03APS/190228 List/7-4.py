# single, next(link) insert, no tail

import sys
sys.stdin = open('7-4.txt', 'r')

class Node:
    def __init__(self, item, link=None):
        self.data = item
        self.link = link


def find(idx):
    curr_idx = -1
    p = head
    if idx == 0:
        return p
    while p.link:
        # print(p.data)
        if curr_idx == idx - 1:
            break
        curr_idx += 1
        p = p.link
    if curr_idx == idx - 1:
        return p
    # else:
    #     print("not found")

def push(item):
    p = head
    while p.link:
        p = p.link
    p.link = Node(item)

def insert(idx, item):
    prev = find(idx)
    prev.link = Node(item, prev.link)

def delete(idx):
    prev = find(idx)
    prev.link = prev.link.link

def change(idx, item):
    prev = find(idx)
    prev.link.data = item

def traverse():
    p = head
    while p.link:
        p = p.link
        print(p.data, end=" ")
    print()
    print()

T = int(input())
for tc in range(1, T + 1):
    n, times_m, idx_l = map(int, input().split())
    nums = list(map(int, input().split()))

    head = Node(None)

    for num in nums:
        push(num)

    # traverse()

    for i in range(times_m):
        comm = input().split()
        # print(comm)
        if comm[0] == 'I':
            insert(int(comm[1]), int(comm[2]))
            # print(f"insert {comm[1]} {comm[2]}")
            # traverse()
        elif comm[0] == 'D':
            delete(int(comm[1]))
            # print(f"delete {comm[1]}")
            # traverse()
        else:
            change(int(comm[1]), int(comm[2]))
            # print(f"change {comm[1]} with {comm[2]}")
            # traverse()

    prev = find(idx_l)
    if prev:
        print(f"#{tc} {prev.link.data}")
    else:
        print(f"#{tc} -1")