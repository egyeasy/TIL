def partitionL(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1

def partitionH(arr, L, R):
    p= L
    i=L
    j=R

    while i < j:
        while i < R and arr[i] <= arr[p]: i += 1
        while j > L and arr[j] >= arr[p]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]

    return j

def qsort(arr, L, R):
    if L < R:
        #p= partitionH(arr, L, R)
        p= partitionL(arr, L, R)
        qsort(arr, L, p-1)
        qsort(arr, p+1, R)

#ary = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
ary = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

qsort(ary, 0, len(ary)-1)
print(ary)

