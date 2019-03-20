def chr_to_dec(chr):
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

def judge_crypto(word):
    if word == '001101':
        return 0
    elif word == '010011':
        return 1
    elif word == '111011':
        return 2
    elif word == '110001':
        return 3
    elif word == '100011':
        return 4
    elif word == '110111':
        return 5
    elif word == '001011':
        return 6
    elif word == '111101':
        return 7
    elif word == '011001':
        return 8
    elif word == '101111':
        return 9
    else:
        print("wrong word")

word = "0269FAC9A0"
len_word = len(word)

bin_word = ""
for i in range(len_word):
    num = chr_to_dec(word[i])
    bin_num = ""
    for j in range(4):
        bin_num = str(num % 2) + bin_num
        num //= 2
    bin_word += bin_num
print(bin_word)

len_bin = 4 * len_word
result = ""
for i in range(len_bin - 1, -1, -1):
    if bin_word[i] == '1':
        j = i
        value = judge_crypto(bin_word[j - 5:j + 1])
        while value != None:
            print(value)
            result = str(value) + " " + result
            j -= 6
            value = judge_crypto(bin_word[j - 5:j + 1])
        break
print(result)

