import sys
sys.stdin = open('sudoku.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    mat = [0] * 9
    for i in range(9):
        mat[i] = list(map(int, input().split()))

    # for i in mat:
    #     print(i)

    judge = 1

    for i in range(9):
        results = [[] for k in range(3)]
        results[0] = mat[i]
        for j in range(9):
            results[1].append(mat[j][i])
            results[2].append(mat[j // 3 + (i // 3) * 3][j % 3 + (i % 3) * 3])
        for j in range(3):
            if len(set(results[j])) != 9:
                judge = 0
                break
        if not judge:
            break
    
    print(f"#{tc} {judge}")