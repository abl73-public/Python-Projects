# This code was written and tested to work with Windows 11 and Python Version 3.13.3


import tkinter
from tkinter import *
from tkinter import messagebox


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        # define our master frame configuration
        self.master = master
        self.master.resizable(width = False, height = False) # with Height and Width False I cannot resize
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title("Learning Tkinter!")
        self.master.config(bg="lightgrey") # bg is background,I can write self.master.config(bg="#D3D3D3")
               
        self.varFName = StringVar()
        self.varLName = StringVar()
        
        self.lblFName = Label(self.master, text='First Name: ', font = ("Helvetica", 16), fg = 'black', bg = 'lightgrey')
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-buttom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))
        
        self.lblLName = Label(self.master, text='Last Name: ', font = ("Helvetica", 16), fg = 'black', bg = 'lightgrey')
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-bottom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))
        
        self.lblLDisplay = Label(self.master, text='', font = ("Helvetica", 16), fg = 'black', bg = 'lightgrey')
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-bottom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.lblLDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))
        
        self.txtFName = Entry(self.master, text = self.varFName, font = ("Helvetica", 16), fg = 'black', bg = 'lightblue')
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-buttom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))
        
        self.txtLName = Entry(self.master, text = self.varLName, font = ("Helvetica", 16), fg = 'black', bg = 'lightblue')
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-buttom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))
        
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-buttom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)
        
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        # we can use pack() self.txtLName.pack() or grid()
        # define position in grid (row and column) and padding (left-right and top-buttom)
        # colspan=2 indicate that I use a field with two columns
        # if I do not specify is the default colspan=1
        # we can use sticky=NE or sticky=N+E that indicates Nord East
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)
        
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblLDisplay.config(text='Hello {} {}!'.format(fn, ln))
        
    def cancel(self):
        self.master.destroy()
        
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
