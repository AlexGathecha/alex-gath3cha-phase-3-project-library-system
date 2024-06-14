# Library Management System

## Description

This web application enables users to manage a library's collection of books and authors. Users can add, delete, and view books and authors within the system. The application maintains a one-to-many relationship between authors and their books, ensuring each author can be associated with multiple books. The system also allows users to search for books by title or author and view detailed information about each entry. A user-friendly interface ensures that library management tasks are straightforward and efficient, streamlining the process of maintaining an organized library database.

## Features

- Add new books and authors.
- Delete existing books and authors.
- View a list of all books and authors.
- Search for books by title or author.
- View detailed information about books and authors.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pipenv install`.
4. Set up the database by running `pipenv run python database/setup.py`.
5. Run the CLI with `python3 cli.py`.

## Usage

- Use the CLI commands to manage books, authors, and categories.
- For a list of available commands, run `pipenv run python cli.py --help`.

## Technologies Used

- Python
- SQLAlchemy (ORM)
- SQLite (Database)
- Click (CLI)

## Project Structure

