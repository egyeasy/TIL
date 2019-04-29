turn = 0
def play(conn, gameData):
    global turn
    if turn == 0:
        angle = 50
        power = 60
    elif turn == 1:
        angle = 90
        power = 100
    elif turn == 2:
        angle = 173
        power = 90

    turn += 1
    conn.send(angle, power)