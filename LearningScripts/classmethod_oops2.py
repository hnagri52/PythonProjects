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


hussein = Employee("Hussein", 123, "Dev")
sabi = Employee("SABI", 22, "nurse")


print(hussein.printDetails())
try:
    print(hussein.__name)
except Exception as e:
    print(e)


#classmethods are used to access class variables... they are like decorators in a way
#the cls refers to the class the object is an instance of, they are used as alternative constructors mainly

hussein.change_peep(76543)

print(hussein.no_of_people)