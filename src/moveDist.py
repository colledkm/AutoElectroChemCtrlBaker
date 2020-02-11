# -------------------------------------------------------------------------
# TODO: When given a distance and direction, make the motor move accordingly.
# -------------------------------------------------------------------------

def movedist (distance, direction_sign,device):
    # removed speed for now (third variable)
    # where device = device number.
    from src.check_command_succeeded import check_command_succeeded
    from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand  # , BinaryReply #Added
    import time # Added

    # -------------------------------------------------------------------------
    # DONE: Create device
    # -------------------------------------------------------------------------

    # command = BinaryCommand(device, 21, steps)   # Added. 21 = move rel
    port = BinarySerial(str(device))                  # Added


    # -------------------------------------------------------------------------
    # TODO: Convert distances to steps.  Put in the true conversion.
    # -------------------------------------------------------------------------

    converter = 1 # converts distance to steps.  (steps/distance)
    steps = distance*converter*direction_sign #number of microsteps to move
    

    # -------------------------------------------------------------------------
    # TODO: Insert motor move command
    # -------------------------------------------------------------------------

    command = BinaryCommand(0, 21, steps)
    port.write(command)  # Added
    # device.move_rel(speed,blocking=True)   # Added Commented Out

    #r eply = device.move_rel(steps)  # move rel 2000 microsteps #A dded Commented out everything below

    # if not check_command_succeeded(reply):
        #print("Device move failed.")
        #exit(1)
    # else:
       # print("Motor moved", distance, "microsteps")
    return

