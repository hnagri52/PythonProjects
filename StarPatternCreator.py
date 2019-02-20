def option1():
	st1=int(input("Enter a width "))
	for i in range(1,st1+1):
		print ("*"*i)
	for i in range(st1-1, -1, -1):
		print ("*"*i)

def option2():
    character=input("Enter a word:")
    length=len(character)
    for i in range(0, length):
        for j in range (0, i+1):
            print (character[j], end="")
        print ()
    for k in range(length,0,-1):
        for l in range (k-2, -1,-1):
            print (character[l], end="")
        print ()


print("Would you like to print half a diamond of stars (1), or would you like")
val = int(input("to print half a diamond with a letter incremementing each time? (2) \n") )

if val == 1:
        option1()
else:
        option2()

