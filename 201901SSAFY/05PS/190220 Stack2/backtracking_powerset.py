def make_powerset(a):
    global target
    result = [0] * len(target)
    idx = 0
    for i in range(1, len(a)):
        if a[i]:
            result[idx] = target[i-1]
            idx += 1
    the_sum = 0
    for i in result:
        the_sum += i
        if the_sum > 10:
            return
    if the_sum == 10:
        print(result)


def powerset(a, k, max_input):
    c = [True, False]
    if k == max_input:
        make_powerset(a)
    else:
        k += 1
        for i in c:
            a[k] = i
            powerset(a, k, max_input)

target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len_tar = len(target)
a = [0] * (len_tar + 1)

powerset(a, 0, 10)