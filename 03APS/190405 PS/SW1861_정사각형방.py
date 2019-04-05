import sys
sys.stdin = open('1861.txt', 'r')

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    N_side = int(input())
    mat = [0] * N_side
    for i in range(N_side):
        mat[i] = list(map(int, input().split()))


    max_num = N_side ** 2
    min_start_value = -1
    max_length = 0

    for i in range(N_side):
        for j in range(N_side):
            start_value = mat[i][j]
            if start_value + max_length - 1 <= max_num:
                # print(i, j)
                # print("visited")
                # # for k in visited_mat:
                # #     print(k)
                # print()
                curr_value = start_value
                curr_length = 1
                while True:
                    for dir in range(4):
                        c_row = i + dx[dir]
                        c_col = j + dy[dir]
                        if 0 <= c_row < N_side and 0 <= c_col < N_side and mat[c_row][c_col] == curr_value + 1:
                            curr_length += 1
                            curr_value += 1
                            i = c_row
                            j = c_col
                            break
                    else:
                        break
                if curr_length > max_length:
                    max_length = curr_length
                    min_start_value = start_value
                elif curr_length == max_length and start_value < min_start_value:
                    min_start_value = start_value

    print(f"#{tc} {min_start_value} {max_length}")





