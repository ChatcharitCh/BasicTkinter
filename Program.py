from tkinter import *

root = Tk()
root.title("My GUI") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ

root.geometry("600x400+100+200") #กว้าง*ยาว+แกนx+แกน y

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

# สร้างหน้าต่างใหม่
def showWindow():
    window = Tk()
    window.title("New Window")
    window.geometry("200x200")
    window.mainloop()

# สร้างเมนูย่อย
menuItem = Menu()
menuItem.add_command(label="New Window", command=showWindow)
menuItem.add_command(label="Open File")
menuItem.add_command(label="Save File")
menuItem.add_command(label="About")
menuItem.add_command(label="Exit")


# เพิ่มเมนู
myMenu.add_cascade(label="File",menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")



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