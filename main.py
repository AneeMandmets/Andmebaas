import tkinter as tk
import mysql.connector
from mysql.connector import connect, Error
from tkinter import *
from getpass import getpass

#usr=input("Enter username: ")
#pasw=getpass("Enter password: ")

con = mysql.connector.connect(user="root", password="L4ste4i40pet4j4", host="localhost", database="lilled")
cursor = con.cursor()
cursor.execute("SELECT idnimi, nimi FROM nimi")
for(idnimi, nimi) in cursor:
    print("{} {}".format(idnimi, nimi))
cursor.close
con.close()
    