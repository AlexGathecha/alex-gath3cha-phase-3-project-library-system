from models.base import Base, engine
from models.author import Author
from models.book import Book
from models.category import Category
from models.book_categories import BookCategories

Base.metadata.create_all(engine)
