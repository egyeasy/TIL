import sys
sys.stdin = open('8-3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    aline = list(map(int, input().split()))
    aline = [0] + aline
    # print(aline)
    for i in range(1, N + 1):
        while i > 1:
            item = aline[i]
            if item < aline[i // 2]:
                aline[i // 2], aline[i] = item, aline[i // 2]
                i //= 2
            else:
                break
    #         print(aline)
    #     print()
    # print(aline)
    idx = N
    result = 0
    while idx != 1:
        idx //= 2
        result += aline[idx]

    print("#{}".format(tc), result)