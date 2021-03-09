from flask import Flask, render_template, request, redirect
import json
import helper

app =  Flask(__name__)

helper.get_tables()


@app.route("/index")
@app.route('/')
def index():    

    return render_template('index.html')

##PAGES
@app.route("/<path>")
def show_page(path): 

    # if path == None:
    #     path = str(request.path)
    #     path = path[1:]
    #     print(path)

    items = helper.get_list(path)

    columns = helper.get_columns(path)

    return render_template(f'{path}.html', columns=columns, items=items)

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