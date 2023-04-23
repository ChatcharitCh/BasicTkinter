from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
from tkinter import ttk # comboBox

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x300+100+200") #กว้าง*ยาว+แกนx+แกน y

Label(text="Address", font=30).grid(row=0, column=0)
choice = StringVar(value="Choose Your Province")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Bangkok", "Nonthaburi", "Chiangmai", "Phuket", "Rayong")
combo.grid(row=0, column=1)

def selectProvince():
    Label(text="You Select " + choice.get(), font=30).grid(row=2, column=0)

btnSelect = Button(text="Send", command=selectProvince)
btnSelect.grid(row=1, column=1)


root.mainloop() # ลูปรันวนเรื่อยๆ