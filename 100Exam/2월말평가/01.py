# 파일명 변경 금지
# 아래에 클래스 Word를 선언하세요.
class Word:
    def __init__(self):
        self.workbook = {}
        
    def add(self, eng, kor):
        self.workbook[eng] = kor

    def delete(self, eng):
        if eng not in self.workbook:
            return False
        else:
            self.workbook.pop(eng)
            return True
    
    def print(self):
        for key, value in self.workbook.items():
            print(f"{key}: {value}")


# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    my_book = Word()
    my_book.add('apple', '사과')
    my_book.add('banana', '바나나')
    my_book.add('cherry', '체리')
    my_book.add('durian', '두리안')
    my_book.print() 
    print(my_book.delete('cherry'))
    print(my_book.delete('durian'))
    print(my_book.delete('egg'))
    my_book.print()