# 짜다 말았음

import sys
sys.stdin = open('02.txt', 'r')

import itertools


cands = []

def judge_babygin(nums):
    global tc_judge
    if nums[0] == nums[1] == nums[2] or (nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]):
        if nums[3] == nums[4] == nums[5] or (nums[3] + 1 == nums[4] and nums[4] + 1 == nums[5]):
            tc_judge = True


def perm(n, k):
    if k == n:
        # print(nums)
        judge_babygin(nums)
        if tc_judge:
            return
    else:
        for i in range(k, n):
            nums[k], nums[i] = nums[i], nums[k]
            perm(n, k + 1)
            nums[k], nums[i] = nums[i], nums[k]


def dfs(arr, k, max_input):

    k += 1
    n_cands = make_cand(arr, k, max_input)
    for c in range(n_cands):
        arr[k] = cands[c]
        dfs(arr, k, max_input)

def make_cand(arr, k, max_input):
    return 0



T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, list(input())))
    print(nums)

    # 재귀적 접근
    tc_judge = False
    perm(6, 0)
    print(tc_judge)

    # 라이브러리 사용
    tc_judge = False
    for e in itertools.permutations(nums):
        judge_babygin(e)
        if tc_judge:
            break
    print(tc_judge)

    # dfs
    arr = [0] * len(nums)
    dfs(arr, 0, len(nums))

    print()