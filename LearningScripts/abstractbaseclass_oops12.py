#abstract method basically tells all of the inheriting classes that they need a certain method defined

from abc import abstractmethod, ABCMeta, ABC

class Shape(metaclass=ABCMeta):
#class Shape (ABC):  ---> this will do the exact same
    @abstractmethod
    def printArea(self):
        return 0


class Rectangle(Shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.width = 4

    #def printArea(self):
    #if you dont have it, it will throw error

#the reason we do this is to have our inheriting class to include certain things and we dont forget
#we cannot create objects of the abstract base class FYI

rect1 = Rectangle()



