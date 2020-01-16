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
from moveRow import moveRow
from moveCol import moveCol
from zaber.serial import BinarySerial, BinaryDevice, BinaryCommand, BinaryReply
from check_command_succeeded import check_command_succeeded

##hardware and OS setup
with BinarySerial("/dev/ttyUSB0") as port:  # Linux
#with BinarySerial("COM3") as port:         # Windows

## Home all devices
# Home the device and check the result.
reply = device.home()
if check_command_succeeded(reply):
    print("Device homed.")
else:
    print("Device home failed.")
    exit(1)

## For Matrix Offset = 0
if matrixOffset == 0:
    #The matrix looks like this
        # - - - - -
        # - - - - -
        # - - - - -
        # - - - - -
        # - - - - -

    for r in nrow:
        for c in ncol:
            # -------------------------------------------------------------------------
            # TODO: Move across the row (finish moveRow function), add in picture command
            # -------------------------------------------------------------------------

            moveRow(horizontalDist,-1^r)

        # -------------------------------------------------------------------------
        # TODO: Move down the column (finish moveCol function), add in picture command
        # -------------------------------------------------------------------------

        moveCol(verticalDist,-1)


## For Matrix Offset = 1
if matrixOffset = 1:
    #The matrix looks like this
        # - - - - -
        #  - - - -
        # - - - - -
        #  - - - -
        # - - - - -
