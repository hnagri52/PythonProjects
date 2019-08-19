

user = int(input("Enter your age, and I will tell you how old you will be in 100 years!"))
isAge = False
isYear = True

if len(user) == 4:
    isYear = True
else:
    isAge = True


if isAge:
    print(f"The age youll be in 100 years is: {user + 100}")
else:
    print(f"")