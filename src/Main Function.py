# -------------------------------------------------------------------------
# TODO: When given the dimensions of a plate, move to each node and
#  record placement in picture.
# -------------------------------------------------------------------------

## Input Data

horizontalDist = 1      #horizontal distance between nodes
verticalDist = 1        #verticle distance between nodes
nrow = 5                #Number of rows
ncol = 5                #Number of columns (maximum) in a row
matrixOffset = 0        #If rows are offset type 0, if rows are inline type 1.
                        # This program assumes it's halfway between each column
## Import functions
from src.moveRow import moveRow
from src.moveCol import moveCol
from zaber.serial import BinarySerial, BinaryDevice
from src.home import home

##hardware and OS setup
with BinarySerial("/dev/ttyUSB0") as port:  # Linux
# with BinarySerial("COM3") as port:         # Windows

# Get a handle for device #1 on the serial chain. This assumes you have a
# device already in Binary 9,600 baud mode at address 1 on your port.
device1 = BinaryDevice(port, 1) # motor on x axis
device2 = BinaryDevice(port, 2) # motor on y axis
device3 = BinaryDevice(port, 3) # motor on z axis


## Home all devices
# Home the device and check the result.
home(device1)
home(device2)
home(device3)

## For Matrix Offset = 0
if matrixOffset == 0:
    #The matrix looks like this
        # - - - - -
        # - - - - -
        # - - - - -
        # - - - - -
        # - - - - -

    for r in range(nrow):
        for c in range(ncol):
            # -------------------------------------------------------------------------
            # TODO: Move across the row (finish moveRow function), add in picture command
            # -------------------------------------------------------------------------

            moveRow(horizontalDist,-1^r)

        # -------------------------------------------------------------------------
        # TODO: Move down the column (finish moveCol function), add in picture command
        # -------------------------------------------------------------------------

        moveCol(verticalDist,-1)


## For Matrix Offset = 1
if matrixOffset != 0:

    #The matrix looks like this
        # - - - - -
        #  - - - -
        # - - - - -
        #  - - - -
        # - - - - -
