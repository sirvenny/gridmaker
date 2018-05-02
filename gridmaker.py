import tkinter
from tkinter import *

#creates frame
top = Tk()
frame = Frame(top)
frame2 = Frame(top)
frame.pack(side = LEFT)
frame2.pack(side = RIGHT)

#set default value
colour = StringVar()
colour.set('#ffffff')

#Colour Hex input
colour_input_txt = Label(frame, text="Colour Hex code")
colour_input_txt.pack(side = TOP, padx = 5, pady = 5)
colour_entry = Entry(frame, bd =5)
colour_entry.pack(side = TOP, padx = 5, pady = 5)

#go button
def gen_colour():
    colour.set(colour_entry.get())
    grid.configure(bg=colour.get())



generate = tkinter.Button(frame, text="Generate!", command=gen_colour)
generate.pack(side = BOTTOM, padx = 5, pady = 5)

label1 = Label(frame, textvariable=colour)
label1.pack(side = TOP, padx = 5, pady = 5)

#canvas
grid = tkinter.Canvas(frame2, bg=colour.get(), height=300, width=300)

coord = 10, 50, 240, 210
grid.create_line(100, 0, 100, 300)


grid.pack(side = RIGHT)


frame.mainloop()
