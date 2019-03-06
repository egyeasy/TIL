import sys
sys.stdin = open('4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    curr_N = 0
    word = [1]
    print("#{}".format(tc))
    while curr_N < N:
        for i in word:
            print(i, end=" ")
        print()
        curr_N += 1
        word = [1] + [word[i] + word[i - 1] for i in range(curr_N) if i] + [1]
