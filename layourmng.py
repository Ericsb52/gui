from tkinter import *

root = Tk()
###### Pack ######
# Pack is the easiest to use of the three geometry managers of Tk and Tkinter.
# Instead of having to declare precisely where a widget should appear on the display screen,
# we can declare the positions of widgets with the pack command relative to each other.
# The pack command takes care of the details. Though the pack command is easier to use,
# this layout managers is limited in its possibilities compared to the grid and place mangers.
# For simple applications it is definitely the manager of choice.
# For example simple applications like placing a number of widgets side by side,
# or on top of each other.

### simple use of pack() ###
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack()
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()

##### Fill Option #####
# In this example, we have packed three labels into the parent widget "root".
# We used pack() without any options. So pack had to decide which way to arrange the labels.
# As you can see, it has chosen to place the label widgets on top of each other and centre them.
# Furthermore, we can see that each label has been given the size of the text.
# If you want to make the widgets as wide as the parent widget, you have to use the fill=X option:
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill = X)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill = X)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill = X)

##### Padding #####
# The pack() manager knows four padding options, i.e.
# internal and external padding and padding in x and y direction:
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill = X, padx = 10, pady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill = X, padx = 10, pady=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill = X, padx = 10, pady=10)

##### Internal padding, horizontally, vertically. #####
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(ipady=10)

##### Placing widgets side by side #####
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(padx=5, pady=10, side=LEFT)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(padx=5, pady=10, side=LEFT)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(padx=5, pady=10, side=LEFT)

w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(padx=5, pady=10, side=RIGHT)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(padx=5, pady=10, side=RIGHT)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(padx=5, pady=10, side=RIGHT)

root.mainloop()