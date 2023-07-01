import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        # this closes app
        self.master.destroy()
        os._exit(0)

#===================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # you must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_fun(self)


def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execut("""INSER INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""", (data)
            conn.commit()
        conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
    count = cur.fetchone() [0]
    return cur,count

# select item in ListBox
def onSelect(self, event):
    # calling the event is the self.1stList1 widget
    varList = event.widget
    select = varList.curselection() [0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # this returns a tuple and we can slive it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt__fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt__lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt__phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt__email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # this will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # this will ensure that the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: # will use this soon
        print("You must enter the email correctly.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.curstor()
            # check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone() [0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName)
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""")
                self.1stList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")


def onDelete(self):
    var_select = self.1stList1.get(self.1stList1.curselection()) # List'box's selected value
    conn = sqlie3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in the database.. cannot delete last recvord or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchon() [0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted".format(var_fullname))
            if confirm:
                 conn = sqlite3.connect('phonebook.db')
                 with conn:
                     cursor = conn.cursor()
                     cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
#####               onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time".format(var_select)
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.1stList1.curselection() [0]
        self.1stList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)


def onRefresh(self):
    # populate the listbox, coinciding with the database
    self.1stList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i =0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall() [i]
            for item in varList:
                self.1stList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.1stList1.curselection() [0] # index of the list selection
        var_value = self.1stList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCancelling the Update request.")
        return
    # the user will only be allowed to update changes for phone and emails. for name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_emaili) > 0: # ensure that there is data present
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in the DB, meaning there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone() [0]
            print(count)
            cur.execute("""SELECT COUNT(col_email_ FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone() [0]
            print(count2)
            if count == 0 or count 2 == 0: #if proposed changes are not already in the databaser, then proceed
                response = messagebox.askokcancel("Update Request","The following changes


















            

























            
