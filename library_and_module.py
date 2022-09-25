




from modules import module1



# get data from imported file

print(module1.data)

summed = module1.sum(2, 3)
print(summed)





# module

from modules import math

summed_data = math.sum(1, 2, 3, 4, 5, 6, 7)
print(summed_data)

multiplied_data = math.multiply(2, 4, 5)
print(multiplied_data)






from modules.math import multiply, sum_two_numbers as sumsum

multiplied2 = multiply(10, 10, 10)
print(multiplied2)

sum2num = sumsum(2, 4)
print(sum2num)





# standard library

import datetime

time = datetime.datetime.now()
print(time)
print(time.year)







import tkinter as tk
from tkinter import ttk # theme tkinter (for edit views)
from tkinter.messagebox import showinfo


window = tk.Tk()

window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)

window.title("Hey")


def handle_submit():
    
    if first_name.get() == "":
        showinfo(title="Try Again", message= "input your first name")
    elif last_name.get() == "":
        showinfo(title="Try Again", message= "input your last name")
    else:
        showinfo(title="Hello", message= f"Hello {first_name.get()} {last_name.get()}")
    
        




input_frame = ttk.Frame(window)
input_frame.pack(padx="10", pady="10", fill="x", expand="true")



# label
first_name_label = ttk.Label(input_frame, text="First Name")
first_name_label.pack(padx="10", fill="x", expand="true")

# inputs
first_name = tk.StringVar()

first_name_input = ttk.Entry(input_frame, textvariable = first_name)
first_name_input.pack(padx="10", fill="x", expand="true")



# label
last_name_label = ttk.Label(input_frame, text="Last Name")
last_name_label.pack(padx="10", fill="x", expand="true")

# inputs
last_name = tk.StringVar()

last_name_input = ttk.Entry(input_frame, textvariable = last_name)
last_name_input.pack(padx="10", fill="x", expand="true")


submit_btn = ttk.Button(input_frame, text="Submit", command = handle_submit) # command do handle_submit function when button clicked
submit_btn.pack(fill="x", expand=True, padx=10, pady=10)






window.mainloop()



