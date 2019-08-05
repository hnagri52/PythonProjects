class Employee:
    no_of_people = 9


    def __init__(self, aname="", asal=0, arole=""):
        self.__name = aname
        self.__role = arole
        self.__salary = asal

    def printDetails(self):
        return f"the name is {self.__name}, the role is {self.__role}, and the salary is {self.__salary}\n"
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
"""
This type of method takes neither a self nor a cls parameter.
Therefore a static method can neither modify object state nor class state.
Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
"""

hussein = Employee("Hussein", 123, "Dev")
sabi = Employee("SABI", 22, "nurse")
jy = Employee.from_str("JY-480-Asstprof")
hussein.print_string("hello world")
print(jy.printDetails())

#------------------------------------------------------------------------- static methods are regular functions that just belong to the class namespace
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area() )
print(p.circle_area(4) )
print(p)