import sys
sys.stdin = open('5249.txt', 'r')


def MST_Prim(r):
    for u in range(V_nodes + 1):
        mat[u][0] = 10000000

    # 스타팅 포인트까지의 거리 = 0
    mat[r][0] = 0
    # edge_list.sort(key=lambda x:x[2])
    q = list(range(V_nodes + 1))

    while sum(visited) != V_nodes + 1:
        # 우선순위 큐에서 가중치 가장 작은 값 빼오기
        u = 0
        min_idx = 0
        for i in range(V_nodes + 1):
            if not visited[i]:
                min_idx = i
                break

        for i in range(V_nodes + 1):
            if mat[i][0] < mat[min_idx][0] and not visited[i]:
                min_idx = i
        u = min_idx

        visited[u] = 1
        # print(visited)

        # u와 인접한 v에 대해
        for v in ad_list[u]:
            if not visited[v] and ad_mat[u][v] < mat[v][0]:
                mat[v][1] = u
                mat[v][0] = ad_mat[u][v]


T = int(input())
for tc in range(1, T + 1):
    V_nodes, E_edges = map(int, input().split())
    edge_list = [0] * E_edges
    ad_list = [[] for _ in range(V_nodes + 1)]
    ad_mat = [[0] * (V_nodes + 1) for _ in range(V_nodes + 1)]
    for i in range(E_edges):
        alist = list(map(int, input().split()))
        edge_list[i] = alist
        ad_list[alist[0]].append(alist[1])
        ad_list[alist[1]].append(alist[0])
        ad_mat[alist[0]][alist[1]] = alist[2]
        ad_mat[alist[1]][alist[0]] = alist[2]

    # for i in edge_list:
    #     print(i)
    # print()

    # for i in ad_list:
    #     print(i)
    # print()

    # key(가중치), pi(부모) 저장할 matrix
    mat = [[-1] * 2 for _ in range(V_nodes + 1)]
    visited = [0] * (V_nodes + 1)
    distance = 0
    MST_Prim(0)
    # print(mat)
    for node in mat:
        distance += node[0]
    print(f"#{tc} {distance}")
    # print()