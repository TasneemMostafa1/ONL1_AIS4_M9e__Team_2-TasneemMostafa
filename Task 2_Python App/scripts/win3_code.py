from tkinter import *
from tkinter import ttk
class Win3Code():
    def win3_fcn(self):
        self.win3=Toplevel()
        self.win3.title("tk")
        self.ws = self.win3.winfo_screenwidth()
        pos_x=round((self.ws-500)/2)
        self.hs = self.win3.winfo_screenheight()
        pos_y=round((self.hs-300)/2)
        self.win3.geometry("500x300+"+str(pos_x)+"+"+str(pos_y))
        self.win3.config(bg="white")
        self.win3.attributes("-topmost",0)
        self.win3.overrideredirect(0)
        self.label2=Label(self.win3,
                text="Label",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                )
        self.label1=Label(self.win3,
                text="Label",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                )
        self.label=Label(self.win3,
                text="Label",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                )
        self.butt=Button(self.win3,
                text="Close",
                bg="gray",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                activebackground="white",
                activeforeground="black",
                relief="flat",
                )
        self.label2.place(x=62,y=154,width=333,height=39)
        self.label1.place(x=62,y=96,width=333,height=36)
        self.label.place(x=59,y=39,width=336,height=35)
        self.butt.place(x=333,y=226,width=56,height=29)