import sys
sys.stdin = open('5-1.txt', 'r')

def push(item):
    global top
    stack[top + 1] = item
    top += 1

def pop():
    global top
    pop_item = stack[top]
    stack[top] = 0
    top -= 1
    return pop_item

def peek():
    global top
    return stack[top]

def iscal(chr):
    cal_list = ['+', '-', '*', '/']
    for i in cal_list:
        if chr == i:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    text = input().split()
    length = len(text)
    stack = ['0'] * length
    top = -1
    judge = True

    for i in range(length):
        if text[i] == '.':
            result = pop()
            if top != -1:
                judge = False
        elif iscal(text[i]):
            if type(peek()) == int:
                b = pop()
            else:
                judge = False
                break
            if type(peek()) == int:
                a = pop()
            else:
                judge = False
                break
            if text[i] == '+':
                push(a + b)
            elif text[i] == '-':
                push(a - b)
            elif text[i] == '*':
                push(a * b)
            else:
                push(a // b)
        else:
            push(int(text[i]))

    if judge:
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} error")