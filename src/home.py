def home(device):
    from src.check_command_succeeded import check_command_succeeded

    reply = device.home()
    if check_command_succeeded(reply):
        print("Device homed.")
    else:
        print("Device home failed.")
        exit(1)

    return;