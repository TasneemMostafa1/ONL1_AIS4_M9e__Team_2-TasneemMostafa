from tkinter import *
from tkinter import ttk
class Win2Code():
    def win2_fcn(self):
        self.win2=Toplevel()
        self.win2.title("tk")
        self.ws = self.win2.winfo_screenwidth()
        pos_x=round((self.ws-400)/2)
        self.hs = self.win2.winfo_screenheight()
        pos_y=round((self.hs-200)/2)
        self.win2.geometry("400x200+"+str(pos_x)+"+"+str(pos_y))
        self.win2.config(bg="white")
        self.win2.attributes("-topmost",0)
        self.win2.overrideredirect(0)
        self.butt=Button(self.win2,
                text="browser the new path",
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
        self.butt1=Button(self.win2,
                text="Informations",
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
        self.label=Label(self.win2,
                text="dwonload your new file : ",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.butt2=Button(self.win2,
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
        self.butt.place(x=214,y=49,width=173,height=26)
        self.butt1.place(x=208,y=110,width=119,height=30)
        self.label.place(x=11,y=48,width=189,height=27)
        self.butt2.place(x=330,y=110,width=56,height=29)