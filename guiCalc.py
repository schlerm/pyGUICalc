from tkinter import *
import sys
import math
from lib2to3.pgen2.token import OP

#Find out how to detect a math overflow error and make an error message for it in a popup.
# if detect error:
#    display error message

#Figure out if tkinter supports backgrounds (hopefully animated ones) and add them in

#Functions and actual calculator stuff

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.inputValue = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
    def number(self,num):
        self.result = False
        ans = display.get()
        input = str(num)
        if self.inputValue:
            self.current = input
            self.inputValue = False
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
        self.inputValue = True
        self.check_sum = False
        self.display(self.total)      
     
    def operator(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.validOperator()
        elif not self.result:
            self.total = self.current
            self.inputValue = True
        self.check_sum = True
        self.op = op
        self.result = False
            
    def clearDisplay(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.inputValue = True
    
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
        
    def percent(self):
        self.result = False
        self.current = (float(display.get())/100)
        self.display(self.current)      
          
#Declaring the calculator and other things

added_value = Calc()
calc=Tk()
frame = Frame(calc)
frame.pack()
calc.title("APCSP Create Task Calculator")
calc.resizable(width = False, height = False)
calclabel=Label(calc,text="GUICalc",font=("Courier New",30,'bold'))

#Display

display=Entry(frame,bd = 20,insertwidth = 1,font = 30)
display.insert(0,"0")
display.pack(side = TOP)
display.configure(state="disabled")

#First row

frame0 = Frame(calc)
frame0.pack(side = TOP)

AC = Button(frame0,padx = 16,pady = 16,bd = 8,text = "C",fg="gray",command = added_value.allClear)
AC.pack(side=LEFT)

negate = Button(frame0,padx = 16,pady = 16,bd = 8,text = "+/-",fg="gray",command = added_value.negate)
negate.pack(side=LEFT)

percent = Button(frame0,padx = 16,pady = 16,bd = 8,text = "%",fg="gray",command = added_value.percent)
percent.pack(side=LEFT)

divide = Button(frame0,padx = 16,pady = 16,bd = 8,text = "/",fg="gray",command = lambda: added_value.operator("divide"))
divide.pack(side=LEFT)

#Second row

frame1 = Frame(calc)
frame1.pack(side = TOP)

seven = Button(frame1,padx = 16,pady = 16,bd = 8,text = "7",fg="gray",command = lambda: added_value.number(7))
seven.pack(side=LEFT)

eight = Button(frame1,padx = 16,pady = 16,bd = 8,text = "8",fg="gray",command = lambda: added_value.number(8))
eight.pack(side=LEFT)

nine = Button(frame1,padx = 16,pady = 16,bd = 8,text = "9",fg="gray",command = lambda: added_value.number(9))
nine.pack(side=LEFT)

times = Button(frame1,padx = 16,pady = 16,bd = 8,text = "*",fg="gray",command = lambda: added_value.operator("times"))
times.pack(side=LEFT)

#Third row

frame2 = Frame(calc)
frame2.pack(side = TOP)

four = Button(frame2,padx = 16,pady = 16,bd = 8,text = "4",fg="gray",command = lambda: added_value.number(4))
four.pack(side=LEFT)

five = Button(frame2,padx = 16,pady = 16,bd = 8,text = "5",fg="gray",command = lambda: added_value.number(5))
five.pack(side=LEFT)

six = Button(frame2,padx = 16,pady = 16,bd = 8,text = "6",fg="gray",command = lambda: added_value.number(6))
six.pack(side=LEFT)

minus = Button(frame2,padx = 16,pady = 16,bd = 8,text = "-",fg="gray",command = lambda: added_value.operator("minus"))
minus.pack(side=LEFT)

#Fourth row

frame3 = Frame(calc)
frame3.pack(side = TOP)

one = Button(frame3,padx = 16,pady = 16,bd = 8,text = "1",fg="gray",command = lambda: added_value.number(1))
one.pack(side=LEFT)

two = Button(frame3,padx = 16,pady = 16,bd = 8,text = "2",fg="gray",command = lambda: added_value.number(2))
two.pack(side=LEFT)

three = Button(frame3,padx = 16,pady = 16,bd = 8,text = "3",fg="gray",command = lambda: added_value.number(3))
three.pack(side=LEFT)

plus = Button(frame3,padx = 16,pady = 16,bd = 8,text = "+",fg="gray",command = lambda: added_value.operator("plus"))
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

equals = Button(frame4,padx = 16,pady = 16,bd = 8,text = "=",fg="gray",command = added_value.equals)
equals.pack(side=LEFT)

#Sixth row

frame5 = Frame(calc)
frame5.pack(side = TOP)

square = Button(frame5,padx = 16,pady = 16,bd = 8,text = "x²",fg="gray",command = added_value.squared)
square.pack(side=LEFT)

cubed = Button(frame5,padx = 16,pady = 16,bd = 8,text = "x³",fg="gray",command = added_value.cubed)
cubed.pack(side=LEFT)




calc.mainloop()

