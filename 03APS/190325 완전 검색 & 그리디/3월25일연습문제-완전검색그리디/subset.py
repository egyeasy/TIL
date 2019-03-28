import time
import itertools

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

def combi(n,r):
    global subset
    if r == 0:
        if len(subset) > 0:
            sum = 0
            for i in range(len(subset)):
                sum += subset[i]
            if sum == 0:
                print(subset)
        return
    elif n < r:
        return
    else:
        subset[r-1] = arr[n - 1]
        combi(n-1, r-1)
        combi(n-1, r)

        return

stime = time.time()
N = len(arr)
for i in range(1, (1<<N)):
    subset = []
    sum = 0
    for j in range(0,N):
        if i & (1<<j):
            subset.append(arr[j])
            sum += arr[j]

    if sum == 0 : print(subset)

etime = time.time()

print(etime - stime, " recursive function \n")
stime = time.time()
for i in range(1, N):
    subset = [0]* i
    combi(N,i)

etime = time.time()
print(etime - stime, " using combinations function \n")
stime = time.time()
setList =[]
for i in range(1,N+1):
    subset = list(itertools.combinations(arr,i))
    for j in range(len(subset)):
        sum = 0
        subset[j] = list(subset[j])
        for k in range(len(subset[j])):
            sum += subset[j][k]

        if sum == 0:
            print(subset[j])

etime = time.time()
print(etime - stime)