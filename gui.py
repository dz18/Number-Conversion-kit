from modules.converters import Converter
from tkinter import *

root = Tk()
root.title("Number Conversion Kit")

tool = Converter()

def convert_input():
      option = selected_option.get()
      tool.set_source(option)
      user_input = str(entry.get())
      results = tool.convert(user_input)
      
      decimal_label.config(text=results[0])
      binary_label.config(text=tool.format_bin(results[1]))
      hex_label.config(text=results[2])
      


HeaderTitle = Label(root, 
                    text="Welcome to the Number Conversion Kit v1.0\nCreated by Dylan Zuniga.",)
HeaderTitle.pack(pady=20)

selected_option = StringVar()

frame1 = Frame(root)
frame1.pack()

Radiobutton(frame1, 
            text="Decimal", 
            variable=selected_option, 
            value="Decimal"
            ).pack(side=LEFT, padx=10)
Radiobutton(frame1, 
            text="Binary", 
            variable=selected_option, 
            value="Binary"
            ).pack(side=LEFT, padx=10)
Radiobutton(frame1, 
            text="Hexidecimal",
            variable=selected_option, 
            value="Hexidecimal", 
            command=tool
            ).pack(side=LEFT, padx=10)

Button(frame1, 
       text="Convert",
       command=convert_input
       ).pack(side=LEFT, padx=10)

spacer1 = Frame(root)
spacer1.pack(pady=5)

InputText = Frame(root)
InputText.pack()
Label(InputText,
      text="Input:                                                                                                              "
      ).pack(side=LEFT)

InputEntry = Frame(root)
InputEntry.pack()
entry = Entry(InputEntry,
              width=60,
              )
entry.pack()

spacer2 = Frame(root)
spacer2.pack(pady=10)

decimalText = Frame(root)
decimalText.pack()
Label(decimalText,
      text="Decimal:                                                                                                          "
      ).pack(side=LEFT)

decimalAnswer = Frame(root)
decimalAnswer.pack()
decimal_label = Label(decimalAnswer,  # Store the label in a variable to update its text later
                     width=52,
                     bg="white",
                     bd=1,
                     relief=SUNKEN)
decimal_label.pack()

BinaryText = Frame(root)
BinaryText.pack()
Label(BinaryText,
      text="Binary:                                                                                                             "
      
      ).pack(side=LEFT)

BinaryAnswer = Frame(root)
BinaryAnswer.pack()
binary_label = Label(BinaryAnswer,
                     width=52,
                     bg="white",
                     bd=1,
                     relief=SUNKEN,
                     )
binary_label.pack()

HexidecimalText = Frame(root)
HexidecimalText.pack()
Label(HexidecimalText,
      text="Hexidecimal:                                                                                                 "
      ).pack(side=LEFT)

HexidecimalAnswer = Frame(root)
HexidecimalAnswer.pack()
hex_label = Label(HexidecimalAnswer,
                          width=52,
                          bg="white",
                          bd=1,
                          relief=SUNKEN,
                          )
hex_label.pack()



root.mainloop()