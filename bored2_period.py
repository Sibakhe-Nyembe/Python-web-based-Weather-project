from bored_period import Library
from bored_period import Library, Lender

book_1= Library("author George Bush", 47776, "Red Roses")
book_return= Lender(f"February 2025", "January 2025", 'RED ROSES', 47776)
book_2 = Library("author James Brown", 15566, "Grow as an adult")
book_return_2 = Lender(f"March 2025","February 2025", "GROW AS AN ADULT", 15566)
book_3 = Library("author Makarov", 12345, "BECOME RESILIENT")
book_return_3 = Lender(f"January 2025", "December 2024", "BECOME RESILIENT", 12345)

book_1.books_available()
book_1.title()
book_return.deadline_day()
book_2.books_available()
book_2.title()
book_return_2.deadline_day()
book_3.books_available()
book_3.title()
book_return_3.deadline_day()

books = book_return.RETURN(), book_return.RETURN2(), book_return.RETURN3()
books()





