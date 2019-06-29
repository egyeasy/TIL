import sys
sys.stdin = open('4366.txt', 'r')


# 2진수, 3진수 각각의 합 계산
def cal_value(word, exp, length):
    value = 0
    for i in range(length):
        value = value * exp + int(word[i])
    # print(value)
    return value


# 3진수 숫자를 돌며 주어진 bin_value와 같은 값 있는지 비교
def find_value(bin_value):
    for i in range(len_tris):
        tri_digit = int(tris[i])
        if tri_digit == 2:
            cand_value_tris_minus_one = value_tris - 3 ** (len_tris - i - 1)
            cand_value_tris_minus_two = value_tris - 2 * 3 ** (len_tris - i - 1)
            if bin_value == cand_value_tris_minus_one or bin_value == cand_value_tris_minus_two:
                print(f"#{tc} {bin_value}")
                return True
        elif tri_digit == 1:
            # 첫째 자리가 1인 경우에 0이 되지 않도록 방지
            if i != 0:
                cand_value_tris_minus = value_tris - 3 ** (len_tris - i - 1)
            else:
                cand_value_tris_minus = -1
            cand_value_tris_plus = value_tris + 3 ** (len_tris - i - 1)
            if bin_value == cand_value_tris_minus or bin_value == cand_value_tris_plus:
                print(f"#{tc} {bin_value}")
                return True
        else:
            cand_value_tris_plus_one = value_tris + 3 ** (len_tris - i - 1)
            cand_value_tris_plus_two = value_tris + 2 * 3 ** (len_tris - i - 1)
            if bin_value == cand_value_tris_plus_one or bin_value == cand_value_tris_plus_two:
                print(f"#{tc} {bin_value}")
                return True
    return False


T = int(input())
for tc in range(1, T + 1):
    bins = input()
    len_bins = len(bins)
    value_bins = cal_value(bins, 2, len_bins)

    tris = input()
    len_tris = len(tris)
    value_tris = cal_value(tris, 3, len_tris)

    for b in range(len_bins):
        bin_digit = int(bins[b])
        if bin_digit == 1:
            # 첫째 자리가 1인 경우에 0이 되지 않도록 방지
            if b == 0:
                continue
            if find_value(value_bins - 2 ** (len_bins - b - 1)):
                break
        elif bin_digit == 0 and find_value(value_bins + 2 ** (len_bins - b - 1)):
            break

