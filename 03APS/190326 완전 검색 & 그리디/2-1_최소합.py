import sys
sys.stdin = open('2-1.txt', 'r')

dx = [0, 1]
dy = [1, 0]


def dfs(s, curr_sum):
    global min_sum
    s_row = s[0]
    s_col = s[1]
    if s_row == N_side - 1 and s_col == N_side - 1:
        min_sum = curr_sum
    for i in range(2):
        c_row = s_row + dx[i]
        c_col = s_col + dy[i]
        if c_row < N_side and c_col < N_side and curr_sum + mat[c_row][c_col] < min_sum:
            dfs([c_row, c_col], curr_sum + mat[c_row][c_col])


T = int(input())
for tc in range(1, T + 1):
    N_side = int(input())
    mat = [0] * N_side
    for i in range(N_side):
        mat[i] = list(map(int, input().split()))
    # for i in mat:
    #     print(i)
    # print()

    min_sum = 100000000
    dfs([0, 0], mat[0][0])

    print(f"#{tc} {min_sum}")