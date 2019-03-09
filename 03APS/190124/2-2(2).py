import sys
sys.stdin = open('2-2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, sum_K = map(int, input().split())
    arr = list(range(1, 13))
    total_cnt = 0
    for i in range(1 << 12):
        curr_sum = 0
        curr_cnt = 0
        for j in range(12):
            if i & (1 << j):
                curr_sum += arr[j]
                curr_cnt += 1
        if curr_cnt == N and curr_sum == sum_K:
            total_cnt += 1
    print("#{}".format(tc), total_cnt)