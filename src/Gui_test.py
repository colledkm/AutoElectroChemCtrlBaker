import tkinter
from tkinter import ttk

def main():
    root=tkinter.Tk()
    frame = ttk.Frame(root, padding=20)
    frame.grid()
    button = ttk.Button(frame, text="Say Hello")


main()
