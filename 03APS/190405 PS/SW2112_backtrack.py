import sys
sys.stdin = open('2112.txt', 'r')

import copy

def judge_visited(i, j_col):
    pass

def backtrack(j_col, cnt_changed, visited):
    global min_changed
    # max 도달했을 때 체크
    if j_col == W_col:
        if cnt_changed < min_changed:
            min_changed = cnt_changed
        return
    # 해당 줄이 멀쩡한지 체크

    # 해당 열에서 k개의 연속된 것을 0 또는 1로 만들어서 넘김
    # 바꾼 줄이 선택되지 않도록 방지
    for i in range(D_row - (k_limit - 1)):
        if visited[i: i + k_limit] == [0] * k_limit:
            # 해당 열 원래 상태 백업
            # 아래 행은 다음 번부터 바꾸지 않는다
            visited[i: i + k_limit] = [1] * k_limit
            # 두 가지 A, B에 대해
            for color in range(2):
                # 행 색깔 바꿔서 다음 열로 넘기기
                backup_rows = [mat[arow][:] for arow in range(i, i + k_limit)]
                this_turn_changed = 0
                for k in range(i, i + k_limit):
                    # print(i, k, j_col)
                    if mat[k][j_col] != color:
                        mat[k] = [color] * W_col
                        this_turn_changed += 1

                backtrack(j_col + 1, cnt_changed + this_turn_changed, visited)
                # 이전 상태 복원
                visited[i: i + k_limit] = [0] * k_limit
                mat[i: i + k_limit] = backup_rows


T = int(input())
for tc in range(1, T + 1):
    D_row, W_col, k_limit = map(int, input().split())
    mat = [0] * D_row
    to_change = [[-1] * W_col for _ in range(D_row)]

    for i in range(D_row):
        mat[i] = list(map(int, input().split()))

    # 해당 줄을 바꿨는지 여부
    visited = [-1] * D_row
    min_changed = D_row
    # print(f"#{tc} D_row {D_row} W_col {W_col}")
    backtrack(0, 0, visited)

    print(f"#{tc} {min_changed}")

