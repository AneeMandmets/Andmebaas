import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from tkinter import READABLE

from kuva2 import *

def kustuta_hosta():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Hosta kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_hosta()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":
            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_iiris():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Iirise kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_iiris()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_paevaliilia():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Päevaliilia kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_paevaliilia()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_liilia():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Liilia kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_liilia()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_jorjen():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Jorjeni kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_jorjen()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_tulp():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Tulbi kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_tulp()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_nartsiss():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Nartsissi kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_nartsiss()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_lauk():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Laugu kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_lauk()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_kanna():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Kanna kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_kanna()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_ip():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Ilupuu või -põõsa kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_ip()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()

def kustuta_muu():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "DELETE FROM nimi WHERE idnimi = %s"

    layout = [[sg.Text("Muu taime kustutamine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Button("OK"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    kuva_muu()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            break
        elif event == "OK":

            cursor.execute(sqlquery, (values['ID'],))
            con.commit()
            window.close()
    window.close()