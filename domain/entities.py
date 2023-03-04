class Book:
    """
    Abstract data type for a Book Entity
    Domain:
        id - integer
        title - string
        author - string
        year - integer
    """

    def __init__(self, id, title, author, year):
        """
        Constructor for Book
        :param id: integer
        :param title: string
        :param author: string
        :param year: integer
        """
        self.__id = id
        self.__title = title
        self.__author = author
        self.__year = year

    def get_id(self):
        """
        Getter for id
        :return: id - integer
        """
        return self.__id

    def get_title(self):
        """
        Getter for title
        :return: title - string
        """
        return self.__title

    def get_author(self):
        """
        Getter for author
        :return: author - string
        """
        return self.__author

    def get_year(self):
        """
        Getter for year
        :return: year - integer
        """
        return self.__year

    def __eq__(self, other):
        """
        Verifies if two book entities are the equal (have the same id)
        :param other: Book instance
        :return: True if equal, False otherwise
        """
        return self.get_id() == other.get_id()
