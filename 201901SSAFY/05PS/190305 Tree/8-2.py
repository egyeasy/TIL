import sys
sys.stdin = open('8-2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = 0
    while 2 ** n - 1 < N:
        n += 1
    n -= 1

    diff = N - (2 ** n - 1)
    # leaf 노드는 1, 3, 5, 7, 9, ...
    leaf = diff * 2 - 1

    print("#{}".format(tc), end=" ")

    # 왼쪽 서브트리가 포화될 때까지 루트 += 1(개수를 늘리려면 하나씩 더 공급해야 함)
    if diff < 2 ** (n - 1):
        print(2 ** (n - 1) + diff, end=" ")
    else:
        print(2 ** n, end=" ")

    # leaf 부모 노드는 +1 또는 -1
    if diff % 2:
        print(leaf + 1)
    else:
        print(leaf - 1)