draw_walls(800,400)
make_turtles()
turtles[0].color('white')
turtles[0].pencolor('black')
turtles[0].pendown()
turtles[1].color('red')
turtles[1].pendown()
turtles[2].color('yellow')
turtles[2].pendown()
# turtles[3].color('blue')
# turtles[3].pendown()

for _ in range(900):
    
    update_vel(0.01)
    check_collision(0.01)
    update_pos(0.01,800,400)
    

    plot_turtles()
   
t.bye()