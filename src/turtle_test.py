import rosegraphics as rg

window = rg.TurtleWindow()

horDist = 50
verDist = 50
nrow = 6 # number of rows
ncol = 6 # number of columns

turtle = rg.SimpleTurtle()

# put the turtle pen at home
turtle.pen = rg.Pen("red",2)
turtle.pen_up()
home = rg.Point(-100,100)
turtle.go_to(home)

# move across the row

for r in range(ncol):
    turtle.pen_down()
    turtle.draw_circle(4)
    turtle.pen_up()
    turtle.forward(horDist)

#for r in nrow:
#    turtle.forward(verDist)


window.close_on_mouse_click()