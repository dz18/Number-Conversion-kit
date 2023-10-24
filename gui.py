from tkinter import *
from modules import *

tool = Converter()

def print_value():


root = Tk()
root.title("Number Conversion Kit")
# Header Title "Number Conversion Kit"

HeaderTitle = Label(root, text="Welcome to the Number Conversion Kit v1.0\nCreated by Dylan Zuniga.").pack()

selected_option = IntVar()

# Function to be called when a radio button is selected

# Create radio buttons
options = ["Decimal", "Binary", "Hexidecimal"]
for index, option in enumerate(options):
    radio_button = Radiobutton(root, text=option, variable=selected_option, value=index, command=tool)
    radio_button.pack(side=LEFT, padx=10)

# Run the Tkinter main loop
root.mainloop()

root.mainloop()