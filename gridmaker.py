import tkinter
from tkinter import *

#creates frame
top = Tk()
frame = Frame(top)
frame2 = Frame(top)
frame.pack(side = LEFT)
frame2.pack(side = RIGHT)


#Colour Hex input
colour_input_txt = Label(frame, text="Colour Hex code")
colour_input_txt.pack(side = TOP, padx = 5, pady = 5)
colour_entry = Entry(frame, bd =5)
colour_entry.pack(side = TOP, padx = 5, pady = 5)

#go button
generate = tkinter.Button(frame, text="Generate!")
generate.pack(side = BOTTOM, padx = 5, pady = 5)


label1 = Label(frame, text=colour_entry.get())
label1.pack(side = TOP, padx = 5, pady = 5)

#canvas
grid = tkinter.Canvas(frame2, bg="blue", height=300, width=300)

coord = 10, 50, 240, 210
arc = grid.create_arc(coord, start=0, extent=150, fill="red")

grid.pack(side = RIGHT)


top.mainloop()
