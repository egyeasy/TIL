import sys
sys.stdin = open('1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    M = int(input())
    # mat = [0] * M
    mid = M // 2
    total_sum = 0
    for i in range(M):
        aline = [int(j) for j in input()]

        if i <= mid:
            total_sum += sum(aline[mid - i:mid + i + 1])
        else:
            total_sum += sum(aline[mid - (M - 1 - i):mid + (M - 1 - i) + 1])

    # for i in mat:
    #     print(i)

    print(total_sum)
