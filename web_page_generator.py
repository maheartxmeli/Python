import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Genereator")
        # Creates button to generate webpage
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,0), pady=(10,10))
        # Creates button for name entry
        self.enterName = Button(self.master, text="Enter Name", width=30, height=2, command=self.enterName)
        self.enterName.grid(row=2, column=1, padx=(0,10), pady=(10,10))
        # Creates entry for name entry
        self.nameEntry = Entry(width=90)
        self.nameEntry.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,10))


    # Creates function that opens new tab from the main frame's default html page button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</html>\n</body>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Creates function that will return the entry
    def enterName(self):
        htmlName = self.nameEntry.get()
        htmlFile = open("index.html", "a")
        htmlContent = "<html>\n<body>\n<h1>" + htmlName + "</h1>\n</html>\n</body>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
