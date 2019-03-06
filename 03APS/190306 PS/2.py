import sys
sys.stdin = open('2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    word = input()
    leng = len(word)
    first = ['.', '.', '#', '.', '.']
    first = '..#.'
    second_front = '#.'
    second_rear = '.'
    third = '.#.#'
    for i in range(leng):
        print(first, end="")
    print(".")
    for i in range(leng):
        print(third, end="")
    print(".")
    for i in  range(leng):
        print(second_front, end="")
        print(word[i], end="")
        print(second_rear, end="")
    print("#")

    for i in range(leng):
        print(third, end="")
    print(".")
    for i in range(leng):
        print(first, end="")
    print(".")



    # print()