class Book:
    def __init__(self, name, author, release_date, page_number):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.page_number = page_number

    def book_info(self):
        return f"Name: {self.name}, Author: {self.author}, Release date: {self.release_date}, Page number: {self.page_number}"

    def check_book_is_new(self):
        return self.release_date >= 2020
