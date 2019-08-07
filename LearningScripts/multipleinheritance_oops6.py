"""
multiple inheritance will take the constructor of the class it is inheriting from first
Multiple inheritance always looks at the variable, methods provided first.
This means if both employee and player have a printdetails function, it will use the one it finds first
so basically, when looking to see what to call, it will go in order of whats provided
"""

class Employee:
    no_of_people = 9
    __name = ""
    __salary = 0
    __role = ""

    def __init__(self, aname="", asal=0, arole=""):
        self.name = aname
        self.role = arole
        self.salary = asal

    def printDetails(self):
        return f"the name is {self.name}, the role is {self.role}, and the salary is {self.salary}\n"

    @classmethod
    def change_peep(cls, peeple):
        cls.no_of_people = peeple

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1],params[2])
        # or one line: return cls(*string.split("-")

    @staticmethod
    def print_string(string):
        print(f"This is a random string: {string}")

class Player:
    no_of_games = 4

    def __init__(self, aname, aage):
        self.name = aname
        self.age = aage

    def printDetails(self):
        return f"the name is {self.name}, the age is {self.age}\n"

class Developer(Employee, Player):
    """The will take Employee classe's constructor. """
    language = "c++"
    def printLanguage(self):
        return f"the language is {self.language}"

hussein = Employee("Hussein", 123, "Dev")
sabi = Employee("SABI", 22, "nurse")

jy = Developer("JY", 234, "full stack")

print(jy.printDetails())
jy.print_string("HEY")
print(jy.printLanguage())

