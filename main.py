from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    current_date = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=True)
    author_name = db.Column(db.String(300), nullable=True)
    text = db.Column(db.Text, nullable=True)
    date = db.Column(db.Text, nullable=True)
    comment_rate = db.Column(db.Integer, nullable=True)

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
    book = Book.query.all()
    return render_template("home.html", book=book)


@app.route('/posts')
def posts():
    book = Book.query.all()
    return render_template('posts.html', book=book)


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


@app.route('/create_post', methods=['POST', 'GET'])
def create_pasta():
    if request.method == "POST":
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        text = request.form['text']
        comment_rate = request.form['comment_rate']
        comment = Book(book_name=book_name, author_name=author_name, text=text, comment_rate=comment_rate)
        try:
            db.session.add(comment)
            db.session.commit()
            return redirect('/home')
        except:
            return "При создании поста произошла ошибка"
    else:
        return render_template("create-comment.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)