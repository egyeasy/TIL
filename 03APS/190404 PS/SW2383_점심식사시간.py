import sys
sys.stdin = open('2383.txt', 'r')

from itertools import combinations
from collections import deque


def calculate(firsts, seconds):
    global min_time
    first_time = calculate_time(firsts, 0)
    second_time = calculate_time(seconds, 1)
    end_time = max(first_time, second_time)
    if end_time < min_time:
        min_time = end_time


def calculate_time(nums, num_stair):
    time = 0
    this_stair, num_stair = stairs[num_stair][:2], stairs[num_stair][2]
    this_people = [people[num] for num in nums]
    # print("this_people", this_people)
    this_people = sorted(this_people, key=lambda x: abs(this_stair[0] - x[0]) + abs(this_stair[1] - x[1]))
    num_people = len(this_people)
    distances = [abs(this_stair[0] - person[0]) + abs(this_stair[1] - person[1]) for person in this_people]

    dq = deque()
    go_cnt = 0
    while go_cnt != num_people:
        # 계단 가는 사람들 시간 더해주기
        for i in range(len(dq)):
            dq[i] += 1

        # 계단에서 시간 된 사람들 빼주기
        for i in range(len(dq) - 1, -1, -1):
            if dq[i] == num_stair:
                del dq[i]
                go_cnt += 1

        # distance 0인 사람들 계단 입장

        if len(dq) < 3:
            for i in range(len(distances) - 1, -1, -1):
                if distances[i] <= 0 and len(dq) < 3:
                    distances.pop(i)
                    dq.append(0)

        # distance, 시간 업데이트
        distances = list(map(lambda x: x - 1, distances))
        time += 1

    return time




T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_side = int(input())
    mat = [[0] * N_side for _ in range(N_side)]

    stairs = [0, 0]
    people = []
    M_people = 0

    for i in range(N_side):
        aline = list(map(int, input().split()))
        for j in range(N_side):
            mat[i][j] = aline[j]
            if mat[i][j] > 1:
                if not stairs[0]:
                    stairs[0] = [i, j, mat[i][j]]
                else:
                    stairs[1] = [i, j, mat[i][j]]
            elif mat[i][j] == 1:
                people.append([i, j])
                M_people += 1

    # print(stairs)
    # print(people)
    # for i in mat:
    #     print(i)
    # print()

    min_time = 100000000000000
    nums_people = list(range(M_people))
    for k in range(M_people + 1):
        for first_set in combinations(nums_people, k):
            first_set = list(first_set)
            # print("first", first_set)
            second_set = list(set(nums_people) - set(first_set))
            # print("second", second_set)
            calculate(first_set, second_set)
            # print()

    print(f"#{tc} {min_time}")



    # for i in range()