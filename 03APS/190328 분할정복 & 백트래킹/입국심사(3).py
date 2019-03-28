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
    # print("simsas", simsas)

    # boonmo = 0
    # for simsa in simsas:
    #     boonmo += all_multiply // simsa
    # print(all_multiply)
    #
    # time = ((M_people * all_multiply) / boonmo)
    #
    # print(time)

    time = 0
    divided = M_people // all_multiply
    l = divided * all_multiply
    r = (divided + 1) * all_multiply
    # print(l, r)
    min_overdone = 100000000000000000000
    former_time = 0
    while True:
        if l > r:
            time += 1
            break
        time = (l + r) // 2
        # if time == former_time:
        #     time += 1
        #     break
        cnt_done = 0
        # if time > 7:
        # print(time, l, r)
        pass_judge = False
        for simsa in simsas:
            cnt_done += time // simsa
            if cnt_done - M_people > min_overdone:
                pass_judge = True
                break
        if pass_judge:
            r = time - 1
            continue
        over_done = cnt_done - M_people
        if over_done == 0:
            break
        elif over_done > 0:
            if over_done < min_overdone:
                min_overdone = over_done
            r = time - 1
        else:
            l = time + 1
        former_time = time

    print(f"#{tc} {time}")