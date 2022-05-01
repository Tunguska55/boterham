from turtle import title
from venv import create
from boterham import app
from flask import render_template
import pyodbc
import os
import subprocess
import json

DB_NAME_JSON = "OefenvragenCWO.json"
TABLE_NAME = "SNEXAMEN"

# TODO add skipped to JSON list

def create_json_db(db_path, table_name):
    json_pure = subprocess.run(["mdb-json", db_path, table_name], capture_output=True, text=True)
    with open(DB_NAME_JSON, 'w') as js:
        json.dump(json_pure.stdout.strip(), js, ensure_ascii=False, indent=4)
    print("DB dumped to JSON for pythonic use")

@app.route("/", methods=['GET', 'POST'])
def index():
    db_path = os.path.join("/boterham/", "OefenvragenCWO.mdb")
    # Need to use alternative method
    if not os.path.exists(DB_NAME_JSON):
        print("JSON DB variant does not exist, creating now")
        create_json_db(db_path, TABLE_NAME)
    with open(DB_NAME_JSON, 'r') as r:
        loaded_db = json.load(r)
    # odbc_connection_str = 'DRIVER={MDBTools};DBQ=' + db_path +';'
    # connection = pyodbc.connect(odbc_connection_str)
    # cursor = connection.cursor()

    # query = "SELECT * FROM SNEXAMEN"
    # cursor.execute(query)
    # rows = cursor.fetchall()
    return render_template("index.html", title="Exam Study", dbrecord=loaded_db)