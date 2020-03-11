from tkinter import *

class Main_menu(Frame):
    def __init__(self,master):
        super(Main_menu, self).__init__(master)
        self.master = master
        self.create_buttons(master)
        self.create_window(master)

    def create_buttons(self,master):
        self.frame = Frame(master,width = 250,height = 500)
        self.frame.pack()
        self.frame.config(bg = "grey")
        self.frame.grid(column = 0,sticky = W)
        self.lbl = Label(self.frame,text = "Options")
        self.lbl.grid(column = 0, row = 0 )
        self.bttn_basic_calc = Button(self.frame,text = "Basic Calculator")
        self.bttn_basic_calc.grid()
        self.bttn_basic_calc["command"] = self.create_basic_calc

    def create_window(self,master):
        self.frame = Frame(master)
        self.frame.grid(column=1,row = 0,sticky = E)
        self.frame.config(bg="black")
        self.lbl = Label(self.frame, text="Option")
        self.lbl.grid(column=0, row=0)
        self.bttn_basic_calc = Button(self.frame, text="Basic Calculator")
        self.bttn_basic_calc.grid()
        self.bttn_basic_calc["command"] = self.create_basic_calc


    def create_basic_calc(self):
        pass

        








def main():
    root = Tk()
    root.title("Enginering calculator")
    root.geometry("800x800")
    menu = Main_menu(root)
    root.mainloop()

main()
