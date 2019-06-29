turn = 0
def play(conn, gameData):
    global turn
    if turn == 0:
        angle = 49
        power = 140
    elif turn == 1:
        angle = 280
        power = 70
    elif turn == 2:
        angle = 100
        power = 50
    elif turn == 3:
        angle = 196
        power = 110
    elif turn == 4:
        angle = 160
        power = 40
    turn += 1
    conn.send(angle, power)