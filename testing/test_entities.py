import unittest

from domain.entities import Book


class BookTestCase(unittest.TestCase):
    def test_constructor_getters(self):
        book = Book(1, "Carte1", "Ion Popescu", 2002)
        self.assertEqual(book.get_id(), 1)
        self.assertEqual(book.get_title(), "Carte1")
        self.assertEqual(book.get_author(), "Ion Popescu")
        self.assertEqual(book.get_year(), 2002)

    def test_equality(self):
        book1 = Book(1, "Carte1", "Ion Popescu", 2002)
        book2 = Book(1, "Carte1", "Ion Popescu", 2003)
        book3 = Book(2, "Carte2", "Ion Popescu", 2002)

        self.assertEqual(book1, book2)
        self.assertEqual(book1, book1)
        self.assertNotEqual(book2, book3)


if __name__ == '__main__':
    unittest.main()
