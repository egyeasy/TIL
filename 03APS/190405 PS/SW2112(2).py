import sys
sys.stdin = open('2112.txt', 'r')


from itertools import combinations

def backtrack(row_idx, cnt_change):
    global min_changed
    if cnt_change == total_change:
        if judge_done() and cnt_change < min_changed:
            min_changed = cnt_change
        return
    if arr_change[row_idx]:
        # print(arr_change, row_idx, cnt_change)
        backup = mat[row_idx][:]
        mat[row_idx] = [0] * W_col
        backtrack(row_idx + 1, cnt_change + 1)
        mat[row_idx] = [1] * W_col
        backtrack(row_idx + 1, cnt_change + 1)
        mat[row_idx] = backup
    else:
        backtrack(row_idx + 1, cnt_change)


def judge_done():
    for j in range(W_col):
        # 바꿔야 하는지 여부 검사
        have_to_change = True
        for i in range(D_row):
            # 0 또는 1이 이어질 때
            for value in range(2):
                if mat[i][j] == value and i + k_limit - 1 < D_row:
                    # 해당 위치부터 아래로 가면서 k개가 연속되는지 본다
                    for go_i in range(i + 1, i + k_limit):
                        if mat[go_i][j] != value:
                            break
                    else:
                        have_to_change = False
            if not have_to_change:
                break
        # 바꿔야 하는 경우 후보군 탐색
        if have_to_change:
            break
    if have_to_change:
        return False
    else:
        return True

T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    D_row, W_col, k_limit = map(int, input().split())
    mat = [0] * D_row
    to_change = [[-1] * W_col for _ in range(D_row)]

    for i in range(D_row):
        mat[i] = list(map(int, input().split()))

    min_changed = D_row
    for i in range(0, D_row):
        arr_change = [0] * D_row
        for j in range(D_row):
            if i & (1 << j):
                arr_change[j] = 1
        # print(arr_change)
        # 행 백업
        total_change = sum(arr_change)
        backup = [0] * D_row
        for i_row in range(D_row):
            if arr_change[i_row]:
                backup[i_row] = mat[i_row][:]
        # if arr_change == [0, 0, 1, 0, 0, 1]:
        #     print(backup)
        backtrack(0, 0)
        for i in range(D_row):
            if arr_change[i]:
                mat[i] = backup[i]


    print(f"#{tc} {min_changed}")


