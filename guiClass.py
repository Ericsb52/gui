from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self,text = "You have clicked the button "+str(self.bttn_clicks) + " Times")
        self.lbl.grid()

        self.bttn1 = Button(self,text = "Add to Count")
        self.bttn1.grid()
        self.bttn1["command"] = self.add_to_count


        Label(self,text = "this is button 2").grid()
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.config(text = "do not click")

        Label(self, text="this is button 3").grid()
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "realy do not Click!!!!!!!!!"

    def add_to_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.lbl.config(text = "You have clicked the button "+str(self.bttn_clicks) + " Times")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg = "green")
        else:
            self.lbl.config(bg = "red")


def main():
    root = Tk()
    root.title("Buttons 2.0")
    root.geometry("720x1080")
    app = Application(root)
    root.mainloop()

main()

