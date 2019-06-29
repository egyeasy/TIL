import sys
sys.stdin = open('02.txt', 'r')


def subset(arr, k, max_input, summ):
    if summ > 10:
        return
    if k == max_input:
        if summ == 10:
            print(arr)
    else:
        k += 1
        arr[k] = 1
        subset(arr, k, max_input, summ + nums[k - 1])
        arr[k] = 0
        subset(arr, k, max_input, summ)


# 순열(여기서 안 씀)
def make_cands(arr, k, cand, max_input):
    in_perm = [0] * (max_input + 1)

    for i in range(1, k):
        in_perm[arr[i]] = 1

    n_cand = 0
    for i in range(1, max_input + 1):
        if in_perm[i] == 0:
            cand[n_cand] = i
            n_cand += 1
    return n_cand


def judge_sum(arr):
    subset_sum = 0
    subset_nums = []
    for i in range(1, N + 1):
        subset_sum += arr[i]
        subset_nums.append(arr[i])

    return subset_sum, subset_nums



nums = list(map(int, input().split()))
N = len(nums)
arr = [0] * (N + 1)
subset(arr, 0, N, 0)