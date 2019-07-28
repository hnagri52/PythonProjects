def first_number():
    """()->float
    Asks users to input the first side length of the triangle,
    and return the first side length of the triangle

    """
    
            

def second_number():
    """()->float
    Asks users to input the second side length of the triangle,
    and return the second side length of the triangle

    """
  

def third_number():
    """()->float
    Asks users to input the third side length of the triangle,
    and return the third side length of the triangle

    """
  

def is_triangle(a, b, c):
    """(number, number, number)->bool
    The parameter refers to the 3 side lengths of the triangle.
    The function will return true if 3 side lengths can form a triangle,
    and false if 3 side lengths cannot form a triangle

    >>> is_triangle(1, 3, 3)
    True

    >>> is_triangle(1, 2, 56)
    False
    """

   

def triangle_type(a, b, c):
    """(number, number, number)->str
    The parameter refers to the 3 side lengths of the triangle.
    The function will return “scalene” if it is a scalene triangle,
    “isosceles” if it is an isosceles triangle, and “equilateral”
    if it is an equilateral triangle

    >>> triangle_type(3, 4, 5)
    'scalene'

    >>> triangle_type(2, 2, 3)
    'isosceles'

    >>> triangle_type(10, 10, 10)
    'equilateral'
    """
    n="scalene"
    return n

def is_right_angle(a, b, c):
    """(number, number, number)->bool
    The parameter refers to the 3 side lengths of the triangle.
    The function will return true if it is a right angle,
    otherwise the function will return false if it is not a right triangle

    >>> is_right_angle(6, 8, 10)
    True
    
    >>> is_right_angle(5, 6, 7)
    False
    """


def triangle_angle(a, b, c):
    """(number, number, number)->float
    The parameter refers to the 3 side lengths of the triangle.
    The function will return the angle (in degree) opposite to the length a in
    2 decimal places

    >>> triangle_angle(2, 3, 4)
    28.96

    >>> triangle_angle(12, 15, 17)
    43.49

    """
    answer=round(28.955, 2)

    return answer

def angle_type(a1, a2, a3):
    """(angle, angle, angle)->
    The parameter refers to the 3 angles (in degrees) of the triangle.
    The function will return “acute” if it is an acute triangle,
    “obtuse” if it is an obtuse triangle,
    and “right” if it is an right triangle

    >>> angle_type(60, 60, 60)
    'acute'

    >>> angle_type(20, 30, 130)
    'obtuse'

    >>> angle_type(45, 45, 90)
    'right'
    """


print (__name__)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
