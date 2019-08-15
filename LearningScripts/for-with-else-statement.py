
food = ["Burger", "Pizza", "roti"]
for item in food:
    if item == "rotiroll":
        break
else:
    print("Your item was not found")

#the else works only if the for loop did not have a break statement executed
#if we did break from the loop, it would skip over the else statement

