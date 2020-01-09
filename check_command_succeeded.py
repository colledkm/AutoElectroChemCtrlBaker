def check_command_succeeded(reply):
    """
    Return true if command succeeded, print reason and return false if command
    rejected

    param reply: BinaryReply

    return: boolean
    """
    
    from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand, BinaryReply
    import time
    
    if reply.command_number == 255: # 255 is the binary error response code.
        print ("Danger! Command rejected. Error code: " + str(reply.data))
        return False
    else: # Command was accepted
        return True
