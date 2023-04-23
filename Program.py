from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x500+100+200") #กว้าง*ยาว+แกนx+แกน y

def showAnswer():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3 = language3.get()
    choice4 = language4.get()
    
    if choice1 == 1:
        Label(text="Choose Python").pack(anchor=W)
    if choice2 == 1:
        Label(text="Choose Java").pack(anchor=W)
    if choice3 == 1:
        Label(text="Choose PHP").pack(anchor=W)
    if choice4 == 1:
        Label(text="Choose C#").pack(anchor=W)
    
language1 = IntVar()
Checkbutton(text="Python", variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="Java", variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="PHP", variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="C#", variable=language4).pack(anchor=W)

Button(text="Show Answer", command=showAnswer).pack(anchor=W)
root.mainloop() # ลูปรันวนเรื่อยๆ