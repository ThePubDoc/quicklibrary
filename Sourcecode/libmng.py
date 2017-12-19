from tkinter import *
import tkinter as tk
import pickle
import os


#This is the Book Issue menu progrmng.
class library(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Label(self,text="Student's Admission no.").grid(row=0)
        Label(self,text="Student's name").grid(row=1)
        Label(self,text='Enter the ID of Book').grid(row=2)
        Label(self, text='Enter the Book Name').grid(row=3)
        Label(self, text='Enter the Author Name').grid(row=4)
        self.e1= tk.Entry(self)
        self.e2= tk.Entry(self)
        self.e3= tk.Entry(self)
        self.e4= tk.Entry(self)
        self.e5= tk.Entry(self)

        self.e1.grid(row=0 , column=1)
        self.e2.grid(row=1 , column=1) 
        self.e3.grid(row=2 , column=1)
        self.e4.grid(row=3 , column=1)
        self.e5.grid(row=4 , column=1)
        
        
        self.button = tk.Button(self, text='Quit', command=self.destroy).grid(row=6, column=1, pady=4)
        self.button2 = tk.Button(self, text='Done', command=self.on_button).grid(row=6, column=2, pady=4)

        

    def on_button(self):

        
        self.x1=self.e1.get()
        self.x2=self.e2.get()
        self.x3=self.e3.get()
        self.x4=self.e4.get()
        self.x5=self.e5.get()
  
        self.f1=open('library.log','ab+')
        self.l1=[self.x1,self.x2,self.x3,self.x4,self.x5]
        if len(self.l1[0])>=1:
            pickle.dump(self.l1,self.f1)
            self.textin="Book issued successfully"
        else:
            self.textin="Book Not Issued"
        self.f1.close()
        self.window=tk.Toplevel()
        label=tk.Label(self.window, text=self.textin)
        label.pack(side="top", fill="both", padx=24, pady=18)
        self.button3 = tk.Button(self.window, text='Okay', command=self.destroyall).pack()
        mainloop()
    def destroyall(self):
        self.window.destroy()
        self.destroy()




#This is Book Deposit Programming
class library2(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Label(self,text='Enter the ID of Book').grid(row=0)
        Label(self,text="Student's Admission no.").grid(row=1)
        self.e1= tk.Entry(self)
        self.e2= tk.Entry(self)

        self.e1.grid(row=0 , column=1)
        self.e2.grid(row=1 , column=1)
        
        self.button = tk.Button(self, text='Quit', command=self.destroy).grid(row=6, column=1, pady=4)
        self.button2 = tk.Button(self, text='Done', command=self.on_button3).grid(row=6, column=2, pady=4)

   

    def on_button3(self):
        self.f2=open("library.log","rb")
        self.objs=[]
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.stu=[]
        self.a=[]
            
        self.f3=open("temprry.log","ab+")
        self.string="No such book Issued"
        for self.i in self.objs:
            
            if self.i[2]==self.e1.get() and self.i[0]==self.e2.get():
                self.stu=self.i
                self.string="Book ",str(self.stu[3])," Successfully Deposited by ",str(self.stu[1])
            else:
                pickle.dump(self.i,self.f3)

        self.f2.close()
        self.f3.close()
        self.window1=tk.Toplevel()
        Label(self.window1,text='Are you sure?').grid(row=0)
        self.button = tk.Button(self.window1, text='Yes', command=self.finall).grid(row=6, column=1, pady=4)

    def finall(self):

        os.remove("library.log")
        os.rename("temprry.log","library.log")
        
        
        self.window2=tk.Toplevel()
        Label(self.window2,text=self.string).grid(row=0)
        self.button = tk.Button(self.window2, text='Okay', command=self.dsall).grid(row=6, column=1, pady=4)

    def dsall(self):
        self.window2.destroy()
        self.window1.destroy()
        self.destroy()


#This is Admin's menu programming
class library3(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Label(self,text="Enter Password").grid(row=0)
        self.e1= tk.Entry(self,show='•')
        self.e1.grid(row=0 , column=1)
        
        self.button = tk.Button(self, text='Cancel', command=self.destroy).grid(row=6, column=1, pady=4)
        self.button2 = tk.Button(self, text='Okay', command=self.on_button3).grid(row=6, column=2, pady=4)
    def on_button3(self):
        if self.e1.get() == "password":
            self.window1=tk.Toplevel()
            self.button = tk.Button(self.window1, text='See whole record', command=self.on_button4).grid(row=6, column=1, pady=4)
            self.button2 = tk.Button(self.window1, text="See a Student's record", command=self.on_button5).grid(row=6, column=2, pady=4)
            self.destroy()
        else:
            self.window1 = tk.Toplevel()
            label = tk.Label(self.window1, text="Wrong password")
            label.pack(side="top", fill="both", padx=24, pady=10)
            self.button = tk.Button(self.window1, text='Quit', command=self.window1.destroy).pack()
    def on_button4(self):
        self.f2=open("library.log",'rb')
        self.objs = []
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.window2=tk.Toplevel()
        self.testout=""
        for self.i in range(len(self.objs)):
            self.adms="Admission no. :"+ str(self.objs[self.i][0])
            self.name="     Name :"+ str(self.objs[self.i][1])
            self.bookid="     Book ID: "+ str(self.objs[self.i][2])
            self.booknam="     Book Name: "+ str(self.objs[self.i][3])
            self.authr="     Book Author: "+ str(self.objs[self.i][4])
            self.testout+=self.adms+self.name+self.bookid+self.booknam+self.authr+'\n'   
        label = tk.Label(self.window2, text=self.testout)
        label.pack(side="top", fill="both", padx=240, pady=180)
        self.f2.close()
    def on_button5(self):
        self.window3=tk.Toplevel()
        Label(self.window3,text="Addmission no.").grid(row=0)
        self.e1= tk.Entry(self.window3)
        self.e1.grid(row=0 , column=1)
        
        self.button = tk.Button(self.window3, text='Quit', command=self.window3.destroy).grid(row=6, column=1, pady=4)
        self.button = tk.Button(self.window3, text='Okay', command=self.on_button6).grid(row=6, column=2, pady=4)
        mainloop()
    def on_button6(self):
        self.f2=open("library.log","rb")
        self.objs=[]
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.stu=[]
            
        self.f2.close()
        for self.i in self.objs:
            if self.i[0]==self.e1.get():
                self.stu=self.i
        self.window4=tk.Toplevel()
        label = tk.Label(self.window4, text=self.stu)
        label.pack(side="top", fill="both", padx=240, pady=180)
        self.button = tk.Button(self.window4, text='Okay', command=self.destroyall2).pack()

    def destroyall2(self):
        self.window4.destroy()
        self.window3.destroy()
        self.window1.destroy()
        

#From here, classes start
def start_issue():
    a= library()
    return (a)
def start_deposit():
    b=library2()
    return (b)
def start_admin():
    c=library3()
    return (c)




#This is the main menu programming.

root = Tk()

Label(root, 
		 text="Welcome",
		 fg = "dark green",
                 bg = "white",
		 font = "Meiryo 22",
                 width = "20").pack()
Label(root, 
		 text="QuickLIBRARY",
		 fg = "white",
		 bg = "dark green",
		 font = "Meiryo 22",
                 width = "20").pack()

Label(root,
                 text="By- Anubhav",
		 fg = "white",
                 bg = "dark green",
		 font = "Meiryo 10",
                 width = "45").pack()
button1 = tk.Button(root, text="Book Issue", command=start_issue, width= "12")
button2 = tk.Button(root, text="Book Deposit", command=start_deposit, width= "12")
button3 = tk.Button(root, text="Admin's Menu", command=start_admin, width= "12")
button4 = tk.Button(root, text="Quit",command=root.destroy, width= "12")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
root.mainloop()
