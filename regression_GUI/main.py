
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
from PIL import ImageTk,Image  
 




def welcome():
    global screen_13
    screen_13=Tk()
    screen_13.configure(bg='white')
    screen_13.geometry("1200x1300+20+40")
    #screen_13.resizable(False)
    Label(screen_13, text=" Data Mining Exp 1", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_13, text="Choose an option:", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg= "#800080", fg= "white", anchor= NW,justify = CENTER).place(x= 225, y= 200)
    Button(screen_13, text= "Regression", width= 18, height= 1, font=("Times New Roman", 15, "bold"), bg="#00CDCD", fg= "white",command = reg, anchor= CENTER).place(x=195, y= 280)
    Button(screen_13, text= "K Means", width= 18, height= 1, font=("Times New Roman", 15, "bold"), bg= "#00CDCD", fg= "white",command = Km, anchor= CENTER).place(x= 195, y= 350)
    Button(screen_13, text= "Isolation Forest", width= 18, height= 1, font=("Times New Roman", 15, "bold"), bg="#00CDCD", fg= "white",command = IF, anchor= CENTER).place(x=195, y= 420)
    Button(screen_13, text= "K Nearest Neighbours", width= 18, height= 1, font=("Times New Roman", 15, "bold"), bg= "#00CDCD", fg= "white",command = KNN, anchor= CENTER).place(x= 195, y= 490)       
    screen_13.mainloop()


def reg():  
    screen_13.destroy()
    root = Tk()  
    canvas = Canvas(root, width = 3000, height = 3000)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("reg.png"))  
    canvas.create_image(200, 200, anchor=NW, image=img) 
    root.mainloop() 
    
def Km():  
    screen_13.destroy()
    root = Tk()  
    canvas = Canvas(root, width = 3000, height = 3000)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("Km.png"))  
    canvas.create_image(200, 200, anchor=NW, image=img) 
    root.mainloop() 

def IF():  
    screen_13.destroy()
    root = Tk()  
    canvas = Canvas(root, width = 3000, height = 3000)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("IF.png"))  
    canvas.create_image(200, 200, anchor=NW, image=img) 
    root.mainloop() 

def KNN():  
    screen_13.destroy()
    root = Tk()  
    canvas = Canvas(root, width = 3000, height = 3000)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("KNN.png"))  
    canvas.create_image(200, 200, anchor=NW, image=img) 
    root.mainloop() 

welcome()    
#option_page()

