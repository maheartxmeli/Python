import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter~!')
        self.master.config(bg='#fff')

        #creating variables BooleanVar, DoubleVar, IntVar, StringVar
        self.varFName = StringVar()
        self.varLName = StringVar()


        self.lblFName = Label(self.master,text='First Name', font=('Helvetica', 16, fg='black', bg='lightblue')
        self.lblFName.grid(row=0, column=0)

        self.lblLName = Label(self.master,text='Last Name', font=('Helvetica', 16, fg='black', bg='lightblue')
        self.lblLName.grid(row=1, column=0)

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.pack(row=0, column=1)

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.pack(row=1, column=1)




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
