from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Window exe")
topframe = Frame(root,height=100,width=500,bg="red")
topframe.pack(fill=BOTH)
lbl =Label(topframe,text="Label")
lbl.pack(padx=40, pady=40)

topgrid = Frame(root,height=200,width=250)
topgrid.pack()
topleft = Frame(topgrid,height=200, width=250,bg="yellow")
topleft.pack(side=LEFT)
tlbttn = Button(topleft,text = "button")
tlbttn.pack(padx=102,pady=90)
topright = Frame(topgrid,height=200, width=250,bg="green")
topright.pack(side=LEFT)
trbttn = Button(topright,text = "button")
trbttn.pack(padx=102,pady=90)

botgrid = Frame(root,height=200,width=250)
botgrid.pack()
botleft = Frame(botgrid,height=200, width=250,bg="red")
botleft.pack(side=LEFT)
topright.pack(side=LEFT)
brbttn = Button(botleft,text = "button")
brbttn.pack(padx=102,pady=90)
botright = Frame(botgrid,height=200, width=250,bg="blue")
botright.pack(side=LEFT)
topright.pack(side=LEFT)
blbttn = Button(botright,text = "button")
blbttn.pack(padx=102,pady=90)



root.mainloop()