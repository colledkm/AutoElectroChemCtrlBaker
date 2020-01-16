def moveCol(verticaldist,verticaldir,speed, device):

    from src.moveDist import movedist

    # -------------------------------------------------------------------------
    # TODO: Move up
    # -------------------------------------------------------------------------

    movedist(distance=10, direction=1,speed=speed,device=device) #move up off of the plate

    # -------------------------------------------------------------------------
    # TODO: Move to the new column, make sure verticalDirection is compatiable with -1 or 1
    # -------------------------------------------------------------------------

    trueHorzDir = verticaldir #convert -1 or 1 to direction
    movedist(distance=verticaldist, direction=trueHorzDir,speed=speed,device=device)

    # -------------------------------------------------------------------------
    # TODO: Move down
    # -------------------------------------------------------------------------
    from src.moveSense import movesense
    movesense()

    return;

