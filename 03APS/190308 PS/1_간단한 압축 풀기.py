import sys
sys.stdin = open('1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    all = ""
    print("#{}".format(tc))
    cnt = 0
    for i in range(N):
        alpha, num = input().split()
        num = int(num)
        for j in range(num):
            print(alpha, end="")
            if (cnt + j) % 10 == 9:
                print()
        cnt += num
    print()

    # print("#{}".format(tc))
    # for i in range(len(all)):
    #     print(all[i], end="")
    #     if i != len(all) - 1 and i % 10 == 9:
    #         print()