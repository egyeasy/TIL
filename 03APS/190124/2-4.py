import sys
sys.stdin = open("2-4.txt", "r")

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    nums = list(map(int, input().split()))

    cnt = 0

    start = 0

    max_idx = 0
    min_idx = 0

    while cnt < 10:
        for i in range(cnt, len(nums)):
            max_idx = cnt
            min_idx = cnt
            if cnt % 2 == 0:
                if nums[i] > nums[max_idx]:
                    nums[i], nums[max_idx] = nums[max_idx], nums[i]
                    max_idx = i

            else:
                if nums[i] < nums[min_idx]:
                    nums[i], nums[min_idx] = nums[min_idx], nums[i]
                    min_idx = i

        cnt += 1

    result = ' '.join([str(i) for i in nums[:10]])

    print(f"#{tc} {result}")
