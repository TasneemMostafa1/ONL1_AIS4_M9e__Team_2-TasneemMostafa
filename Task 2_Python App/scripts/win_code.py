from tkinter import *
from tkinter import ttk
class WinCode():
    def win_fcn(self):
        self.win=Toplevel()
        self.win.title("file browser")
        self.ws = self.win.winfo_screenwidth()
        pos_x=round((self.ws-550)/2)
        self.hs = self.win.winfo_screenheight()
        pos_y=round((self.hs-200)/2)
        self.win.geometry("550x200+"+str(pos_x)+"+"+str(pos_y))
        self.win.config(bg="white")
        self.win.attributes("-topmost",0)
        self.win.overrideredirect(0)
        self.button_select=Button(self.win,
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
        self.Label2=Label(self.win,
                text="choose the extension",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.combo=ttk.Combobox(self.win)
        self.label1=Label(self.win,
                text="this your first file",
                bg="white",
                fg="black",
                font=("arial",13),
                )
        self.Button_finish=Button(self.win,
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