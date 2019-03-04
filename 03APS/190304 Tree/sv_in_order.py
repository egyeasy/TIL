import sys
sys.stdin = open('sv.txt', 'r')

def in_order(idx):
    if idx:
        in_order(tree[idx][0])
        print(tree[idx][3], end="")
        in_order(tree[idx][1])

T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    for i in range(1, N + 1):
        aline = input().split()
        if len(aline) == 2:
            tree[i][3] = aline[1]
        elif len(aline) == 3:
            tree[i][3] = aline[1]
            tree[i][0] = int(aline[2])
            tree[int(aline[2])][2] = i
        else:
            tree[i][3] = aline[1]
            tree[i][0] = int(aline[2])
            tree[i][1] = int(aline[3])
            tree[int(aline[2])][2] = i
            tree[int(aline[3])][2] = i
    print("#{}".format(tc), end=" ")
    in_order(1)
    print()