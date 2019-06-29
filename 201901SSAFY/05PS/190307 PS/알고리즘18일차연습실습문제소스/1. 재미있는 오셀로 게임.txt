import sys
sys.stdin = open("input.txt", "r")

def makeboard(n):
    # 1 : black, 2 : white
    if n == 4:
        b = [[0, 0, 0, 0], [0, 2, 1, 0], [0, 1, 2, 0], [0, 0, 0, 0] ]
    if n == 6:
        b = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    if n == 8:
        b = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 1, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    return b

def updateboard(x, y, dol):
    global board
    board[y][x] = dol
    for i in range(8):
        newX, newY = x + dx[i], y + dy[i]
        while 0 <= newX < N and 0 <= newY < N and board[newY][newX] != 0 and board[newY][newX] != dol:
            newX, newY = newX + dx[i], newY + dy[i]

        if 0 <= newX < N and 0 <= newY < N and board[newY][newX] == dol:
            newX, newY = x + dx[i], y + dy[i]
            while 0 <= newX < N and 0 <= newY < N and board[newY][newX] != dol:
                board[newY][newX] = dol
                newX, newY = newX + dx[i], newY + dy[i]




dx = [ 0,  1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1,  1,  0, -1]

TC = int(input())
for tc in range(1, TC + 1):
    N, roundcnt = list(map(int, input().split()))

    board = makeboard(N)

    for i in range(roundcnt):
        x, y, dol = list(map(int, input().split()))
        updateboard(x - 1, y - 1, dol)

    cnt1 = cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 : cnt1 += 1
            if board[i][j] == 2 : cnt2 += 1

    print("#%d"%tc, cnt1, cnt2)






