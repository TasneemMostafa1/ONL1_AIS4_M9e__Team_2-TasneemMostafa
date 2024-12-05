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




import pandas as pd
from tkinter import filedialog,Tk,simpledialog,messagebox

#libraries of cleaning
import unicodedata
import re
#minig of data
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize



from sqlalchemy import create_engine



class new(SelfCode,Win1Code,Win2Code,Win3Code):
    def __init__(self):
        super().__init__()
        self.button_select.config(command=self.upload)
        self.Button_finish.config(command=self.destroyy)
        self.combo['values']=['csv','json','xlsx','sql']
        self.combo.set('csv')
        self.butt_next.config(command=self.win1_new)
        self.k=0
        self.df=pd.DataFrame()
        
    def destroyy(self):
        self.destroy()
        
    def upload(self):
        lis=['second','third']
        # Initialize tkinter
        self.label1.config(text='Browser your '+lis[self.k]+' file')
        file_extension =self.combo.get() #extension_var.get()
        #Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
        file_type = (file_extension, f'*.{file_extension}')
        file_location = filedialog.askopenfilename(filetypes=[file_type])  
        # Show an "Open" dialog box and return the path to the selected file
    
        # Read the file into a pandas DataFrame
        if file_extension == 'csv':
            df = pd.read_csv(file_location, encoding='latin-1')
        elif file_extension == 'json':
            df = pd.read_json(file_location)
        elif file_extension == 'xlsx':
            df = pd.read_excel(file_location)
        elif file_extension == 'sql':
            # Assuming you have a connection string or engine
            connection_string = simpledialog.askstring("Input", "Enter your SQL connection string:")
            df = pd.read_sql(file_location, connection_string)
        else:
            raise ValueError("Unsupported file extension")
        self.df=df
        return self.df

        
    def win1_new(self):
        self.win1_fcn()
        self.columns=list(self.df.columns)
        self.listbox.config(selectmode=MULTIPLE)
        self.listbox1.config(selectmode=MULTIPLE)
        
        for i in self.columns:
            self.listbox.insert('end',i)
        self.butt.config(command=self.choose_columns)
        self.butt1.config(command=self.win2_new)
        return self.columns

        
    def win2_new(self):
        self.column_process=[self.listbox1.get(i) for i in self.listbox.curselection()]
        self.clean(self.df,self.column_process)
        self.win1.withdraw()
        self.win2_fcn()
        self.butt.config(command=self.download)
        self.butt1.config(command=self.info)
        self.butt2.config(command=self.close)
        
    def close(self):
        self.win1.destroy()
        self.win2.destroy()
        


    def download():
        # Prompt user to select file format
        file_format = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                   filetypes=[("CSV files", "*.csv"), 
                                                              ("Excel files", "*.xlsx"), 
                                                              ("JSON files", "*.json"), 
                                                              ("All files", "*.*")])
        if file_format:
            if file_format.endswith('.csv'):
                self.df.to_csv(file_format, index=False)
            elif file_format.endswith('.xlsx'):
                self.df.to_excel(file_format, index=False)
            elif file_format.endswith('.json'):
                self.df.to_json(file_format)
            else:
                messagebox.showerror("Error", "Unsupported file format!")
            messagebox.showinfo("Success", f"DataFrame saved to {file_format}")
            
        
    def info(self):
        self.win3_fcn()
        self.butt,cofig(command=self.win3.destroy)
        self.label.config(text='the total records of data is :'+str(self.num_rows))
        self.label1.config(text='the records is null in data  :'+str(self.num_rows_nulls))
        self.label2.config(text='the final total records after cleaning :'+str(self.num_rows_final))
        

    def choose_columns(self):
        selected=[self.listbox.get(i) for i in self.listbox.curselection()]
        for i in self.columns:
            if i in selected:
                self.listbox1.insert('end',i)
                continue
            else:
                self.df.drop([i],axis=1,inplace=True)
        return
    
    #change date to timestamp then get years only then make it int to remove zeros
    def year(self,df):
        if 'year' in list(df.coulmns):
            df['year'] = df['year'].astype('datetime64[ns]')
            df['year']=df['year'].dt.year
            df['year']=df['year'].astype(int)
            # sort as year
            df.sort_values(by='year' , axis=0,inplace=True)
        

    #fun to clean data second method
    def remove_non_ascii(self,text):
        return re.sub(r'[^\x00-\x7F]+', '', text)

    #remove rebeted numbers and letters
    def lett(self,column):
        result = []
        for item in column:
            m = ''
            k=''
            for char in item:
                if char.isalpha() or char==' ':
                    if k==char:
                        continue
                    else:
                        m += char
                        k=char
            result.append(m)
        return result

    # Preprocess tweets
    def preprocess_tweet(self,tweet):
        # Remove URLs, mentions, and special characters
        # Convert to lowercase
        # Tokenize the tweet
        return word_tokenize(str(tweet).lower())

    # Sentiment analysis
    def get_sentiment(self,tweet):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(' '.join(tweet))
        return sentiment_scores['compound']

    # Categorize tweets based on sentiment scores
    def categorize_tweets(self,score):
        if score > 0.05:
            return 'Positive'
        elif score < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    #main fun for dataframe cleaning
    def clean(self,dataframe,column):
        compined=pd.DataFrame(columns=['com'])
        dataframe=self.year(dataframe)
        #removie nulls
        self.num_rows=dataframe.shape[0]
        dataframe.dropna(axis=0,inplace=True)
        self.num_rows_nulls=num_rows-dataframe.shape[0]
        k=0
        for i in column:
            #removie duplicates
            dataframe.drop_duplicates(subset=[i],keep='first',inplace=True)
            #clean data from unicodes
            #first method
            dataframe[i]=dataframe[i].apply(lambda x: unicodedata.normalize('NFKD', x)\
                                            .encode('ascii', 'ignore').decode('utf-8'))
            #second method
            dataframe[i]=dataframe[i].apply(self.remove_non_ascii)
            
            #third method
            dataframe[i]=self.lett(dataframe[i])
            
            #remove duplicates again
            dataframe.drop_duplicates(subset=[i],keep='first',inplace=True)
            
            #make data mining
            #compined coulmn
            if k ==0:
                compined['com']=dataframe[i]
                k+=1
            else:
                compined['com']+= ' ' +dataframe[i]

        self.num_rows_final=self.num_rows - self.num_rows_nulls
        pocessed_tweets = compined['com'].apply(self.preprocess_tweet)
        dataframe['sentiment_score'] = pocessed_tweets.apply(self.get_sentiment)
        dataframe['sentiment_category'] =dataframe['sentiment_score'].apply(self.categorize_tweets)
        return   

    


a=new()
a.mainloop()













































































































