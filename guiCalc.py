from tkinter import *
import sys
import math

#Declaring the calculator and eval strings for later

calc=Tk()
frame = Frame(calc)
frame.pack()
calc.title("APCSP Create Task Calculator")
calclabel=Label(calc,text="GUICalc",font=("Courier New",30,'bold'))
evaluation=StringVar()
operator=""

#Display

txtDisplay=Entry(frame,textvariable = evaluation,bd = 20,insertwidth = 1,font = 30)
txtDisplay.pack(side = TOP)

#First row

frame0 = Frame(calc)
frame0.pack(side = TOP)

AC = Button(frame0,padx = 16,pady = 16,bd = 8,text = "C",fg="gray")
AC.pack(side=LEFT)

negate = Button(frame0,padx = 16,pady = 16,bd = 8,text = "+/-",fg="gray")
negate.pack(side=LEFT)

percent = Button(frame0,padx = 16,pady = 16,bd = 8,text = "%",fg="gray")
percent.pack(side=LEFT)

divide = Button(frame0,padx = 16,pady = 16,bd = 8,text = "/",fg="gray")
divide.pack(side=LEFT)

#Second row

frame1 = Frame(calc)
frame1.pack(side = TOP)

seven = Button(frame1,padx = 16,pady = 16,bd = 8,text = "7",fg="gray")
seven.pack(side=LEFT)

eight = Button(frame1,padx = 16,pady = 16,bd = 8,text = "8",fg="gray")
eight.pack(side=LEFT)

nine = Button(frame1,padx = 16,pady = 16,bd = 8,text = "9",fg="gray")
nine.pack(side=LEFT)

times = Button(frame1,padx = 16,pady = 16,bd = 8,text = "*",fg="gray")
times.pack(side=LEFT)

#Third row

frame2 = Frame(calc)
frame2.pack(side = TOP)

four = Button(frame2,padx = 16,pady = 16,bd = 8,text = "4",fg="gray")
four.pack(side=LEFT)

five = Button(frame2,padx = 16,pady = 16,bd = 8,text = "5",fg="gray")
five.pack(side=LEFT)

six = Button(frame2,padx = 16,pady = 16,bd = 8,text = "6",fg="gray")
six.pack(side=LEFT)

minus = Button(frame2,padx = 16,pady = 16,bd = 8,text = "-",fg="gray")
minus.pack(side=LEFT)

#Fourth row

frame3 = Frame(calc)
frame3.pack(side = TOP)

one = Button(frame3,padx = 16,pady = 16,bd = 8,text = "1",fg="gray")
one.pack(side=LEFT)

two = Button(frame3,padx = 16,pady = 16,bd = 8,text = "2",fg="gray")
two.pack(side=LEFT)

three = Button(frame3,padx = 16,pady = 16,bd = 8,text = "3",fg="gray")
three.pack(side=LEFT)

plus = Button(frame3,padx = 16,pady = 16,bd = 8,text = "+",fg="gray")
plus.pack(side=LEFT)

#Fifth row

frame4 = Frame(calc)
frame4.pack(side = TOP)

zero = Button(frame4,padx = 16,pady = 16,bd = 8,text = "0",fg="gray")
zero.pack(side=LEFT)

pi = Button(frame4,padx = 16,pady = 16,bd = 8,text = "π",fg="gray")
pi.pack(side=LEFT)

decimal = Button(frame4,padx = 16,pady = 16,bd = 8,text = ".",fg="gray")
decimal.pack(side=LEFT)

equals = Button(frame4,padx = 16,pady = 16,bd = 8,text = "=",fg="gray")
equals.pack(side=LEFT)


calc.mainloop()

