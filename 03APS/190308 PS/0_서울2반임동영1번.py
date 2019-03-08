# import sys
# sys.stdin = open('1.txt', 'r')

def cnt_sum(s_i, s_j):
    right_sum = 0
    left_sum = 0
    for i in range(dogu_K):
        right_sum += mat[s_i + i][s_j + i]
        left_sum += mat[s_i + i][s_j + (dogu_K - 1 - i)]
    # print(right_sum, left_sum)
    return abs(right_sum - left_sum)



T = int(input())
for tc in range(1, T + 1):
    side_N, dogu_K = map(int, input().split())
    mat = [0] * side_N

    for i in range(side_N):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)

    min_diff = 10000000000

    for i in range(side_N - dogu_K + 1):
        for j in range(side_N - dogu_K + 1):
            each_diff = cnt_sum(i, j)
            # print(each_diff)
            if each_diff < min_diff:
                min_diff = each_diff

    print("#{}".format(tc), min_diff)

