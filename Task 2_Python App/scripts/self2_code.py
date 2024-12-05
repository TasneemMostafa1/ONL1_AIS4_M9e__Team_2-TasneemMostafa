from tkinter import *
from tkinter import ttk
class Self2Code():
    def self2_fcn(self):
        self.self2=Toplevel()
        self.self2.title("tk")
        self.ws = self.self2.winfo_screenwidth()
        pos_x=round((self.ws-500)/2)
        self.hs = self.self2.winfo_screenheight()
        pos_y=round((self.hs-500)/2)
        self.self2.geometry("500x500+"+str(pos_x)+"+"+str(pos_y))
        self.self2.config(bg="white")
        self.self2.attributes("-topmost",0)
        self.self2.overrideredirect(0)
        self.Checkbutton5=Checkbutton(self.self2,
                text="Checkbutton",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                highlightcolor=None,
                highlightbackground=None,
                activebackground=None,
                activeforeground=None,
                )
        self.Label1=Label(self.self2,
                text="choose columns that you want ",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.Checkbutton5.place(x=11,y=54,width=121,height=30)
        self.Label1.place(x=10,y=10,width=284,height=36)