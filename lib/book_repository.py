from lib.book import Book

class BookRepository:

    # # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
        

    # # Retrieve all artists
    # No arguments
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')

        books = []
        for row in rows:
            item = Book(row['id'], row['title'], row['author_name'])
            books.append(str(item))
        return books
