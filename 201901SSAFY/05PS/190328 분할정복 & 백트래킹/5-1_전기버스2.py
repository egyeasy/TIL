import sys
sys.stdin = open('5-1.txt', 'r')


def backtrack(s, change_cnt):
    global min_cnt
    if s >= N - 1:
        if change_cnt < min_cnt:
            min_cnt = change_cnt
        return
    # print(s)
    for i in range(s + charges[s], s, -1):
        if change_cnt < min_cnt:
            backtrack(i, change_cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    N, charges = nums[0], nums[1:]
    change_cnt = -1
    min_cnt = 10000000
    backtrack(0, 0)
    print(f"#{tc} {min_cnt - 1}")