# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:12:44 2020

@author: Hitesh Pattanayak
"""

from tkinter import *


window = Tk()
window.title("km to miles converter")

def kmToMiles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,miles)

l1=Label(window, text="km")
l1.grid(row=0,column=1)

l2=Label(window, text="miles")
l2.grid(row=0,column=2)

b1=Button(window,text="Conv. Km to Miles",command=kmToMiles)
b1.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=1,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=2)

window.mainloop()