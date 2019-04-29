turn = 0
def play(conn, gameData):
    global turn
    if turn == 0:
        angle = 75
        power = 100
    elif turn == 1:
        angle = 248
        power = 110

    turn += 1
    conn.send(angle, power)