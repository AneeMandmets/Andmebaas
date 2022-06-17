import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kuva2 import *
from lisamine import *
from kustutamine import *
from muutmine import *
from fmenuu import *

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
    [sg.Button("Rododendronid")],
    [sg.Button("Maitsetaimed")],
    [sg.Button("Muu")],
    [sg.Button("Liigid")],
    [sg.Button("Tagasi")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Kõik":
            window.close()
            kuva_koik()
        elif event == "Hostad":
            window.close()
            kuva_hosta()
        elif event == "Iirised":
            window.close()
            kuva_iiris()
        elif event == "Päevaliiliad":
            window.close()
            kuva_paevaliilia()
        elif event == "Liiliad":
            window.close()
            kuva_liilia()
        elif event == "Jorjenid":
            window.close()
            kuva_jorjen()
        elif event == "Tulbid":
            window.close()
            kuva_tulp()
        elif event == "Nartsissid":
            window.close()
            kuva_nartsiss()
        elif event == "Laugud":
            window.close()
            kuva_lauk()
        elif event == "Kannad":
            window.close()
            kuva_kanna()
        elif event == "Ilupuud ja -põõsad":
            window.close()
            kuva_ip()
        elif event == "Rododendronid":
            window.close()
            kuva_rodo()
        elif event == "Maitsetaimed":
            window.close()
            kuva_maitsetaim()
        elif event == "Muu":
            window.close()
            kuva_muu()
        elif event == "Liigid":
            window.close()
            kuva_liigid()
        elif event == "Tagasi":
            window.close()
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
    [sg.Button("Rododendron")],
    [sg.Button("Maitsetaim")],
    [sg.Button("Muu")],
    [sg.Button("Uus liik")],
    [sg.Button("Tagasi")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Hosta":
            window.close()
            lisa_hosta()
        elif event == "Iiris":
            window.close()
            lisa_iiris()
        elif event == "Päevaliilia":
            window.close()
            lisa_paevaliilia()
        elif event == "Liilia":
            window.close()
            lisa_liilia()
        elif event == "Jorjen":
            window.close()
            lisa_jorjen()
        elif event == "Tulp":
            window.close()
            lisa_tulp()
        elif event == "Nartsiss":
            window.close()
            lisa_nartsiss()
        elif event == "Lauk":
            window.close()
            lisa_lauk()
        elif event == "Kanna":
            window.close()
            lisa_kanna()
        elif event == "Ilupuu või -põõsas":
            window.close()
            lisa_ip()
        elif event == "Rododendron":
            window.close()
            lisa_rodo()
        elif event == "Maitsetaim":
            window.close()
            lisa_maitsetaim()
        elif event == "Muu":
            window.close()
            lisa_muu()
        elif event == "Uus liik":
            window.close()
            lisa_liik()
        elif event == "Tagasi":
            window.close()
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
    [sg.Button("Rododendron")],
    [sg.Button("Maitsetaim")],
    [sg.Button("Muu")],
    [sg.Button("Tagasi")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == "Hosta":
            window.close()
            kustuta_hosta()
        elif event == "Iiris":
            window.close()
            kustuta_iiris()
        elif event == "Päevaliilia":
            window.close()
            kustuta_paevaliilia()
        elif event == "Liilia":
            window.close()
            kustuta_liilia()
        elif event == "Jorjen":
            window.close()
            kustuta_jorjen()
        elif event == "Tulp":
            window.close()
            kustuta_tulp()
        elif event == "Nartsiss":
            window.close()
            kustuta_nartsiss()
        elif event == "Lauk":
            window.close()
            kustuta_lauk()
        elif event == "Kanna":
            window.close()
            kustuta_kanna()
        elif event == "Ilupuu või -põõsas":
            window.close()
            kustuta_ip()
        elif event == "Rododendron":
            window.close()
            kustuta_rodo()
        elif event == "Maitsetaim":
            window.close()
            kustuta_maitsetaim()
        elif event == "Muu":
            window.close()
            kustuta_muu()
        elif event == "Tagasi":
            window.close()
        elif event == sg.WIN_CLOSED:
            break

    window.close()

