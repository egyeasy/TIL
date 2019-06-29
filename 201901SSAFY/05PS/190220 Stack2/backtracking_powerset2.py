def powerset(a, k, max_input, summ):
    c = [True, False]
    if k == max_input:
        make_powerset(a)
    else:
        k += 1
        for i in c:
            a[k] = i
            if i:
                summ += k
                print(summ)
                if summ > 10:
                    return
                else:
                    powerset(a, k, max_input, summ)
            else:
                powerset(a, k, max_input, summ)

target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len_tar = len(target)
a = [0] * (len_tar + 1)

powerset(a, 0, 10, 0)