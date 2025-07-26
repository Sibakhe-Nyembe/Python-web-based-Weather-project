#Hey, i am bored so i thought i should do a mini library system
import sys
class Library:
    def __init__(self,author,book_number,book_name):
        self.author=author
        self.book_no=book_number
        self.bookname=book_name

    def books_available(self):
        print("Welcome to the Library. Readily available and free to read: ") 
        print(self.bookname)  

    def title(self):
         print("\nHello there. Here's more information on this book. ")
         print(f'This book: {self.bookname}\nWritten by author: {self.author}\nBook reference: {self.book_no}\n')

class Lender(Library):
    def __init__(self, deadline, start_date, book_no, book_name):
        super().__init__(self, book_name, book_no)
        self.deadline=deadline
        self.start=start_date

    def deadline_day(self):
        print(f"Book name, {self.bookname}, has the following: \nReference: {self.book_no}"
              f"\nBorrowed period: {self.start} \nReturn during this deadline period: {self.deadline}\n")

    def RETURN(self):
        book = input("Which book do you wish to return?\nEnter book name😃: ").upper()
        if book == "RED ROSES":
            print("Thanks for returning this book. I have been patiently waiting for its return. Wait a minute...")
        else:
            sys.exit("Something isn't right...")

        book_ref = int(input("Please enter reference for confirmation👍: "))
        reference = 47776
        if book_ref == reference:
            print("Book has been received😎. A step closer as your reward awaits...") 
        else:    
            sys.exit("AHA! I KNEW IT, something was wrong all along.")      

        deadline = input("Enter deadline period start(month,year): ").upper()
        month = f"FEBRUARY 2025"
        date = f'{month}'.upper()
        if deadline == date:
            print("Congratulations. You made it on time. Reward will be given to you😊")
        else:
            print("RETURN DURING DEADLINE PERIOD OF FEBRUARY 2025.")

    def RETURN2(self):
        book = input("Which book do you wish to return?\nEnter book name😃: ").upper()
        if book == "GROW AS AN ADULT":
            print("Thanks for returning this book. I have been patiently waiting for its return. Wait a minute...")
        else:
            sys.exit("Something isn't right...")

        book_ref = int(input("Please enter reference for confirmation👍: "))
        reference = 15566
        if book_ref == reference:
            print("Book has been received😎. A step closer as your reward awaits...") 
        else:    
            sys.exit("AHA! I KNEW IT, something was wrong all along.")      

        deadline = input("Enter set deadline day(day,month): ").upper()
        month = f"MARCH 2025"
        date = f'{month}'.upper()
        if deadline != date:
            print("Congratulations. You made it on time. Reward will be given to you😊")
        else:
            print("RETURN BOOK DURING DEADLINE PERIOD OF MARCH 2025.")  

    def RETURN3(self):
        book = input("Which book do you wish to return?\nEnter book name😃: ").upper()
        if book == "BECOME RESILIENT":
            print("Thanks for returning this book. I have been patiently waiting for its return. Wait a minute...")
        else:
            sys.exit("Something isn't right...")

        book_ref = int(input("Please enter reference for confirmation👍: "))
        reference = 12345
        if book_ref == reference:
            print("Book has been received😎. A step closer as your reward awaits...") 
        else:    
            sys.exit("AHA! I KNEW IT, something was wrong all along.")      

        deadline = input("Enter set deadline day(day,month): ").upper()
        month= f"JANUARY 2025"
        date = f'{month}'.upper()
        if deadline == date:
            print("Congratulations. You made it on time. Reward will be given to you😊")
        else:
            print("RETURN BOOK DURING DEADLINE PERIOD OF JANUARY 2025.")           







