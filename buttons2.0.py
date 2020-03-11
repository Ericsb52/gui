from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.button_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.frame_top = Frame(self,height = 100, width = 500,bg = "grey")
        self.frame_top.grid(row = 0, column = 0, columnspan = 2)
        self.lbl = Label(self.frame_top, text = "I have clicked the button " + str(self.button_clicks) + " Times")
        self.lbl.grid(row = 0, column = 0, columnspan = 2)


        self.frame1_0 = Frame(self, height = 200, width = 250,bg = "green")
        self.frame1_0 .grid(row=1, column=0)
        self.bttn1 = Button(self.frame1_0,text = "add to count")
        self.bttn1.grid()
        self.bttn1["command"] = self.add_to_count
        

        self.frame1_1 = Frame(self, height=200, width=250, bg="blue")
        self.frame1_1.grid(row=1, column=1)

        self.frame2_0 = Frame(self, height=200, width=250, bg="brown")
        self.frame2_0.grid(row=2, column=0)

        self.frame2_1 = Frame(self, height=200, width=250, bg="yellow")
        self.frame2_1.grid(row=2, column=1)

    def add_to_count(self):
        self.button_clicks +=1
        self.lbl.config(text = "I have clicked the button " + str(self.button_clicks) + " Times")




def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Buttons 2.0")

    #create application
    app = App(root)

    root.mainloop()
main()
