# Library Management System

## Description

This web application enables users to manage a library's collection of books, authors, and categories. Users can add, delete, and view books, authors, and categories within the system. The application maintains a one-to-many relationship between authors and their books, ensuring each author can be associated with multiple books. The system also allows users to search for books by title or author and view detailed information about each entry. A user-friendly interface ensures that library management tasks are straightforward and efficient, streamlining the process of maintaining an organized library database.

## Features

- Add new books, authors, and categories.
- Delete existing books, authors, and categories.
- View a list of all books, authors, and categories.
- Search for books by title or author.
- View detailed information about books and authors.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pipenv install`.
4. Set up the database by running `pipenv run python database/setup.py`.
5. Run the CLI with `pipenv run python cli.py menu`.

## Usage

- Use the CLI commands to manage books, authors, and categories.
- For a list of available commands, run `pipenv run python cli.py --help`.

## Technologies Used

- Python
- SQLAlchemy (ORM)
- SQLite (Database)
- Click (CLI)


## CLI Commands

### Book Commands

- **Create Book**
    ```
    pipenv run python cli.py create-book --title "Book Title" --year 2023 --author_id 1 --isbn "1234567890123"
    ```

- **Delete Book**
    ```
    pipenv run python cli.py delete-book --book_id 1
    ```

- **Display Books**
    ```
    pipenv run python cli.py display-books
    ```

- **Find Book**
    ```
    pipenv run python cli.py find-book --book_id 1
    ```

### Author Commands

- **Create Author**
    ```
    pipenv run python cli.py create-author --name "Author Name" --bio "Short bio" --birth_date "1970-01-01" --nationality "Nationality"
    ```

- **Delete Author**
    ```
    pipenv run python cli.py delete-author --author_id 1
    ```

- **Display Authors**
    ```
    pipenv run python cli.py display-authors
    ```

- **Find Author**
    ```
    pipenv run python cli.py find-author --author_id 1
    ```

### Category Commands

- **Create Category**
    ```
    pipenv run python cli.py create-category --name "Category Name" --description "Category Description"
    ```

- **Delete Category**
    ```
    pipenv run python cli.py delete-category --category_id 1
    ```

- **Display Categories**
    ```
    pipenv run python cli.py display-categories
    ```

- **Find Category**
    ```
    pipenv run python cli.py find-category --category_id 1
    ```

## Functions

### Book Management Functions

- **create_book(title, year, author_id, isbn)**
    - Prompts the user for the book's title, publication year, author ID, and ISBN, then creates and adds a new book to the database.

- **delete_book(book_id)**
    - Prompts the user for the book ID and deletes the corresponding book from the database.

- **display_books()**
    - Displays a list of all books in the database, showing each book's ID, title, author ID, publication year, and ISBN.

- **find_book(book_id)**
    - Prompts the user for the book ID and displays detailed information about the corresponding book if found.

### Author Management Functions

- **create_author(name, bio, birth_date, nationality)**
    - Prompts the user for the author's name, bio, birth date, and nationality, then creates and adds a new author to the database.

- **delete_author(author_id)**
    - Prompts the user for the author ID and deletes the corresponding author from the database.

- **display_authors()**
    - Displays a list of all authors in the database, showing each author's ID, name, bio, birth date, and nationality.

- **find_author(author_id)**
    - Prompts the user for the author ID and displays detailed information about the corresponding author if found, including a list of books written by the author.

### Category Management Functions

- **create_category(name, description)**
    - Prompts the user for the category's name and description, then creates and adds a new category to the database.

- **delete_category(category_id)**
    - Prompts the user for the category ID and deletes the corresponding category from the database.

- **display_categories()**
    - Displays a list of all categories in the database, showing each category's ID, name, and description.

- **find_category(category_id)**
    - Prompts the user for the category ID and displays detailed information about the corresponding category if found.

