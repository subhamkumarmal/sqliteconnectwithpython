import sqlite3
def cursor():

    conn = sqlite3.connect('Inventory.db')
    curs = conn.cursor()
    return curs,conn