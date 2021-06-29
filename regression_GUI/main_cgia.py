# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:34:16 2020

@author: jain
"""

import tkinter as tk
import datetime
from datetime import date
import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from pandas import DataFrame
from PIL import ImageTk
import PIL.Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from q13 import *

from q18 import *



def welcome():
    global screen_13
    screen_13=Tk()
    screen_13.configure(bg='white')
    screen_13.geometry("600x665+20+40")
    #screen_13.resizable(False) 
    Label(screen_13, text=" Linear regression ", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_13, text="",bg='#B9FFFF',width=76,height=34).place(x=32,y=80)
          
    Label(screen_13, text="Choose an option:", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg= "#800080", fg= "white", anchor= NW).place(x= 225, y= 200)
    Button(screen_13, text= "Regression", width= 18, height= 1, font=("Times New Roman", 15, "bold"),command=gui_13, bg="#00CDCD", fg= "white", anchor= CENTER).place(x=195, y= 280)
    Button(screen_13, text= "update", width= 18, height= 1, font=("Times New Roman", 15, "bold"),command=destroy_screen_2, bg= "#00CDCD", fg= "white", anchor= CENTER).place(x= 195, y= 350)       
    screen_13.mainloop()

def destroy_screen_1():
    screen_13.destroy()
    gui_18_1()
    welcome()
    
def destroy_screen_2():
    screen_13.destroy()
    gui_18_2()
    welcome()
    
welcome()    
#option_page()