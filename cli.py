import argparse
from models import Author, Book, session

def add_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Author '{name}' added.")

def add_book(author_id, title, genre):
    author = session.query(Author).get(author_id)
    if author:
        author.add_book(title, genre)
    else:
        print(f"No author found with ID {author_id}.")

def list_books(author_id):
    books = Book.get_books_by_author(author_id)
    if books:
        print(f"Books by Author ID {author_id}:")
        for book in books:
            print(f"- {book.title} ({book.genre})")
    else:
        print(f"No books found for Author ID {author_id}.")

def list_authors():
    authors = session.query(Author).all()
    if authors:
        print("Authors in the library:")
        for author in authors:
            print(f"- ID: {author.id}, Name: {author.name}")
    else:
        print("No authors found.")

def main():
    parser = argparse.ArgumentParser(description='Library Management System')
    parser.add_argument('--add-author', help='Add a new author')
    parser.add_argument('--add-book', nargs=3, metavar=('AUTHOR_ID', 'TITLE', 'GENRE'),
                        help='Add a new book to an author (AUTHOR_ID TITLE GENRE)')
    parser.add_argument('--list-books', type=int, help='List all books by author ID')
    parser.add_argument('--list-authors', action='store_true', help='List all authors')

    args = parser.parse_args()
    
    if args.add_author:
        add_author(args.add_author)
    
    if args.add_book:
        add_book(int(args.add_book[0]), args.add_book[1], args.add_book[2])
    
    if args.list_books is not None:
        list_books(args.list_books)
    
    if args.list_authors:
        list_authors()

if __name__ == '__main__':
    main()
