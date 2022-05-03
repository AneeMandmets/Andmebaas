import mysql.connector
from mysql.connector import connect, Error
from tkinter import *
from kuva import *
from lisa import *

con = mysql.connector.connect(user="root", password="L4ste4i40pet4j4", host="localhost", database="lilled")
cursor = con.cursor()

window=Tk()
window.title("Lillede andmebaas")
greet = Label(window, font = ("arial", 30, "bold"), text = "Lillede andmebaas")
greet.grid(row=0, columnspan=3)

viewbtn=Button(window, text="Kuva lilled", command=kuva, bg="DodgerBlue2", fg="white", font=("arial", 20, "bold"))
viewbtn.grid(row=3, columnspan=3)

addbtn=Button(window, text="Lisa lilli", command=lisa, bg="DodgerBlue2", fg="white", font=("arial", 20, "bold"))
addbtn.grid(row=5, columnspan=3)

window.mainloop()
