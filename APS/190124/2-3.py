import sys
sys.stdin = open("2-3.txt", "r")


def bin_search(page, target):
    start = 1
    end = page
    cnt = 1
    mid = int((start + end) / 2)


    while start <= end:
        if mid == target:
            return cnt

        elif mid < target:
            start = mid

        else:
            end = mid

        mid = int((start + end) / 2)
        cnt += 1


    if start > end:
        return 9999
    else:
        return cnt


T = int(input())

for tc in range(1, T+1):
    p, a_tar, b_tar = list(map(int, input().split()))

    a_result = bin_search(p, a_tar)
    b_result = bin_search(p, b_tar)

    if a_result == b_result:
        print(f"#{tc} 0")

    elif a_result < b_result:
        print(f"#{tc} A")

    else:
        print(f"#{tc} B")