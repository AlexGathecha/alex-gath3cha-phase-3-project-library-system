import click
import sys
import os
import datetime

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.book import Book
from models.author import Author
from models.category import Category
from models.base import session

@click.group()
def cli():
    pass

# Book Commands

@cli.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--year', prompt='Publication year', help='The publication year of the book.', type=int)
@click.option('--author_id', prompt='Author ID', help='The ID of the author.', type=int)
@click.option('--isbn', prompt='ISBN', help='The ISBN of the book.')
def create_book(title, year, author_id, isbn):
    """Create a new book."""
    book = Book(title=title, publication_year=year, author_id=author_id, isbn=isbn)
    session.add(book)
    session.commit()
    click.echo(f'Book "{title}" created successfully!')

@cli.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book to delete.', type=int)
def delete_book(book_id):
    """Delete a book by ID."""
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        click.echo(f'Book with ID {book_id} deleted successfully!')
    else:
        click.echo(f'Book with ID {book_id} not found.')

@cli.command()
def display_books():
    """Display all books."""
    books = session.query(Book).all()
    for book in books:
        click.echo(f'{book.id}: {book.title} by Author ID {book.author_id}, Published in {book.publication_year}, ISBN: {book.isbn}')

@cli.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book to find.', type=int)
def find_book(book_id):
    """Find a book by ID."""
    book = session.get(Book, book_id)
    if book:
        click.echo(f'{book.id}: {book.title} by Author ID {book.author_id}, Published in {book.publication_year}, ISBN: {book.isbn}')
    else:
        click.echo(f'Book with ID {book_id} not found.')


# Author Commands

@cli.command()
@click.option('--name', prompt='Author name', help='The name of the author.')
@click.option('--bio', prompt='Author bio', help='A short biography of the author.')
@click.option('--birth_date', prompt='Author birth date (YYYY-MM-DD)', help='The birth date of the author.')
@click.option('--nationality', prompt='Author nationality', help='The nationality of the author.')
def create_author(name, bio, birth_date, nationality):
    """Create a new author."""
    try:
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
    except ValueError:
        click.echo('Invalid date format. Please provide the birth date in YYYY-MM-DD format.')
        return

    author = Author(name=name, bio=bio, birth_date=birth_date, nationality=nationality)
    session.add(author)
    session.commit()
    click.echo(f'Author "{name}" created successfully!')

@cli.command()
@click.option('--author_id', prompt='Author ID', help='The ID of the author to delete.', type=int)
def delete_author(author_id):
    """Delete an author by ID."""
    author = session.query(Author).get(author_id)
    if author:
        session.delete(author)
        session.commit()
        click.echo(f'Author with ID {author_id} deleted successfully!')
    else:
        click.echo(f'Author with ID {author_id} not found.')

@cli.command()
def display_authors():
    """Display all authors."""
    authors = session.query(Author).all()
    for author in authors:
        click.echo(f'{author.id}: {author.name}, Bio: {author.bio}, Birth Date: {author.birth_date}, Nationality: {author.nationality}')

@cli.command()
@click.option('--author_id', prompt='Author ID', help='The ID of the author to find.', type=int)
def find_author(author_id):
    """Find an author by ID."""
    author = session.get(Author, author_id)
    if author:
        click.echo(f'{author.id}: {author.name}, Bio: {author.bio}, Birth Date: {author.birth_date}, Nationality: {author.nationality}')
        click.echo("Books:")
        for book in author.books:
            click.echo(f'  {book.id}: {book.title}, Published in {book.publication_year}')
    else:
        click.echo(f'Author with ID {author_id} not found.')

# Category Commands

@cli.command()
@click.option('--name', prompt='Category name', help='The name of the category.')
@click.option('--description', prompt='Category description', help='The description of the category.')
def create_category(name, description):
    """Create a new category."""
    category = Category(name=name, description=description)
    session.add(category)
    session.commit()
    click.echo(f'Category "{name}" created successfully!')

@cli.command()
@click.option('--category_id', prompt='Category ID', help='The ID of the category to delete.', type=int)
def delete_category(category_id):
    """Delete a category by ID."""
    category = session.query(Category).get(category_id)
    if category:
        session.delete(category)
        session.commit()
        click.echo(f'Category with ID {category_id} deleted successfully!')
    else:
        click.echo(f'Category with ID {category_id} not found.')

@cli.command()
def display_categories():
    """Display all categories."""
    categories = session.query(Category).all()
    for category in categories:
        click.echo(f'{category.id}: {category.name}, Description: {category.description}')

@cli.command()
@click.option('--category_id', prompt='Category ID', help='The ID of the category to find.', type=int)
def find_category(category_id):
    """Find a category by ID."""
    category = session.get(Category, category_id)
    if category:
        click.echo(f'{category.id}: {category.name}, Description: {category.description}')
        click.echo("Books:")
        for book in category.books:
            click.echo(f'  {book.id}: {book.title}, Published in {book.publication_year}')
    else:
        click.echo(f'Category with ID {category_id} not found.')

# Menu Command

@cli.command()
def menu():
    """Display the menu and handle user input."""
    while True:
        click.echo("\nLibrary Management System Menu:")
        click.echo("1. Create Book")
        click.echo("2. Delete Book")
        click.echo("3. Display Books")
        click.echo("4. Find Book")
        click.echo("5. Create Author")
        click.echo("6. Delete Author")
        click.echo("7. Display Authors")
        click.echo("8. Find Author")
        click.echo("9. Create Category")
        click.echo("10. Delete Category")
        click.echo("11. Display Categories")
        click.echo("12. Find Category")
        click.echo("13. Exit")

        choice = click.prompt('Please choose an option', type=int)

        if choice == 1:
            title = click.prompt('Book title')
            year = click.prompt('Publication year', type=int)
            author_id = click.prompt('Author ID', type=int)
            isbn = click.prompt('ISBN')
            create_book.callback(title, year, author_id, isbn)
        elif choice == 2:
            book_id = click.prompt('Book ID', type=int)
            delete_book.callback(book_id)
        elif choice == 3:
            display_books.callback()
        elif choice == 4:
            book_id = click.prompt('Book ID', type=int)
            find_book.callback(book_id)
        elif choice == 5:
            name = click.prompt('Author name')
            bio = click.prompt('Author bio')
            birth_date = click.prompt('Author birth date (YYYY-MM-DD)')
            nationality = click.prompt('Author nationality')
            create_author.callback(name, bio, birth_date, nationality)
        elif choice == 6:
            author_id = click.prompt('Author ID', type=int)
            delete_author.callback(author_id)
        elif choice == 7:
            display_authors.callback()
        elif choice == 8:
            author_id = click.prompt('Author ID', type=int)
            find_author.callback(author_id)
        elif choice == 9:
            name = click.prompt('Category name')
            description = click.prompt('Category description')
            create_category.callback(name, description)
        elif choice == 10:
            category_id = click.prompt('Category ID', type=int)
            delete_category.callback(category_id)
        elif choice == 11:
            display_categories.callback()
        elif choice == 12:
            category_id = click.prompt('Category ID', type=int)
            find_category.callback(category_id)
        elif choice == 13:
            click.echo('Exiting...')
            break
        else:
            click.echo('Invalid choice. Please try again.')

if __name__ == '__main__':
    cli()
