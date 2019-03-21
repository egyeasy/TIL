import sys
sys.stdin = open('1-1.txt')

def hex_to_bin(char):
    if char <= '9':
        value = ord(char) - ord('0')
    else:
        value = ord(char) - ord('A') + 10
    result = ""
    for i in range(4):
        result = str(value % 2) + result
        value //= 2
    # print(result)
    return result

T = int(input())
for tc in range(1, T + 1):
    N_hex, word = input().split()
    N_hex = int(N_hex)
    total_result = ""
    for i in range(N_hex):
        char = word[i]
        total_result += hex_to_bin(char)
    print(f"#{tc} {total_result}")