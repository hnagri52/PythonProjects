def MidtermGradeCalc():
    def scale_midterm_grades(grades, multiplier, bonus):
        #loop through the length of grades
        for i in range(0,len(grades)):
            #update the grades by multiplying with the multiplier and adding the bonus
            grades[i]=grades[i]*multiplier+bonus
            #check if the grade is over 100, if it is, set it to 100
            if grades[i] > 100:
                    grades[i]=100
        #return the list of grades
        return grades
    #this is an example
    print("An example with multiplier of 2 and bonus of 3 with the list [1,3,6,10,3] is:")
    grades=[1,3,6,10,3]
    print(scale_midterm_grades(grades,2,3))
MidtermGradeCalc()

