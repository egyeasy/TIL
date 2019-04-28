import math
import turtle as t

k1 = 1 # k1 ; dt / mass of ball
a = 20 # 가속도 - mue / g
r = 10 # 반지름

balls = []
turtles = []
walls = []

class Ball:
    def __init__(self,x,y,v,theta):
        self.x = x
        self.y = y
        self.v = v
        self.theta = theta

def hit(f0,theta,ball):
    ball.theta = theta
    ball.v = f0*k1
        
def update_vel(dt):
    for ball in balls:
        if ball.v:
            ball.v -= a*dt
        if ball.v <= 0:
            ball.v = 0

def update_pos(dt,w,h):
    for ball in balls:
        ball.x += ball.v * math.cos(ball.theta) * dt
        ball.y += ball.v * math.sin(ball.theta) * dt
        if ball.x >= w/2:
            ball.theta = math.radians(180)-ball.theta
#             ball.x = w/2 - r
            
        elif ball.x <= -w/2:
            ball.theta = math.radians(180)-ball.theta
#             ball.x = w/2 + r
            
        elif ball.y >= h/2:
            ball.theta = math.radians(360)-ball.theta
#             ball.y = h/2 - r
            
        elif ball.y <= -h/2:
            ball.theta = math.radians(360)-ball.theta
#             ball.y = h/2 + r


            

def make_turtles():
    n = len(balls)
    for _ in range(n):
        turtles.append(t.Turtle("circle"))
        turtle = turtles[_]
        ball = balls[_]
        turtle.penup()
        turtle.goto(ball.x,ball.y)

def plot_turtles():
    for _ in range(len(turtles)):
        ball = balls[_]
        turtle = turtles[_]
        turtle.goto(ball.x,ball.y)

def check_collision(dt):
    for i in range(len(balls)):
        for j in range(i+1,len(balls)):
            b1 = balls[i]
            b2 = balls[j]
            if math.sqrt((b1.x-b2.x)**2 + (b1.y-b2.y)**2) <= 2*r:
                collision(b1,b2)
#                 d = math.sqrt((b1.x-b2.x)**2 + (b1.y-b2.y)**2)
#                 b1_nex = b1.x + b1.v*math.cos(b1.theta)*dt
#                 b1_ney = b1.y + b1.v*math.sin(b1.theta)*dt
#                 b2_nex = b2.x + b2.v*math.cos(b2.theta)*dt
#                 b2_ney = b2.y + b2.v*math.sin(b2.theta)*dt
#                 nexd = math.sqrt((b1_nex-b2_nex)**2 + (b1_ney-b2_ney)**2)
#                 if nexd < d:    
#                     collision(b1,b2)
            
            

            
def draw_walls(w,h):
    c = t.Turtle("turtle")
    c.penup()
    c.goto(-w/2,-h/2)
    c.pendown()
    for _ in range(2):
        c.forward(w)
        c.left(90)
        c.forward(h)
        c.left(90)



def collision(ball1,ball2):
    vx1 = ball1.v*math.cos(ball1.theta)
    vy1 = ball1.v*math.sin(ball1.theta)
    print(f"theta1 : {math.degrees(ball1.theta)} v1 : {ball1.v}")
    print(f"vx1 : {vx1} vy1 : {vy1}")
    vx2 = ball2.v*math.cos(ball2.theta)
    vy2 = ball2.v*math.sin(ball2.theta)
    print(f"theta2 : {math.degrees(ball2.theta)} v2 : {ball2.v}")    
    print(f"vx2 : {vx2} vy2 : {vy2}")
    alpha = math.atan((ball1.y-ball2.y)/(ball1.x-ball2.x))
    print(f"alpha : {math.degrees(alpha)}")

    vx1p = vx2*math.cos(alpha) + vy2*math.sin(alpha)
    vy1p = vy1*math.cos(alpha) - vx1*math.sin(alpha)
    print(f"vx1p : {vx1p} vy1p : {vy1p}")

    vx2p = vx1*math.cos(alpha) + vy1*math.sin(alpha)
    vy2p = vy2*math.cos(alpha) - vx2*math.sin(alpha)
    print(f"vx2p : {vx2p} vy2p : {vy2p}")

    vx1 = vx1p*math.cos(alpha) - vy1p*math.sin(alpha)
    vy1 = vx1p*math.sin(alpha) + vy1p*math.cos(alpha)
    print(f"after vx1 : {vx1} vy1 : {vy1}")
    vx2 = vx2p*math.cos(alpha) - vy2p*math.sin(alpha)
    vy2 = vx2p*math.sin(alpha) + vy2p*math.cos(alpha)
    print(f"after vx2 : {vx2} vy2 : {vy2}")
    if vx1 == 0 or vy1 == 0:
        ball1.theta = 0
        ball1.v = 0
    else:
        ball1.theta = math.atan2(vy1,vx1)
        ball1.v = math.sqrt(vx1**2 + vy1**2)
    
    print(f"after theta1 : {math.degrees(ball1.theta)} v1 : {ball1.v}")

    if vx2 == 0 or vy2 == 0:
        ball2.theta = 0
        ball2.v = 0
    else:
        ball2.theta = math.atan2(vy2,vx2)
        ball2.v = math.sqrt(vx2**2 + vy2**2)
    print(f"after theta2 : {math.degrees(ball2.theta)} v2 : {ball2.v}")
    print()


# balls = [Ball(0,0,0,0),Ball(100,100,0,0)]

# hit(100,math.radians(225),balls[1])
# 
balls = [Ball(0,0,0,0),Ball(110,100,0,0),Ball(180,175,0,0)]


# hit(200,math.radians(45),balls[0])
# hit(200,math.radians(40),balls[0])
# hit(800,math.radians(225),balls[1])
hit(800,math.radians(225),balls[0])