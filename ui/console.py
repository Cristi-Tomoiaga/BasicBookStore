from domain.exceptions import RepositoryException, ServiceException


class Console:
    """
    Command based user interface
    """

    def __init__(self, srv_book):
        """
        Constructor for console
        :param srv_book: BookService instance
        """
        self.__srv_book = srv_book

    def __get_command(self):
        """
        Prints the menu and reads a command
        :return: the command - string
        """

        menu = "\nMeniu:\n1 - Adauga carte\n2 - Sterge carti\n3 - Setare filtru\n4 - Undo\nq - Quit"

        print(menu)

        cmd = input(">>> ").strip()
        return cmd

    def __ui_add_book(self):
        """
        Adds a book in the application
        """
        try:
            id = int(input("id: ").strip())
            title = input("titlu: ").strip()
            author = input("autor: ").strip()
            year = int(input("an aparitie: ").strip())

            try:
                self.__srv_book.add(id, title, author, year)
                print("Carte adaugata!")
            except RepositoryException as re:
                print(re)
        except ValueError:
            print("Valoare intreaga invalida pentru id sau an!")

    def __ui_delete_books(self):
        """
        Delete books that match the given condition
        """
        try:
            digit = int(input("cifra: ").strip())
            if 0 <= digit <= 9:
                self.__srv_book.delete_by_digit(digit)
                print("Cartile selectate au fost sterse!")
            else:
                print("Cifra invalida!")
        except ValueError:
            print("Cifra invalida!")

    def __ui_set_filter(self):
        """
        Sets a new filter given by the user
        """
        try:
            text = input("text: ").strip()
            number = int(input("nr: ").strip())

            self.__srv_book.set_filter(text, number)
        except ValueError:
            print("Valoare intreaga invalida pentru numar!")

    def __ui_print_books(self, books):
        """
        Prints the list of Book objects
        :param books: a list of Book objects
        """
        if len(books) == 0:
            print("Lista vida!")
            return

        for book in books:
            print(f"{book.get_id()}, {book.get_title()}, {book.get_author()}, {book.get_year()}")

    def __ui_print_filter(self):
        """
        Prints the current filter and the filtered list
        """
        filter = self.__srv_book.get_filter()
        print(f"Filtru curent: '{filter[0]}' | {filter[1]}")

        print(f"Lista filtrata:")
        filtered_books = self.__srv_book.apply_filter()
        self.__ui_print_books(filtered_books)
        print("")

    def __ui_undo(self):
        """
        Undo the last deletion
        """
        try:
            self.__srv_book.undo()
        except ServiceException as se:
            print(se)
        except RepositoryException as re:
            print(re)

    def run(self):
        """
        Starts the application
        """
        while True:
            self.__ui_print_filter()
            cmd = self.__get_command()

            if cmd == "1":
                self.__ui_print_filter()
                self.__ui_add_book()
            elif cmd == "2":
                self.__ui_print_filter()
                self.__ui_delete_books()
            elif cmd == "3":
                self.__ui_print_filter()
                self.__ui_set_filter()
            elif cmd == "4":
                self.__ui_print_filter()
                self.__ui_undo()
            elif cmd == "q":
                exit()
            else:
                print("Comanda invalida!")
