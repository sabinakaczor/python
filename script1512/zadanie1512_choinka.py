#coding: utf-8

from Tkinter import *
root = Tk()
root.title("Choinka")

canvas = Canvas(root, width=400, height = 600, bg="white")
canvas.pack(expand = YES, fill = BOTH)


canvas.create_polygon((200, 50, 150, 110, 250, 110), fill="green")
canvas.create_polygon((180, 110, 130, 170, 270, 170, 220, 110), fill="green")
canvas.create_polygon((160, 170, 110, 230, 290, 230, 240, 170), fill="green")
canvas.create_polygon((140, 230, 90, 290, 310, 290, 260, 230), fill="green")
canvas.create_polygon((120, 290, 70, 360, 330, 360, 280, 290), fill="green")


canvas.create_rectangle(190,360,211,381,fill='black')

canvas.create_oval(160,100,180,120, width=2, fill='yellow')
canvas.create_oval(220,100,240,120, width=2, fill='blue')
canvas.create_oval(150,160,170,180, width=2, fill='blue')
canvas.create_oval(200,150,220,170, width=2, fill='orange')
canvas.create_oval(130,220,150,240, width=2, fill='red')
canvas.create_oval(260,220,280,240, width=2, fill='red')
canvas.create_oval(250,270,270,290, width=2, fill='yellow')
canvas.create_oval(220,310,240,330, width=2, fill='blue')
canvas.create_oval(110,340,130,360, width=2, fill='red')
canvas.create_oval(280,340,300,360, width=2, fill='orange')
canvas.create_oval(190,230,210,250, width=2, fill='blue')
canvas.create_oval(140,280,160,300, width=2, fill='orange')


#canvas.create_arc(180,120,240,200)


root.mainloop()