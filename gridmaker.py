import tkinter
from tkinter import *

#creates frame

class FRM(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
root = Tk()
app = FRM(master=root)
app.master.title("Gridmaker")

frame = Frame(root)
frame2 = Frame(root)
frame.pack(side = LEFT)
frame2.pack(side = RIGHT)

#set default values
colour = StringVar(root, value = '#ffffff')
num_lines = IntVar()
canvasx = 300
canvasy = 300

#Colour Hex input
colour_input_txt = Label(frame, text="Colour Hex code")
colour_input_txt.pack(side = TOP, padx = 5, pady = 5)
colour_entry = Entry(frame, bd =5, textvariable=colour)
colour_entry.pack(side = TOP, padx = 5, pady = 5)

#Number of lines input
num_lines_label = Label(frame, text="Number of Lines")
num_lines_label.pack(side = TOP, padx = 5, pady = 5)
num_lines_entry = Entry(frame, bd =5)
num_lines_entry.pack(side = TOP, padx = 5, pady = 5)


#go button
def generate():
    canvas.configure(bg=colour.get())
    num_lines = int((num_lines_entry.get()))

    for i in range(num_lines + 1):
        horiz_lines = canvas.create_line(i*(canvasx/(num_lines+1)), 0, i*(canvasx/(num_lines+1)), canvasy)
        vert_lines = canvas.create_line(0, i*(canvasy/(num_lines+1)), canvasx, i*(canvasy/(num_lines+1)))

# Reset Button
def reset():
    canvas.delete("all")
    canvas.update()

#Buttons
reset_btn = tkinter.Button(frame, text="Reset lines", command=reset)
reset_btn.pack(side = BOTTOM, padx = 5, pady = 5)

generate_btn = tkinter.Button(frame, text="Generate!", command=generate)
generate_btn.pack(side = BOTTOM, padx = 5, pady = 5)

#canvas
canvas = tkinter.Canvas(frame2, bg=colour.get(), height=canvasy, width=canvasx)
canvas.pack(side = RIGHT)


frame.mainloop()
