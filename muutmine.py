import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *
from menyy import *

def muutmine():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "UPDATE nimi SET nimi = %s WHERE idnimi = %s"

    layout = [[sg.Text("Taime nime muutmine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta ID", size=(15, 1)), sg.Input(key='ID')],
    [sg.Text("Sisesta uus nimi", size=(15, 1)), sg.InputText(key='NIMI')],
    [sg.Button("OK"), sg.Button("Tagasi")],
    ]
    window = sg.Window("Andmebaas", layout)
    kuva_koik()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Tagasi":
            window.close()
        elif event == "OK":
            cursor.execute(sqlquery, (values['NIMI'], values['ID']))
            con.commit()
            window.close()
    window.close()
