import sys
sys.stdin = open('5-3.txt', 'r')

def merge(alist):
    i = 0
    j = len(alist) - 1
    if j == 0:
        return [alist[0]]
    if j == 1:
        if alist[0][1] == alist[1][1] + 1 or alist[0][1] == alist[1][1] - 2 or alist[0][1] == alist[1][1]:
            return [alist[0]]
        else:
            return [alist[1]]
    else:
        mid = (i + j)//2 + 1
        return merge(merge(alist[:mid]) + merge(alist[mid:]))

T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    text = list(map(int, input().split()))
    # print(text)
    for i in range(m):
        text[i] = (i+1, text[i])
    # print(text)

    result = merge(text)
    # print(result)
    print(f"#{tc} {result[0][0]}")