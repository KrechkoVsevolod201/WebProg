from flask import Flask, render_template, url_for, request, redirect
import sqlalchemy
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def null_page():
    return render_template("about.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)