import sys
sys.stdin = open('01.txt', 'r')


def QuickSort(arr, l, r):
    if l < r:
        s = LomutoPartition(arr, l, r)
        # print(arr)
        # print()
        QuickSort(arr, l, s - 1)
        QuickSort(arr, s + 1, r)


def HoarePartition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
            # if i > j:
            #     break
        while i <= j and arr[j] >= p:
            j -= 1
            # if i > j:
            #     break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def LomutoPartition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(nums)
    QuickSort(nums, 0, len(nums) - 1)
    print(nums)
    print()