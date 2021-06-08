import sqlite3

DB_PATH = 'DeviceManager.db'


def get_tables():

    tables = []

    conn = sqlite3.connect(DB_PATH)

    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table'")

    for table in c.fetchall():
        tables.append(table[0])
    
    tables.sort()

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
        c.execute(sqlCommand)

        for item in c.fetchall():

            items.append(item)

        conn.close()

        return items

    except Exception as e:
        print("Error get_list: ", e)
        return None

def find_item_details(table, itemID):
    
    try:

        columns = get_columns(table)

        itemDetails = []

        sqlCommand = f"SELECT * FROM {table} WHERE ID={itemID}"

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()
        c.execute(sqlCommand)

        for detail in c.fetchall():
            for item in detail:
                itemDetails.append(item)

        conn.close()

        return itemDetails

    except Exception as e:
        print("Error get_list: ", e)
        return None


def add_to_list(table, values):

    columns = get_columns(table)

    columns = columns[1:]

    try:
        columnString = ""
        valueString = ""

        for column in columns:
            columnString += column + ","

        columnString = columnString[:-1]
        
        for value in values:
            
            valueString += '"' + value + '"' + ','

        valueString = valueString[:-1]

        sqlCommand = f"INSERT INTO {table} ({columnString}) VALUES ({valueString})"

        print(sqlCommand)

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute(sqlCommand)
        
        conn.commit()

        conn.close()


    except Exception as e:
        print('Error: ', e)
        return None

def edit_item(table, itemID, newItemDetails):
    try:

        columns = get_columns(table)

        setCommand = ''

        for i, column in enumerate(columns):

            if(column == "ID"):
                tempStr = newItemDetails[i].replace(" ", "")

            tempStr = "'" + newItemDetails[i] + "'"

            if(column != "ID"):
                setCommand += f"{column}={tempStr}, "

        setCommand = setCommand[:-2]

        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        sqlCommand = f"UPDATE {table} SET {setCommand} WHERE ID={itemID}"

        c.execute(sqlCommand)

        conn.commit()
        conn.close()

    except Exception as e:
        print("Error: ", e)
        return None

def delete_item(table, itemID):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        sqlCommand = f"DELETE FROM {table} WHERE ID={itemID}"

        c.execute(sqlCommand)

        conn.commit()
        conn.close()


    except Exception as e:
        print("Error: ", e)
        return None
        