class A():
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside A's constructor"
        self.classvar1 = "I am an instance variable inside class A"
        self.special = "SPECIAL"


class B(A):
    classvar1 = "im a class method in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside B's constructor"
        self.classvar1 = "Instance var in class B"
        print(self.special, self.classvar1, self.var1 )
        super().__init__()
        print(self.special, self.classvar1, self.var1 )
        print("This is a special call " , super().classvar1)





a = A()
b = B()

#the class accesses instance elements before looking at class elemtents
print(b.classvar1)

#first, it will look for instance variables, then it will go to other classes it inherits from to find instance variables,
#then it goes to its class to find class variables, then other classes to find class variables. THIS IS THE ORDER