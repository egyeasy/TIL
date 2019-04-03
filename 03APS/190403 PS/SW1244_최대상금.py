import sys
sys.stdin = open('1244.txt', 'r')


def go_to_max():
    found = False
    the_end = -1
    for front in range(length):
        front_value = nums[front]
        for end in range(length - 1, front, -1):
            if nums[end] > front_value:
                if the_end == -1:
                    the_end = end
                elif nums[end] > nums[the_end]:
                    the_end = end
                found = True
    if found:
        print("found", "front", front, "end", the_end)
        nums[front], nums[the_end] = nums[the_end], nums[front]

def go_to_min():
    found = False
    the_end = -1
    for front in range(length):
        front_value = nums[front]
        for end in range(length - 1, front, -1):
            if nums[end] == front_value:
                the_end = end
                found = True
                break
        if found:
            nums[front], nums[the_end] = nums[the_end], nums[front]

    if not found:
        # for front in range(length - 2, -1, -1):
        #     front_value = nums[front]
        #     for end in range(front + 1, length):
        nums[length - 2], nums[length - 1] = nums[length - 1], nums[length - 2]

T = int(input())
# for tc in range(1, T + 1):
for tc in range(1, 2):
    nums, max_change = input().split()
    value_max = int(''.join(sorted(nums, reverse=True)))
    nums = list(map(int, list(nums)))
    max_change = int(max_change)

    length = len(nums)

    print(nums, max_change)
    print(value_max)

    times_changed = 0

    while times_changed != max_change:
        if list(str(value_max)) != nums:
            print("not max")
            go_to_max()
            print(nums)
        else:
            print("max")
            go_to_min()
        times_changed += 1

    print(f"#{tc} {''.join(map(str, (nums)))}")

    # print()