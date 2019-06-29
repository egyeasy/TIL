import sys
sys.stdin = open('practice1.txt', 'r')

def pre_order(idx):
    if idx:
        print(idx)
        pre_order(mat[idx][0])
        pre_order(mat[idx][1])

def in_order(idx):
    if idx:
        in_order(mat[idx][0])
        print(idx)
        in_order(mat[idx][1])

def post_order(idx):
    if idx:
        post_order(mat[idx][0])
        post_order(mat[idx][1])
        print(idx)

m = int(input())
mat = [[0] * 3 for _ in range(m + 1)]
aline = list(map(int, input().split()))
for i in range(m - 1):
    if not mat[aline[2 * i]][0]:
        mat[aline[2 * i]][0] = aline[2 * i + 1]
    else:
        mat[aline[2 * i]][1] = aline[2 * i + 1]
    mat[aline[2 * i + 1]][2] = aline[2 * i]

for i in mat:
    print(i)

print()
pre_order(1)
print()
in_order(1)
print()
post_order(1)