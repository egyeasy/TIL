import sys
sys.stdin = open("3.txt", "r")


T = int(input())

for tc in range(1, T+1):
    p = input()
    text = input()
    counts = [0 for i in p]

    for i in text:
        in_idx = 0
        for j in p:
            if i == j:
                counts[in_idx] += 1
            in_idx += 1

    maxx = counts[0]
    for i in counts:
        if i > maxx:
            maxx = i

    print(f"#{tc} {maxx}")