import sys
sys.stdin = open('4-3.txt', 'r')


def binary_search(l, r, go_left):
    global total_cnt
    # print("l", l, "r", r)
    if l == r:
        if b_nums[l] in a_nums:
            # print(b_nums[l])
            total_cnt += 1
    elif l > r:
        return
    else:
        mid = (l + r) // 2
        if b_nums[mid] in a_nums:
            # print(b_nums[mid])
            total_cnt += 1
        if go_left:
            go_left = False
            binary_search(l, mid - 1, go_left)
        else:
            go_left = True
            binary_search(mid + 1, r, go_left)


T = int(input())
for tc in range(1, T + 1):
    M_b, N_a = map(int, input().split())
    b_nums = list(map(int, input().split()))
    a_nums = list(map(int, input().split()))

    b_nums.sort()
    a_nums.sort()

    total_cnt = 0
    is_left = True
    # first_mid = True
    binary_search(0, M_b - 1, is_left)
    is_left = False
    binary_search(0, M_b - 1, is_left)
    if b_nums[(M_b - 1) // 2] in a_nums:
        total_cnt -= 1
    print(f"#{tc} {total_cnt}")
    # print()