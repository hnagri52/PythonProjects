def func1():
    print("This is hussein")
func2 = func1
del func1
func2()


def funret(num):
    if num == 0:
        return print
    elif num == 1:
        return sum

a = funret(1)
print(a)


def funcInFunc(somefun):
    somefun("This is a try")

funcInFunc(print)


#//////////////////////////DECORATOR functions://///////////////////////////////////////////////

def dec1(func):
    def nowexec():
        print("Executing now!!!")
        func()
        print("Now it has been executed")
    return nowexec

@dec1
def hussein():
    print("Hussein is a SYDE man")

#hussein = dec1(hussein)

hussein()

#the use of a dectorator is that if u have multiple functions that essentially do the same thing, u can use a decorator to not repeat code