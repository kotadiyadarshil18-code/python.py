a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Maximum number is:", a)
    else:
        print("Maximum number is:", c)
else:
    if b >= c:
        print("Maximum number is:", b)
    else:
        print("Maximum number is:", c)

#Q2
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
#Q3


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b:
    if a >= c:
        if a >= d:
            print("Maximum number is:", a)
        else:
            print("Maximum number is:", d)
    else:
        if c >= d:
            print("Maximum number is:", c)
        else:
            print("Maximum number is:", d)
else:
    if b >= c:
        if b >= d:
            print("Maximum number is:", b)
        else:
            print("Maximum number is:", d)
    else:
        if c >= d:
            print("Maximum number is:", c)
        else:
            print("Maximum number is:", d)

#Q4

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = None
match operator:
        case '+':
            result = num1 + num2
            print("answer is",result)
        case '-':
            result = num1 - num2
            print("answer is",result)
        case '*':
            result = num1 * num2
            print("answer is",result)
        case '/':
            result = num1 / num2
            print("answer =",result)

#Q5
print("press 1 to order sandwhich")
print("press 2 to order Pizza")
print("press 3 to order Burger")
print("press 4 to order Thin crust pizza")
print("press 5 to order Cheese Burst pizza")
print("press 6 to order Fresh Dough pizza")

num=int(input("Enter a number to orader fast food:"))


match num:
    case 1:
        print("sandwhich")
    case 2:
        print("pizza")
    case 3:
        print("burger")

    case 4:
        print("Thin crust pizza")
    case 5:
        print(" Cheese Burst pizza")
    case 6:
        print("Fresh Dough pizza")

#Q6

print("press 1 to telecone calling into English")
print("press 2 to telecone calling into Hindi")
print("press 3 to telecone calling into Gujarati")


lang = int(input("Enter your choice (1-3): "))

match lang:
    case 1:
        print("English")
    case 2:
        print("Hindi")
    case 3:
        print("Gujarati")
