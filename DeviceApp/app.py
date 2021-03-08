from flask import Flask, render_template, request, redirect
import json
import helper

app =  Flask(__name__)

@app.route("/")
def index():    

    return render_template('index.html')

@app.route("/device_tracker")
def device_tracker():

    items = helper.get_list("device_tracker")

    columns = helper.get_columns("device_tracker")

    return render_template('device_tracker.html', columns=columns, items=items)

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