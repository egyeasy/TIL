import sys
sys.stdin = open("4.txt", "r")
top = -1
def push(item):
    global top
    stack[top + 1] = item
    top += 1

def peek():
    global top
    return stack[top]

def pop():
    global top
    result = stack[top]
    stack[top] = 0
    top -= 1
    return result

T = int(input())
for tc in range(1, T+1):
    text = input()
    length = len(text)

    stack = [0]*length
    top = -1
    visited = []
    push(text[0])
    for i in range(1, length):
        if text[i] == peek():
            pop()
        else:
            push(text[i])

    # print(stack)
    result = 0
    for i in range(length):
        if not stack[i]:
            break
        result += 1

    print(f"#{tc} {result}")