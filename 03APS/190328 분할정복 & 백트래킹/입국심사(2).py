import sys
sys.stdin = open('입국심사.txt', 'r')

import math

T = int(input())
for tc in range(1, T + 1):
    N_simsa, M_people = map(int, input().split())
    simsas = [0] * N_simsa
    all_sum = 0
    all_multiply = 1
    for i in range(N_simsa):
        value = int(input())
        all_sum += value
        all_multiply *= value
        simsas[i] = value
    print("simsas", simsas)

    boonmo = 0
    for simsa in simsas:
        boonmo += all_multiply // simsa
    print(all_multiply)

    time = ((M_people * all_multiply) / boonmo)

    print(time)


    # while True:
    #     cnt_done = 0
    #     for simsa in simsas:
    #         cnt_done += time // simsa
    #     if cnt_done >= M_people:
    #         break
    #     time += 1



    print(f"#{tc} {time}")