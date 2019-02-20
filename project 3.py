def question1():
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

question1()


def question2():
    #establishing values of variables
    n=1  #in this case, people
    temp=1
    #this will check if the condition is true and will continue to loop these lines until the condition becomes false, which is when the loop reaches 365
    while n!=366:
        #keeps looping(increasing by 1) until the condition becomes false, then it stops the for loop.
        for i in range (1, n+1):
            #calculates the probability in percentage of 2 people having the same birthday in a group
            temp*=(366-i)/(365)
            answer=(1-temp)*100
            #prints out the probability in percentage for 2 people having the same birthday in a specific group size (depending on the value of n).
        print ("for", n, "people", "the probability of at least two people having the same birthday is", answer, "%")
        #reestablishes the value of these variables.
        n=n+1
        temp=1

question2()


def question3():
    #answering the following examples
    """
    (list of number, int) -> list of number

    Return a new list consisting of those numbers in nums

    that are below threshold,

    in the same order as in nums.

    >>> collect_underperformers([1, 2, 3, 4], 3)

    [1, 2]

    >>> collect_underperformers([1, 2, 108, 3, 4], 50)

    [1, 2, 3, 4]

    """
    #defining the function
    def collect_underperformers(n,thres):
        #Initialize an empty list
        outlist = list()
        #loops the following code until it hits the length of n
        for i in range(0, len(n)):
            #checks whether the value is less than the threshold
            if n[i]<thres:
                #if the number is less than the value of thres, append it to "outlist")
                outlist.append(n[i])
        #after the loop is finish, print out the new list
        print (outlist)
        #example
    n=[5,6,7,8,9,1,3,4,5,2,5]
    thres=7
    print (collect_underperformers(n,thres))


question3()



def question4():
    #establishing that this variable is true
    palindromerun=True
    #while the variable is true, do the following
    while palindromerun==True:
        #ask users for input
        text=input("Please enter a palindrome ")
        #if the text is 999999999, the variable will become false and stop the program
        if text == "999999999":
            palindromerun=False
            #if this condition is not met, do the following
        else:
            #converting all letters to lowercase
            text=text.lower()
            #establishiing the value of i
            i = 0
            #loop throught the text
            while i < len(text):
                #checking to make sure that the element is a letter
                if text[i] !="a" and text[i] !="b" and text[i] !="c" and text[i] !="d" and text[i] !="e" and text[i] !="f" and text[i]!="g" and text[i] !="h" and text[i] !="i" and text[i] !="j" and text[i] !="k" and text[i] !="l" and text[i] !="m" and text[i] !="n" and text[i] !="o" and text[i] !="p" and text[i] !="q" and text[i]!="r" and text[i] !="s" and text[i] !="t" and text[i] !="u" and text[i] !="v" and text[i] !="w" and text[i] !="x" and text[i] !="y" and text[i] !="z":
                    text=text.replace(text[i],"")
                    #re-establishing i
                    i=i-1
                else:
                    #reverse the text
                    i=i+1
                    #establishing new variable
                    reverse=text[::-1]
            #this checks whether the reversed text and the input text matches. It states whether or not it is a palindrome accordingly
            if text == reverse:
                print("\nThis is a palindrome!\n")
            else:
                print("\nThis is not a palindrome!\n")
question4()

def question5():
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
question5()

