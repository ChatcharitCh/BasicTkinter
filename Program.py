from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ

root.geometry("600x500+100+200") #กว้าง*ยาว+แกนx+แกน y

# หน้าต่างเลือกสี
def selectColor():
    color = askcolor()
    myLabel = Label(text="Hello Tkinter", bg=color[1]).pack()

# หน้าต่างเลือกไฟล์
def selectFile():
    fileOpen = askopenfilename()
    fileContent = open(fileOpen, encoding="utf8")
    myLabel = Label(text=fileContent.read()).pack()

btnColor = Button(text="Choose Color", command=selectColor).pack()
btnFile = Button(text="Choose File", command=selectFile).pack()

# # ใส่ข้อความในหน้าจอ

# myLabel = Label(root, text="Hello Chatcharit", fg="red", font=40, bg="yellow").pack()


# def showMessage():
#     message = txt.get()
#     print(message)
#     #Label(root, text="Hello Chatcharit", fg="red", font=40, bg="yellow").pack()

# def openWindow():
#     # หน้าจอที่ 2
#     myWindow = Tk()
#     myWindow.title("Report")
#     myWindow.geometry("500x300")

# # กล่องข้อความ
# txt = StringVar()
# myText = Entry(root, textvariable=txt).pack()

# # ใส่ปุ่ม
# btnTest = Button(root, text="Test",fg="black", bg="white", command=showMessage).pack()
# btn2 = Button(root, text="Open Report", fg="white", bg="green", command=openWindow).pack()



root.mainloop() # ลูปรันวนเรื่อยๆ