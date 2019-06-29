import sys
sys.stdin = open('1486.txt', 'r')

min_sum = 0

def BackTrack(arr, k, max_input, summ):
    global min_sum, found
    if summ > min_sum:
        return
    if k == max_input:
        part_sum = 0
        for i in range(N_saram):
            if arr[i]:
                part_sum += nums[i]
        if part_sum >= B_target and part_sum < min_sum:
            min_sum = part_sum
            # print(arr, min_sum)
        if part_sum == B_target:
            found = True
            return
    else:
        k += 1
        arr[k - 1] = 1
        BackTrack(arr, k, max_input, summ + nums[k - 1])
        if found:
            return
        arr[k - 1] = 0
        BackTrack(arr, k, max_input, summ)

T = int(input())
for tc in range(1, T + 1):
    N_saram, B_target = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = [0] * N_saram
    min_sum = sum(nums)
    found = False
    BackTrack(arr, 0, N_saram, 0)

    print(f"#{tc} {min_sum - B_target}")