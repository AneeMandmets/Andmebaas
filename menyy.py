import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
from kustuta_simp import kustuta_lill
from muutmine import *
from kuva_simp import *
from kustuta_simp import *
from lisa_simp import *

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
            kuva_lill(1)
        elif event == "Iirised":
            window.close()
            kuva_lill(2)
        elif event == "Päevaliiliad":
            window.close()
            kuva_lill(3)
        elif event == "Liiliad":
            window.close()
            kuva_lill(4)
        elif event == "Jorjenid":
            window.close()
            kuva_lill(5)
        elif event == "Tulbid":
            window.close()
            kuva_lill(6)
        elif event == "Nartsissid":
            window.close()
            kuva_lill(7)
        elif event == "Laugud":
            window.close()
            kuva_lill(8)
        elif event == "Kannad":
            window.close()
            kuva_lill(9)
        elif event == "Ilupuud ja -põõsad":
            window.close()
            kuva_lill(10)
        elif event == "Rododendronid":
            window.close()
            kuva_lill(12)
        elif event == "Maitsetaimed":
            window.close()
            kuva_lill(13)
        elif event == "Muu":
            window.close()
            kuva_lill(11)
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
            lisa_lill(1)
        elif event == "Iiris":
            window.close()
            lisa_lill(2)
        elif event == "Päevaliilia":
            window.close()
            lisa_lill(3)
        elif event == "Liilia":
            window.close()
            lisa_lill(4)
        elif event == "Jorjen":
            window.close()
            lisa_lill(5)
        elif event == "Tulp":
            window.close()
            lisa_lill(6)
        elif event == "Nartsiss":
            window.close()
            lisa_lill(7)
        elif event == "Lauk":
            window.close()
            lisa_lill(8)
        elif event == "Kanna":
            window.close()
            lisa_lill(9)
        elif event == "Ilupuu või -põõsas":
            window.close()
            lisa_lill(10)
        elif event == "Rododendron":
            window.close()
            lisa_lill(12)
        elif event == "Maitsetaim":
            window.close()
            lisa_lill(13)
        elif event == "Muu":
            window.close()
            lisa_lill(11)
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
            kustuta_lill(1)
        elif event == "Iiris":
            window.close()
            kustuta_lill(2)
        elif event == "Päevaliilia":
            window.close()
            kustuta_lill(3)
        elif event == "Liilia":
            window.close()
            kustuta_lill(4)
        elif event == "Jorjen":
            window.close()
            kustuta_lill(5)
        elif event == "Tulp":
            window.close()
            kustuta_lill(6)
        elif event == "Nartsiss":
            window.close()
            kustuta_lill(7)
        elif event == "Lauk":
            window.close()
            kustuta_lill(8)
        elif event == "Kanna":
            window.close()
            kustuta_lill(9)
        elif event == "Ilupuu või -põõsas":
            window.close()
            kustuta_lill(10)
        elif event == "Rododendron":
            window.close()
            kustuta_lill(12)
        elif event == "Maitsetaim":
            window.close()
            kustuta_lill(13)
        elif event == "Muu":
            window.close()
            kustuta_lill(11)
        elif event == "Tagasi":
            window.close()
        elif event == sg.WIN_CLOSED:
            break

    window.close()

