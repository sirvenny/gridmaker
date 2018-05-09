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
colour = StringVar(root, value = 'ffffff')
grid_colour = StringVar(root, value = '000000')
num_lines = IntVar()
grid_width = IntVar(root, value = 1)
fade_width = IntVar(root, value = 0)
canvas_size = IntVar(root, value = 300)

#Canvas size
canvas_size_label = Label(frame, text="Canvas size (pixels)")
canvas_size_label.pack(side = TOP, padx = 5, pady = 5)

canvas_size_entry = Entry(frame, bd =5, textvariable=canvas_size)
canvas_size_entry.pack(side = TOP, padx = 5, pady = 5)

#Background Colour Hex input
colour_input_label = Label(frame, text="Background Colour Hex code")
colour_input_label.pack(side = TOP, padx = 5, pady = 5)

colour_entry = Entry(frame, bd =5, textvariable=colour)
colour_entry.pack(side = TOP, padx = 5, pady = 5)

#Grid Colour Hex input
grid_input_label = Label(frame, text="Grid Colour Hex code")
grid_input_label.pack(side = TOP, padx = 5, pady = 5)

grid_colour_entry = Entry(frame, bd =5, textvariable=grid_colour)
grid_colour_entry.pack(side = TOP, padx = 5, pady = 5)

#Number of lines input
num_lines_label = Label(frame, text="Number of Lines")
num_lines_label.pack(side = TOP, padx = 5, pady = 5)

num_lines_entry = Entry(frame, bd =5)
num_lines_entry.pack(side = TOP, padx = 5, pady = 5)

#Grid line width
grid_width_label = Label(frame, text="Grid line width")
grid_width_label.pack(side = TOP, padx = 5, pady = 5)

grid_width_entry = Entry(frame, bd =5, textvariable=grid_width)
grid_width_entry.pack(side = TOP, padx = 5, pady = 5)

#Fade Grid line width
fade_width_label = Label(frame, text="Fade Grid line width")
fade_width_label.pack(side = TOP, padx = 5, pady = 5)

fade_width_entry = Entry(frame, bd =5, textvariable=fade_width)
fade_width_entry.pack(side = TOP, padx = 5, pady = 5)

#convert hex colour to rgb
def hex_to_rgb(hexcolour):
    return(list(int(str(hexcolour)[i:i+2], 16) for i in (0, 2 ,4)))

def rgb_to_hex(rgbcolour):
    r = rgbcolour[0]
    g = rgbcolour[1]
    b = rgbcolour[2]
    return("{:02x}{:02x}{:02x}".format(r,g,b))

#go button
def generate():
    #Reset canvas - delete old grid
    canvas.delete("all")
    canvas.update()
    #change canvas background colour and size
    canvas.configure(bg=('#' + colour.get()), height=canvas_size.get(), width=canvas_size.get())

    #retrive number of lines
    num_lines = int((num_lines_entry.get()))

    #convert hex colour to rgb
    bg_rgb_colour = hex_to_rgb(colour.get())
    grid_rgb_colour = hex_to_rgb(grid_colour.get())
    fade_rgb_colour = [sum(x)/len(x) for x in zip(*[bg_rgb_colour, grid_rgb_colour])]
    fade_rgb_colour = [round(x) for x in fade_rgb_colour]
    fade_hex_colour = rgb_to_hex(fade_rgb_colour)

    #draw horizontal and vertical lines according to num_lines input
    for i in range(num_lines + 1):
        fade_vert_lines = canvas.create_line(i*(canvas_size/(num_lines+1)), 0,
            i*(canvas_size/(num_lines+1)), canvas_size, fill=('#' + fade_hex_colour),
            width=(grid_width.get() + 2*fade_width.get()))

        fade_horiz_lines = canvas.create_line(0, i*(canvas_size/(num_lines+1)),
            canvas_size, i*(canvas_size/(num_lines+1)), fill=('#' + fade_hex_colour),
            width=(grid_width.get() + 2*fade_width.get()))

    for i in range(num_lines + 1):
        vert_lines = canvas.create_line(i*(canvas_size/(num_lines+1)), 0,
            i*(canvas_size/(num_lines+1)), canvas_size, fill=('#' + grid_colour.get()),
            width=grid_width.get())

        horiz_lines = canvas.create_line(0, i*(canvas_size/(num_lines+1)), canvas_size,
            i*(canvas_size/(num_lines+1)), fill=('#' + grid_colour.get()), width=grid_width.get())

#Buttons

generate_btn = tkinter.Button(frame, text="Generate!", command=generate)
generate_btn.pack(side = BOTTOM, padx = 5, pady = 5)

#canvas
canvas = tkinter.Canvas(frame2, bg=('#' + colour.get()), height=canvas_size.get(), width=canvas_size.get())
canvas.pack(side = RIGHT)


frame.mainloop()
