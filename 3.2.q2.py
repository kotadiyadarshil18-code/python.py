# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Using nested if
if a <= b:
    if a <= c:
        print("Minimum  number is:", a)
    else:
        print("Minimum  number is:", c)
else:
    if b <= c:
        print("Minimum  number is:", b)
    else:
        print("Minimum  number is:", c)
