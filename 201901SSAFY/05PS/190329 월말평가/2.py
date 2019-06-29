import sys
sys.stdin = open('2test.txt', 'r')

from itertools import combinations

def cal_sum(comb):
    global max_sum
    part_sum = 0
    for i in range(2):
        for j in range(i + 1, 3):
            part_sum += abs(sum_array[comb[i]] - sum_array[comb[j]])
    if part_sum > max_sum:
        max_sum = part_sum


T = int(input())
for tc in range(1, T + 1):
    N_row, M_col = map(int, input().split())
    mat = [0] * N_row
    for i in range(N_row):
        mat[i] = list(map(int, input().split()))

    max_sum = 0

    for row_cut in combinations(range(1, N_row), 1):
        for col_cut in combinations(range(1, M_col), 2):
            row_first = row_cut[0]
            col_first = col_cut[0]
            col_second = col_cut[1]
            sum_array = [0] * 6

            for i in range(N_row):
                for j in range(M_col):
                    value = mat[i][j]
                    if i < row_first:
                        if j < col_first:
                            sum_array[0] += value
                        elif col_first <= j < col_second:
                            sum_array[1] += value
                        else:
                            sum_array[2] += value
                    else:
                        if j < col_first:
                            sum_array[3] += value
                        elif col_first <= j < col_second:
                            sum_array[4] += value
                        else:
                            sum_array[5] += value
            for comb in combinations(range(6), 3):
                cal_sum(comb)

    print(f"#{tc} {max_sum}")