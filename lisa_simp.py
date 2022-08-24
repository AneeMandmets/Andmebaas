from tkinter import READABLE
import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error

def lisa_lill(id):
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = id

    layout = [[sg.Text("Taime lisamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Nimi", size=(15, 1)), sg.InputText(key='NIMI')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":
            cursor.execute(sqlquery, (values['NIMI'], val))
            con.commit()
            window.close()
    window.close()

def lisa_liik():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO liigid (liik) VALUES (%s)"

    layout = [[sg.Text("Uue liigi lisamine")],  
    [sg.Text("_" * 20)],
    [sg.Text("Liigi nimi", size=(15, 1)), sg.InputText(key='NIMI')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":
            cursor.execute(sqlquery, (values['NIMI'],))
            con.commit()
            window.close()
    window.close()