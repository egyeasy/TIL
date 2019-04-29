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
    elif turn == 5:
        angle = 140
        power = 50
    elif turn == 6:
        angle = 76
        power = 30
    elif turn == 7:
        angle = 165
        power = 50
    elif turn == 8:
        angle = 130
        power = 40
    elif turn == 9:
        angle = 358
        power = 150
    elif turn == 10:
        angle = 59
        power = 80
    elif turn == 11:
        angle = 150
        power = 20
    elif turn == 12:
        angle = 3
        power = 20

    turn += 1
    conn.send(angle, power)