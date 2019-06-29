import sys
sys.stdin = open("input.txt", "r")

def check(x, y):
    if x < 0 or x > 99 : return False
    if y < 0 or y > 99 : return False

    if mat[x][y] : return True
    else : return False

def solve( ):
    tmin = 1234567890
    ansidx = 0

    for i in range(100):
        if mat[0][i] :
            y = i
            x = 0
            cnt = 0
            d = 0       # -1(왼쪽), 0(아래), 1(오른쪽)

            while x < 100 :
                if   ((d == 0 or d == -1) and check(x, y - 1)) : d = -1; y -= 1; cnt += 1
                elif ((d == 0 or d ==  1) and check(x, y + 1)) : d =  1; y +=1; cnt += 1
                else :	d = 0; x += 1

            if tmin >= cnt :
                tmin = cnt
                ansidx = i

    return ansidx



for tc in range(1, 11):
    input()
    mat = [0] * 100
    for i in range(100):
        mat[i] = list(map(int, input().split()))

    print('#%d'%tc, solve( ))