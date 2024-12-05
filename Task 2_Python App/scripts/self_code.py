from tkinter import *
from tkinter import ttk
class SelfCode(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("file browser")
        self.ws = self.winfo_screenwidth()
        pos_x=round((self.ws-550)/2)
        self.hs = self.winfo_screenheight()
        pos_y=round((self.hs-200)/2)
        self.geometry("550x200+"+str(pos_x)+"+"+str(pos_y))
        self.config(bg="white")
        self.attributes("-topmost",0)
        self.overrideredirect(0)
        self.button_select=Button(self,
                text="select  file",
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
        self.Label2=Label(self,
                text="choose the extension",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.combo=ttk.Combobox(self)
        self.label1=Label(self,
                text="browser your first file",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.Button_finish=Button(self,
                text="close",
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
        self.butt_next=Button(self,
                text="Next",
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
        self.button_select.place(x=417,y=88,width=106,height=27)
        self.Label2.place(x=48,y=88,width=165,height=38)
        self.combo.place(x=246,y=94,width=143,height=21)
        self.label1.place(x=150,y=20,width=305,height=31)
        self.Button_finish.place(x=373,y=156,width=70,height=27)
        self.butt_next.place(x=456,y=155,width=75,height=26)