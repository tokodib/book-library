# 📚 Book Library

A personal web-based book library application.

## About the project

I have some previous experience with **Delphi + MySQL**, and more recently I created a small book management application using **Lazarus + ZeosDB + MariaDB** to keep track of the books I have at home.

The original application was created primarily for personal use and currently uses a single MariaDB table to store the book collection.

The goal of this project is to **port the existing application to the web** and gradually turn it into a web-based application that I can host on my own server. This will allow me to store and manage my book collection centrally and access it from anywhere and from any device.

## Why this project?

This project is also a practical learning opportunity.

While developing it, I want to improve and connect my existing knowledge with new technologies and concepts, including:

- Python
- Flask
- MariaDB and database management
- Linux server administration
- Git and GitHub
- Docker
- CI/CD
- Kubernetes
- deployment and troubleshooting

The project will gradually evolve from a simple Flask application into a containerized application with automated build and deployment processes.

## Learning approach

I am using ChatGPT as a learning assistant during development, but **not as a copy-paste code generator**.

The project is being built step by step. Each component and technology is introduced gradually, with an emphasis on understanding:

- what the code does,
- why a particular solution is used,
- how the different components communicate,
- how to troubleshoot problems,
- and how the individual technologies fit together into a complete system.

The goal is not only to get a working application, but to **understand the technologies and the connections between them**.

## Original application

The original application was developed with:

- Lazarus
- ZeosDB
- MariaDB

The existing database contains my current book collection and serves as the starting point for the new web application.

## Planned technologies

The project is planned to include:

- [x] Python
- [x] Flask
- [x] MariaDB
- [x] SQLAlchemy
- [x] Git / GitHub
- [ ] Docker
- [ ] Docker Compose
- [ ] Docker Swarm
- [ ] CI/CD
- [ ] GitHub Actions
- [ ] Kubernetes / k3s
- [x] Linux
- [ ] Deployment and troubleshooting

## Project status

🚧 **Work in progress**

The project is being developed incrementally, starting with a basic Flask application and gradually adding database integration, containerization, CI/CD and orchestration.

### August 31, 2026 - Initial project setup
- Created `.gitignore`
- Created the Python virtual environment: `python3 -m venv .venv` 
- Activated the virtual environment: `source .venv/bin/activate`
- Installed Flask: `pip install Flask`
- saved the installed dependecies: `pip freeze > requirements.txt`
- Created: `app.py`
- Started the Flask development server with: `python app.py`
- Verified that the application was accessible at: `http://127.0.0.1:5000` 
**"Book Library is running!"**
- 
**VS Code → Python → Flask → Browser → Book Library is running!**

### August 31, 2026 - Flask, SQLAlchemy and PyMySQL
- Installed Flask-SQLAlchemy and PyMySQL: `pip install Flask-SQLAlchemy PyMySQL` -
- Installed python-dotenv for environment variable management: `pip install python-dotenv`
- Updated `requirements.txt`
- Created the `.env` file for database configuration and secrets

### September 02, 2026 - Connect Flask to MariaDB
- Connected the Flask application to the existing MariaDB database
- Created `Book` SQLAlchemy model for the existing `konyvek` table
- Created the `/test-db` route to test the database connection
- Verified the database connection: **Database connection OK: 248**
- Created `templates/books.html`
- Displayed the complete book collection in the web browser
- Created `templates/book_detail.html`
- Added links to individual book details
- Added a search box and search functionality
- Added a **"No books found"** message when the search returns no results

### September 03, 2026 - Create and edit books
- Created the `/add-book` route
- Created `templates/add_book.html`
- Added the ability to create new books
- Created the `/books/<id>/edit` route
- Created `templates/edit_book.html`
- Added the ability to edit existing books
- Added navigation links for:
  - Add Book
  - Edit Book
  - Cancel
  - Back to Book List

### September 04, 2026 - Delete books and code cleanup
- Created the `/books/<id>/delete` route
- Added a confirmation dialog before deleting book
- Tested the delete functionality
- Cleaned up the HTML templates
- Removed development-only debug `print()` statements
- Verified thet the application still works after the clean up

### September 05, 2026 - Testing the application
- Activated virtual environment: `source .venv/bin/activate`
- Installed pytest pip module: `pip install pytest`
- Created new folder and files: `mkdir tests` and `touch tests/test_app.py`, `__init__.py`
- Executed the test: `pytest`