# 아래에 코드를 작성해주세요.
import turtle

window = turtle.Screen() # 스크린 클래스
window.bgcolor("red") # background color 설정

ggobugi = turtle.Turtle() # 거북이 클래스
ggobugi.color("yellow")
ggobugi.shape("turtle")
ggobugi.speed(10) # 속도 설정

for i in range(100):
    for i in range(4):
        ggobugi.forward(100)
        ggobugi.left(90)
    ggobugi.right(5)

window.exitonclick() # 커널 죽을 때 사용. 윈도우를 원할 때 닫기