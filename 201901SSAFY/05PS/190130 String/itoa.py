nums = 123053
words = ""

while nums != 0:
    num = nums % 10
    words = chr(num + 48) + words
    nums = nums // 10

print(words, type(words))