from tkinter import *
from tkinter import ttk
class Win1Code():
    def win1_fcn(self):
        self.win1=Toplevel()
        self.win1.title("tk")
        self.ws = self.win1.winfo_screenwidth()
        pos_x=round((self.ws-600)/2)
        self.hs = self.win1.winfo_screenheight()
        pos_y=round((self.hs-400)/2)
        self.win1.geometry("600x400+"+str(pos_x)+"+"+str(pos_y))
        self.win1.config(bg="white")
        self.win1.attributes("-topmost",0)
        self.win1.overrideredirect(0)
        self.label=Label(self.win1,
                text="choose the columns you want",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.listbox=Listbox(self.win1,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="orange",
                highlightbackground="black",
                )
        self.butt=Button(self.win1,
                text="Select",
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
        self.label1=Label(self.win1,
                text="choose columns to make word minig",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.listbox1=Listbox(self.win1,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="orange",
                highlightbackground="black",
                )
        self.butt1=Button(self.win1,
                text="Next",
                bg="Gray",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                activebackground="white",
                activeforeground="black",
                relief="flat",
                )
        self.label.place(x=8,y=15,width=250,height=33)
        self.listbox.place(x=34,y=53,width=182,height=202)
        self.butt.place(x=163,y=269,width=56,height=29)
        self.label1.place(x=292,y=19,width=287,height=27)
        self.listbox1.place(x=326,y=52,width=182,height=202)
        self.butt1.place(x=455,y=266,width=56,height=29)