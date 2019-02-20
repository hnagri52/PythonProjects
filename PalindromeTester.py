def isPalindrome():
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
isPalindrome()


