from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_pasta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pasta(db.Model):
    __tablename__ = 'pasta'
    current_date = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=current_date)

    def __init__(self, title, intro, text):
        self.title = title.strip()
        self.intro = intro.strip()
        self.text = text.strip()


@app.route('/')
def null_page():
    return render_template("about.html")


@app.route('/home')
def home():
    q = request.args.get('q')

    if q:
        articles = Pasta.query.filter(Pasta.title.contains(q) | Pasta.intro.contains(q) | Pasta.text.contains(q)).all()
    else:
        articles = Pasta.query.order_by(Pasta.date.desc()).all()
    return render_template("home.html", articles=articles)


@app.route('/admin')
def password_menu():
    password = request.args.get('password')
    pas = "1234"
    if password == pas:
        return redirect('/admin/home')
    return render_template("admin-pass.html")


@app.route('/admin/home')
def home_admin():
    q = request.args.get('q')

    if q:
        articles = Pasta.query.filter(Pasta.title.contains(q) | Pasta.intro.contains(q) | Pasta.text.contains(q)).all()
    else:
        articles = Pasta.query.order_by(Pasta.date.desc()).all()
    return render_template("home-admin.html", articles=articles)


@app.route('/about')
def about():
    return render_template("about.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)