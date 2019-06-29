# Brute Foce 구현

t = "abcdefgheuckrr"
p = "euckr"


def brute_force(t, p):
    idx = 0
    for i in t:
        if i == p[0] and len(t) - idx >= len(p):
            print(i)
            for j in range(1, len(p)):
                print(t[idx+j], p[j])
                if t[idx+j] != p[j]:
                    break
            else:
                return idx
        idx += 1
    else:
        return -1

print(brute_force(t, p))


def brute_force2(t, p):
    idx = 0