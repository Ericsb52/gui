from tkinter import *

master=Tk()
master.geometry("500x500")
master.config(bg = "black")
baseFrame = Frame(master,width = 399, height = 299, bg = "black")
baseFrame.grid(sticky = NSEW)


frame1=Frame(baseFrame, width=100, height=100, background="Blue")
frame1.grid(row=0, column=0)

frame2=Frame(baseFrame, width=200, height=150, background="Red")
frame2.grid(row=1, column=0)

frame3=Frame(baseFrame, width=200, height=150, background="Green")
frame3.grid(row=0, column=1)

frame4=Frame(baseFrame, width=200, height=150, background="Yellow")
frame4.grid(row=1, column=1)

master.mainloop()