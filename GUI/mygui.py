from tkinter import Tk,Label,Entry,Button,W
from tkinter import messagebox
def thanx():
        messagebox.showinfo('Submition Done','Thank you')

root=Tk()
root.title('My Form')
Label(root, text='User Name').grid(row=0, padx=12,pady=5)
Label(root, text='Password').grid(row=1, padx=12,pady=5)
Entry(root).grid(row=0,column=1,columnspan=2)
Entry(root).grid(row=1,column=1,columnspan=2)
root.show=Button(root,text='Submit',command=thanx())
root.show.grid(row=2,column=1,pady=4)
root.geometry("230x140")
root.configure(background='#f5499c')
root.mainloop()
