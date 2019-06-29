import sys
sys.stdin = open('03.txt', 'r')


def pre_order(num):
    if num:
        print(num, end=" ")
        pre_order(mat[num][0])
        pre_order(mat[num][1])


def in_order(num):
    if num:
        post_order(mat[num][0])
        print(num, end=" ")
        post_order(mat[num][1])


def post_order(num):
    if num:
        post_order(mat[num][0])
        post_order(mat[num][1])
        print(num, end=" ")

N_nodes = int(input())
edge_list = list(map(int, input().split()))
# 자식노드 1, 자식노드 2, 부모노드
mat = [[0] * 3 for _ in range(N_nodes + 1)]
for i in range(N_nodes - 1):
    if not mat[edge_list[2 * i]][0]:
        mat[edge_list[2 * i]][0] = edge_list[2 * i + 1]
    else:
        mat[edge_list[2 * i]][1] = edge_list[2 * i + 1]
    mat[edge_list[2 * i + 1]][2] = edge_list[2 * i]

for i in mat:
    print(i)

print("preorder:")
pre_order(1)
print()
print()

print("inorder:")
in_order(1)
print()
print()

print("postorder:")
post_order(1)