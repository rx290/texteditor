#Default GUI lib for python
import tkinter as tk

# importing available dialog boxes 
from tkinter.filedialog import askopenfilename, asksaveasfilename

#app initilization
app = tk.Tk()

# Adding a title to the app which has been initialized
app.title('Text Editor')

# Windows Configuration for desktop file row means horizontal scale and column mean vertical scale
app.rowconfigure(1,minsize=800,weight=1)
app.columnconfigure(0,minsize=800,weight=1)
# This configuration will now force our app to have atleast a 800 x 800 windows size

#functionality

def openfile():
    filepath = askopenfilename(
        # Using Some RE to define text files selectin and all file selection
        filetypes= [("Text Files","*.txt"),("All Files","*.*")]
    )
    # if file is not found return nothing so program will continue its execution
    if not filepath:
        return
    # otherwise if there is any content in the text area destroy it
    editor.delete(1.0,tk.END)
    # Now open the file in read mode and as an alias of inputfile
    with open(filepath, "r") as inputfile:
        # If there are characters in the file then treat them as the part of the text file and store them in a variable content
        content = inputfile.read()
        # Add that content to the text area to further use
        editor.insert(tk.END, content)
    # This will show the path file of the text file in the titlebar
    app.title(f"Text Editor - {filepath}")

def savefileas():
    filepath= asksaveasfilename(
        defaultextension='txt',
        filetypes= [("Text Files","*.txt"),("All Files","*.*"),("PDF","*.pdf")]
    )
    if not filepath:
        return
    # Open file in write mode as an alias of outputfile
    with open(filepath, "w") as outputfile:
        # get the content in the text area save it in a variable content
        content = editor.get(1.0,tk.END)
        # now write the content to the file
        outputfile.write(content)
    app.title(f"Text Editor - {filepath}")

def close():
    exit()


# Text area for adding, editing and delete text
editor = tk.Text(app)

# frame or toolbar area to add options / choices as functional buttons
toolbar = tk.Frame(app)

# Open Button
open_button = tk.Button(toolbar , text= 'Open', command = openfile)
# Save as Button
saveas_button = tk.Button(toolbar , text= 'Save As', command = savefileas)
# Close Button
close_button = tk.Button(toolbar , text= 'Close', command = close )

# Placing the buttons by using grid system
open_button.grid(row = 0, column =0, sticky='ew',padx=5 ,pady=5)

saveas_button.grid(row = 0, column =1, sticky='ew',padx=5 ,pady=5)

close_button.grid(row = 0, column =2, sticky='ew',padx=5 ,pady=5)

toolbar.grid(row=0,column =0, sticky ='ns')

editor.grid(row=1, column=0, sticky='nsew')

