import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from menyy import *
from lisa_simp import *
from muutmine import *
from otsimine import *

layout = [[sg.Text("Lillede andmebaas\nVali tegevus, mida teha:")],
[sg.Text("_" * 40)], 
[sg.Button("Kuvamine")],
[sg.Button("Otsimine")],
[sg.Button("Lisamine")],
[sg.Button("Kustutamine")],
[sg.Button("Muutmine")],
[sg.Button("Lahkumine")],
]

window = sg.Window("Andmebaas", layout, resizable=True)
while True:
    event, values = window.read()
    if event == "Kuvamine":
        kuvamine()
    elif event == "Otsimine":
        otsimine()
    elif event == "Lisamine":
        lisamine()
    elif event == "Kustutamine":
        kustutamine()
    elif event == "Muutmine":
        muutmine()
    elif event == "Lahkumine":
        window.close()
    elif event == sg.WIN_CLOSED:
        break

window.close()


