import sys
sys.stdin = open('rotate.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    mat = [[0] * m for i in range(m)]
    for i in range(m):
        aline = list(input().split())
        mat[i] = aline

    # for i in mat:
    #     print(i)
    print(f"#{tc}")

    for i in range(m):
        result = [''] * 3
        for j in range(m):
            result[0] += mat[m - j - 1][i]
            result[1] += mat[m - i - 1][m - j - 1]
            result[2] += mat[j][m - i - 1]
        print(' '.join(result))