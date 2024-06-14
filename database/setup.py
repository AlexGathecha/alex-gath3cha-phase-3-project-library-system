import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base import Base, engine
from models.author import Author
from models.book import Book
from models.category import Category
from models.book_categories import BookCategories

def setup_database():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    setup_database()
