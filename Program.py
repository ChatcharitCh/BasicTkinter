from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("600x500+100+200") #กว้าง*ยาว+แกนx+แกน y

# เพิ่มตัวเลือกในโปรแกรม
language = IntVar()
Radiobutton(text="Python", variable=language, value=1).grid(row=0, column=0)
Radiobutton(text="C#", variable=language, value=2).grid(row=0, column=1)
Radiobutton(text="Java", variable=language, value=3).grid(row=0, column=2)
Radiobutton(text="PHP", variable=language, value=4).grid(row=0, column=3)


root.mainloop() # ลูปรันวนเรื่อยๆ