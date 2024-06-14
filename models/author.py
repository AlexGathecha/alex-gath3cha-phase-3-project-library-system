from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(String)
    birth_date = Column(Date)
    nationality = Column(String)

    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f'<Author(id={self.id}, name="{self.name}")>'
