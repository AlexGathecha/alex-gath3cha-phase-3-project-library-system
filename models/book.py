from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .book_categories import BookCategories 

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    isbn = Column(String, unique=True)

    author = relationship('Author', back_populates='books')
    categories = relationship('Category', secondary='book_categories', back_populates='books')

    def __repr__(self):
        return f'<Book(id={self.id}, title="{self.title}")>'
