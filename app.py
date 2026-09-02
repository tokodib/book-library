import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

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

@app.route('/')
def index():
    return "Book Library is running!"

@app.route('/test-db')
def test_db():
    result = db.session.execute(text("SELECT COUNT(*) FROM konyvek"))
    count = result.scalar()

    return f"Database connection OK: {count}"


if __name__ == '__main__':
    app.run(debug=True)