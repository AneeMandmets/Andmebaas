import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *
from menyy import *

layout = [[sg.Text("Lillede andmebaas\nVali tegevus, mida teha:")], 
[sg.Button("Kuvamine")],
[sg.Button("Lisamine")],
]

window = sg.Window("Andmebaas", layout)
while True:
    event, values = window.read()
    if event == "Kuvamine":
        kuvamine()
    elif event == sg.WIN_CLOSED:
            break

window.close()