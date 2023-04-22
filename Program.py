from tkinter import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# ใส่ข้อความในหน้าจอ

myLabel = Label(root, text="Hello Chatcharit", fg="red", font=40, bg="yellow").pack()


def showMessage():
    Label(root, text="Hello Chatcharit", fg="red", font=40, bg="yellow").pack()

# ใส่ปุ่ม
btnTest = Button(root, text="Test",fg="black", bg="white", command=showMessage).pack()








# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("600x400+100+200") #กว้าง*ยาว+แกนx+แกน y
root.mainloop() # ลูปรันวนเรื่อยๆ