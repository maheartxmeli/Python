import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # sets title of GUI window
        self.master.title("File Transfer")

        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # Positions source button in GU using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0,padx=(20,10),pady=(30,0))

        # Creates entry to source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() pax and pady are the same as the button to ensure they will line up
        self.source_dir.grid(row=0,column=1,columnspan=2,padx=(20,10),pady=(30,0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter gruid() on the next row under the source button
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.destination_dir.grid(row=1,column=1,columnspan=2,padx=(20,10),pady=(15,10))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0, 15))

        # Creates an exit button
        self.exit_btn = Button(text="Exit",width=20, command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0, 15))

    # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget, this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

    # Creates function to select source directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget, this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0,END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0, selectDestDir)
        # Creates button to select files from source directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        # Gets source directory
        source = self.source_dir.get()
        # Gets destination directory
        destination = self.destination_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)
        # Moves files modified 24 hours or less to dest folder
        def modfiles_day(i):
            for i in source_files:
                timestamp = os.path.getmtime(source_files)
                if datetime.fromtimestamp(timestamp) >= (datetime.now()- timedelta(hours=24)):
                    continue
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')


    # Creates function to exit program
    def exit_program(self):
        # root is the main GUI window, the tkinter destroy method. Tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
    
        

if __name__ == "__main__":
    root = tk.Tk()
    App =  ParentWindow(root)
    root.mainloop()
