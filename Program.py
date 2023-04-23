from tkinter import *
from tkinter import ttk # comboBox

root = Tk()
root.title("Calculator") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
# root.geometry("600x200") #กว้าง*ยาว+แกนx+แกน y

fontFormat = ('aerial', 30, 'bold')
content = ""
txtInput = StringVar(value="0")

def btn(number):
    global content
    content += str(number)
    txtInput.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txtInput.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txtInput.set("")
    display.insert(0, "0")


# row x colums = 5 x 4
display = Entry(font= fontFormat, fg="white", bg="green", textvariable=txtInput ,justify="right")
display.grid(columnspan=4)

# Button

# row1
btn7 = Button(fg="black", font=fontFormat, text="7", command=lambda:btn(7), padx=30, pady=15).grid(row=1, column=0)
btn8 = Button(fg="black", font=fontFormat, text="8", command=lambda:btn(8), padx=30, pady=15).grid(row=1, column=1)
btn9 = Button(fg="black", font=fontFormat, text="9", command=lambda:btn(9), padx=30, pady=15).grid(row=1, column=2)
btnClear = Button(fg="black", bg="orange", font=fontFormat, text="C", command=clear, padx=30, pady=15).grid(row=1, column=3)

# row2
btn4 = Button(fg="black", font=fontFormat, text="4", command=lambda:btn(4), padx=30, pady=15).grid(row=2, column=0)
btn5 = Button(fg="black", font=fontFormat, text="5", command=lambda:btn(5), padx=30, pady=15).grid(row=2, column=1)
btn6 = Button(fg="black", font=fontFormat, text="6", command=lambda:btn(6), padx=30, pady=15).grid(row=2, column=2)
btnPlus = Button(fg="black", bg="orange", font=fontFormat, text="+", command=lambda:btn("+"), padx=35, pady=15).grid(row=2, column=3)

# row3
btn1 = Button(fg="black", font=fontFormat, text="1", command=lambda:btn(1), padx=30, pady=15).grid(row=3, column=0)
btn2 = Button(fg="black", font=fontFormat, text="2", command=lambda:btn(2), padx=30, pady=15).grid(row=3, column=1)
btn3 = Button(fg="black", font=fontFormat, text="3", command=lambda:btn(3), padx=30, pady=15).grid(row=3, column=2)
btnPlus = Button(fg="black", bg="orange", font=fontFormat, text="-", command=lambda:btn("-"), padx=40, pady=15).grid(row=3, column=3)

# row4
btnDot = Button(fg="black", font=fontFormat, text=".",command=lambda:btn("."), padx=35, pady=15).grid(row=4, column=0)
btn0 = Button(fg="black", font=fontFormat, text="0", command=lambda:btn("0"), padx=30, pady=15).grid(row=4, column=1)
btnDivision = Button(fg="black", bg="orange" ,font=fontFormat, text="/", command=lambda:btn("/"), padx=35, pady=15).grid(row=4, column=2)
btnMultiply = Button(fg="black", bg="orange", font=fontFormat, text="X", command=lambda:btn("*"), padx=35, pady=15).grid(row=4, column=3)

# row5
btnEqual = Button(fg="black", bg="cyan" ,font=fontFormat, text="=",command=equal, padx=95, pady=15).grid(row=5, column=0, columnspan=2)
btnOpen = Button(fg="black", font=fontFormat, text="(", command=lambda:btn("("), padx=35, pady=15).grid(row=5, column=2)
btnClose = Button(fg="black", bg="orange" ,font=fontFormat, text=")", command=lambda:btn(")"), padx=35, pady=15).grid(row=5, column=3)


root.mainloop() # ลูปรันวนเรื่อยๆ






# # โปรแกรมแปลงสกุลเงิน

# # Input
# money = IntVar()
# Label(text="Amount (THB)", padx=10, font=30).grid(row=0, sticky=W)
# et1 = Entry(font=30, width=30, textvariable=money)
# et1.grid(row=0, column=1)

# # Process
# choice = StringVar(value="Select Currency")
# Label(text="Currency", padx=10, font=30).grid(row=1, sticky=W)
# ttk.Combobox(width=30, font=30)
# combo = ttk.Combobox(width=30, font=20, textvariable=choice)
# combo["values"] = ("EUR", "JPY", "USD", "GBP")
# combo.grid(row=1, column=1)

# # Output
# Label(text="Result", padx=10, font=30).grid(row=2, sticky=W)
# et2 = Entry(font=30, width=30)
# et2.grid(row=2, column=1)

# def calculate():
#     amount = money.get()
#     currency = choice.get()

#     if currency == "EUR":
#         et2.delete(0, END)
#         result = ((amount * 0.026), "EUR")
#         et2.insert(0, result)
#     elif currency == "JPY":
#         et2.delete(0, END)
#         result = ((amount * 3.486), "JPY")
#         et2.insert(0, result)
#     elif currency == "USD":
#         et2.delete(0, END)
#         result = ((amount * 0.031), "USD")
#         et2.insert(0, result)
#     elif currency == "GBP":
#         et2.delete(0, END)
#         result = ((amount * 0.023), "GBP")
#         et2.insert(0, result)
#     else:
#         et2.delete(0, END)
#         result = "Please Select Currency!!"
#         et2.insert(0, result)

# def deleteText():
#     et1.delete(0, END)
#     et2.delete(0, END)

# btnCal = Button(text="Calculate", font=30, width=15, command=calculate).grid(row=3, column=1, sticky=W)
# btnDel = Button(text="Delete", font=30, width=15, command=deleteText).grid(row=3, column=1, sticky=E)