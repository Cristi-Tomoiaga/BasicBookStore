from repository.book_repository import BookRepository
from services.book_service import BookService
from ui.console import Console

repo = BookRepository("books.txt")
srv = BookService(repo)
console = Console(srv)
console.run()
