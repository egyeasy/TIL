import sys
sys.stdin = open('task.txt', 'r')

def dfsR(s):
    visited[s] = 1
    for i in range(1, node_V + 1):
        if mat[s][i] and not visited[i]:
            dfsR(i)
    print(s, end=" ")

for tc in range(1, 11):
    node_V, edge_E = map(int, input().split())
    # print(node_V, edge_E)
    mat = [[0] * (node_V + 1) for _ in range(node_V + 1)]
    aline = list(map(int, input().split()))
    for i in range(edge_E):
        mat[aline[2 * i + 1]][aline[2 * i]] = 1
    # for i in mat:
    #     print(i)
    # print()

    visited = [0] * (node_V + 1)
    print("#{}".format(tc), end=" ")
    for i in range(1, node_V + 1):
        if not visited[i]:
            dfsR(i)
    print()
