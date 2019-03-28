import sys
sys.stdin = open('1224.txt', 'r')

top = 0

def push(item, stack):
    global top
    stack[top + 1] = item
    top += 1

def pop(stack):
    global top
    if top == -1:
        return -1
    pop_item = stack[top]
    stack[top] = -1
    top -= 1
    return pop_item

def peek(stack):
    global top
    if top == -1:
        return -1
    return stack[top]


# for tc in range(1, 2):
for tc in range(1, 11):
    length = int(input())
    text = input()
    # print(len(text), length)
    post_result = [-1] * length
    post_stack = [0] * length
    top = -1
    idx = 0
    for i in range(length):
        c = text[i]
        if c == '(' or c == '*':
            push(c, post_stack)
        elif c == '+':
            while peek(post_stack) == '*':
                post_result[idx] = pop(post_stack)
                idx += 1
            push(c, post_stack)
        elif c == ')':
            while peek(post_stack) != '(':
                post_result[idx] = pop(post_stack)
                idx += 1
            pop(post_stack)
        else:
            post_result[idx] = c
            idx += 1

    # print(post_result)

    cal_stack = [-1] * length

    for i in range(length):
        # print(top, cal_stack)
        c = post_result[i]
        if not c == -1:
            if c == '*':
                b = pop(cal_stack)
                a = pop(cal_stack)
                push(a * b, cal_stack)
            elif c == '+':
                b = pop(cal_stack)
                a = pop(cal_stack)
                push(a + b, cal_stack)
            else:
                push(int(c), cal_stack)
    # print(cal_stack)
    result = pop(cal_stack)
    print(f"#{tc} {result}")
