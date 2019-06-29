turn = 0
def play(conn, gameData):
    global turn
    if turn == 0:
        angle = 88
        power = 140
    elif turn == 1:
        angle = 190
        power = 70
    elif turn == 2:
        angle = 133
        power = 80
    elif turn == 3:
        angle = 145
        power = 90
    elif turn == 4:
        angle = 134
        power = 140
    turn += 1
    conn.send(angle, power)