import sys
sys.stdin = open('01.txt', 'r')

series = input()
length = len(series)
for i in range(length // 7):
    result = 0
    for j in range(6, -1, -1):
        result += int(series[i * 7 + (6 - j)]) * 2 ** j
    print(result, end=" ")
print()
