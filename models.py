# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')
    
    def add_book(self, title, genre):
        new_book = Book(title=title, genre=genre, author=self)
        session.add(new_book)
        session.commit()
        print(f"Book '{title}' added to author '{self.name}'.")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    
    @classmethod
    def save(cls, book):
        session.add(book)
        session.commit()
    
    @classmethod
    def get_books_by_author(cls, author_id):
        return session.query(cls).filter_by(author_id=author_id).all()

# Create the tables
Base.metadata.create_all(engine)
