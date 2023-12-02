import sqlite3
import tkinter as tk
def create_db():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('database.db')

    # Datenbankcursor erstellen
    cursor = conn.cursor()

    # Tabelle "Login" erstellen
    cursor.execute('''CREATE TABLE Login (
                        Username TEXT PRIMARY KEY,
                        Fullname TEXT,
                        Password TEXT,
                        Roll TEXT,
                        Budget REAL
                    )''')

    # Tabelle "Produkt" erstellen
    cursor.execute('''CREATE TABLE Produkt (
                        id INTEGER PRIMARY KEY,
                        Hersteller TEXT,
                        Typ TEXT,
                        Ps INTEGER,
                        KMh INTEGER,
                        Preis REAL,
                        Baujahr INTEGER,
                        Anzahl INTEGER,
                        Photo TEXT,
                        verkaufer TEXT,
                        FOREIGN KEY (verkaufer) REFERENCES Login(Username)
                    )''')

    # Tabelle "Bestellung" erstellen
    cursor.execute('''CREATE TABLE Bestellung (
                        user TEXT,
                        P_id INTEGER,
                        Datum DATE,
                        verkaufer TEXT,
                        Anzahl INTEGER,
                        Preis REAL,
                        FOREIGN KEY (user) REFERENCES Login(Username),
                        FOREIGN KEY (P_id) REFERENCES Produkt(id),
                        FOREIGN KEY (verkaufer) REFERENCES Login(Username)
                    )''')

    # Datenbankverbindung schließen

    conn.close()

def ask():
    conn = sqlite3.connect('database.db')
    root= tk.Tk()
    # Datenbankcursor erstellen
    cursor = conn.cursor()
    cursor.execute('''select * From login''')
    row = cursor.fetchall()
    username=[]
    for rows in row:
        username.append(rows[0])

    Label = tk.Label(root, text=username)
    Label.pack()
    root.mainloop()
    print(row)

# ask()

counter = 0
def count(counter):
    counter= counter +1