import sys
sys.stdin = open("input.txt", "r")

def makeline(line):
    if len(line) < 2 : return line
    tt = []
    while len(line):
        if 2 <= len(line) and line[0] == line[1]:
            tt.append(line.pop(0) + line.pop(0))
        else:
            tt.append(line.pop(0))
    return tt

def update():
    t = []
               
    if S == 'left':
        for i in range(N):
            for j in range(N):
                if mat[i][j] != 0:
                    t.append(mat[i][j])
                mat[i][j] = 0
            t = makeline(t)
            for j in range(len(t)):
                mat[i][j] = t.pop(0)

    if S == 'right':
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if mat[i][j] != 0:
                    t.append(mat[i][j])
                mat[i][j] = 0
            t = makeline(t)
            for j in range(len(t)):
                mat[i][N - j - 1] = t.pop(0)

    if S == 'up':
        for j in range(N):
            for i in range(N):
                if mat[i][j] != 0:
                    t.append(mat[i][j])
                mat[i][j] = 0
            t = makeline(t)
            for i in range(len(t)):
                mat[i][j] = t.pop(0)

    if S == 'down':
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if mat[i][j] != 0:
                    t.append(mat[i][j])
                mat[i][j] = 0
            t = makeline(t)
            for i in range(len(t)):
                mat[N - i - 1][j] = t.pop(0)

TC = int(input())
for tc in range(1, TC + 1):
    N, S = input().split()
    N = int(N)

    mat = [list(map(int, input().split())) for i in range(N) ]

    update()
    print('#%d'%tc)
    for i in range(N):
        for x in mat[i]:print(x, end = ' ')
        print()

