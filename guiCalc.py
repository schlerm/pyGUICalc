from tkinter import *

def calc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj