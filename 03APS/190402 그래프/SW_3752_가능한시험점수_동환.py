TC = int(input())
for tc in range(1, 1 + TC):
    n = int(input())
    num_lists = list(map(int, input().split()))
    max_range = sum(num_lists) + 1
    result_lists = [0] * max_range
    result_lists[0] = 1

    for a in range(n):
        temp = result_lists[:]
        for b in range(max_range):
            if temp[b] == 1:
                if b + num_lists[a] < max_range:
                    result_lists[b + num_lists[a]] = 1

    print("#{} {}".format(tc, sum(result_lists)))