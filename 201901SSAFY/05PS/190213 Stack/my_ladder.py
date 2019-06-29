import sys
sys.stdin = open("input.txt", "r")

def judge(po, dir):
    x = po[0]
    y = po[1]
    if dir == 0:
        if x == 0:
            return -1
        if y != 0 and matrix[x][y - 1] == '1':
            return 1
        elif y != 99 and matrix[x][y + 1] == '1':
            return 2
        else:
            return dir
    elif dir == 1 or dir == 2:
        if matrix[x - 1][y] == '1':
            return 0
        else:
            return dir

for t in range(1, 11):
    tc = input()

    matrix = [0]*100

    for i in range(100):
        row = input().split()
        matrix[i] = row

    for i in range(100):
        if matrix[99][i] == '2':
            point = [99, i]

    direction = 0

    row_direction = [-1, 0, 0]
    col_direction = [0, -1, 1]

    while direction != -1:
        point[0] += row_direction[direction]
        point[1] += col_direction[direction]
        direction = judge(point, direction)

    print(f"#{tc} {point[1]}")