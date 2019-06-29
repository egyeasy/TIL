import sys
sys.stdin = open('5-2.txt', 'r')


def backtrack(arr, k, part_sum):
    global min_sum
    if k == N:
        if part_sum < min_sum:
            min_sum = part_sum
        return
    else:
        # print(arr, k, mat[k], "partsum", part_sum)
        k += 1
        cands = make_cands(arr, k)
        for i in cands:
            if part_sum + mat[k - 1][i] < min_sum:
                arr[k] = i + 1
                backtrack(arr, k, part_sum + mat[k - 1][i])
                arr[k] = 0


def make_cands(arr, k):
    in_perms = [0] * N
    cands = []

    for i in range(1, k):
        if arr[i]:
            in_perms[arr[i] - 1] = 1

    for i in range(N):
        if not in_perms[i]:
            cands.append(i)

    # print("cands", cands)

    return cands


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    min_sum = 10000000000
    arr = [0] * (N + 1)
    backtrack(arr, 0, 0)
    print(f"#{tc} {min_sum}")