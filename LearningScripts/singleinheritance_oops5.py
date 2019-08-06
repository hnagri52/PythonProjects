"""
There is a differnece between:
name --> can be called from outside the class (print(hussein.name))
_name --> semi private variable
__name --> cannot access outside of class

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

class Developer(Employee):
    no_of_langs = 0
    def __init__(self, aname="", asal=0, arole="", languages=""):
        #should use super keyword to override
        self.name = aname
        self.role = arole
        self.salary = asal
        self.languages = languages

    def printprog(self):
        return f"The programmer's name is: {self.name}. The role is: {self.role}, pay is: {self.salary}. They know: {self.languages} "


hussein = Employee("Hussein", 123, "Dev")
sabi = Employee("SABI", 22, "nurse")

jy = Developer("JY", 234, "full stack", ["python"])
ahmed = Developer("Ahmed", 34234, "QA", ["java"])
print(jy.printprog() )