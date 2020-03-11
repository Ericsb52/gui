from tkinter import *

root = Tk()

root.title("simple GUI with Label and buttons")
root.geometry("500x500")

app = Frame(root)
app.grid()

lbl = Label(app, text = "this is my Label")
lbl.grid()

bttn = Button(app, text = "do not click me")
bttn.grid()
bttn.config(bg = "red")


root.mainloop()