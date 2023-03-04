import unittest

from domain.entities import Book
from domain.exceptions import RepositoryException, ServiceException
from repository.book_repository import BookRepository
from services.book_service import BookService


class BookServiceTestCase(unittest.TestCase):
    def setUp(self):
        # saves the original content of the files
        with open("test_file.txt", "r") as fh:
            self.__copy_file = fh.read()

        self.__repo = BookRepository("test_file.txt")
        self.__srv = BookService(self.__repo)

    def tearDown(self):
        # restores the original content of the files
        with open("test_file.txt", "w") as fh:
            fh.write(self.__copy_file)

    def test_add(self):
        book1 = Book(10, "Carte10", "Anonim", 1780)

        self.assertEqual(self.__repo.size(), 4)
        book_r = self.__srv.add(10, "Carte10", "Anonim", 1780)
        self.assertEqual(self.__repo.size(), 5)
        self.assertEqual(book1, book_r)

        with self.assertRaises(RepositoryException) as cm:
            self.__srv.add(1, "Carte10", "Anonim", 1780)
        self.assertEqual(str(cm.exception), "Id existent!")

    def test_delete_by_digit(self):
        self.assertEqual(self.__repo.size(), 4)
        self.__srv.delete_by_digit(3)
        self.assertEqual(self.__repo.size(), 4)

        self.assertEqual(self.__repo.size(), 4)
        self.__srv.delete_by_digit(9)
        self.assertEqual(self.__repo.size(), 2)

    def test_filter_getter_setter(self):
        self.assertEqual(self.__srv.get_filter(), ["", -1])
        self.__srv.set_filter("ala", 2)
        self.assertEqual(self.__srv.get_filter(), ["ala", 2])

    def test_apply_filter(self):
        book1 = Book(1, "Carte1", "Ion Popescu", 2002)
        book2 = Book(2, "Carte2", "Mihai Eugen", 1990)
        book3 = Book(3, "Carte3", "Ion Popescu", 2010)
        book4 = Book(4, "Carte4", "Ion Ionescu", 1999)

        books = self.__srv.apply_filter()
        self.assertEqual(books, [book1, book2, book3, book4])

        self.__srv.set_filter("arte", 2000)
        books = self.__srv.apply_filter()
        self.assertEqual(books, [book2, book4])

        self.__srv.set_filter("1", 2011)
        books = self.__srv.apply_filter()
        self.assertEqual(books, [book1])

        self.__srv.set_filter("abc", 2000)
        books = self.__srv.apply_filter()
        self.assertEqual(books, [])

    def test_undo(self):
        self.assertEqual(self.__repo.size(), 4)
        self.__srv.delete_by_digit(3)
        self.assertEqual(self.__repo.size(), 4)
        with self.assertRaises(ServiceException) as cm:
            self.__srv.undo()
        self.assertEqual(str(cm.exception), "Nu exista operatii pt undo!")

        self.assertEqual(self.__repo.size(), 4)
        self.__srv.delete_by_digit(9)
        self.assertEqual(self.__repo.size(), 2)
        self.__srv.undo()
        self.assertEqual(self.__repo.size(), 4)

        self.assertEqual(self.__repo.size(), 4)
        self.__srv.delete_by_digit(9)
        self.__srv.delete_by_digit(0)
        self.assertEqual(self.__repo.size(), 0)
        self.__srv.undo()
        self.assertEqual(self.__repo.size(), 2)
        self.__srv.undo()
        self.assertEqual(self.__repo.size(), 4)


if __name__ == '__main__':
    unittest.main()
