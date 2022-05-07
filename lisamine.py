from tkinter import READABLE
import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error

def lisa_hosta():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 1

    layout = [[sg.Text("Hosta lisamine")], 
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

def lisa_iiris():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 2

    layout = [[sg.Text("Iirise lisamine")], 
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

def lisa_paevaliilia():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 3

    layout = [[sg.Text("Päevaliilia lisamine")], 
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

def lisa_liilia():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 4

    layout = [[sg.Text("Liilia lisamine")], 
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

def lisa_jorjen():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 5

    layout = [[sg.Text("Jorjeni lisamine")], 
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

def lisa_tulp():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 6

    layout = [[sg.Text("Tulbi lisamine")], 
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

def lisa_nartsiss():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 7

    layout = [[sg.Text("Nartsissi lisamine")], 
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

def lisa_lauk():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 8

    layout = [[sg.Text("Laugu lisamine")], 
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

def lisa_kanna():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 9

    layout = [[sg.Text("Kanna lisamine")], 
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

def lisa_ip():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 10

    layout = [[sg.Text("Ilupuu või -põõsa lisamine")], 
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

def lisa_muu():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "INSERT INTO nimi (nimi, liik_idliik) VALUES (%s, %s)"
    val = 11

    layout = [[sg.Text("Muu taime lisamine")],  
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