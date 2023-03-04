from domain.entities import Book
from domain.exceptions import ServiceException


class BookService:
    """
    Use case GRASP Controller(Service) for books
    """

    def __init__(self, repo):
        """
        Constructor for BookService
        :param repo: BookRepository object
        """
        self.__repo = repo
        self.__filter = ["", -1]
        self.__undo_list = []

    def add(self, id, title, author, year):
        """
        Adds a book to the repository
        :param id: integer
        :param title: string
        :param author: string
        :param year: integer
        :return: Book object
        :raises RepositoryException: if the id of book is already used in the repository
        """
        book = Book(id, title, author, year)
        self.__repo.add(book)

        return book

    def delete_by_digit(self, digit):
        """
        Deletes all books that contain the given digit in the year
        :param digit: integer
        """
        books = self.__repo.get_all()
        deleted_books = []

        for book in books:
            if str(digit) in str(book.get_year()):
                deleted_books.append(book)
                self.__repo.delete(book.get_id())
        if deleted_books:
            self.__undo_list.append(deleted_books)

    def set_filter(self, text, number):
        """
        Setter for filter
        :param text: string
        :param number: integer
        """
        self.__filter = [text, number]

    def get_filter(self):
        """
        Getter for filter
        :return: the filter - a list
        """
        return self.__filter

    def apply_filter(self):
        """
        Applies the current filter and returns the filtered list
        :return: a list of Books
        """
        filtered_books = []
        books = self.__repo.get_all()

        for book in books:
            if (self.__filter[0] == "" or self.__filter[0] in book.get_title()) and (self.__filter[1] == -1 or book.get_year() < self.__filter[1]):
                filtered_books.append(book)

        return filtered_books

    def undo(self):
        """
        Undoes the last deletion
        :raises ServiceException: if there is nothing to undo
        :raises RepositoryException: if the undo operation collides with existing data
        """
        if len(self.__undo_list) == 0:
            raise ServiceException("Nu exista operatii pt undo!")

        last_deleted_books = self.__undo_list.pop()

        for book in last_deleted_books:
            self.__repo.add(book)
