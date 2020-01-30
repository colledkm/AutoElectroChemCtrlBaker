

# Here's an area where you can do code testing with out it impacting the rest of the functions!  Enjoy!

# go here for help: https://www.rose-hulman.edu/class/csse/csse120/201920/
# preparations have videos


# nrow = 5
# ncol = 5

from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand  # , BinaryReply
import time

# Assume that our serial port can be found at COM1

port = BinarySerial("COM13")    # be mindful of which COM port to use; check device manager; may need to restart port
# with BinarySerial("COM13") as port:
# Device number 0, command number 1.    1 is Home. 0 is Reset, move absolute is 20, relative is 21
# command = BinaryCommand(0, 1)
# note: Binary motor commands are blocking. Syntax: BinaryCommand(device#, command#, dataValue)
# List of command #s can be found at: https://www.zaber.com/wiki/Manuals/Binary_Protocol_Manual#Command_Reference
# port.write(command)

# Assume that we have 1 devices connected.
ndevices = 1

# for i in range(0, ndevices):
# port.read()     #returns a BinaryReply. Discards when not assigned to a variable.

# Assume we have a BinarySerial object called "port".
device1 = BinaryDevice(port, 1)

# device1.move_abs(5000)
device1.home()          # don't recommend using device.functions because only certain common commands have functions & send oesn't seem to work
time.sleep(5)
# device1.move_rel(5000)
# device1.send("home")    # doesn't work
