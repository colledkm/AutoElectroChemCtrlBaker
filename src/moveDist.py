# -------------------------------------------------------------------------
# TODO: When given a distance and direction, make the motor move accordingly.
# -------------------------------------------------------------------------

def movedist (distance, direction,speed,device):
    from src.check_command_succeeded import check_command_succeeded
    from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand  # , BinaryReply #Added
    import time #Added
    # -------------------------------------------------------------------------
    # TODO: Convert direction into +1 or -1  Put in the true conversion.
    # -------------------------------------------------------------------------

    if direction=="E":  #Changed from R to E for extend since + = extend - = retract in commands
        direction_sign = 1 #extend
    else:
        direction_sign = -1 #retract

    # -------------------------------------------------------------------------
    # TODO: Convert distances to steps.  Put in the true conversion.
    # -------------------------------------------------------------------------

    converter = 1 #converts distance to steps.  (steps/distance)
    steps = distance*converter*direction_sign #number of microsteps to move

    # -------------------------------------------------------------------------
    # TODO: Insert motor move command
    # -------------------------------------------------------------------------
    #device.move_rel(speed,blocking=True)   #Added Commented Out
    port = BinarySerial("COM13")            #Added
    command = BinaryCommand(0, 21, steps)   #Added. 21 = move rel
    port.write(command)                     #Added

    #reply = device.move_rel(steps)  # move rel 2000 microsteps #Added Commented out everything below

    #if not check_command_succeeded(reply):
        #print("Device move failed.")
        #exit(1)
    #else:
        #print("Motor moved", distance, "microsteps")
    return;