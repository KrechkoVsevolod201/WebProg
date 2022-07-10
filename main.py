from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_pasta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'pasta'
    current_date = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author_name = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    comment_rate = db.Column(db.Integer, nullable=False)

    def __init__(self, book_name, author_name, text, comment_rate):
        self.book_name = book_name.strip()
        self.author_name = author_name.strip()
        self.text = text.strip()
        self.comment_rate = comment_rate.strip()


@app.route('/')
def null_page():
    return render_template("about.html")


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/posts')
def posts():
    book = Book.query.first()
    return render_template('posts.html')


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
    return render_template("home-admin.html")


@app.route('/about')
def about():
    return render_template("about.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)