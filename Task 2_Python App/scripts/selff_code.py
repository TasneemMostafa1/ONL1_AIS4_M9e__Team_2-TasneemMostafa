from tkinter import *
from tkinter import ttk
class SelffCode():
    def selff_fcn(self):
        self.selff=Toplevel()
        self.selff.title("file browser")
        self.ws = self.selff.winfo_screenwidth()
        pos_x=round((self.ws-550)/2)
        self.hs = self.selff.winfo_screenheight()
        pos_y=round((self.hs-200)/2)
        self.selff.geometry("550x200+"+str(pos_x)+"+"+str(pos_y))
        self.selff.config(bg="white")
        self.selff.attributes("-topmost",0)
        self.selff.overrideredirect(0)
        self.button_select=Button(self.selff,
                text="select  file",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                activebackground="white",
                activeforeground="black",
                relief="flat",
                )
        self.Label2=Label(self.selff,
                text="choose the extension",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.combo=ttk.Combobox(self.selff)
        self.label1=Label(self.selff,
                text="this your first file",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.Button_finish=Button(self.selff,
                text="finish",
                bg="#f0f0f0",
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
        self.label1.place(x=227,y=18,width=153,height=32)
        self.Button_finish.place(x=439,y=149,width=56,height=29)