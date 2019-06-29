import sys
sys.stdin = open('5249.txt', 'r')


def make_set(x):
    p[x] = x


def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]


def Union(x, y):
    p[find_p(y)] = find_p(x)


def MST_Kruskal():
    global distance
    # 트리를 담을 공집합 A
    A = set()
    for v in range(V_nodes + 1):
        make_set(v)

    # G.E에 포함된 간선들을 가중치 w에 의해 정렬
    edge_list.sort(key=lambda x: x[2])

    # print(edge_list)

    for edge in edge_list:
        u, v = edge[0], edge[1]
        if find_p(u) != find_p(v):
            A = A.union({u, v})
            Union(u, v)
            distance += edge[2]

    return A


T = int(input())
for tc in range(1, T + 1):
    V_nodes, E_edges = map(int, input().split())
    edge_list = [0] * E_edges
    for i in range(E_edges):
        edge_list[i] = list(map(int, input().split()))

    # for i in edge_list:
    #     print(i)

    p = [0] * (V_nodes + 1)
    distance = 0
    MST_Kruskal()
    print(f"#{tc} {distance}")
    # print()