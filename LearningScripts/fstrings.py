# F strings
# Inneficient String Formating

name = "Hussein"
print("My name is %s"%name)

import math

number = 5

ans = f"This is the fast way of string formatting: {name} {number} {math.cos(math.pi)}"
ans2 = "this is so {1} ".format("cool", 57)

print(ans)
print(ans2)

