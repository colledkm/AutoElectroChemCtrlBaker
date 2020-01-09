# -------------------------------------------------------------------------
# TODO: When given a distance and direction, make the motor move accordingly.
# -------------------------------------------------------------------------

def movedist (distance, direction,speed,device):
    from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand, BinaryReply
    import time
    # -------------------------------------------------------------------------
    # TODO a: Convert distances to steps.  Put in the true conversion.
    # -------------------------------------------------------------------------

        converter = 1 #converts distance to steps.  (steps/distance)
        steps = distance*converter #number of microsteps to move

    # -------------------------------------------------------------------------
    # TODO a: Insert motor move command
    # -------------------------------------------------------------------------
    reply = device.move_rel(steps)  # move rel 2000 microsteps
    if not check_command_succeeded(reply):
        print("Device move failed.")
        exit(1)
    else print("Motor moved", distance, "microsteps")
    return;