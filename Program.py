from tkinter import *
from tkinter import ttk # comboBox

root = Tk()
root.title("Currency Convert") # กำหนดชื่อโปรแกรม

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("600x200") #กว้าง*ยาว+แกนx+แกน y

# โปรแกรมแปลงสกุลเงิน

# Input
money = IntVar()
Label(text="Amount (THB)", padx=10, font=30).grid(row=0, sticky=W)
et1 = Entry(font=30, width=30, textvariable=money)
et1.grid(row=0, column=1)

# Process
choice = StringVar(value="Select Currency")
Label(text="Currency", padx=10, font=30).grid(row=1, sticky=W)
ttk.Combobox(width=30, font=30)
combo = ttk.Combobox(width=30, font=20, textvariable=choice)
combo["values"] = ("EUR", "JPY", "USD", "GBP")
combo.grid(row=1, column=1)

# Output
Label(text="Result", padx=10, font=30).grid(row=2, sticky=W)
et2 = Entry(font=30, width=30)
et2.grid(row=2, column=1)

def calculate():
    amount = money.get()
    currency = choice.get()

    if currency == "EUR":
        et2.delete(0, END)
        result = ((amount * 0.026), "EUR")
        et2.insert(0, result)
    elif currency == "JPY":
        et2.delete(0, END)
        result = ((amount * 3.486), "JPY")
        et2.insert(0, result)
    elif currency == "USD":
        et2.delete(0, END)
        result = ((amount * 0.031), "USD")
        et2.insert(0, result)
    elif currency == "GBP":
        et2.delete(0, END)
        result = ((amount * 0.023), "GBP")
        et2.insert(0, result)
    else:
        et2.delete(0, END)
        result = "Please Select Currency!!"
        et2.insert(0, result)

def deleteText():
    et1.delete(0, END)
    et2.delete(0, END)

btnCal = Button(text="Calculate", font=30, width=15, command=calculate).grid(row=3, column=1, sticky=W)
btnDel = Button(text="Delete", font=30, width=15, command=deleteText).grid(row=3, column=1, sticky=E)

root.mainloop() # ลูปรันวนเรื่อยๆ