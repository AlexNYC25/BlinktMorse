# create the main layout for the GUi in this file

import tkinter as tk
from MorseAlphabet import *
from MainMorse import *

def printContents():
    MorseTest.conversion(stringEntryField.get())
    stringEntryField.delete(0, "end")

MorseTest = MainMorse()

mainWindow = tk.Tk()
mainWindow.title("Blinkit Morse Tool")

stringEntryField = tk.Entry(mainWindow)
processButton = tk.Button(master=mainWindow, text="GO", command=printContents)


stringEntryField.grid(row=0, columnspan=3)
processButton.grid(row=1, column=1)

mainWindow.mainloop()