import tkinter
from tkinter import *
from PIL import Image
import io

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
num_lines = IntVar(root, value = 1)
grid_width = IntVar(root, value = 1)
fade_width = IntVar(root, value = 0)
canvas_size = IntVar(root, value = 300)
filename = StringVar(root, value = 'image')
outline_width = IntVar(root, value = 1)

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

num_lines_entry = Entry(frame, bd =5, textvariable=num_lines)
num_lines_entry.pack(side = TOP, padx = 5, pady = 5)

#Grid line width
grid_width_label = Label(frame, text="Grid line width")
grid_width_label.pack(side = TOP, padx = 5, pady = 5)

grid_width_entry = Entry(frame, bd =5, textvariable=grid_width)
grid_width_entry.pack(side = TOP, padx = 5, pady = 5)

#Outline line width
outline_width_label = Label(frame, text="Outline line width")
outline_width_label.pack(side = TOP, padx = 5, pady = 5)

outline_width_entry = Entry(frame, bd =5, textvariable=outline_width)
outline_width_entry.pack(side = TOP, padx = 5, pady = 5)

#Fade Grid line width
fade_width_label = Label(frame, text="Fade Grid line width")
fade_width_label.pack(side = TOP, padx = 5, pady = 5)

fade_width_entry = Entry(frame, bd =5, textvariable=fade_width)
fade_width_entry.pack(side = TOP, padx = 5, pady = 5)

#Filename
filename_label = Label(frame, text="File name")
filename_label.pack(side = TOP, padx = 5, pady = 5)

filename_entry = Entry(frame, bd =5, textvariable=filename)
filename_entry.pack(side = TOP, padx = 5, pady = 5)

#convert hex colour to rgb
def hex_to_rgb(hexcolour):
    return(list(int(str(hexcolour)[i:i+2], 16) for i in (0, 2 ,4)))

def rgb_to_hex(rgbcolour):
    r = rgbcolour[0]
    g = rgbcolour[1]
    b = rgbcolour[2]
    return("{:02x}{:02x}{:02x}".format(r,g,b))

def save():
    filename = filename_entry.get() + '.jpg'
    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save(filename)


#go button
def generate():
    #Reset canvas - delete old grid
    canvas.delete("all")
    canvas.update()

    #retrieve canvas size
    canvas_size = int(canvas_size_entry.get())

    #retrive number of lines
    num_lines = int(num_lines_entry.get())

    #retrieve outline width
    outline_width = outline_width_entry.get()

    #change canvas background colour and size
    canvas.configure(bg=('#' + colour.get()), height=canvas_size, width=canvas_size)

    #convert hex colour to rgb
    bg_rgb_colour = hex_to_rgb(colour.get())
    grid_rgb_colour = hex_to_rgb(grid_colour.get())
    fade_rgb_colour = [sum(x)/len(x) for x in zip(*[bg_rgb_colour, grid_rgb_colour])]
    fade_rgb_colour = [round(x) for x in fade_rgb_colour]
    fade_hex_colour = rgb_to_hex(fade_rgb_colour)

    #draw background as box for postscript save to work
    background_box = canvas.create_rectangle(0, 0, canvas_size + 10, canvas_size + 10, fill = '#' + colour.get())

    #draw horizontal and vertical lines according to num_lines input
    #draw fade lines
    for i in range(num_lines + 1):
        fade_vert_lines = canvas.create_line(i*(canvas_size/(num_lines+1)), 0,
            i*(canvas_size/(num_lines+1)), canvas_size, fill=('#' + fade_hex_colour),
            width=(grid_width.get() + 2*fade_width.get()))

        fade_horiz_lines = canvas.create_line(0, i*(canvas_size/(num_lines+1)),
            canvas_size, i*(canvas_size/(num_lines+1)), fill=('#' + fade_hex_colour),
            width=(grid_width.get() + 2*fade_width.get()))

    #draw grid lines
    for i in range(1, num_lines + 1):
        vert_lines = canvas.create_line(i*(canvas_size/(num_lines+1)), 0,
            i*(canvas_size/(num_lines+1)), canvas_size + 10, fill=('#' + grid_colour.get()),
            width=grid_width.get())

        horiz_lines = canvas.create_line(0, i*(canvas_size/(num_lines+1)), canvas_size + 10,
            i*(canvas_size/(num_lines+1)), fill=('#' + grid_colour.get()), width=grid_width.get())

    #draw outline Lines
    top_outline = canvas.create_line(0, 0, canvas_size+10, 0, fill=('#' + grid_colour.get()), width=int(outline_width)*1)
    bottom_outline = canvas.create_line(0, canvas_size + 4, canvas_size+10, canvas_size + 4, fill=('#' + grid_colour.get()), width=int(outline_width)*1)
    left_outline = canvas.create_line(0, 0, 0, canvas_size+10, fill=('#' + grid_colour.get()), width=int(outline_width)*1)
    right_outline = canvas.create_line(canvas_size + 4, 0, canvas_size + 4, canvas_size+10, fill=('#' + grid_colour.get()), width=int(outline_width)*1)

#Buttons
#save button
save_btn = tkinter.Button(frame, text="Save", command=save)
save_btn.pack(side = BOTTOM, padx = 5, pady = 5)

#generate button
generate_btn = tkinter.Button(frame, text="Generate!", command=generate)
generate_btn.pack(side = BOTTOM, padx = 5, pady = 5)

#canvas
canvas = tkinter.Canvas(frame2, bg=('#' + colour.get()), height=canvas_size.get(), width=canvas_size.get())
canvas.pack(side = RIGHT)

frame.mainloop()
