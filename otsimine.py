import PySimpleGUI as sg
import mysql.connector
from mysql.connector import connect, Error

def otsimine():
    con = mysql.connector.connect(host ="localhost",user = "root",password = 'L4ste4i40pet4j4',database='lilled')
    cursor = con.cursor()
    sqlquery = "SELECT idnimi, nimi FROM nimi WHERE nimi LIKE %s"

    headings = ['ID', 'NIMI']

    layout = [[sg.Text("Lillede otsimine")], 
    [sg.Text("_" * 20)],
    [sg.Text("Sisesta nimi", size=(15, 1)), sg.Input(key='NIMI')],
    [sg.Button("Otsi"), sg.Button("Katkesta")],
    ]

    window = sg.Window("Andmebaas", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Katkesta":
            Vastused = []
            rows_affected = 0
            #window.close()
            break
        elif event == "Otsi":
            window.close()
            cursor.execute(sqlquery, ("%" + values['NIMI'] + "%",))
            Vastused = cursor.fetchall()
            rows_affected = cursor.rowcount
            layout2 = [[sg.Table(Vastused, headings = headings, justification="center", key="-VASTUSED-")],
                [sg.Text("Vasteid kokku:"), sg.Text(rows_affected)],]
            window = sg.Window("Lillede andmebaas", layout2, finalize=True)
            while True:
                event, values = window.read()
                if event==sg.WINDOW_CLOSED:
                    break
                print(event, values)
            break

    window.close()

    
