import tkinter
from tkinter import ttk

def directCtrlFrame(root):

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left Speed")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    step_numb_label = ttk.Label(main_frame, text="Number of Steps")
    step_numb_label.grid(row=0, column=1)
    step_numb_entry = ttk.Entry(main_frame, width=8)
    step_numb_entry.insert(0, "20")
    step_numb_entry.grid(row=1, column=1)

    right_speed_label = ttk.Label(main_frame, text="Right Speed")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=3, column=1)
    forward_button['command'] = lambda: print("Forward button")
    root.bind('<Up>', lambda event: print("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=4, column=0)
    left_button['command'] = lambda: print("Left button")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=4, column=1)
    stop_button['command'] = lambda: print("Stop button")
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=4, column=2)
    right_button['command'] = lambda: print("Right button")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=5, column=1)
    back_button['command'] = lambda: print("Back button")
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=6, column=0)
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=7, column=0)
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=6, column=2)
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=7, column=2)
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

    #Matrix Type

    matrix_types = ['Regular', 'Offset']
    matrix_var = tkinter.StringVar()
    matrix_menu = tkinter.OptionMenu(root, matrix_var, *matrix_types)
    matrix_menu.grid()

    return frame

def main():
    root = tkinter.Tk()

    dirCtrl_frame = directCtrlFrame(root)
    dirCtrl_frame.grid(row=0,column=0)


    matrix_frame = matrixFrame(root)
    matrix_frame.grid(row=0, column = 1)

    root.mainloop()

main()