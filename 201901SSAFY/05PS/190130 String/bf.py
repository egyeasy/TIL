t = "abcduf"
p = "du"
N = len(t)
M = len(p)


def BruteForce(t, p):
    i = 0
    j = 0

    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return t[i], i - M
    else:
        return -1

print(BruteForce(t, p))