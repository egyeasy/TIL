import sys
sys.stdin = open("input.txt", "r")

code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

TC = int(input())
for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))

    mat = ['' for i in range(N)]
    for i in range(N):
        mat[i] = input()

    for i in range(N):
        px = i
        py = mat[i][::-1].find('1')
        if py != -1: break

    py = M - py - 56

    tcode = [0] * 8
    for i in range(8):
        tcode[i] = code.get(mat[px][py:py+7])
        py += 7

    tvc = (tcode[0] + tcode[2] + tcode[4] + tcode[6]) * 3 + tcode[1] + tcode[3] + tcode[5] + tcode[7]


    if not tvc % 10 :
        print("#%d" % tc, sum(tcode))
    else:
        print("#%d" % tc, 0)






