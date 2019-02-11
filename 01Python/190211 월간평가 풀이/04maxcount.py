def alphabet_count(word):
    result = {}
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    
    max_count = max(result.values())

    # for char, count in result.items():
    #     if count == max_count:
    #         return char

    return max(result.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
    print(alphabet_count('hello'))