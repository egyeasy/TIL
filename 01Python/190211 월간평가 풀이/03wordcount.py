
def alphabet_count(word):
    result = {}
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
            
    return result



if __name__ == "__main__":
    print(alphabet_count('hello'))