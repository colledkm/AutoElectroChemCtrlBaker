import tkinter
from tkinter import ttk
from moveDist import movedist
from zaber.serial import BinarySerial, BinaryDevice


def deviceInputFrame(root):

    deviceframe = ttk.Frame(root, padding=20)
    deviceframe.grid()  # only grid call that does NOT need a row and column

    # xaxis motor
    xmotor_label = ttk.Label(deviceframe, text="x-axis motor")
    xmotor_label.grid(row=0, column=0)
    xmotor_entry = ttk.Entry(deviceframe, width=15)
    xmotor_entry.insert(0, "/dev/ttyUSB0")
    xmotor_entry.grid(row=1, column=0)

    # yaxis motor
    ymotor_label = ttk.Label(deviceframe, text="y-axis motor")
    ymotor_label.grid(row=0, column=1)
    ymotor_entry = ttk.Entry(deviceframe, width=15)
    ymotor_entry.insert(0, "/dev/ttyUSB0")
    ymotor_entry.grid(row=1, column=1)

    # zaxis motor
    zmotor_label = ttk.Label(deviceframe, text="z-axis motor")
    zmotor_label.grid(row=0, column=2)
    zmotor_entry = ttk.Entry(deviceframe, width=15)
    zmotor_entry.insert(0, "/dev/ttyUSB0")
    zmotor_entry.grid(row=1, column=2)

    return deviceframe

def directCtrlFrame(root):

    #Main frame define
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    # xaxis motor
    xmotor_label = ttk.Label(main_frame, text="x-axis motor")
    xmotor_label.grid(row=0, column=0)
    xmotor_entry = ttk.Entry(main_frame, width=15)
    xmotor_entry.insert(0, "/dev/ttyUSB0")
    xmotor_entry.grid(row=1, column=0)
    # with BinarySerial(str(xmotor_entry.get())) as port:  # Linux
    # #with BinarySerial("xmotor_entry") as port:         # Windows
    #     xmotor = BinaryDevice(port, 1)  # motor on x axis

    # yaxis motor
    ymotor_label = ttk.Label(main_frame, text="y-axis motor")
    ymotor_label.grid(row=0, column=1)
    ymotor_entry = ttk.Entry(main_frame, width=15)
    ymotor_entry.insert(0, "/dev/ttyUSB0")
    ymotor_entry.grid(row=1, column=1)
    # with BinarySerial(str(ymotor_entry.get())) as port:  # Linux
    # #with BinarySerial("ymotor_entry") as port:         # Windows
    #     ymotor = BinaryDevice(port, 2)  # motor on x axis

    # zaxis motor
    zmotor_label = ttk.Label(main_frame, text="z-axis motor")
    zmotor_label.grid(row=0, column=2)
    zmotor_entry = ttk.Entry(main_frame, width=15)
    zmotor_entry.insert(0, "/dev/ttyUSB0")
    zmotor_entry.grid(row=1, column=2)
    # with BinarySerial(str(zmotor_entry.get())) as port:  # Linux
    # #with BinarySerial("zmotor_entry") as port:         # Windows
    #     zmotor = BinaryDevice(port, 3)  # motor on x axis

    # # Speed
    # speed_label = ttk.Label(main_frame, text="Speed")
    # speed_label.grid(row=2, column=0)
    # speed_entry = ttk.Entry(main_frame, width=8)
    # speed_entry.insert(0, "600")
    # speed_entry.grid(row=3, column=0)

    # Distance
    dist_label = ttk.Label(main_frame, text="Distance")
    dist_label.grid(row=2, column=1)
    dist_entry = ttk.Entry(main_frame, width=8)
    dist_entry.insert(0, "20")
    dist_entry.grid(row=3, column=1)

    ttk.Label(main_frame, text=" ").grid(row=4, column=1) #Inserts a blank row for formatting purposes

    #Forward button
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=5, column=1)
    forward_button['command'] = lambda: movedist (dist_entry.get(), 1,ymotor_entry.get())
    root.bind('<Up>', lambda event: print("Forward key"))

    #back button
    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=7, column=1)
    back_button['command'] = lambda: movedist (dist_entry.get(), -1,ymotor_entry.get())
    root.bind('<Down>', lambda event: print("Back key"))

    # Left button
    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=6, column=0)
    left_button['command'] = lambda: movedist (dist_entry.get(), -1,xmotor_entry.get())
    root.bind('<Left>', lambda event: print("Left key"))

    # Right button
    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=6, column=2)
    right_button['command'] = lambda: movedist (dist_entry.get(), 1,xmotor_entry.get())
    root.bind('<Right>', lambda event: print("Right key"))

    # Stop button
    # stop_button = ttk.Button(main_frame, text="Stop")
    # stop_button.grid(row=6, column=1)
    # stop_button['command'] = lambda: movedist (dist_entry, direction,speed_entry,device)
    # root.bind('<space>', lambda event: print("Stop key"))

    #Up button
    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=9, column=0)
    up_button['command'] = lambda: movedist (dist_entry.get(), -1,zmotor_entry.get())
    root.bind('<u>', lambda event: print("Up key"))

    #Down button
    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=10, column=0)
    down_button['command'] = lambda: movedist (dist_entry.get(), 1,zmotor_entry.get())
    root.bind('<j>', lambda event: print("Down key"))

    # # home buttons
    # home_button = ttk.Button(main_frame, text="Home")
    # home_button.grid(row=9, column=2)
    # home_button['command'] = lambda: print("Home button")

    # #Set home button
    # set_home_button = ttk.Button(main_frame, text="Set Home")
    # set_home_button.grid(row=10, column=2)
    # set_home_button['command'] = lambda: print("Set Home button")

    ttk.Label(main_frame, text=" ").grid(row=9, column=1) #blank for for formatting

    # Buttons for quit and exit
    # q_button = ttk.Button(main_frame, text="Quit")
    # q_button.grid(row=14, column=0)
    # q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=12, column=2)
    e_button['command'] = lambda: exit()


    return main_frame

def matrixFrame(root):

    frame = ttk.Frame(root, padding=20)
    frame.grid()  # only grid call that does NOT need a row and column

    # Matrix Dimentions
    matrix_dim_label = ttk.Label(frame, text="Matrix Dim")
    matrix_dim_label.grid(row=0, column=1)

    row_numb_label = ttk.Label(frame, text="Row")
    row_numb_label.grid(row=1, column=0)
    row_numb_entry = ttk.Entry(frame, width=8)
    row_numb_entry.insert(0, "10")
    row_numb_entry.grid(row=2, column=0)

    ttk.Label(frame, text="x").grid(row=2, column=1)

    col_numb_label = ttk.Label(frame, text="Col")
    col_numb_label.grid(row=1, column=2)
    col_numb_entry = ttk.Entry(frame, width=8)
    col_numb_entry.insert(0, "10")
    col_numb_entry.grid(row=2, column=2)

    ttk.Label(frame, text=" ").grid(row=3, column=1)
    ttk.Label(frame, text="Seperation Distance").grid(row=4, column=1)

    col_dist_label = ttk.Label(frame, text="Col Dist")
    col_dist_label.grid(row=5, column=2)
    col_dist_entry = ttk.Entry(frame, width=8)
    col_dist_entry.insert(0, "10")
    col_dist_entry.grid(row=6, column=2)

    row_dist_label = ttk.Label(frame, text="Row Dist")
    row_dist_label.grid(row=5, column=0)
    row_dist_entry = ttk.Entry(frame, width=8)
    row_dist_entry.insert(0, "10")
    row_dist_entry.grid(row=6, column=0)

    #Matrix Type
    matrix_types = ['Regular', 'Offset']
    matrix_var = tkinter.StringVar(value='Select Matrix Type')
    matrix_menu = tkinter.OptionMenu(root, matrix_var, *matrix_types)
    matrix_menu.grid(row = 4, column =1)

    return frame

def main():
    root = tkinter.Tk()

    frameList = {}
#    deviceInput_frame = deviceInputFrame(root)
#    deviceInput_frame.grid(row=0, column =0)
#    frameList["input Frame"] = deviceInput_frame
#    deviceInput_frame.

    dirCtrl_frame = directCtrlFrame(root)
    dirCtrl_frame.grid(row=1,column=0)

 #   matrix_frame = matrixFrame(root)
 #   matrix_frame.grid(row=1, column = 1)



    root.mainloop()

main()