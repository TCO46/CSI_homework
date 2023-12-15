class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def info(self):
        return f"Name: {self.name}, Phone number: {self.phone_number}, Email: {self.email}"
