from flask import Flask, render_template, request, redirect, url_for
import json
import helper

app =  Flask(__name__)

@app.context_processor
def layoutVariables():

    try:
        pageNames = []

        dataTables = helper.get_tables()

        dataTables.remove("sqlite_sequence")

        for table in dataTables:
            table = table.replace("_", " ")
            table = table.title()
            pageNames.append(table)

        return dict(dataTables=dataTables, pageNames=pageNames)

    except Exception as e:
        print("Not loading variables: ", e)


@app.route("/index")
@app.route('/')
def index():

    return render_template('index.html')

##DISPLAY PAGES FROM TABLES
@app.route("/tables/<table>")
def show_page(table): 


    items = helper.get_list(table)
    items.reverse()

    columns = helper.get_columns(table)

    tableName = table.replace("_",  " ")

    return render_template('tablePage.html', table=table, tableName=tableName, columns=columns, items=items)

##-----------------------------

@app.route('/add', methods=['POST'])
def add_page():

    table = request.form['table']

    columns = helper.get_columns(table)

    columns = columns[1:]

    #Each item in rows is a row itself
    rows = []
    #Each item in row is a column which then get inserted into the rows list
    row = []

    for i, column in enumerate(columns, 1):

        #Every 4 items make a new row
        if(i % 4 == 0 and i > 0):
            row.append(column)
            rows.append(row)
            row = []
          
        else:
            row.append(column)
    #If less than 4 items, just append the row to the rows list once all columns are added
    rows.append(row)

    tableName = table.replace("_",  " ")

    return render_template('addItem.html', table=table, tableName=tableName, columns=columns, rows=rows)


@app.route('/add/submit', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.form

    print(req_data)

    table = req_data['table']

    values = []

    for item in req_data:
        if (item == "table"):
            pass
        else:
            print(req_data[item])
            values.append(req_data[item])



    # Add item to the list
    res_data = helper.add_to_list(table, values)

    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit_item():
    
    item = list(request.form)
    itemInfo = item[0].split(':')
    table = itemInfo[0]
    itemID = itemInfo[1]

    print(f"Table: {table} - Item ID: {itemID}")

    columns = helper.get_columns(table)
    columns = columns[1:]

    itemDetails = helper.find_item_details(table, itemID)
    itemDetails = itemDetails[1:]

    return render_template('editPage.html', table=table, columns=columns, itemID=itemID, itemDetails=itemDetails)

@app.route('/edit/submit', methods=["POST"])
def submit_edit():

    newItemDetails = []

    editData = request.form

    table = editData['table']
    itemID = editData['itemID']

    editDataKeys = list(editData)

    for i, key in enumerate(editDataKeys):
        if i == 0:
            pass
        else:
            newItemDetails.append(editData[str(key)])

    helper.edit_item(table, itemID, newItemDetails)


    return redirect(url_for('show_page', table=table))

@app.route('/delete', methods=['POST'])
def delete_item():
    
    item = list(request.form)
    itemInfo = item[0].split(':')
    table = itemInfo[0]
    itemID = itemInfo[1]

    return render_template('confirmPage.html', table=table, itemID=itemID)

@app.route('/delete/submit', methods=['POST'])
def delete_item_confirm():
    
    itemData = request.form
    table = itemData['table']
    itemID = itemData['itemID']

    print(f"Table: {table} - Item ID: {itemID}")

    helper.delete_item(table, itemID)

    return redirect(url_for('show_page', table=table))

@app.route('/delete/undo', methods=['POST'])
def no_delete():

    table = request.form['table']

    return redirect(url_for('show_page', table=table))


if __name__ == "__main__":
    app.run(debug=True)