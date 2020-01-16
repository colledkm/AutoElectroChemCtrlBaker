def home(device):

    from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand, BinaryReply
    from check_command_check import check_command_check

    reply = device.home()
    if check_command_succeeded(reply):
        print("Device homed.")
    else:
        print("Device home failed.")
        exit(1)
return;
