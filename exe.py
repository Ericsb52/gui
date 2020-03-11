from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Window exe")

top = Frame(root,bg="red",height=100,width=500)
top.pack(fill=BOTH)
lbl = Label(top,text="Label")
lbl.pack(padx=40,pady=40)

mid = Frame(root,bg="orange",height=150,width=500)
mid.pack()

topleft = Frame(mid,bg="yellow",height=146,width=246)
topleft.pack(fill=BOTH,padx=2,pady=2,side=LEFT)

topright = Frame(mid,bg="green",height=146,width=246)
topright.pack(fill=BOTH,padx=2,pady=2,side=LEFT)

bot = Frame(root,bg="blue",height=150,width=500)
bot.pack()

root.mainloop()