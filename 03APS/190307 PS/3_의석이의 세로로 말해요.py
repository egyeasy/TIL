import sys
sys.stdin = open('3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    mat = [[0] * 15 for _ in range(15)]
    for i in range(5):
        aline = list(input())
        leng = len(aline)
        for j in range(15):
            if j < leng:
                mat[i][j] = aline[j]
    # for i in mat:
    #     print(i)
    print("#{}".format(tc), end=" ")
    for i in range(15):
        for j in range(15):
            if mat[j][i]:
                print(mat[j][i], end="")

    print()