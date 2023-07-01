# Python version:   3.5.1
#
# Author:           Mahea Paiva
#
# Purpose:          Phonebook project, learning OOP, Tkinter GUI module, using Tkinter
#                   Parent and Child relationships.
#
# Tested OS:        This code was writtena nd tested to work with Mac OS.

from tkinter import *
import tkinter as tk

# be sure to import the other modules needed to have access to them.
import phonebook_gui
import phonebook_func

# frame is the Tkinter frame class that our own class will inherit from:
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (height, width)
        self.master.maxsize(500,300)

        # this CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")

        # tihs protocol method is a tkinter built-in method to catch if the user clicks the upper corner "x" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI wwidgets from a separate module, keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
