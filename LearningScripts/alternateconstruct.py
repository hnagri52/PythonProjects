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

#this is used mainly when reading from a text file, and u dont want to keep writing the .split function.. just use this
    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1],params[2])
        # or one line: return cls(*string.split("-")



hussein = Employee("Hussein", 123, "Dev")
sabi = Employee("SABI", 22, "nurse")

jy = Employee.from_str("JY-480-Asstprof")

print(jy.printDetails())
