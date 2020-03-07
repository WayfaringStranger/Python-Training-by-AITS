from tkinter import *
from time import *
class Clock():
    def update(self):
        cur=strftime("%H:%M:%S")
        tt.configure(text=cur)
        root.after(1000,self.update)

root=Tk()
tt=Label(root,text='')
tt.pack()
cl=Clock()
cl.update()
root.mainloop()
