# Anonymous or lambda  functions are shortcuts to functions

#two ways of writing the same thing
def addition(a,b):
    return a+b

add = lambda a,b:a+b


# commonly used in sorted functions -> so that u can pass in a key

a = [[1,2,3,4], [43534353,4,99], [4543,334]]

a = sorted(a, key=lambda x:x[1], reverse=True)

print(a)


