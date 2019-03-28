import sys
sys.stdin = open('1242.txt', 'r')

total_result = 0

data = {'0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9}

# 배수 찾기
def find_times(i, j):
    baesu = 1
    print(mat[i][:j + 1])
    bin_word = hex_to_bin(mat[i][:j + 1], j + 1)
    # print(mat[i][:j + 1])
    # print(bin_word)
    # print("bin_word", bin_word)
    print("tc", tc, "baesu", baesu, bin_word)
    # print(i, j, mat[i][j], visited[i][j + 1])
    while True:
        # start = -1
        # # 뒤에서부터 와서 1로 시작하는 start point 찾기
        # while bin_word[start] == '0':
        #     start -= 1
        found = False
        failed = False
        for start in range(8):
            word = ""
            for k in range(7):
                word = str(bin_word[-1 - 7 * start * baesu - k * baesu]) + word
            if word in data:
                continue
            else:
                failed = True
                break
            if failed:
                break
        else:
            found = True
        if found:
            break
        baesu += 1
    return baesu


def hex_to_bin(word, length):
    total_result = ""
    for i in range(length):
        char = word[i]
        result = ""
        if char <= '9':
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10
        for j in range(4):
            result = str(value % 2) + result
            value //= 2
        total_result += result
    last_idx = -1
    idx_changed = False
    print("making bin", total_result)
    while last_idx - 1 >= -(M_col) and total_result[last_idx] == '0':
        idx_changed = True
        last_idx -= 1
    if idx_changed:
        total_result = total_result[:last_idx + 1]
    # print("total_result", total_result)
    return total_result


def analyze_code(i, j, baesu):
    # find_j = j - 14
    # while mat[i][find_j - 1] != '0':
    #     find_j -= 1
    start_j = j - 15 * baesu if j - 15 * baesu >= 0 else 0
    word = mat[i][start_j: j + 1]
    print("word", word, baesu)
    # print("word", word)
    bin_word = hex_to_bin(word, len(word))
    # print(bin_word)
    len_bin_word = len(bin_word)
    # 코드 전체 숫자 담을 리스트
    total_code = [0] * 8
    # 코드 한 숫자
    part_word = ""
    start = -1
    print("bin word", bin_word, baesu)
    for time in range(8):
        # 코드 한 숫자 찾기
        for idx in range(7):
            part_word = bin_word[start - baesu * 7 * time - idx * baesu] + part_word
        # print("part_word", part_word)
        total_code[7 - time] = data[part_word]
        print("total_code", total_code)
        part_word = ""
    # print("total_code", total_code)

    return total_code

# visited 처리
def manage_visited(i_start, j_start, baesu):
    start_value = mat[i_start][j_start]
    i_going = i_start
    while i_going < N_row and mat[i_going][j_start] == start_value:
        for j in range(j_start - baesu * 14, j_start + 1):
            if j >= 0:
                visited[i_going][j] = 1
        i_going += 1

def judge_valid(code):
    global total_result
    sum_code = sum(code)
    if (2 * (code[0] + code[2] + code[4] + code[6]) + sum_code) % 10 == 0:
        total_result += sum_code



T = int(input())
# for tc in range(1, T + 1):
for tc in range(1, T + 1):
    N_row, M_col = map(int, input().split())
    mat = [0] * N_row

    for i in range(N_row):
        mat[i] = input()

    # for i in mat:
    #     print(i)
    # print()
    total_result = 0
    visited = [[0] * M_col for _ in range(N_row)]
    # print("0000000068B46DDB9346F40000")
    for i in range(N_row):
        for j in range(M_col - 1, -1, -1):
            if mat[i][j] != '0' and not visited[i][j]:
                baesu = find_times(i, j)
                # print("baesu", baesu)
                total_code = analyze_code(i, j, baesu)
                manage_visited(i, j, baesu)
                judge_valid(total_code)
                # print("part_total_result", total_result)
    print(f"#{tc} {total_result}")