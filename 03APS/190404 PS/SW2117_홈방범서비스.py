import sys
sys.stdin = open('2117.txt', 'r')

def find(i_start, j_start, k):
    global max_cnt_house
    cnt_house = 0
    for i in range(-(k - 1), k):
        for j in range(-(k - 1), k):
            if abs(j) < k - abs(i) and 0 <= i_start + i < N_side and 0 <= j_start + j < N_side and mat[i_start + i][j_start + j]:
                cnt_house += 1
    if cnt_house > max_cnt_house:
        max_cnt_house = cnt_house
        # print("find max 갱신")
        # print("max", max_cnt_house, "num_house", num_house, "ij", i_start, j_start, "k", k)
        # print("this_수입", M_fee * max_cnt_house - this_cost)
        # print()


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_side, M_fee = map(int, input().split())
    mat = [[0] * N_side for _ in range(N_side)]
    num_house = 0
    for i in range(N_side):
        aline = list(map(int, input().split()))
        for j in range(N_side):
            if aline[j]:
                mat[i][j] = aline[j]
                num_house += 1

    # print(num_house)
    # for i in mat:
    #     print(i)
    # print()

    # global_max_money = -9999999999999999
    max_cnt_house = 0
    k = 1
    global_house = 0
    while k < 2 * (N_side - 1):
        this_cost = k ** 2 + (k - 1) ** 2
        k_height = 2 * k - 1
        found = False
        # 가운데부터 먼저 보기
        center_idx = N_side // 2
        # print(k)
        if N_side % 2:
            find(center_idx, center_idx, k)
            if max_cnt_house == num_house:
                # print("max", max_cnt_house, "num_house", num_house, "ij", i, j, "k", k)
                # print("this_수입", M_fee * max_cnt_house - this_cost)
                found = True
        else:
            for i in range(center_idx, center_idx - 2, -1):
                for j in range(center_idx, center_idx - 2, -1):
                    find(i, j, k)
                    if max_cnt_house == num_house:
                        # print("max", max_cnt_house, "num_house", num_house, "ij", i, j, "k", k)
                        # print("this_수입", M_fee * max_cnt_house - this_cost)
                        found = True
                        break
                if found:
                    break

        if found:
            this_money = M_fee * max_cnt_house - this_cost
            if this_money >= 0:
                global_house = max_cnt_house
            break

        else:
            for i in range(N_side):
                for j in range(N_side):
                    find(i, j, k)
                    if max_cnt_house == num_house:
                        # print("max", max_cnt_house, "num_house", num_house, "ij", i, j, "k", k)
                        # print("this_수입", M_fee * max_cnt_house - this_cost)
                        found = True
                        break
                if found:
                    found_cost = this_cost
                    break

        this_money = M_fee * max_cnt_house - this_cost
        if this_money >= 0:
            global_house = max_cnt_house

        k += 1


    # global_money = M_fee * max_cnt_house - found_cost
    # if global_money >= 0:
    #     global_house = max_cnt_house



    print(f"#{tc} {global_house}")