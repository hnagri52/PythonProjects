from HighSchool import Goldbach_Conjecture

#Repeatedly get numbers and test each one to see
#if Goldbach's Conjecture is correct for that value.
#The value zero causes the program to stop

value= Goldbach_Conjecture.nextNumber()
while value!=0:
    Goldbach_Conjecture.testGoldbach(value)
    value= Goldbach_Conjecture.nextNumber()
