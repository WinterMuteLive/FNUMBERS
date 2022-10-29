from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import messagebox

def draw(event):
  x1, y1 = (event.x - 5), (event.y - 5)
  x2, y2 = (event.x + 5), (event.y + 5)
  canvas.create_oval(x1, y1, x2, y2, fill=COLOR, width=5)
  draw.ellipse((x1, y1, x2, y2), fill=COLOR, width=5)

def clear_canvas():
  canvas.delete('all')
  #draw.rectangle((0,0,320,320), width=0, fill='white')

x = 0
y = 0

root = Tk()
root.title("Цифроблядствищество")
root.geometry('320x320')
root.resizable(0,0)

COLOR = 'black'

root.columnconfigure(6, weight=1)    
root.rowconfigure(2, weight=1)  

canvas = Canvas(root, bg='white')
canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
#HUI = Button(text='GOTOHUI', width=10, command=clear_canvas)
#HUI.pack(0)

canvas.bind('<B1-Motion>', draw)
canvas.bind('<B3-Motion>', clear_canvas)
canvas.pack(expand=1, fill=BOTH)

image1 = Image.new('RGB', (320, 320), 'white')
draw = ImageDraw.Draw(image1)

root.mainloop()
