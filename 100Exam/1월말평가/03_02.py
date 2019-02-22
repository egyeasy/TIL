# 파일명 변경 금지
def alphabet_mode(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # word에서 가장 많이 발생한 알파벳 하나를 반환합니다.
    result = {}
    for char in word:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    max_val = 0
    max_key = 0

    for char in word:
        if result[char] > max_val:
            max_val = result[char]
            max_key = char

    return max_key




# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_mode('hello'))
    print(alphabet_mode('internationalization'))
    print(alphabet_mode('haha'))