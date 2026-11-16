class Book:
    def __init__(self,title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError("не могут быть отрицательными")
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._pages = pages
        self._is_available = True
        self._last_read_pages = 0


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книги нет")
        self._is_available = False

    def give_back(self, pages_read):
        if self._is_available:
            raise ValueError("Книга на полке")
        if not 0 <= pages_read <= self._pages:
            raise ValueError("прочитанные страницы должны быть от 0 до количества страниц")
        self._is_available = True
        self._last_read_pages = pages_read

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._isbn == other._isbn

    def __lt__(self,other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._year < other._year

    def __repr__(self):
        return (f"Book({self._title!r}, {self._author!r}, {self._isbn!r}, {self._year}, {self._pages})")

class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0

    def __repr__(self):
        return f"Reader({self.name!r})"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Только Класс Книга")
        if any(b is book for b in self._books):
            raise ValueError("Уже есть")
        self._books.append(book)

    def find_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
            return None

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def lend(self, isbn, reader):
        copies = [b for b in self._books if b.isbn == isbn]
        if not copies:
            raise KeyError(isbn)
        book = next((b for b in copies if b.is_available), None)
        if book is None:
            raise ValueError("Выдана")
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        book = next((b for b in reader.books if b.isbn == isbn), None)
        if book is None or not any(b is book for b in self._books):
            raise ValueError("нету у него такой книги")
        book.give_back(pages_read)
        reader.books[:] = [b for b in reader.books if b is not book]
        reader.pages_read += pages_read

    def available(self):
        return [book for book in self._books if book.is_available]

    def unfinished(self):
        return [book for book in self._books if 0 < book.last_read_pages < book.pages]

    def __len__(self):
        return len(self._books)