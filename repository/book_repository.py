from domain.entities import Book
from domain.exceptions import RepositoryException


class BookRepository:
    """
    Implements a repository for Book entities
    """

    def __init__(self, filename):
        """
        Constructor for BookRepository
        :param filename: string
        """
        self.__filename = filename
        self.__books = []

    def __load_from_file(self):
        """
        Loads the books from the file
        """
        self.__books = []
        try:
            with open(self.__filename, "r") as fh:
                for line in fh:
                    attrs = line.strip().split(",")
                    id = int(attrs[0].strip())
                    title = attrs[1].strip()
                    author = attrs[2].strip()
                    year = int(attrs[3].strip())

                    book = Book(id, title, author, year)
                    self.__books.append(book)
        except IOError:
            return  # empty repository

    def __save_to_file(self):
        """
        Saves the books to the file
        """
        try:
            with open(self.__filename, "w") as fh:
                for book in self.__books:
                    str_book = f"{book.get_id()},{book.get_title()},{book.get_author()},{book.get_year()}\n"
                    fh.write(str_book)
        except IOError:
            return  # invalid file

    def size(self):
        """
        Returns the size of the repository
        :return: integer
        """
        self.__load_from_file()
        return len(self.__books)

    def get_all(self):
        """
        Returns all the books in the repository
        :return: list of Book objects
        """
        self.__load_from_file()
        return self.__books

    def add(self, book):
        """
        Adds a Book object to the repository
        :param book: Book object
        :raises RepositoryException: if the id of book is already used in the repository
        """
        self.__load_from_file()

        if book in self.__books:
            raise RepositoryException("Id existent!")

        self.__books.append(book)

        self.__save_to_file()

    def find(self, id):
        """
        Searches for the book with the given id
        :param id: integer
        :return: the found Book instance or None otherwise
        """
        self.__load_from_file()
        for book in self.__books:
            if book.get_id() == id:
                return book

        return None  # no book found

    def delete(self, id):
        """
        Deletes the book with the given id
        :param id: integer
        :raises RepositoryException: if the book with the given id doesn't exist
        """
        self.__load_from_file()
        book = self.find(id)
        if book is None:
            raise RepositoryException("Id inexistent!")

        self.__books.remove(book)
        self.__save_to_file()
