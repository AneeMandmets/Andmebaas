import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *
from lisamine import *
from kustutamine import *

def kuvamine():
    layout = [[sg.Text("Lillede andmebaas\nVali lilled, mida kuvada:")],
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
    [sg.Button("Ilupuud ja -põõsad")],
    [sg.Button("Muu")],
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
        elif event == "Ilupuud ja -põõsad":
            kuva_ip()
        elif event == "Muu":
            kuva_muu()
        elif event == sg.WIN_CLOSED:
            break

    window.close()

def lisamine():
    layout = [[sg.Text("Lillede andmebaas\nVali lill, mida lisada:")], 
    [sg.Button("Hosta")],
    [sg.Button("Iiris")],
    [sg.Button("Päevaliilia")],
    [sg.Button("Liilia")],
    [sg.Button("Jorjen")],
    [sg.Button("Tulp")],
    [sg.Button("Nartsiss")],
    [sg.Button("Lauk")],
    [sg.Button("Kanna")],
    [sg.Button("Ilupuu või -põõsas")],
    [sg.Button("Muu")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Hosta":
            lisa_hosta()
        elif event == "Iiris":
            lisa_iiris()
        elif event == "Päevaliilia":
            lisa_paevaliilia()
        elif event == "Liilia":
            lisa_liilia()
        elif event == "Jorjen":
            lisa_jorjen()
        elif event == "Tulp":
            lisa_tulp()
        elif event == "Nartsiss":
            lisa_nartsiss()
        elif event == "Lauk":
            lisa_lauk()
        elif event == "Kanna":
            lisa_kanna()
        elif event == "Ilupuu või -põõsas":
            lisa_ip()
        elif event == "Muu":
            lisa_muu()
        elif event == sg.WIN_CLOSED:
            break

    window.close()

def kustutamine():
    layout = [[sg.Text("Lillede andmebaas\nVali lill, mida kustutada:")], 
    [sg.Button("Hosta")],
    [sg.Button("Iiris")],
    [sg.Button("Päevaliilia")],
    [sg.Button("Liilia")],
    [sg.Button("Jorjen")],
    [sg.Button("Tulp")],
    [sg.Button("Nartsiss")],
    [sg.Button("Lauk")],
    [sg.Button("Kanna")],
    [sg.Button("Ilupuu või -põõsas")],
    [sg.Button("Muu")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Hosta":
            kustuta_hosta()
        elif event == "Iiris":
            kustuta_iiris()
        elif event == "Päevaliilia":
            kustuta_paevaliilia()
        elif event == "Liilia":
            kustuta_liilia()
        elif event == "Jorjen":
            kustuta_jorjen()
        elif event == "Tulp":
            kustuta_tulp()
        elif event == "Nartsiss":
            kustuta_nartsiss()
        elif event == "Lauk":
            kustuta_lauk()
        elif event == "Kanna":
            kustuta_kanna()
        elif event == "Ilupuu või -põõsas":
            kustuta_ip()
        elif event == "Muu":
            kustuta_muu()
        elif event == sg.WIN_CLOSED:
            break

    window.close()
