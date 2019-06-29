def cipher(word, n):
    result = ''

    n = n % 26

    for c in word:
        # w = ord(c) + n

        # if w > 122:
        #     w = w - 26

        # result += chr(w)

        result += chr((ord(c) - 97 + n) % 26 + 97)
    return result

    # return ''.join([chr(ord(c) - 97 + n) % 26 + 97) for c in word])


if __name__ == "__main__":
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))