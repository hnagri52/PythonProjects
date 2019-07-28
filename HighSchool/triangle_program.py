from HighSchool import triangle_functions

s1= triangle_functions.first_number()
s2= triangle_functions.second_number()
s3= triangle_functions.third_number()

while (s1!=0 and s2!=0 and s3!=0):
    if (triangle_functions.is_triangle(s1, s2, s3)==False):
        print ("It is not a triangle! Please reenter 3 side again")
        s1= triangle_functions.first_number()
        s2= triangle_functions.second_number()
        s3= triangle_functions.third_number()
        continue
    else:
        print ("It is a triangle")
        if (triangle_functions.triangle_type(s1, s2, s3)== "scalene"):
            print ("It is a scalane triangle")
        elif (triangle_functions.triangle_type(s1, s2, s3) == "isosceles"):
            print ("It is an isosceles triangle")
        else: 
            print ("It is an equilateral triangle")

        if (triangle_functions.is_right_angle(s1, s2, s3)==True):
            print ("The triangle is a right angle")
        else:
            print ("The triangle is not a right angle")

        angle1= triangle_functions.triangle_angle(s1, s2, s3)
        angle2= triangle_functions.triangle_angle(s2, s1, s3)
        angle3= triangle_functions.triangle_angle(s3, s1, s2)

        print ("The 3 angles are ", angle1, "degrees, " ,angle2, "degrees, and "
               , angle3)

        

        if (triangle_functions.angle_type(angle1, angle2, angle3)== "acute"):
            print("It is an acute triangle")
        elif (triangle_functions.angle_type(angle1, angle2, angle3) == "obtuse"):
            print ("It is an obtuse triangle")

        print ("The analysis has been completed.")
        print ("Please enter the 3 sides of a triangle again")

    s1= triangle_functions.first_number()
    s2= triangle_functions.second_number()
    s3= triangle_functions.third_number()

        
