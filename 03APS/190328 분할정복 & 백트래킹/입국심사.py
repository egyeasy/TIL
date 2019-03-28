import sys
sys.stdin = open('입국심사.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N_simsa, M_people = map(int, input().split())
    simsas = [0] * N_simsa
    for i in range(N_simsa):
        simsas[i] = int(input())

    time = 1
    n_times = 0
    while True:
        cnt_done = 0
        for simsa in simsas:
            cnt_done += (time * 10) // simsa
        if cnt_done >= M_people:
            break
        time *= 10
        n_times += 1

    for exp in range(n_times, -1, -1):
        while True:
            cnt_done = 0
            for simsa in simsas:
                cnt_done += (time + 10 ** exp) // simsa
            if cnt_done >= M_people:
                break
            time += 10 ** exp

    print(f"#{tc} {time + 1}")