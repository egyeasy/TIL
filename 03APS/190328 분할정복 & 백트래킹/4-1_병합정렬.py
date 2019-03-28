import sys
sys.stdin = open('4-1.txt', 'r')


def part_sort(alist):
    global cnt
    length = len(alist)
    if length == 1:
        return alist
    if length == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]
            cnt += 1
        return alist
    # elif length == 3:
    #     if alist
    else:
        mid = length // 2
        left = part_sort(alist[:mid])
        right = part_sort(alist[mid:])
    mid = length // 2
    len_left = mid
    len_right = length - mid
    if left[-1] > right[-1]:
        # print(left, right)
        # print(left[-1], right[-1])
        # print()
        cnt += 1
    merged_list = [0] * (len_left + len_right)
    merged_idx = 0
    i = 0
    j = 0
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged_list[merged_idx] = left[i]
            i += 1
            merged_idx += 1
        else:
            merged_list[merged_idx] = right[j]
            j += 1
            merged_idx += 1
    if i < len_left:
        merged_list[merged_idx:] = left[i:]
    if j < len_right:
        merged_list[merged_idx:] = right[j:]
    return merged_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    # print(nums)
    result = part_sort(nums)

    print(f"#{tc} {result[N // 2]} {cnt}")
    # print(result)