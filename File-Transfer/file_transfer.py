import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Set the title of the GUI window
        self.master.title("File Transfer")
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width = 20, command=self.sourceDir)
        #Position the source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30, 0))
        
        #Create entry for source directory selection
        self.source_dir = Entry(width=75)
        #Position the entry in the GUI using tkinter grid() 
        #padx and pady are the same as the button to ensure they line up
        self.source_dir.grid(row=0, column=1,  padx=(20,10), pady=(30,0))
        
        #Create button to select destination of files from file directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Position the button in GUI using tkinter grid() on the next row under the source
        #button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        
        #Create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Position entry in GUI using tkinter grid()
        #padx and pady are the same as the button to ensure they line up
        self.destination_dir.grid(row=1, column=1, padx=(20,10), pady=(15,10))
        
        #Create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Position transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
        
        #Create the Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Position the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Create a function to select the source directory    
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the btn content that is inserted in the Entry widget,
        #which allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)

    #Create a function to select destination directory    
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #The .delete(0,END) will clear the btn content that is inserted in the Entry widget,
        #which allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)
        
    #Create a function to transfer files from one directory to another
    def transferFiles(self):
        #Get source directory
        source = self.source_dir.get()
        #Get destination directory
        destination = self.destination_dir.get()
        #Get a list of files in the source directory
        source_files = os.listdir(source)
        #Run through each file in the source directory
        for i in source_files:
            #Get the document file path
            file_path = os.path.join(source, i)
            #Set a variable to determine 24 hours ago
            one_day_ago = datetime.datetime.now() - timedelta(hours = 24)
            #Get the last modified time of the file
            modification_time = os.path.getmtime(file_path)
            #Determine the time difference between the file modified date and now
            date_time_of_file = datetime.datetime.fromtimestamp(modification_time)
            #if the file was modified within 24 hours, move the file
            if one_day_ago < date_time_of_file:
                #Move each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was succesfully transferred.')

    #Create a function to exit the program           
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method 
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
