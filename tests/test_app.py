import os

import pytest
from dotenv import load_dotenv

load_dotenv(".env.test")

from app import create_app, db, Book



@pytest.fixture
def app():
    test_database_url = (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
        f"/konyvek_test"
    )

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": test_database_url
    })

    with app.app_context():
        db.drop_all()
        db.create_all()

        book = Book(
            Iro="Test Author",
            Kiado="Test Publisher",
            Tema="Test",
            Cim="Test Book",
            ISBN="1234567890",
            KiadasEve=2026,
            Nyelv="English"
        )

        db.session.add(book)
        db.session.commit()

    yield app

    with app.app_context():
        db.session.remove()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b"Book Library is running!" in response.data

def test_database_connection(client):
    response = client.get('/test-db')

    assert response.status_code == 200
    assert b"Database connection OK" in response.data

def test_books_page(client):
    response = client.get('/books')

    assert response.status_code == 200
    assert b"Book Library" in response.data

def test_book_detail(app, client):
    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}')

    assert response.status_code == 200
    assert book.Cim.encode() in response.data

def test_add_book_page(client):
    response = client.get('/add-book')

    assert response.status_code == 200
    assert b"Add Book" in response.data

def test_edit_book_page(app, client):
    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}/edit')

    assert response.status_code == 200
    assert book.Cim.encode() in response.data

def test_delete_book_reuires_post(app, client):

    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}/delete')

    assert response.status_code == 405

def test_add_book(client, app):
    respose = client.post('/add-book', data={
        'Iro': 'Test POST Author',
        'Kiado': 'Test POST Publisher',
        'Tema': 'Testing',
        'Cim': 'POST Test Book',
        'ISBN': '9876543210',
        'KiadasEve': '2026',
        'Nyelv': 'English'
    })

    assert respose.status_code == 302

    with app.app_context():
        book = Book.query.filter_by(Cim='POST Test Book').first()

        assert book is not None
        assert book.Iro == 'Test POST Author'
        assert book.Kiado == 'Test POST Publisher'
        assert book.ISBN == '9876543210'

def test_edit_book(client, app):
    with app.app_context():
        book = Book.query.first()
        book_id = book.ID

    response = client.post(f'/books/{book_id}/edit', data={
        'Iro': 'Edited Author',
        'Kiado': 'Edited Publisher',
        'Tema': 'Edited Topic',
        'Cim': 'Edited Test Book',
        'ISBN': '1111111111',
        'KiadasEve': '2025',
        'Nyelv': 'Hungarian'        
    })

    assert response.status_code == 302
    with app.app_context():
        book = db.session.get(Book, book_id)

        assert book.Iro == 'Edited Author'
        assert book.Kiado == 'Edited Publisher'
        assert book.Tema == 'Edited Topic'
        assert book.Cim == 'Edited Test Book'
        assert book.ISBN == '1111111111'
        assert book.KiadasEve == 2025
        assert book.Nyelv == 'Hungarian'

def test_delete_book(client, app):
    with app.app_context():
        book = Book.query.first()
        book_id = book.ID

    response = client.post(f'/books/{book_id}/delete')

    assert response.status_code == 302

    with app.app_context():
        book = db.session.get(Book, book_id)

        assert book is None
