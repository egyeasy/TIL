# pf 코드 참조
import sys
sys.stdin = open('02.txt', 'r')

def hexa_to_deci(chr):
    if chr == 'A':
        return 10
    elif chr == 'B':
        return 11
    elif chr == 'C':
        return 12
    elif chr == 'D':
        return 13
    elif chr == 'E':
        return 14
    elif chr == 'F':
        return 15
    else:
        return int(chr)

hexas = input()
len_hexas = len(hexas)
bins = ""
value = 0
idx = 0
for i in range(len_hexas):
    num = hexa_to_deci(hexas[i])
    bin = ""
    for j in range(4):
        bin += str(num % 2)
        value = value * 2 + num % 2
        idx += 1
        num //= 2
        if idx % 7 == 0:
            print(value, end=" ")
            value = 0
    # print(bin)
    bins += bin

print()

print(bins)