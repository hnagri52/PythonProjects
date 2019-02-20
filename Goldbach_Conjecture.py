def nextNumber():
    #ask users for input
    name=int(input("Please enter an even positive number: "))
    #while the number is less than or equalled to 2, re-enter an even positive integer
    while name<=2:
        print("We need an even integer bigger than 2")
        name=int(input("Please enter an even positive number: "))
    #while the number divide by 2 has 1 remainder, print it's an odd number and re-enter an even positive integer
    while name%2==1:
        print ("It is an odd number.")
        name=int(input("Please enter an even positive number: "))
    #return the number(name)
    return name
def isPrime(n):
    #checks if the number is 2, if it is, return True(it is a prime number)
    if n==2:
        return True
    #otherwise if the number isn't 2
    else:
        #check for the divisibility from 2 to n(the number)
        for i in range (2, n):
            #if it is divisible by a number(without remainder being present), then return false
            if n%i==0:
                return False
    #if it is not divisble by any number, then return true        
    return True

n=nextNumber()
answer=isPrime(n)
print (answer)

def primeAfter(n):
    #this checks for the prime number for each number that is greater than n
    while(True):
        #This will increment n to make n's value increase by 1 until the condition becomes true
        n = n + 1
        #checks if the number is prime by using my isPrime function already created
        if(isPrime(n)):
            #this will break the loop if the number is a prime number
            break
    #return the new value of n
    return n

def testGoldbach(n):
    #checks if a is a prime number or not
    for a in range(2,n):
        if isPrime(a):
            #if a is a prime number, check if b is a prime number
            for b in range(2,n):
                #if b is a primer number, then...
                if isPrime(b):
                    #if the value of n is equal to value a, and value b combined/added
                    if (n == a+b):
                        #print those two values
                        print (a,b)
                        #return true 
                        return True
    #otherwise, return false
    return False
