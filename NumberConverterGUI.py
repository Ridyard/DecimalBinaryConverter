
# binary & decimal converter, GUI

from tkinter import *
from NumberConverterFunctions import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText


# convert decimal to binary
def dec2bin(num):
    # call the Decimal to Binary function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    d2bOutput = decToBinary(int(num), bRunningTotal)
    updateOutput(num, d2bOutput, "binary")


# convert binary to decimal
def bin2dec(num):
    # call the Binary to Decimal function; it takes a 'running-total' list as an arg
    dRunningTotal = []
    b2dOutput = binaryToDec(int(num), dRunningTotal)
    b2dOutput = f"{b2dOutput:,}"
    updateOutput(num, b2dOutput, "decimal")


# convert decimal to hex
def dec2hex(num):
    # call the Decimal to Hex function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    d2hOutput = decToHex(num, bRunningTotal)
    print(d2hOutput)
    updateOutput(num, d2hOutput, "hexadecimal")   


# convert hex to decimal
def hex2dec(num):
    # call the Hex to Decimal function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    h2dOutput = hexToDec(num, bRunningTotal)
    h2dOutput = f"{h2dOutput:,}"
    updateOutput(num, h2dOutput, "decimal")  


# convert binary to hexadecimal
def bin2hex(num):
    # call the Binary to Hex function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    b2hOutput = binToHex(num, bRunningTotal)
    updateOutput(num, b2hOutput, "hexadecimal") 


# convert hexadecimal to binary
def hex2bin(num):
    # call the Hex to Binary function; it takes a 'running-total' list as an arg
    bRunningTotal = [] 
    h2bOutput = hexToBinary(num, bRunningTotal)
    updateOutput(num, h2bOutput, "binary") 


# update & display via the output widgets
def updateOutput(num, numOutput, numFormat):
    numDigits = len(str(num))
    numOutputDigits = len(str(numOutput))

    # update the label
    outputLabel.config(text=str(num) + " (" + str(numDigits) + " digits)" + " in " + numFormat + " is \n" + str(numOutput) + " (" + str(numOutputDigits) + " digits)")

    # update the value in the entry box
    numBox.delete(0, END)
    numBox.insert(0, str(numOutput))

def updateScrollBar(*args):
    numBox.xview(*args)

# called from the "go" button; get the number formats and call the relevant conversion function
def clickHandler(numIn):

    if ',' in numIn:
        numIn = numIn.replace(",","") # standardise by removing any comma-separators

    if clickedFrom.get() == "decimal" and clickedTo.get() == "binary":
        dec2bin(int(numIn)) # standardise entry by converting to int
    
    if clickedFrom.get() == "binary" and clickedTo.get() == "decimal":
        bin2dec(int(numIn)) # standardise entry by converting to int

    if clickedFrom.get() == "decimal" and clickedTo.get() == "hexadecimal":
        dec2hex(int(numIn)) # standardise entry by converting to int

    if clickedFrom.get() == "hexadecimal" and clickedTo.get() == "decimal":
        hex2dec(numIn.upper()) # standardise entry by converting to upper-case

    if clickedFrom.get() == "binary" and clickedTo.get() == "hexadecimal":
        bin2hex(int(numIn)) # standardise entry by converting to int

    if clickedFrom.get() == "hexadecimal" and clickedTo.get() == "binary":
        hex2bin(numIn.upper()) # standardise entry by converting to upper-case

    if clickedFrom.get() == "Select Number Type" or clickedTo.get() == "Select Number Type":
        outputLabel.config(text="Please select number type(s)")



#=================================
# widgets:


# set root window
root=tb.Window(themename="superhero")
#root = Tk()
root.title("Number Converter")
root.geometry("650x380")
root.iconbitmap(r'C:\Users\alexa\Documents\Workspace\Python\Projects - small\Decimal Converter\file_binary_icon_160156.ico') # needs to be an ico file, as a raw string

# label
promptLabel = Label(root, text="From")
promptLabel.grid(row=0, column=0, pady=(50,0))#, columnspan=4, padx=50, pady=(30,0))

# options for dropdown menus
options = ["decimal","binary","hexadecimal"]
clickedFrom = StringVar()
clickedFrom.set("Select Number Type")
clickedTo = StringVar()
clickedTo.set("Select Number Type")

# 'from' number-type dropdown
numFrom = OptionMenu(root, clickedFrom, *options)
numFrom.config(width=20)
numFrom.grid(row=1, column=0, columnspan=1, padx=(50,0))

# "convert to" label
prompt2Label = Label(root, text="Convert to", justify=CENTER)
prompt2Label.grid(row=1, column=1, padx=20)

# label
promptLabel = Label(root, text="To")
promptLabel.grid(row=0, column=2, pady=(30,0))

# 'to' number-type dropdown
numTo = OptionMenu(root, clickedTo, *options)
numTo.config(width=20)
numTo.grid(row=1, column=2, columnspan=1)

# # entry text box
# numBox = tb.Entry(root, width=40, justify=CENTER, bootstyle="primary active", font=("Helvetica", 14))
# numBox.grid(row=2, column=0, columnspan=3, padx=(50,0), pady=(50,0), sticky="ew")
# entryScroll = tb.Scrollbar(root, orient="horizontal", command=updateScrollBar)
# entryScroll.grid(row=3, column=0, columnspan=3)
# numBox.config(xscrollcommand=entryScroll.set)

# Create a frame to contain the entry widget and scrollbar
entry_frame = Frame(root)
entry_frame.grid(row=2, column=0, columnspan=3, padx=(50, 0), pady=(50, 0), sticky="ew")

# entry text box
numBox = tb.Entry(entry_frame, width=40, justify=CENTER, bootstyle="primary active", font=("Helvetica", 14))
numBox.grid(row=0, column=0, sticky="ew")

# Create a horizontal scrollbar for the entry widget
entryScroll = tb.Scrollbar(entry_frame, orient="horizontal", command=updateScrollBar)
entryScroll.grid(row=1, column=0, sticky="ew")

# Configure the entry widget to use the scrollbar for horizontal scrolling
numBox.config(xscrollcommand=entryScroll.set)



# convert button
conButt = tb.Button(root, text="Convert...", command=lambda:clickHandler(numBox.get()), bootstyle="primary outline")
conButt.grid(row=3, column=1, pady=(30,0))

# label to print the output
outputLabel = Label(root, text="", justify=CENTER)
outputLabel.grid(row=4, column=0, columnspan=3, padx=(50,0), pady=(25,0))

# Set grid row and column weights to make the Entry widget expand horizontally
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)


root.mainloop()
