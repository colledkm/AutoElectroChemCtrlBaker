

#Here's an area where you can do code testing with out it impacting the rest of the functions!  Enjoy!

# go here for help: https://www.rose-hulman.edu/class/csse/csse120/201920/
#preparations have videos


#nrow = 5
#ncol = 5

from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand, BinaryReply
import time

# Assume that our serial port can be found at COM1.

port = BinarySerial("COM1")
with BinarySerial("COM1") as port
    # Device number 0, command number 1.
    command = BinaryCommand(0, 1)
    #note: Binary motor commands are blocking
    port.write(command)

    # Assume that we have 1 devices connected.
    ndevices = 1

    #for i in range(0, ndevices):
        #port.read()     #returns a BinaryReply. Discards when not assigned to a variable.

    # Assume we have a BinarySerial object called "port".
    device1 = BinaryDevice(port, 1)

    device1.move_abs(300)
    device1.move_rel(1000)
