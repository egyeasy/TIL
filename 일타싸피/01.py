turn = 0
def play(conn, gameData):
    global turn
    if turn == 0:
        angle = 75
        power = 100

    turn += 1
    conn.send(angle, power)