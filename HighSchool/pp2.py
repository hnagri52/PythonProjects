
number = int(input("Enter the number you want to check"))
lower = int(input("ENter the lower rangge"))
higher = int(input("Enter the higher range"))


for num in range(lower,higher+1):
    if num % number == 0:
        print(f"the number {number} is divisible by {num}")
    else:
        print(f"the number {number} is not divisible by {num}")


