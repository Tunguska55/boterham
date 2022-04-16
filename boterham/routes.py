from turtle import title
from boterham import app
from flask import render_template
import pyodbc
import os
import subprocess
import json

def create_json_db(db_path, table_name):
    json_pure = subprocess.run(["mdb-json", db_path, table_name], capture_output=True, text=True)
    with open('"OefenvragenCWO.json', 'w') as js:
        json.dump(json_pure, js)

@app.route("/", methods=['GET', 'POST'])
def index():
    db_path = os.path.join("/boterham/", "OefenvragenCWO.mdb")
    # Need to find alternative method
    
    # odbc_connection_str = 'DRIVER={MDBTools};DBQ=' + db_path +';'
    # connection = pyodbc.connect(odbc_connection_str)
    # cursor = connection.cursor()

    # query = "SELECT * FROM SNEXAMEN"
    # cursor.execute(query)
    # rows = cursor.fetchall()
    return render_template("index.html", title="Exam Study", dbrecord=rows)