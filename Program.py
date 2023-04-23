from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x300+100+200") #กว้าง*ยาว+แกนx+แกน y

Label(text="Radius:", font=30).grid(row=0,sticky=W)
radius = IntVar()
et1 = Entry(width=30, textvariable=radius, font=30)
et1.grid(row=0,column=1)

Label(text="Area:", font=30).grid(row=1,sticky=W)
et2 = Entry(width=30, font=30)
et2.grid(row=1,column=1)

def calculate():
    et2.delete(0, END)
    r = radius.get()
    a = 3.14 * r * r
    et2.insert(0, a)

def deleteText():
    et1.delete(0, END)
    et2.delete(0, END)

btnCalculate = Button(text="Calculate", command=calculate).grid(row=2, column=1, sticky=W)
btnDelete = Button(text="Delete", command=deleteText).grid(row=2, column=1, sticky=E)


root.mainloop() # ลูปรันวนเรื่อยๆ