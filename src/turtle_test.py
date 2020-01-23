import rosegraphics as rg
from drawPoint import drawpoint

window = rg.TurtleWindow()

horDist = 50
verDist = 100
nrow = 3 # number of rows
ncol = 3 # number of columns

turtle = rg.SimpleTurtle()

# put the turtle pen at home
turtle.pen = rg.Pen("red",2)
home = rg.Point(-100,100)

# move across the row
Loc = rg.Point(turtle.x_cor(),turtle.y_cor())
for c in range(ncol):
   # drawpoint(turtle, Loc)
    if c%2 == 0:
        for r in range(nrow):
            drawpoint(turtle,Loc)
            if r != nrow-1:
                Loc.x = turtle.x_cor()+horDist

    else:
        for r in range(nrow):
            drawpoint(turtle,Loc)
            if r != nrow-1:
                Loc.x = turtle.x_cor()-horDist
    Loc.y = turtle.y_cor()-verDist


window.close_on_mouse_click()