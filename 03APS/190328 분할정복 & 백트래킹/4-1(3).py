import sys
sys.stdin = open('4-1.txt', 'r')


def part_sort(alist, l, r):
    # length = len(alist)
    if r - l == 1:
        return alist
    else:
        mid = (l + r) // 2
        left = part_sort(alist, l, mid)
        right = part_sort(alist, mid, r)
        merged = merge(left, right, l, mid, r)
        print(merged)
        return merged


def merge(left, right, l, mid, r):
    global cnt
    len_left = mid - l
    len_right = r - mid
    # print("left", left, "right", right, l, mid, r)
    if left[mid - 1] > right[r - 1]:
        # print(left, right)
        # print(left[-1], right[-1])
        # print()
        cnt += 1
    # merged_list = [0] * (len_left + len_right)
    # merged_idx = 0
    merged_list = nums[:]
    merged_idx = l
    i = l
    j = mid
    while i < mid and j < r:
        if left[i] <= right[j]:
            merged_list[merged_idx] = left[i]
            i += 1
            merged_idx += 1
        else:
            merged_list[merged_idx] = right[j]
            j += 1
            merged_idx += 1
    while i < mid:
        merged_list[merged_idx] = left[i]
        i += 1
        merged_idx += 1
    while j < r:
        merged_list[merged_idx] = right[j]
        j += 1
        merged_idx += 1
    # print("merged list", merged_list)
    # print(nums)
    return merged_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    # print(nums)
    result = part_sort(nums, 0, N)

    print(f"#{tc} {result[N // 2]} {cnt}")
    # print(result)