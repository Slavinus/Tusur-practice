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