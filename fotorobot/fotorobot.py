from tkinter import*
fotorobot=Tk()
fotorobot.title("Фоторобот")

canvas=Canvas(fotorobot,width=620, height=350, bd=0, highlightthickness=0)
canvas.pack()
fotorobot.update

def on_wasd(event):
    print(event.x, event.y)
    mouse_x=canvas.winfo_pointerx()-canvas.winfo_rootx()
    mouse_y=canvas.winfo_pointery()-canvas.winfo_rooty()
    print("Real mouse x,y: ", mouse_x, mouse_y)
canvas.bind_all("<Button-1>", on_wasd)
canvas.bind_all("<Button-3>", on_wasd)

def head():
    c.create_rectangle((290, 60, 60, 290), fill="black", outline="black", width="3")
    c.create_polygon([(95,287), (95,85), (253,85), (253,287)], fill="white") 

def eyes():
    c.create_rectangle((105, 105, 150, 150), fill="blue", outline="black", width="4")
    c.create_rectangle((102, 102, 147, 147), fill="white", outline="white", width="0")
    c.create_rectangle((250, 105, 205, 150), fill="blue", outline="black", width="4")
    c.create_rectangle((247, 102, 202, 147), fill="white", outline="white", width="0")

def mouth():
    c.create_polygon([(164, 161), (164, 196), (363, 181)], fill="orange", outline="black")

def hair():
    c.create_polygon([(57, 55), (107, 55), (69, 95)], fill="red")
    c.create_polygon([(62, 55), (112, 55), (94, 95)], fill="orange")
    c.create_polygon([(93, 55), (143, 55), (112, 95)], fill="yellow")
    c.create_polygon([(110, 55), (160, 55), (134, 95)], fill="lightgreen")
    c.create_polygon([(139, 55), (189, 55), (156, 95)], fill="green")
    c.create_polygon([(157, 55), (207, 55), (180, 95)], fill="blue")
    c.create_polygon([(190, 55), (240, 55), (204, 95)], fill="purple")
    c.create_polygon([(205, 55), (255, 55), (230, 95)], fill="grey")
    c.create_polygon([(231, 55), (281, 55), (250, 95)], fill="brown")
    c.create_polygon([(253, 55), (296, 55), (266, 95)], fill="black")
    
def lol():
    c.create_polygon([(334, 55), (369, 187), (332, 55)], fill="beige", outline="black")

f1=Frame(canvas,width=620,height=300)
f1.pack(side=LEFT)

f2=Frame(canvas,width=620,height=300)
f2.pack(side=RIGHT)

lbl=Label(f1,text="Фоторобот",font="Calibri 36",fg="black",justify=CENTER)
lbl.pack()

w1=Checkbutton(f1,text="Голова",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=head)
w1.pack(side=BOTTOM)

w2=Checkbutton(f1,text="Рот",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=mouth)
w2.pack(side=BOTTOM)

w4=Checkbutton(f1,text="Глаза",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=eyes)
w4.pack(side=BOTTOM)

w3=Checkbutton(f1,text="Волосы",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=hair)
w3.pack(side=BOTTOM)

w5=Checkbutton(f1,text="Оружие убийства",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=lol)
w5.pack(side=BOTTOM)

c=Canvas(f2, width=600, height=350, bg="lightblue") 
c.pack() 

fotorobot.mainloop()
