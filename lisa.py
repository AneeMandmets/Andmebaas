import mysql.connector
from tkinter import *
from lisa_hosta import *
from lisa_iiris import *

def lisa():
    con = mysql.connector.connect(user="root", password="L4ste4i40pet4j4", host="localhost", database="lilled")
    cursor = con.cursor()

    window=Tk()
    window.title("Lillede andmebaas")
    greet = Label(window, font = ("arial", 30, "bold"), text = "Mida soovid lisada?")
    greet.grid(row=0, columnspan=3)

    viewbtn=Button(window, text="Hosta", command=lambda:[lisa_hosta(), window.destroy()], bg="DodgerBlue2", fg="white", font=("arial", 20, "bold"))
    viewbtn.grid(row=3, columnspan=3)

    addbtn=Button(window, text="Iiris", command=lambda:[lisa_iiris(), window.destroy()], bg="DodgerBlue2", fg="white", font=("arial", 20, "bold"))
    addbtn.grid(row=5, columnspan=3)
    pass
