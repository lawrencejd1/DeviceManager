import sqlite3

DB_PATH = 'DeviceManager.db'

def get_tables():

    tables = []

    conn = sqlite3.connect(DB_PATH)

    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table'")

    # print(c.fetchall())

    for table in c.fetchall():
        tables.append(table[0])

    return tables

def get_columns(table):

    try:
        columnNames = []

        sqlCommand = f"PRAGMA table_info({table})"

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute(sqlCommand)
        
        for item in c.fetchall():
            columnNames.append(item[1])

        conn.close()

        return columnNames

    except Exception as e:
        print('Error: ', e)
        return None


def get_list(table):
    try:

        items = []

        sqlCommand = f"SELECT * FROM {table}"

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()
        print("1")
        c.execute(sqlCommand)
        print("2")

        for item in c.fetchall():

            items.append(item)

        conn.close()

        return items

    except Exception as e:
        print("Error get_list: ", e)
        return None

def add_to_list(columns, values):
    try:
        columnString = ""
        valueString = ""

        for column in columns:
            columnString += column + ","
        
        for value in values:
            valueString += value + ","

        sqlCommand = f"INSERT INTO Items ({columnString}) VALUES ({valueString})"
        print(sqlCommand)

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        # c.execute()
        
        conn.commit()

        conn.close()


    except Exception as e:
        print('Error: ', e)
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
        