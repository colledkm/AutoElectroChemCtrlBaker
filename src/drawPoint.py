def drawpoint(cursor, pointloc):
    import rosegraphics as rg
    cursor.pen_up()
    cursor.go_to(pointloc)
    cursor.pen_down()
    cursor.draw_circle(4)
    cursor.pen_up()

    return;