def selSort(n):
    if n == (len(inp)-1) :
        return

    minVal = inp[n]
    for i in range(n+1, len(inp)):
        if inp[i] < minVal:
            minVal = inp[i]
            mIdx = i

    temp = inp[n]
    inp[n] = inp[mIdx]
    inp[mIdx] = temp

    selSort(n + 1)

    return

inp = list(map(int, input().split()))
selSort(0)
print(inp)
