import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n, length = input().split()
    series = list(input().split())
    counts = [0] * 10
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in series:
        in_idx = 0
        for num in nums:
            if i == num:
                counts[in_idx] += 1
            in_idx += 1

    print(f"#{tc}", end =" ")

    idx = 0
    for num in nums:
        total = counts[idx]
        for i in range(total):
            print(num, end = " ")
        idx += 1

