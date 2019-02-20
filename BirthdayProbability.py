def BirthdayProbs():
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

BirthdayProbs()

