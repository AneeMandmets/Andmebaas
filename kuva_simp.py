import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error
def kuva_lill(id):
    headings = ['ID', 'NIMI']
    con = mysql.connector.connect(host ="localhost", user = "root", password = "L4ste4i40pet4j4", database="lilled")
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = %s"
    cursor.execute(sqlquery, (id,))

    lilled = cursor.fetchall()
    rows_affected = cursor.rowcount

    layout = [[sg.Table(lilled, headings = headings, justification="center", key="-LILLED-")],
    [sg.Text("Lilli kokku:"), sg.Text(rows_affected)],]
    window = sg.Window("Lillede andmebaas", layout, finalize=True)

    while True:
        event, values = window.read()
        if event==sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()

def kuva_koik():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()    
    sqlquery = "SELECT idnimi, nimi FROM nimi"
    cursor.execute(sqlquery)

    lilled = cursor.fetchall()
    rows_affected = cursor.rowcount

    layout = [[sg.Table(lilled, headings = headings, justification="center", key="-LILLED-")],
    [sg.Text("Lilli kokku:"), sg.Text(rows_affected)],]
    window = sg.Window("Lillede andmebaas", layout, finalize=True)

    while True:
        event, values = window.read()
        if event==sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()

def kuva_liigid():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idliik, liik FROM liigid"
    cursor.execute(sqlquery)

    lilled = cursor.fetchall()
    rows_affected = cursor.rowcount

    layout = [[sg.Table(lilled, headings = headings, justification="center", key="-LIIGID-")],
    [sg.Text("Liike kokku:"), sg.Text(rows_affected)],]
    window = sg.Window("Lillede andmebaas", layout, finalize=True)

    while True:
        event, values = window.read()
        if event==sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()