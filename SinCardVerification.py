def SinCardVerify():
    #establish that the variable is true 
    sinrun=True
    #while the sinrun is true, do the following
    while sinrun is True:
        #asking user to input their sin numbers
        sin=list(input("Please enter your SIN number: "))
        #establishing that it continues to work until the sin given is 999999999
        if sin != list(str(999999999)):
            #defining a new function that multiplies the given index number by 2
            def numfind(sin,sindex):
                num=int(sin[sindex])*2
                #if the number after being multiplied is over 9, it adds the first and second digit of the product together
                if num > 9:
                    num = str(num)
                    num = int(num[0])+int(num[1])
                    return num
                #otherwise, if the number is under 9, then it returns the product (under 9)
                else:
                    return num
            #using the funtion on all of the needed index's
            num2=numfind(sin,1)
            num4=numfind(sin,3)
            num6=numfind(sin,5)
            num8=numfind(sin,7)
            #add all of the outcomes together
            addition=num2+num4+num6+num8
            #add the 1, 3, 5, 7 number in the SIN number together
            addition=addition+(int(sin[0])+int(sin[2])+int(sin[4])+int(sin[6]))
            #If the the addition's second number -10 is equalled to the laqst digit of the sin number, then the sin is valid, otherwise, it's not valid
            if 10-(addition%10) == int(sin[8]):
                print("This is a valid SIN!")
            else:
                print("This is an invalid SIN!")
            #stop the program
        else:
            sinrun=False

SinCardVerify()


