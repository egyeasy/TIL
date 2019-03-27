import sys
sys.stdin = open('1865.txt', 'r')


def BackTrack(arr, k, curr_prob):
    global max_prob
    # print("arr", arr, "k", k, "curr_prob", curr_prob)
    if len(arr) == N:
        if curr_prob > max_prob:
            max_prob = curr_prob
    else:
        k += 1
        for i in range(N):
            if i not in arr and curr_prob * (mat[k - 1][i] / 100) > max_prob:
                BackTrack(arr + [i], k, curr_prob * (mat[k - 1][i] / 100))
                


T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 5):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)

    arr = []
    max_prob = 0
    # visited = []
    BackTrack(arr, 0, 1)
    result = max_prob * 100
    # print(result)
    print(f"#{tc} {round(result, 6):.6f}")