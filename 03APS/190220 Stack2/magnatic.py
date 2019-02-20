import sys
sys.stdin = open('magnatic.txt', 'r')

def push(item):
    global top
    stack[top + 1] = item
    top += 1

def pop():
    global top
    item = stack[top]
    stack[top] = 0
    top -= 1
    return item

def peek():
    global top
    if top == -1:
        return -1
    return stack[top]


for tc in range(1, 11):
    m = int(input())

    cnt = 0

    matrix = [[0] * m for i in range(m)]

    for i in range(m):
        matrix[i] = list(map(int, input().split()))

    for i in range(m):
        stack = [0] * m
        top = -1

        aline = [0] * m
        for j in range(m):
            aline[j] = matrix[j][i]
        # print(aline)
        a_len = len(aline)
        for k in range(a_len):
            letter = aline[k]
            if letter == 1:
                push(1)
            elif letter == 2:
                judge = False
                while peek() == 1:
                    judge = True
                    pop()
                if judge:
                    cnt += 1

    print(f"#{tc} {cnt}")
