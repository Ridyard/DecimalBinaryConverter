# binary & decimal converter, GUI

from tkinter import *
from NumberConverterFunctions import decToBinary, binaryToDec


# convert decimal to binary
def d2b(num):
    # call the Decimal to Binary function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    d2bOutput = decToBinary(num, bRunningTotal)
    print(d2bOutput)

    updateOutput(num, d2bOutput, "binary")


# convert binary to decimal
def b2d(num):
    # call the Binary to Decimal function; it takes a 'running-total' list as an arg
    dRunningTotal = []
    b2dOutput = binaryToDec(list(str(num)), dRunningTotal)

    updateOutput(num, b2dOutput, "decimal")
    

# update & display via the output widgets
def updateOutput(num, numOutput, numFormat):
    # update the label
    outputLabel.config(text=str(num) + " in " + numFormat + " is " + str(numOutput))

    # update the value in the entry box
    numBox.delete(0, END)
    numBox.insert(0, str(numOutput))



# set root window
root = Tk()
root.title("Binary & Decimal Number Converter")
root.geometry("375x250")


# set window widgets:
# label
promptLabel = Label(root, text="Enter a number")
promptLabel.grid(row=0, column=2, columnspan=4, padx=50, pady=(30,0))

# entry text box
numBox = Entry(root, width=55)
numBox.grid(row=1, column=2, columnspan=4, padx=(20,0), pady=15)

prompt2Label = Label(root, text="Convert to...")
prompt2Label.grid(row=2, column=2, columnspan=4, padx=50, pady=(0,20))

# button: convert to binary
binButt = Button(root, text="Binary", command=lambda:d2b(int(numBox.get())))
binButt.grid(row=3, column=3)

# button: convert to decimal
decButt = Button(root, text="Decimal", command=lambda:b2d(int(numBox.get())))
decButt.grid(row=3, column=4)

# label to print the output
outputLabel = Label(root, text="")
outputLabel.grid(row=4, column=2, columnspan=4, pady=25)














root.mainloop()