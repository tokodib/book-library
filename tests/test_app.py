from app import app, Book


def test_home_page():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"Book Library is running!" in response.data

def test_database_connection():
    client = app.test_client()

    response = client.get('/test-db')

    assert response.status_code == 200
    assert b"Database connection OK" in response.data

def test_books_page():
    client = app.test_client()

    response = client.get('/books')

    assert response.status_code == 200
    assert b"Book Library" in response.data

def test_book_detail():
    client = app.test_client()

    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}')

    assert response.status_code == 200
    assert book.Cim.encode() in response.data

def test_add_book_page():
    client = app.test_client()

    response = client.get('/add-book')

    assert response.status_code == 200
    assert b"Add Book" in response.data

def test_edit_book_page():
    client = app.test_client()

    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}/edit')

    assert response.status_code == 200
    assert book.Cim.encode() in response.data

def test_delete_book_reuires_post():
    client = app.test_client()

    with app.app_context():
        book = Book.query.first()

    response = client.get(f'/books/{book.ID}/delete')

    assert response.status_code == 405

