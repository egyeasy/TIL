from tkinter import *
import webbrowser

# 위를 실행하면 아래와 같은 방식으로 변수들 다 만듦 => 메모리 많이 사용해서 비효율적
# Tk = tkinter.Tk
# Label = tkinter.Label

def browser():
    webbrowser.open("https://www.daum.net")

root = Tk() # 클래스

label = Label(root, text="Hello", fg="red", bg="blue") # 어떤 tkinter 윈도우/프로그램에 넣을지, text 메시지
label2 = Label(root, text="Young Lim's widget")

btn = Button(root, text="This is a button", command=browser) # command : 버튼 눌렀을 때 실행할 명령어. browser 함수 실행

label.pack() # 라벨을 포장해줌. 위치를 specific하게 잡아주는 게 아니라 위에서부터 넣어라.
label2.pack()
btn.pack()

root.mainloop() # 계속해서 프로그램이 돌아가면서 클릭이 있을 때 그걸 실행시켜주는 위젯 만들기

