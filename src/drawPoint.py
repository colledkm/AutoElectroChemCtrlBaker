def drawPoint(self, pointLoc):
    import rosegraphics as rg

    self.go_to(pointLoc)
    self.pen_down()
    self.draw_circle(4)
    self.pen_up()

    return;