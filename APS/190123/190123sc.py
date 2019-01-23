import sys
sys.stdin = open("input.txt", "r")


for t in range(1, 11):
    tc = int(input())
    arr = []

    for i in range(100):
        arr.append(list(map(int, input().split())))

    col_sum = [0 for i in range(100)]

    dig_sum1 = 0
    dig_sum2 = 0

    for i in range(len(arr)):
        row_sum = 0
        for j in range(len(arr[0])):
            if i == j:
                dig_sum1 += arr[i][j]
            if i+j == len(arr) - 1:
                dig_sum2 += arr[i][j]
            row_sum += arr[i][j]
            col_sum[j] += arr[i][j]
        if i == 0:
            row_max = row_sum
        elif row_sum > row_max:
            row_max = row_sum


    total_sum = col_sum + [row_max, dig_sum1, dig_sum2]
    maxx = total_sum[0]
    for i in total_sum:
        if i > maxx:
            maxx = i

    print(f"#{tc} {maxx}")