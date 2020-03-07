from tkinter import Tk,Label,Entry,Button,W
from tkinter import messagebox
class MyForm:
    def thanx(self):
        messagebox.showinfo('Submition Done','Thank you')

    def __init__(self):
        self.root=Tk()
        self.root.title('My Form')
        Label(self.root, text='User Name').grid(row=0, padx=12,pady=5)
        Label(self.root, text='Password').grid(row=1, padx=12,pady=5)
        Entry(self.root).grid(row=0,column=1,columnspan=2)
        Entry(self.root).grid(row=1,column=1,columnspan=2)
        self.show=Button(self.root,text='Submit',command=self.thanx)
        self.show.grid(row=2,column=1,pady=4)
        self.root.geometry("230x140")
        self.root.configure(background='#f5499c')
        self.root.mainloop()


if __name__ =='__main__':
    app=MyForm()
