import sys
sys.stdin = open("2-2.txt", "r")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(a)

subset = []

for i in range(1 << n):
    elements = []
    for j in range(n):
        if i & (1 << j):
           elements.append(a[j])
    subset.append(elements)

T = int(input())

for tc in range(1, T+1):
    n, k = list(map(int, input().split()))

    cnt = 0

    for sub in subset:
        sub_sum = 0
        if len(sub) == n:
            for s in sub:
                sub_sum += s
            if sub_sum == k:
                cnt += 1

    print(f"#{tc} {cnt}")