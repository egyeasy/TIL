import sys
sys.stdin = open("1.txt", "r")

T = int(input())

def my_len(alist):
    cnt = 0
    for i in alist:
        cnt += 1
    return cnt

for tc in range(1, T+1):
    p = input()
    text = input()

    N = my_len(p)
    M = my_len(text)

    i = N - 1
    j = N - 1
    while i < M and j > -1:
        if text[i] != p[j]:
            for k in range(N-1, -1, -1):
                if p[k] == text[i]:
                    i += N - k
                    j = N
                    break
            else:
                i += N
        i -= 1
        j -= 1

    print(f"#{tc}", end=" ")

    if j == -1:
        print(1)
    else:
        print(0)