from socket import NI_NUMERICHOST
from tkinter import *
from tkinter import messagebox
import mysql.connector

def lisa_and_iiris():
    global nimi

    lnimi=nimi.get()

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()

    sqlquery="INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = (lnimi, 2)
    try:
        cursor.execute(sqlquery, val)
        con.commit()
        messagebox.showinfo("Lisamine õnnestus!")
    except:
        messagebox.showinfo("Lisamine ebaõnnestus")

def lisa_iiris():
    global nimi

    window=Tk()
    window.title("Lillede andmebaas")
    greet = Label(window, font=("arial", 20, "bold"), text="Iirise lisamine")
    greet.grid(row=0, columnspan=3)

    L = Label(window, font = ('arial', 15, 'bold'), text = "Sisesta iirise nimi: ")
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    nimi=Entry(window,width=5,font =('arial', 15, 'bold'))
    nimi.grid(row=2,column=3)


    submitbtn=Button(window, text="Lisa", command=lambda:[lisa_and_iiris(), window.destroy()], bg="DodgerBlue2", fg="white", font=("arial", 15, "bold"))
    submitbtn.grid(row=4, columnspan=3)
    pass