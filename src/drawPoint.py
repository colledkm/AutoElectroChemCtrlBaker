def drawPoint(self, pointLoc):
    import rosegraphics as rg

    self.go_to(pointLoc)
    turtle.pen_down()
    turtle.draw_circle(4)
    turtle.pen_up()