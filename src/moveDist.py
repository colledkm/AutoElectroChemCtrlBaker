# -------------------------------------------------------------------------
# TODO: When given a distance and direction, make the motor move accordingly.
# -------------------------------------------------------------------------

def movedist (distance, direction,speed,device):
    from src.check_command_succeeded import check_command_succeeded

    # -------------------------------------------------------------------------
    # TODO: Convert direction into +1 or -1  Put in the true conversion.
    # -------------------------------------------------------------------------

    if direction=="R":
        direction_sign = 1 #rotate clockwise
    else:
        direction_sign = -1 #rotate counterclockwise

    # -------------------------------------------------------------------------
    # TODO: Convert distances to steps.  Put in the true conversion.
    # -------------------------------------------------------------------------

    converter = 1 #converts distance to steps.  (steps/distance)
    steps = distance*converter*direction_sign #number of microsteps to move

    # -------------------------------------------------------------------------
    # TODO: Insert motor move command
    # -------------------------------------------------------------------------
    device.move_rel(speed,blocking=True)
    reply = device.move_rel(steps)  # move rel 2000 microsteps

    if not check_command_succeeded(reply):
        print("Device move failed.")
        exit(1)
    else:
        print("Motor moved", distance, "microsteps")
    return;