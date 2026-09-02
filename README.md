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

The existing database contains the current book collection and serves as the starting point for the new web application.

## Planned technologies

The project is planned to include:

- Python
- Flask
- MariaDB
- SQLAlchemy
- Git / GitHub
- Docker
- Docker Compose
- Docker Swarm
- CI/CD
- GitHub Actions
- Kubernetes / k3s
- Linux

## Project status

🚧 **Work in progress**

The project is being developed incrementally, starting with a basic Flask application and gradually adding database integration, containerization, CI/CD and orchestration.

### Aug 31, 2026 - Initial project setup
- Create: .gitignore
- `python3 -m venv .venv` - Create virtual environment
- `source .venv/bin/activate` - Activating VE
- `pip install Flask`
- `pip freeze > requirements.txt` - save independecies
- create **app.py** and run with `python app.py` command in terminal.
- I can see result in internet browser on address `http://127.0.0.1:5000` ("Book Library is running!")
- 
**VS code->Python->Flask->http://127.0.0.1:5000->Book Library is running!**

### Aug 31, 2026 - Flask - SQLAlchemy PyMySQL
- `pip install Flask-SQLAlchemy PyMySQL` -> for communicating with MariaDB
- `pip install python-dotenv` -> for handling .env files
- `pip freeze > requirements.txt`
- creating .env secret file

### Sep 02, 2026 - Connect Flask to MariaDB
- I can read result on site: `http://127.0.0.1:5000/test-db` "Database connection OK: 248"