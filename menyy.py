import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *

def kuvamine():
    layout = [[sg.Text("Lillede andmebaas\n Vali lilled, mida kuvada:")],
    [sg.Button("Kõik")], 
    [sg.Button("Hostad")],
    [sg.Button("Iirised")],
    [sg.Button("Päevaliiliad")],
    [sg.Button("Liiliad")],
    [sg.Button("Jorjenid")],
    [sg.Button("Tulbid")],
    [sg.Button("Nartsissid")],
    [sg.Button("Laugud")],
    [sg.Button("Kannad")],
    [sg.Button("Ilupuud ja põõsad")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Kõik":
            kuva_koik()
        elif event == "Hostad":
            kuva_hosta()
        elif event == "Iirised":
            kuva_iiris()
        elif event == "Päevaliiliad":
            kuva_paevaliilia()
        elif event == "Liiliad":
            kuva_liilia()
        elif event == "Jorjenid":
            kuva_jorjen()
        elif event == "Tulbid":
            kuva_tulp()
        elif event == "Nartsissid":
            kuva_nartsiss()
        elif event == "Laugud":
            kuva_lauk()
        elif event == "Kannad":
            kuva_kanna()
        elif event == "Ilupuud ja põõsad":
            kuva_ip()
        elif event == sg.WIN_CLOSED:
            break

    window.close()