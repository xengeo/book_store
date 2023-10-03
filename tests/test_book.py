from lib.book import Book

"""
Book constructs with an id, title and author_name
"""

def test_book_constructs():
    book = Book(1, "Test Book", "Test Author")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test Author"


"""
We can format books to strings nicely
"""

def test_books_format_nicely():
    book = Book(1, "Test Book", "Test Author")
    assert str(book) == "1 - Test Book - Test Author"


"""
We can compare two identical books
And have them be equal
"""

def test_books_are_equal():
    book_1 = Book(1, "Test Book", "Test Author")
    book_2 = Book(1, "Test Book", "Test Author")
    assert book_1 == book_2
    
# def test_artists_are_equal():
#     artist1 = Artist(1, "Test Artist", "Test Genre")
#     artist2 = Artist(1, "Test Artist", "Test Genre")
#     assert artist1 == artist2
#     # Try commenting out the `__eq__` method in lib/artist.py
#     # And see what happens when you run this test again.
