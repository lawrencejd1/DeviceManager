from flask import Flask, render_template, request, redirect
import json
import helper

app =  Flask(__name__)

@app.route("/")
def main():

    items = helper.get_list()

    columns = helper.get_columns()
    

    return render_template('index.html', columns=columns, items=items)

@app.route('/add', methods=['POST'])
def add_item():

    columns = helper.get_columns()

    return render_template('addItem.html', columns=columns)

    # # Get item from the POST body
    # req_data = request.form
    # title = req_data['title']
    # content = req_data['content']

    # # Add item to the list
    # res_data = helper.add_to_list(title, content)

@app.route('/delete', methods=['POST'])
def delete_items():
    
    helper.delete_all_items()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)