# -------------------------------------------------------------------------
# TODO: When given a distance and direction, make the motor move accordingly.
# -------------------------------------------------------------------------

def movedist (distance, direction,speed):

# -------------------------------------------------------------------------
# TODO a: Convert distances to steps.  Put in the true conversion.
# -------------------------------------------------------------------------

    converter = 1 #converts distance to steps.  (steps/distance)
    steps = distance*converter #number of steps to move

# -------------------------------------------------------------------------
# TODO a: Insert motor move command
# -------------------------------------------------------------------------

    print("Motor moved", distance, "steps")
    return;