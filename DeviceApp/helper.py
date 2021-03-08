import sqlite3

DB_PATH = 'DeviceManager.db'

def get_columns():

    columnNames = []

    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute("PRAGMA table_info(Items)")
        
        for item in c.fetchall():
            columnNames.append(item[1])

        conn.close()

        return columnNames

    except Exception as e:
        print('Error: ', e)
        return None

def add_to_list(title, content):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute("INSERT INTO Items (title, content) VALUES (?,?)", (title, content))
        
        conn.commit()

        conn.close()


    except Exception as e:
        print('Error: ', e)
        return None

def get_list():
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute("SELECT * FROM Device_Tracker")

        items = c.fetchall()

        conn.close()

        return items

    except Exception as e:
        print("Error: ", e)
        return None

def delete_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute("DELETE FROM Items")

        conn.commit()
        conn.close()
    except Exception as e:
        print("Error: ", e)
        return None
        