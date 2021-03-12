from flask import Flask, render_template, request, redirect
import json
import helper

app =  Flask(__name__)

@app.context_processor
def layoutVariables():

    try:
        pageNames = []

        dataTables = helper.get_tables()

        for table in dataTables:
            table = table.replace('_', " ")
            table = table.title()
            pageNames.append(table)
            print(pageNames)

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

    return render_template('tablePage.html', columns=columns, items=items)

##-----------------------------

@app.route('/add', methods=['POST'])
def add_page():

    columns = helper.get_columns()

    return render_template('addItem.html', columns=columns)


@app.route('/add/submit', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.form
    title = req_data['title']
    content = req_data['content']

    # Add item to the list
    res_data = helper.add_to_list(columns, values)

    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_items():
    
    helper.delete_all_items()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)