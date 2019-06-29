import sys
sys.stdin = open('operation.txt', 'r')

def post_order(idx):
    global result
    if idx:
        # print("idx", idx)
        if type(tree[idx][3]) == int:
            # print(idx, tree[idx][3])
            return tree[idx][3]
        else:
            # print("else")
            a = post_order(tree[idx][0])
            b = post_order(tree[idx][1])
            # print(a, b)
            if tree[idx][3] == '+':
                return a + b
            elif tree[idx][3] == '-':
                return a - b
            elif tree[idx][3] == '*':
                return a * b
            else:
                return a / b


T = 10
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    for i in range(1, N + 1):
        aline = input().split()
        if len(aline) == 2:
            tree[i][3] = int(aline[1])
        else:
            tree[i][3] = aline[1]
            tree[i][0] = int(aline[2])
            tree[i][1] = int(aline[3])
            tree[int(aline[2])][2] = i
            tree[int(aline[3])][2] = i

    # for i in tree:
    #     print(i)

    print("#{}".format(tc), int(post_order(1)))