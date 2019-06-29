import sys
sys.stdin = open('1244.txt', 'r')


def backtrack(nums, k):
    global global_max
    if k == max_change:
        this_value = int(''.join(map(str, nums)))
        if this_value > global_max:
            global_max = this_value
    else:
        k += 1
        for i in range(length - 1):
            for j in range(i + 1, length):
                new_nums = nums[:]
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
                this_value = int(''.join(map(str, new_nums)))
                if k not in visited[this_value]:
                    visited[this_value].append(k)
                    backtrack(new_nums, k)

T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    nums, max_change = input().split()
    value_max = int(''.join(sorted(nums, reverse=True)))
    nums = list(map(int, list(nums)))
    max_change = int(max_change)

    length = len(nums)

    # print(nums, max_change)
    # print(value_max)
    visited = [[] for _ in range(value_max + 1)]
    global_max = 0
    backtrack(nums, 0)
    print(f"#{tc} {global_max}")