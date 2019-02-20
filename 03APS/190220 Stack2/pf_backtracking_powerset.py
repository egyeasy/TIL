def backtrack(a, k, sum):
    global cnt
    cnt += 1
    if k == N:
        if sum == 10:
            for i in range(1, 11):
                if a[i] == True:
                    print(i, end=' ')
            print()
    else:
        k += 1
        # 가지치기 추가
        if sum + k <= 10:
            a[k] = 1; backtrack(a, k, sum + k)
        #
        # a[k] = 1; backtrack(a, k, sum + k) # 가지치기 없으면 이 줄 써야
        a[k] = 0; backtrack(a, k, sum)

N = 10
a = [0] * (N + 1)

cnt = 0
backtrack(a, 0, 0)
print("cnt : ", cnt)