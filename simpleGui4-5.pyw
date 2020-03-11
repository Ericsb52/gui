from tkinter import *
root = Tk()

root.title("Simple GUI")
root.geometry("500x500")

frame = Frame(root)
frame.grid()

lbl = Label(frame,bg = "green",text = "this is my fancy label")
lbl.grid()

text_ent = Entry(frame)
text_ent.grid()
bttn1 = Button(frame, bg = "red",text = "do not click")
bttn1.grid()



root.mainloop()