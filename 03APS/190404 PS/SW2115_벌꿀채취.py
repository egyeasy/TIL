import sys
sys.stdin = open('2115.txt', 'r')


def go_honey(i, j):
    go_list = mat[i][j: j + M_series]
    this_max_honey = 0
    this_max_revenue = 0
    for i in range(1 << M_series):
        total_honey = 0
        total_revenue = 0
        for j in range(M_series):
            if i & (1 << j):
                total_honey += go_list[j]
                total_revenue += go_list[j] ** 2
        if total_honey == C_container:
            this_max_revenue = total_revenue
            break
        elif total_honey < C_container and total_revenue > this_max_revenue:
            this_max_honey = total_honey
            this_max_revenue = total_revenue

    return this_max_revenue


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_side, M_series, C_container = map(int, input().split())
    mat = [0] * N_side
    for i in range(N_side):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)
    # print()

    global_revenue = 0
    visited = [[0] * N_side for _ in range(N_side)]

    # a가 채취할 때 처리
    for i in range(N_side):
        for j in range(N_side - M_series + 1):
            visited[i][j: j + M_series] = [1] * M_series
            this_revenue = 0
            a_revenue = go_honey(i, j)
            this_revenue += a_revenue
            # b에 대해 처리
            for k in range(N_side):
                for m in range(N_side - M_series + 1):
                    for l in range(m, m + M_series):
                        if 0 <= l < N_side and visited[k][l]:
                            break
                    else:
                        b_revenue = go_honey(k, m)
                        this_revenue += b_revenue
                        if this_revenue > global_revenue:
                            global_revenue = this_revenue
                        this_revenue -= b_revenue
            visited[i][j: j + M_series] = [0] * M_series

    print(f"#{tc} {global_revenue}")

