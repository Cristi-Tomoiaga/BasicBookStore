import unittest

from domain.entities import Book
from domain.exceptions import RepositoryException
from repository.book_repository import BookRepository


class BookRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        # saves the original content of the files
        with open("test_one_entity.txt", "r") as fh:
            self.__copy_file1 = fh.read()
        with open("test_file.txt", "r") as fh:
            self.__copy_file2 = fh.read()

        self.__repo1 = BookRepository("test_one_entity.txt")
        self.__repo2 = BookRepository("test_file.txt")
        self.__repo3 = BookRepository("empty")

    def tearDown(self):
        # restores the original content of the files
        with open("test_one_entity.txt", "w") as fh:
            fh.write(self.__copy_file1)
        with open("test_file.txt", "w") as fh:
            fh.write(self.__copy_file2)

    def test_add(self):
        book1 = Book(10, "Carte10", "Anonim", 1780)
        book2 = Book(1, "Carte10", "Anonim", 1780)

        self.assertEqual(self.__repo3.size(), 0)

        self.assertEqual(self.__repo1.size(), 1)
        self.__repo1.add(book1)
        self.assertEqual(self.__repo1.size(), 2)
        books = self.__repo1.get_all()
        self.assertEqual(books[-1], book1)

        self.assertEqual(self.__repo2.size(), 4)
        self.__repo2.add(book1)
        self.assertEqual(self.__repo2.size(), 5)
        books = self.__repo2.get_all()
        self.assertEqual(books[-1], book1)

        with self.assertRaises(RepositoryException) as cm:
            self.__repo2.add(book2)
        self.assertEqual(str(cm.exception), "Id existent!")

    def test_find(self):
        exp_book = Book(1, "Carte1", "Ion Popescu", 2002)
        ret_book = self.__repo2.find(1)
        self.assertEqual(exp_book, ret_book)

        self.assertIsNone(self.__repo2.find(10))

    def test_get_all(self):
        book = Book(1, "Carte1", "Ion Popescu", 2002)
        self.assertEqual(self.__repo1.get_all(), [book])

    def test_delete(self):
        self.assertEqual(self.__repo2.size(), 4)
        self.__repo2.delete(4)
        self.assertEqual(self.__repo2.size(), 3)

        with self.assertRaises(RepositoryException) as cm:
            self.__repo2.delete(20)
        self.assertEqual(str(cm.exception), "Id inexistent!")


if __name__ == '__main__':
    unittest.main()
