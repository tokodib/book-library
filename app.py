import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_

load_dotenv()

app = Flask(__name__)

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", "***" if os.getenv("DB_PASSWORD") else "MISSING")

database_url = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_NAME')}"
)


app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'konyvek'

    ID = db.Column(db.Integer, primary_key=True)
    Iro = db.Column(db.String(100), nullable=False)
    Kiado = db.Column(db.String(50), nullable=True)
    Tema = db.Column(db.String(50), nullable=False)
    Cim = db.Column(db.String(150), nullable=False)
    Leiras = db.Column(db.LargeBinary, nullable=True)
    Kep = db.Column(db.LargeBinary, nullable=True)
    ISBN = db.Column(db.String(15), nullable=True)
    KiadasEve = db.Column(db.Integer, nullable=True)
    Nyelv = db.Column(db.String(15), nullable=True)

@app.route('/')
def index():
    return "Book Library is running!"

@app.route('/test-db')
def test_db():
    result = db.session.execute(text("SELECT COUNT(*) FROM konyvek"))
    count = result.scalar()

    return f"Database connection OK: {count}"

@app.route('/books')
def get_books():

    search = request.args.get('search', '')
    print("SEARCH:", search)
    if search:
        search_pattern = f'%{search}%'

        books = Book.query.filter(
            or_(
                Book.Cim.ilike(search_pattern),
                Book.Iro.ilike(search_pattern),
                Book.Kiado.ilike(search_pattern),
                Book.Tema.ilike(search_pattern)
            )
        ).all()
    else:
        books = Book.query.all()

    return render_template('books.html', books=books)

@app.route('/books/<int:book_id>')
def book_detail(book_id):

    book = db.get_or_404(Book, book_id)

    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)