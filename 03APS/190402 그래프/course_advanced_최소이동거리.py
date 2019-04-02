import sys
sys.stdin = open('5251.txt', 'r')


def dijkstra(s):
    U = set({0})

    for i in range(N_lastnode + 1):
        D[i] = ad_mat[s][i]

    # print("D", D)

    V = set(range(N_lastnode + 1))
    visited = [0] * (N_lastnode + 1)
    while U != V:
        w = -1
        # found = False
        for i in range(1, N_lastnode + 1):
            if not visited[i]:
                if w == -1: # 초기 설정
                    w = i
                elif D[i] < D[w]:
                    # found = True
                    w = i

        # if not found:
        #     break

        # print("w", w)
        U = U.union({w})
        visited[w] = 1

        for v in range(N_lastnode + 1):
            if 0 < ad_mat[w][v] <= 1000000:
                D[v] = min(D[v], D[w] + ad_mat[w][v])
        # print("D", D, "U", U, "V", V)


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_lastnode, E_edges = map(int, input().split())
    edge_list = [0] * E_edges
    ad_mat = [[9999999] * (N_lastnode + 1) for _ in range(N_lastnode + 1)]

    for i in range(E_edges):
        alist = list(map(int, input().split()))
        edge_list[i] = alist
        ad_mat[alist[0]][alist[1]] = alist[2]

    for i in range(N_lastnode + 1):
        ad_mat[i][i] = 0

    # for i in edge_list:
    #     print(i)
    # print()
    #
    # print("ad mat")
    # for i in ad_mat:
    #     print(i)
    # print()

    D = [0] * (N_lastnode + 1)
    dijkstra(0)
    print(f"#{tc} {D[N_lastnode]}")
