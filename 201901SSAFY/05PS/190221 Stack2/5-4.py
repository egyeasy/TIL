import sys
sys.stdin = open('5-4.txt', 'r')

def backt(a, k, max_input, pre_sum):
    global m, min_sum
    c = [0] * m
    if k == max_input:
        the_sum = 0
        for i in range(m):
            the_sum += matrix[i][a[i + 1]]
        if the_sum < min_sum:
            # print(a)
            min_sum = the_sum
        return
    else:
        k += 1
        # print(a)
        ncandidates = construct_candidates(a, k, max_input, c)
        for i in range(ncandidates):
            the_value = matrix[k - 1][c[i]]
            if pre_sum >= min_sum:
                return
            else:
                a[k] = c[i]
                backt(a, k, max_input, pre_sum + the_value)

def construct_candidates(a, k, max_input, c):
    in_perm = [False] * max_input

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(0, max_input):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    matrix = [0] * m
    visited = [0] * m

    for i in range(m):
        aline = list(map(int, input().split()))
        matrix[i] = aline
    # print(matrix)

    a = [0] * (m + 1)
    min_sum = 10000000000000000000
    backt(a, 0, m, 0)


    print(f"#{tc} {min_sum}")