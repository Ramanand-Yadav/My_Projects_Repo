import tkinter as tk
import tkinter.font as font
from tkinter import ttk
root = tk.Tk()
root.title("milestone")


font.nametofont("TkDefaultFont").configure(size=15)

def calculate_feet(*args):
    try:
        metres = float(metre_box.get())
        feets = metres * 3.28084
        feet_values.set(f"{feets:.3f}")
    except ValueError:
        pass


metres_valu = tk.StringVar()
feet_values = tk.StringVar(value="feet shown here")

frame = ttk.Frame(root,padding=(30,15))
frame.grid()

root.columnconfigure(0,weight=1)


metre = ttk.Label(frame,text="Metres:")
metre_box = ttk.Entry(frame,width=10,textvariable=metres_valu,font=("Segoe UI",15))
feet = ttk.Label(frame,text="Feet:")
feet_value = ttk.Label(frame,textvariable=feet_values)
button = ttk.Button(frame,text="Convert",command=calculate_feet)

metre.grid(row=0,column=0,sticky="W")
metre_box.grid(row=0,column=1,sticky="ew")
metre_box.focus()

feet.grid(row=1,column=0,sticky="W")
feet_value.grid(row=1,column=1,sticky="ew")
button.grid(row=2,column=0,columnspan=2,sticky="ew")

for child in frame.winfo_children():
    child.grid_configure(padx=15,pady=15)

root.bind("<Return>",calculate_feet)
root.bind("<KP_Enter>",calculate_feet)


root.mainloop()