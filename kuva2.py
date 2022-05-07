import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error

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


def kuva_hosta():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '1'"
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

def kuva_iiris():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '2'"
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

def kuva_paevaliilia():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '3'"
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

def kuva_liilia():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '4'"
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

def kuva_jorjen():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '5'"
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

def kuva_tulp():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '6'"
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

def kuva_nartsiss():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '7'"
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

def kuva_lauk():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '8'"
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

def kuva_kanna():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '9'"
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

def kuva_ip():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '10'"
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

def kuva_muu():
    headings = ['ID', 'NIMI']

    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE liik_idliik = '11'"
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