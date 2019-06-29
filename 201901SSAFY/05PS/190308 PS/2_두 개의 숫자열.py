import sys
sys.stdin = open('2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_nums = list(map(int, input().split()))
    M_nums = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        N_nums, M_nums = M_nums, N_nums
    max_sum = 0
    for i in range(M - N + 1):
        each_sum = 0
        for j in range(N):
            each_sum += N_nums[j] * M_nums[i + j]
            # print(N_nums[j], M_nums[i + j], each_sum)
        if each_sum > max_sum:
            max_sum = each_sum
    print("#{}".format(tc), max_sum)
