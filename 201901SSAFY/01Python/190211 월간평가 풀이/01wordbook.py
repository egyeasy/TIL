class Word:
    def __init__(self):
        self.wordbook = {}

    def add(self, en, ko):
        self.wordbook.update({en: ko})

    def delete(self, en):
        if en in self.wordbook:
            self.wordbook.pop(en)
            return True
        else:
            return False

    def print(self):
        for en, ko in self.wordbook.items():
            print(f"{en}: {ko}")
    
if __name__ == "__main__":
    mybook = Word()
    mybook.add('apple', '사과')
    mybook.add('banana', '바나나')
    mybook.add('cherry', '체리')
    mybook.add('durian', '두리안')
    mybook.print()
    print(mybook.delete('cherry'))
    print(mybook.delete('durian'))
    print(mybook.delete('egg'))
    mybook.print()