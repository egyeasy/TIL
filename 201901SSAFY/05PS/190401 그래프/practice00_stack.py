N = 100
stack = [0] * N
top = -1


def push(item):
    global top
    if isFull():
        print("overflow")
    else:
        top += 1
        stack[top] = item


def pop():
    global top
    if isEmpty():
        print("underflow")
    else:
        pop_item = stack[top]
        stack[top] = 0
        top -= 1
        return pop_item


def isFull():
    return top == N - 1


def isEmpty():
    return top == -1


push(1)
push(2)
push(3)
print(stack)
print(pop())
print(pop())
print(pop())
pop()