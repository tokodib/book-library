from app import app


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