class BookAppException(Exception):
    """
    Base class for all exceptions in the application
    """
    pass


class RepositoryException(BookAppException):
    """
    Exception class for repository
    """
    pass


class ServiceException(BookAppException):
    """
    Exception class for service
    """
    pass
