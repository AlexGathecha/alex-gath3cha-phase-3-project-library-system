from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

class BookCategories(Base):
    __tablename__ = 'book_categories'

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)
