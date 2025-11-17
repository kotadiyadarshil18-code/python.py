#Q1

number=int(input("Enter a number:"))

if (number % 2 ==0):
    print("Number is Even")

else:
    print("Number is Odd")

#Q2

age=int(input("Enter your Age:"))

if (age >= 12):
    print("You are child")
elif (age >= 19):
    print("You are Teenger")
elif (age >= 59):
    print("You are Adult")
else:
    print("You are senior")

#Q3

num1=int(input("Enter your first integers:"))
num2=int(input("Enter your secound in tntegers:"))
num3=int(input("Enter your third integers:"))

if (num1 > num2):
    print(num1,"is greater")
elif(num2 > num3):
    print(num2,"is greater")
elif(num3 > num1):
    print(num3,"is greater")
elif(num1==num2):
    print(num1 and num2,"both are equal")
elif(num2==num3):
    print(num2 and num3,"both are equal")

else:
    print(num1 and num2,"both are equal")

    #Q4

number1=int(input("Enter a number:"))

if(number1==0):
    print("Number is neturel")
elif(number1 > 0 ):
    print("Number is positive ")
else:
    print("Number is negative ")
    

