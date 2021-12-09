from tkinter import *
import math

def leftClickButton(event):
    weigth = float(textBoxWeight.get())
    height = float(textBoxHeight.get())/100
    bmi = float(format(weigth/height**2, '.2f'))
    print(bmi)
    print(type(bmi))
    if (bmi > 30.0):
        text2show = "อ้วนมาก"
    elif ((bmi <= 29.9) &(bmi >= 25.0)):
        text2show = "อ้วน"
    elif ((bmi <= 24.9) &(bmi >= 23.0)):
        text2show = "น้ำหนักเกิน"
    elif ((bmi <= 22.9) &(bmi >= 18.6)):
        text2show = "น้ำหนักปกติ"
    else:
        text2show = "ผอมเกินไป"
    print(text2show)
    labelResult.configure(text=text2show)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()