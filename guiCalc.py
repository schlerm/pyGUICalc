from tkinter import *
import sys
import os
import math
from lib2to3.pgen2.token import OP
from reportlab.graphics.samples.excelcolors import backgroundGrey
import pymsgbox

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.inputVal = True
        self.check_sum = False
        self.op = ""
        self.result = False
        self.power = ""
                
    def number(self,num):
        self.result = False
        ans = display.get()
        input = str(num)
        if self.inputVal:
            self.current = input
            self.inputVal = False
        else:
            if input == ".":
                if input in ans:
                    return
            self.current = ans + input
        self.display(self.current)
    
    def validOperator(self):
        if self.op == "plus":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.inputVal = True
        self.check_sum = False
        self.display(self.total)      
     
    def operator(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.validOperator()
        elif not self.result:
            self.total = self.current
            self.inputVal = True
        self.check_sum = True
        self.op = op
        self.result = False
            
    def clearDisplay(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.inputVal = True
    
    def allClear(self):
        self.clearDisplay()
        self.total = 0
        
    def equals(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.validOperator()
        else:
            self.total = float(display.get())
    
    def display(self,value):
        display.configure(state="normal")
        display.delete(0,END)
        display.insert(0,value)
        display.configure(state="disabled")

    
    def negate(self):
        self.result = False
        self.current = -(float(display.get()))
        self.display(self.current)
  
    def squared(self):
        self.result = False
        self.current = math.pow((float(display.get())),2)
        self.display(self.current)
    
    def cubed(self):
        self.result = False
        self.current = math.pow((float(display.get())),3)
        self.display(self.current)
        
    def cuberoot(self):
        self.result = False
        self.current = math.pow((float(display.get())),(1/3))
        self.display(self.current)
        
    def squareroot(self):
        self.result = False
        self.current = math.pow((float(display.get())),(1/2))
        self.display(self.current)
        
    def percent(self):
        self.result = False
        self.current = (float(display.get())/100)
        self.display(self.current)      
    
    def pi(self):
        self.result = False
        self.current = float(math.pi)
        self.display(self.current)
        
    def natnumber(self):
        self.result = False
        self.current = float(math.e)
        self.display(self.current)
          
#Declaring the calculator and other things

added_value = Calc()
calc=Tk()
frame = Frame(calc)
frame.pack()
calc.title("APCSP Create Task Calculator")
calc.resizable(width = False, height = False)
calclabel=Label(calc,text="GUICalc",font=("Courier New",30,'bold'))
calc.configure(background="gray")

#Display

display=Entry(frame,bd = 10,insertwidth = 1,font = 30)
display.insert(0,"0")
display.pack(side = TOP)
display.config(state = "disabled",disabledbackground = "deepskyblue",disabledforeground="red")

#First row

frame0 = Frame(calc)
frame0.pack(side = TOP)

AC = Button(frame0,padx = 16,pady = 16,bd = 4,text = "C",fg="red",background="deepskyblue",command = added_value.allClear)
AC.pack(side=LEFT)

negate = Button(frame0,padx = 16,pady = 16,bd = 4,text = chr(177),fg="red",background="deepskyblue",command = added_value.negate)
negate.pack(side=LEFT)

percent = Button(frame0,padx = 16,pady = 16,bd = 4,text = "%",fg="red",background="deepskyblue",command = added_value.percent)
percent.pack(side=LEFT)

divide = Button(frame0,padx = 16,pady = 16,bd = 4,text = "/",fg="red",background="deepskyblue",command = lambda: added_value.operator("divide"))
divide.pack(side=LEFT)

#Second row

frame1 = Frame(calc)
frame1.pack(side = TOP)

seven = Button(frame1,padx = 16,pady = 16,bd = 4,text = "7",fg="red",background="deepskyblue",command = lambda: added_value.number(7))
seven.pack(side=LEFT)

eight = Button(frame1,padx = 16,pady = 16,bd = 4,text = "8",fg="red",background="deepskyblue",command = lambda: added_value.number(8))
eight.pack(side=LEFT)

nine = Button(frame1,padx = 16,pady = 16,bd = 4,text = "9",fg="red",background="deepskyblue",command = lambda: added_value.number(9))
nine.pack(side=LEFT)

times = Button(frame1,padx = 16,pady = 16,bd = 4,text = "*",fg="red",background="deepskyblue",command = lambda: added_value.operator("times"))
times.pack(side=LEFT)

#Third row

frame2 = Frame(calc)
frame2.pack(side = TOP)

four = Button(frame2,padx = 16,pady = 16,bd = 4,text = "4",fg="red",background="deepskyblue",command = lambda: added_value.number(4))
four.pack(side=LEFT)

five = Button(frame2,padx = 16,pady = 16,bd = 4,text = "5",fg="red",background="deepskyblue",command = lambda: added_value.number(5))
five.pack(side=LEFT)

six = Button(frame2,padx = 16,pady = 16,bd = 4,text = "6",fg="red",background="deepskyblue",command = lambda: added_value.number(6))
six.pack(side=LEFT)

minus = Button(frame2,padx = 16,pady = 16,bd = 4,text = "-",fg="red",background="deepskyblue",command = lambda: added_value.operator("minus"))
minus.pack(side=LEFT)

#Fourth row

frame3 = Frame(calc)
frame3.pack(side = TOP)

one = Button(frame3,padx = 16,pady = 16,bd = 4,text = "1",fg="red",background="deepskyblue",command = lambda: added_value.number(1))
one.pack(side=LEFT)

two = Button(frame3,padx = 16,pady = 16,bd = 4,text = "2",fg="red",background="deepskyblue",command = lambda: added_value.number(2))
two.pack(side=LEFT)

three = Button(frame3,padx = 16,pady = 16,bd = 4,text = "3",fg="red",background="deepskyblue",command = lambda: added_value.number(3))
three.pack(side=LEFT)

plus = Button(frame3,padx = 16,pady = 16,bd = 4,text = "+",fg="red",background="deepskyblue",command = lambda: added_value.operator("plus"))
plus.pack(side=LEFT)

#Fifth row

frame4 = Frame(calc)
frame4.pack(side = TOP)

zero = Button(frame4,padx = 16,pady = 16,bd = 4,text = "0",fg="red",background="deepskyblue",command = lambda: added_value.number(0))
zero.pack(side=LEFT)

pi = Button(frame4,padx = 16,pady = 16,bd = 4,text = "π",fg="red",background="deepskyblue",command = added_value.pi)
pi.pack(side=LEFT)

decimal = Button(frame4,padx = 16,pady = 16,bd = 4,text = ".",fg="red",background="deepskyblue",command = lambda: added_value.number("."))
decimal.pack(side=LEFT)

equals = Button(frame4,padx = 16,pady = 16,bd = 4,text = "=",fg="red",background="deepskyblue",command = added_value.equals)
equals.pack(side=LEFT)

#Sixth row

frame5 = Frame(calc)
frame5.pack(side = TOP)

square = Button(frame5,padx = 16,pady = 16,bd = 4,text = "x²",fg="red",background="deepskyblue",command = added_value.squared)
square.pack(side=LEFT)

cubed = Button(frame5,padx = 16,pady = 16,bd = 4,text = "x³",fg="red",background="deepskyblue",command = added_value.cubed)
cubed.pack(side=LEFT)

cbroot = Button(frame5,padx = 16,pady = 16,bd = 4,text = "∛",fg="red",background="deepskyblue",command = added_value.cuberoot)
cbroot.pack(side=LEFT)

sqroot = Button(frame5,padx = 16,pady = 16,bd = 4,text = "√",fg="red",background="deepskyblue",command = added_value.squareroot)
sqroot.pack(side=LEFT)

#Seventh row

frame6 = Frame(calc)
frame6.pack(side = TOP)

e = Button(frame6,padx = 16,pady = 16,bd = 4,text = "e",fg="red",background="deepskyblue",command = added_value.natnumber)
e.pack(side=LEFT)

calc.mainloop()

