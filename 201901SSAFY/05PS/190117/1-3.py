# import sys
# sys.stdin = open("input1-3.txt", "r")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    alist = input()
    c = [0]*10
    for a in alist:
        c[int(a)]  += 1
    maxx = 0
    max_cnt = 0
    for num, cnt in enumerate(c):
        if cnt >= max_cnt:
            maxx = num
            max_cnt = cnt
    print(f"#{t} {maxx} {max_cnt}")