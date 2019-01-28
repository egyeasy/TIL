import sys
sys.stdin = open("2-sc.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    series = list(map(int, input().split()))
    num_list = []
    for i in range(n):
        num_list.append([series[2*i], series[2*i+1]])

    k = len(num_list)
    origin = num_list[:]


    for j in range(k):
        num_list = origin[:]
        num_list = [num_list[j]] + num_list[:j] + num_list[j+1:]
        i = 0

        while True:
            num = num_list[0]
            rest = num_list[:0] + num_list[1:]
            # print("num_list: ", num_list, rest)
            # print("i, len-1: ", i, len(num_list) - 1)
            # if i >= len(rest):
            #     break
            if len(num_list) == 1:
                break
            for m in range(len(rest)):
                if num[-1] == rest[m][0]:
                    num_list = [num + rest.pop(m)] + rest
                    break
                if num[0] == rest[m][-1]:
                    num_list = [rest.pop(m) + num] + rest
                    break
            i += 1

        if j == 0:
            max_num = len(num_list[0])
            max_series = list(map(str, num_list[0]))
        else:
            if len(num_list[0]) > max_num:
                max_num = len(num_list[0])
                max_series = list(map(str, num_list[0]))

    print(f"#{tc} {' '.join(max_series)}")
