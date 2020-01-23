import rosegraphics as rg
import drawpoint from drawPoint

window = rg.TurtleWindow()

horDist = 50
verDist = 50
nrow = 3 # number of rows
ncol = 3 # number of columns

turtle = rg.SimpleTurtle()

# put the turtle pen at home
turtle.pen = rg.Pen("red",2)
turtle.pen_up()
home = rg.Point(-100,100)
turtle.go_to(home)

# move across the row
Loc = home



Loc.x = turtle.x_cor()+50


#turtle.right(90)
#turtle.forward(verDist)
#turtle.right(90)
#turtle.forward(horDist)

#for r in range(nrow):
#    turtle.pen_down()
#    turtle.draw_circle(4)
#    turtle.pen_up()
#    turtle.forward(horDist)

#turtle.right(-90)
#turtle.forward(verDist)
#turtle.right(-90)
#turtle.forward(horDist)


window.close_on_mouse_click()