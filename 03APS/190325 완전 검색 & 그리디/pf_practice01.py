arr = [5, 4, 3, 2, 1]

def SelSort(A, n):
    if n == 1:
        return 0
    minn = SelSort(A, n - 1)
    if A[n] > A[minn]:
        swap(A[n], A[min])
    else:
        minn = n
    return minn