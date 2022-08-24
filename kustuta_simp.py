import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from tkinter import READABLE
from kuva_simp import *

def kustuta_lill(id):
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Hosta kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_lill(id)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":
            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()