import sys
sys.stdin = open('3test.txt', 'r')
import time

def backtrack(arr, k, curr_sum):
    global min_sum, zero_found
    if k == N_position:
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum == 0:
            zero_found = True
    else:
        k += 1
        cands = make_cands(arr, k)
        for cand in cands:
            arr[k] = cand + 1
            distance = cal_distance(k - 1, cand)
            if curr_sum + distance < min_sum:
                backtrack(arr, k, curr_sum + distance)
            arr[k] = 0
            if zero_found:
                return


def cal_distance(robot_idx, target_idx):
    robot = robots[robot_idx]
    target = snacks[target_idx]
    distance = abs(robot[0] - target[0]) + abs(robot[1] - target[1])
    return distance


def make_cands(arr, k):
    in_perm = [False] * N_position
    cands = []
    for i in range(1, k):
        in_perm[arr[i] - 1] = True

    for i in range(N_position):
        if in_perm[i] == False:
            cands.append(i)
    return cands


T = int(input())
for tc in range(1, T + 1):

    time_start = time.time()
    N_position = int(input())
    nums = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    snacks = [0] * N_position
    robots = [0] * N_position
    for i in range(N_position):
        snacks[i] = [nums[2 * i], nums[2 * i + 1]]
        robots[i] = [nums2[2 * i], nums2[2 * i + 1]]

    arr = [0] * (N_position + 1)
    min_sum = 100000000000000000
    zero_found = False
    backtrack(arr, 0, 0)

    print(f"#{tc} {min_sum}")

    print(time.time() - time_start)