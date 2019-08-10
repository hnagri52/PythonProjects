class Employee:
    no_of_people = 9 #public
    _protect = 923 #protected --> can print and access, but cant change i think, sub classes do inherit
    __private = 4  #private --> cannot access outside of the class, other classes dont inherit


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




hussein = Employee("Hussein", 123, "Dev")
#to call a private, do the following
print(hussein._Employee__private)


#/////////////////////////////polymorphism

print(5+6)
print("5" + "6")
#polymorphism is basically when u override functional commands to act in other ways