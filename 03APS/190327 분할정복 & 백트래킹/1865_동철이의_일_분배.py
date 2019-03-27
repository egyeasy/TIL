import sys
sys.stdin = open('1865.txt', 'r')


def BackTrack(arr, k, max_input, curr_prob):
    global max_prob
    if k == max_input:
        if curr_prob > max_prob:
            max_prob = curr_prob
            # print(arr)
    else:
        k += 1
        n_cands = make_cands(arr, k, max_input)
        print()
        print(arr, n_cands, cands)
        for i in range(n_cands):
            if curr_prob * (mat[k - 1][cands[i]] / 100) > max_prob:
                arr[k - 1] = cands[i]
                print("curr_prob", curr_prob, (mat[k - 1][cands[i]] / 100))
                BackTrack(arr, k, max_input, curr_prob * (mat[k - 1][cands[i]] / 100))

def make_cands(arr, k, max_input):
    global cands
    in_perm = [0] * N
    cands = [0] * N

    for i in range(k - 1):
        in_perm[arr[i]] = 1

    n_cands = 0
    for i in range(N):
        if not in_perm[i]:
            cands[n_cands] = i
            n_cands += 1
    return n_cands



T = int(input())
# for tc in range(1, T + 1):
for tc in range(1, 3):
    N = int(input())
    mat = [0] * N

    for i in range(N):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)

    arr = [0] * N
    # visited = [0] * N
    found = False
    cands = [0] * N
    max_prob = 0
    BackTrack(arr, 0, N, 1)
    print(f"#{tc} {max_prob}")