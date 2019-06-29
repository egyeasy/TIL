import sys
sys.stdin = open('3.txt', 'r')

def row_judge(i, j):
    # 해당칸만큼 비어있는지 체크
    for k in range(1, K):
        if not mat[i][j + k]:
            return False
    # 이전 칸이 막혀있는지 체크
    if j - 1 >= 0 and mat[i][j - 1]:
        return False
    # 다음 칸이 막혀있는지 체크
    if j + K < side_N and mat[i][j + K]:
        return False
    return True

def col_judge(i, j):
    for k in range(1, K):
        if not mat[i + k][j]:
            return False
    if i - 1 >= 0 and mat[i - 1][j]:
        return False
    if i + K < side_N and mat[i + K][j]:
        return False
    return True


T = int(input())
for tc in range(1, T + 1):
    side_N, K = map(int, input().split())
    mat = [0] * side_N
    for i in range(side_N):
        mat[i] = list(map(int, input().split()))

    total_cnt = 0
    for i in range(side_N):
        for j in range(side_N):
            if j < side_N - K + 1 and mat[i][j]:
                if row_judge(i, j):
                    # print("row", i, j)
                    total_cnt += 1
            if i < side_N - K + 1 and mat[i][j]:
                if col_judge(i, j):
                    # print("col", i, j)
                    total_cnt += 1
    print("#{}".format(tc), total_cnt)