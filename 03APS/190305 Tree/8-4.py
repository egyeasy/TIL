import sys
sys.stdin = open('8-4.txt', 'r')

def post_order(idx):
    if idx < N + 1:
        if data[idx]:
            return data[idx]
        else:
            a = post_order(2 * idx)
            b = post_order(2 * idx + 1)
            if idx == idx_L:
                print("#{}".format(tc), a + b)
            return a + b
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, leaf_M, idx_L = map(int, input().split())
    data = [0] * (N + 1)
    for i in range(leaf_M):
        aline = list(map(int, input().split()))
        data[aline[0]] = aline[1]
    
    post_order(1)