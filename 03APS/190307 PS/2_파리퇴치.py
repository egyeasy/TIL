import sys
sys.stdin = open('2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            this_sum = 0
            for k in range(M):
                this_sum += sum(mat[i+k][j:j+M])
            # print(this_sum)
            if this_sum > max_sum:
                max_sum = this_sum

    print("#{}".format(tc), max_sum)