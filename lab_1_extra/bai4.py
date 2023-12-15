class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = math
        self.literature = literature
        self.english = english

    def average_score(self):
        return (self.math + self.literature + self.english) / 3

    def hoc_luc(self):
        if (self.average_score() >= 8):
            return "gioi"
        elif (self.average_score() < 8 and self.average_score() >= 6.5):
            return "kha"
        else:
            return "trung binh"
