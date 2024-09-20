# Library Management System

A simple command-line interface (CLI) application for managing a library's authors and books. This project allows users to add authors, add books associated with those authors, and list authors and their books.

## Features

- Add new authors
- Add books to existing authors
- List all books by a specific author
- List all authors in the library

## Technologies Used

- Python
- SQLAlchemy (for ORM)
- argparse (for command-line interface)

## Getting Started

### Prerequisites

- Python 3.x
- SQLAlchemy
- A configured database (e.g., SQLite, PostgreSQL)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/franklinstyles/python-project
   ```

2. Navigate to the folder
    ```bash
    cd python-project
    ```
3. Open it in your vs code
   ```bash
   code .
   ```

### How it works

1. You can add authors by opening the terminal in vs code and typing "python cli.py --add-author 'author name' "
2. You check the list of authors by typing in terminal, "python cli.py --list-authors"
3. You can still add books by typing in terminal, "python cli.py --add-book 1 'book name' 'category' "
4. You can check the list of books by typing in terminal, "python cli.py --list-books 1"

### Author 
 franklin ndegwa 

### date
sept 20,2024 

       