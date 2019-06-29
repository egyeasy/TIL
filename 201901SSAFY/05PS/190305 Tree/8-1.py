import sys
sys.stdin = open('8-1.txt', 'r')

cnt = 0

def pre_order(idx):
    global cnt
    if idx:
        # print(idx)
        cnt += 1
        pre_order(tree[idx][0])
        pre_order(tree[idx][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = [[0] * 3 for _ in range(E + 2)]
    aline = list(map(int, input().split()))
    for i in range(E):
        parent, child = aline[2 * i], aline[2 * i + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    # for i in tree:
    #     print(i)

    cnt = 0
    pre_order(N)

    print("#{}".format(tc), cnt)