

from tkinter import *
from math import *

def btn(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
    
def btnclear():
    global operator
    operator=""
    text_input.set("")
    
def btnequal():
    global operator
    text_input.set(str(eval(operator)))
    operator=""

def btnsqrt():
    global operator
    sqrt=math.sqrt()
    text_input.set("")
    operator=""
    
calci = Tk()
calci.title("Python Calci")
operator=""
text_input=StringVar()

txtdisp = Entry(calci,font=('arial',20,'bold'),textvariable=text_input,bd=30,bg="blue").grid(columnspan=3)

btnclr = Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="CLR",bg="Honeydew3",command=btnclear).grid(row=0,column=3)

btnPi = Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="π",bg="Honeydew3",command=lambda:btn("3.1415")).grid(row=1,column=0)
    
btnSqrt=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="√",bg="Honeydew3",command=btnsqrt).grid(row=1,column=1)
 
btnPer=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="%",bg="Honeydew3",command=lambda:btn("/100")).grid(row=1,column=2)
 
btnDiv=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="Honeydew3",command=lambda:btn("/")).grid(row=1,column=3)

btn7=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="Honeydew3",command=lambda:btn("7")).grid(row=2,column=0)

btn8=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="Honeydew3",command=lambda:btn("8")).grid(row=2,column=1)

btn9=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="Honeydew3",command=lambda:btn("9")).grid(row=2,column=2)

btnMul=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="Honeydew3",command=lambda:btn("*")).grid(row=2,column=3)

btn4=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="Honeydew3",command=lambda:btn("4")).grid(row=3,column=0)

btn5=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="Honeydew3",command=lambda:btn("5")).grid(row=3,column=1)

btn6=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="Honeydew3",command=lambda:btn("6")).grid(row=3,column=2)

btnSub=Button(calci,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="Honeydew3",command=lambda:btn("-")).grid(row=3,column=3)

btn1=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="Honeydew3",command=lambda:btn("1")).grid(row=4,column=0)

btn2=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="Honeydew3",command=lambda:btn("2")).grid(row=4,column=1)

btn3=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="Honeydew3",command=lambda:btn("3")).grid(row=4,column=2)

btnAdd=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="Honeydew3",command=lambda:btn("+")).grid(row=4,column=3)

btnDot=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text=".",bg="Honeydew3",command=lambda:btn(".")).grid(row=5,column=0)

btn0=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="Honeydew3",command=lambda:btn("0")).grid(row=5,column=1)

btnBrack1=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="(",bg="Honeydew3",command=lambda:btn("(")).grid(row=5,column=2)

btnBrack2=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text=")",bg="Honeydew3",command=lambda:btn(")")).grid(row=5,column=3)

btnEqual=Button(calci,padx=10,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="Honeydew3",command=btnequal).grid(row=6,column=3)


calci.mainloop()    
