from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    item_count = 0   # class/static counter

    def __init__(self, title, year):
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @abstractmethod
    def displayInfo(self):
        pass


# Subclass: Book
class Book(LibraryItem):
    def __init__(self, title, year, author="Unknown"):
        super().__init__(title, year)
        self.author = author   # default argument (constructor flexibility)

    def displayInfo(self):
        print(f"[Book] Title: {self.title}, Author: {self.author}, Year: {self.year}")


# Subclass: DVD
class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre="General"):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):
        print(f"[DVD] Title: {self.title}, Duration: {self.duration} mins, Genre: {self.genre}, Year: {self.year}")


# ---------------- TESTING ----------------

# Create objects
item1 = Book("Python Programming", 2022, "Guido van Rossum")
item2 = Book("Data Structures", 2021)   # using default author
item3 = DVD("Inception", 2010, 148, "Sci-Fi")
item4 = DVD("Interstellar", 2014, 169)  # using default genre

# Polymorphism (collection of base class type)
library = [item1, item2, item3, item4]

print("----- Library Items -----")
for item in library:
    item.displayInfo()   # polymorphic call

# Show total items using class counter
print("\nTotal Library Items:", LibraryItem.item_count)