
def backtrack(ary, k, n, sum):
    if sum > 10:
        return
    if k == n:  #process solution
        if sum == 10:
            for j in range(n):
                if chk[j]:
                    print(ary[j], end = " ")
            print()
        return

    k += 1
    cand = [0,1]  # make_candidates

    for i in range(2):
        chk[k-1] = cand[i]  #make candidates
        if cand[i]:
            backtrack(ary, k, n, sum+ary[k-1])
        else:
            backtrack(ary, k, n, sum)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chk = [0]*10
backtrack(arr, 0, 10, 0)