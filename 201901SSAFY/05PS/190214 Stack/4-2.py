import sys
sys.stdin = open("2.txt", "r")

top = -1
def push(item):
    global top
    stack[top + 1] = item
    top += 1

def find(item):
    brackets = ['}', '{', ')', '(']
    idx = 0
    for i in brackets:
        if i == item:
            return brackets[idx + 1]
        idx += 1

def peek():
    global top
    return stack[top]

def pop():
    global top
    if top == -1:
        return 0
    pop_item = stack[top]
    stack[top] = 0
    top -= 1
    return pop_item

T = int(input())
for tc in range(1, T+1):
    text = input()
    length = len(text)
    stack = [0] * length
    top = -1
    judge = True
    for i in range(length):
        if text[i] == '{' or text[i] == '(':
            push(text[i])
            # print("{", stack)
        elif text[i] == '}' or text[i] == ')':
            if peek() == find(text[i]):
                # print("}", stack)
                pop()
                # print("pop", stack)
            else:
                # print("false", stack)
                judge = False
                break
    if top != -1:
        judge = False

    print(f"#{tc} {judge*1}")