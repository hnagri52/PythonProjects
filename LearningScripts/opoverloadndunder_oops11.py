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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f"Employee: ('{self.name}', {self.salary}, '{self.role}')"
    def __str__(self):
        return f"the name is {self.name}, the role is {self.role}, and the salary is {self.salary}\n"

#refer mapping operators to functions

Huss = Employee("Hussein", 354, "dev")
Sab = Employee("Sabi", 6, "Nurse")

print(Huss+ Sab)
print(Huss)
print(repr(Huss))