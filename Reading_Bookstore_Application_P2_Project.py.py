import random
from abc import ABC, abstractmethod

# Abstract Book Class
class Book(ABC):
    def __init__(self, title, author, isbn, price, genre, imdb_rating):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.genre = genre
        self.imdb_rating = imdb_rating
    
    def display_book_info(self):
        print(f"Name: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: {self.price}")
        print(f"Genre: {self.genre}")
        print(f"IMDB Rating: {self.imdb_rating}")

# Concrete Book Class
class RegularBook(Book):
    pass

# Concrete Upcoming Books Class
class UpcomingBooks(Book):
    def __init__(self, title, author, isbn, price, genre, imdb_rating): 
        super().__init__(title, author, isbn, price, genre, imdb_rating)
        self.user_request_book_list = []
        self.coming_book_list = ["The Familiar", "You Are Here", "Funny Story", "A Little Life",
                                 "House of Flame and Shadows", "House Maid is Watching", "Fate Inked in Blood"]
    
    def display_upcoming_books(self):
        print("Upcoming Books: ")
        for book in self.coming_book_list:
            print(book)
    
    def request_book(self):
        print("You can request a book to be added.")
        request_input = input("Enter the name of the book which you want to see in the bookstore: ")
        self.user_request_book_list.append(request_input)
        print("The book has been added and will arrive soon")

# Book Factory Classes
class BookFactory(ABC):
    @abstractmethod
    def create_book(self, title, author, price, genre, imdb_rating):
        pass

class RegularBookFactory(BookFactory):
    def create_book(self, title, author, price, genre, imdb_rating):
        isbn = random.randint(1000, 2500)
        return RegularBook(title, author, isbn, price, genre, imdb_rating)

class UpcomingBookFactory(BookFactory):
    def create_book(self, title, author, price, genre, imdb_rating):
        isbn = random.randint(1000, 2500)
        return UpcomingBooks(title, author, isbn, price, genre, imdb_rating)

# Payment Strategies
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}... Payment successful!")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}... Payment successful!")

# User Class
class User:
    def __init__(self):
        self.cart = []
        self.payment_strategy = None
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def add_to_cart(self, book):
        self.cart.append(book)
        print(f"Book: *{book.title}* added to cart.")
    
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Books in your cart are: ")
        for book in self.cart:
            book.display_book_info()
    
    def make_payment(self):
        if not self.cart:
            print("Your cart is empty. Please add books before making payment.")
            return
        total_amount = sum(book.price for book in self.cart)
        print(f"Total Amount: * ${total_amount} *")
        if self.payment_strategy:
            self.payment_strategy.pay(total_amount)
            self.cart.clear()
        else:
            print("Payment strategy not set.")

# Admin Class
class Admin:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book: *{book.title}* added successfully!")
    
    def view_books(self):
        if not self.books:
            print("No Books Available")
            return
        for book in self.books:
            book.display_book_info()

    def update_book(self, isbn, title=None, author=None, price=None, genre=None, imdb_rating=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if price:
                    book.price = price
                if genre:
                    book.genre = genre
                if imdb_rating:
                    book.imdb_rating = imdb_rating
                print(f"Book with ISBN '{isbn}' updated successfully!")
                return
        print(f"Book with ISBN '{isbn}' not found.")
    
    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN '{isbn}' deleted successfully!")
                return
        print(f"Book with ISBN '{isbn}' not found.")

def main():
    admin = Admin()
    user = User()
    
    while True:
        print("Welcome to Readings Bookstore!")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nAdmin Menu:")
                print("1. Add Books")
                print("2. View Books")
                print("3. Update Books")
                print("4. Delete Books")
                print("5. Log out")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    book_type = input("Enter book type (regular/upcoming): ").lower()
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    price = float(input("Enter book price: "))
                    genre = input("Enter book genre: ")
                    imdb_rating = float(input("Enter book IMDB rating: "))
                    
                    if book_type == 'regular':
                        book_factory = RegularBookFactory()
                    elif book_type == 'upcoming':
                        book_factory = UpcomingBookFactory()
                    else:
                        print("Invalid book type.")
                        continue
                    
                    new_book = book_factory.create_book(title, author, price, genre, imdb_rating)
                    admin.add_book(new_book)

                elif admin_choice == '2':
                    admin.view_books()

                elif admin_choice == '3':
                    isbn = int(input("Enter book ISBN to update: "))
                    title = input("Enter new title (leave blank to keep unchanged): ")
                    author = input("Enter new author (leave blank to keep unchanged): ")
                    price = input("Enter new price (leave blank to keep unchanged): ")
                    genre = input("Enter new genre (leave blank to keep unchanged): ")
                    imdb_rating = input("Enter new IMDB rating (leave blank to keep unchanged): ")
                    price = float(price) if price else None
                    imdb_rating = float(imdb_rating) if imdb_rating else None
                    admin.update_book(isbn, title, author, price, genre, imdb_rating)

                elif admin_choice == '4':
                    isbn = int(input("Enter book ISBN to delete: "))
                    admin.delete_book(isbn)

                elif admin_choice == '5':
                    print("Logging out of admin.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                print("\nUser Menu:")
                print("1. View Books")
                print("2. Add Book to Cart")
                print("3. View Cart")
                print("4. Make Payment")
                print("5. Logout")
                
                user_choice = input("Enter your choice: ")
                
                if user_choice == '1':
                    admin.view_books()
                
                elif user_choice == '2':
                    isbn = int(input("Enter book ISBN to add to cart: "))
                    for book in admin.books:
                        if book.isbn == isbn:
                            user.add_to_cart(book)
                            break
                    else:
                        print(f"Book with ISBN '{isbn}' not found.")
                
                elif user_choice == '3':
                    user.view_cart()
                
                elif user_choice == '4':
                    print("Choose payment method:")
                    print("1. Credit Card")
                    print("2. PayPal")
                    payment_choice = input("Enter your choice: ")
                    if payment_choice == '1':
                        user.set_payment_strategy(CreditCardPayment())
                    elif payment_choice == '2':
                        user.set_payment_strategy(PayPalPayment())
                    else:
                        print("Invalid choice. Defaulting to Credit Card.")
                        user.set_payment_strategy(CreditCardPayment())
                    user.make_payment()
                
                elif user_choice == '5':
                    print("Logging out of user.")
                    break
                
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Thank you for using the Bookstore application!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
