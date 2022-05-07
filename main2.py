import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *
from menyy import *
from lisamine import *
from muutmine import *


layout = [[sg.Text("Lillede andmebaas\nVali tegevus, mida teha:")], 
[sg.Button("Kuvamine")],
[sg.Button("Lisamine")],
[sg.Button("Kustutamine")],
[sg.Button("Muutmine")],
]

window = sg.Window("Andmebaas", layout, resizable=True)
while True:
    event, values = window.read()
    if event == "Kuvamine":
        kuvamine()
    elif event == "Lisamine":
        lisamine()
    elif event == "Kustutamine":
        kustutamine()
    elif event == "Muutmine":
        muutmine()
    elif event == sg.WIN_CLOSED:
        break

window.close()
