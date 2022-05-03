from tkinter import *
from tkinter import messagebox
import mysql.connector

def kuva():
    global id

    window=Tk()
    window.title("Lillede andmebaas")

    greet = Label(window, font = ("arial", 20, "bold"), text = "Lillede kuvamine")
    greet.grid(row=0, columnspan=3)
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()

    sqlquery = "SELECT idnimi, nimi FROM nimi"
    try:
        cursor.execute(sqlquery)
        L = Label(window, font=("arial", 20), text = "%-20s%-20s"%("ID", "Nimi"))
        L.grid(row=1, columnspan=2)
        L=Label(window, font=("arial", 20), text="------------------------------------------------")
        L.grid(row=2, columnspan=2)
        x=4
        for (idnimi, nimi) in cursor:
            L=Label(window, font=("arial", 15), text="%-10s%-20s"%(idnimi, nimi))
            L.grid(row = x, columnspan=2)
            x+=1
    except:
        messagebox.showinfo("Error andmete saamisel.")
    pass

        