import sys
sys.stdin = open('2112.txt', 'r')


def judge_change():
    need_changes = [True] * W_col
    for j in range(W_col):
        # 바꿔야 하는지 여부 검사
        judge_change = True
        for i in range(D_row):
            # 0 또는 1이 이어질 때
            for value in range(2):
                if mat[i][j] == value and i + k_limit - 1 < D_row:
                    # 해당 위치부터 아래로 가면서 k개가 연속되는지 본다
                    for go_i in range(i + 1, i + k_limit):
                        if mat[go_i][j] != value:
                            break
                    else:
                        judge_change = False
            if not judge_change:
                need_changes[j] = False
                break
        # 바꿔야 하는 경우 후보군 탐색
        if judge_change:
            pass



T = int(input())
for tc in range(1, T + 1):
    D_row, W_col, k_limit = map(int, input().split())
    mat = [0] * D_row
    to_change = [[-1] * W_col for _ in range(D_row)]

    for i in range(D_row):
        mat[i] = list(map(int, input().split()))

    judge_change()

