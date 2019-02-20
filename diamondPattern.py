#Asks users to politely input a string
string=input("Please enter string: ")
#If the string is over 10 characters, this
#tells the program to use only the first 10 characters from the input
if len(string) > 10:
	string=string[0:10]
for i in range(0,len(string)):
#Adjusts the spaces to go in the top half of the diamond form
	print(" "*(len(string)-i-1), end="")
#prints the characters forward
	for j in range(0,i+1):
		print(string[j],end="")
#prints the characters backwards
	for k in range(i-1,-1,-1):
		print(string[k],end="")
#prints the line
	print()

for i in range(len(string)-1,0,-1):
#adjusts the spaces to go in the bottom half of the diamond form
	print(" "*(len(string)-i), end="")
#prints the characters forwards
	for j in range(0,i):
		print(string[j],end="")
#prints the characters backwards
	for k in range(i-2,-1,-1):
		print(string[k],end="")
#prints the line
	print()
