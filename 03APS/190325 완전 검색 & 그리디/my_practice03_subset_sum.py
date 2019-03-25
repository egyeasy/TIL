import sys
sys.stdin = open('03.txt', 'r')

N_num = int(input())
nums = list(map(int, input().split()))

for i in range(1, 1 << N_num):
    subset = []
    for j in range(N_num):
        if i & (1 << j):
            subset.append(nums[j])
    if sum(subset) == 10:
        print(subset)
