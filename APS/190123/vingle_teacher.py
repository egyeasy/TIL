sorted_ary = [[0] * 5 for _ in range(5)]

ary = [list(reversed([1, 2, 3, 4, 5])), list(reversed([6, 7, 8, 9, 10])),
list(reversed([11, 12, 13, 14, 15])), list(reversed([16, 17, 18, 19, 20])),
list(reversed([21, 22, 23, 24, 25]))]

def sel_min():
    minX, minY = 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j
    min = ary[minX][minY]
    ary[minX][minY] = 99
    return min

# 중략


def isWall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    if sorted_ary[x][y] != 0: return True
    return False

X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0

for i in range(25):
    cur_min = sel_min()
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if isWall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4 # 여기가 중요한 듯
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]

for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=" ")
    print()