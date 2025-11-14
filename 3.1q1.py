number=int(input("Enter a number to cheak even and odd" ))

if(number %2 ==0):
    print("Number is even")
else:
    print("Number is odd")

#Q2
age=int(input("Enter your age:"))

if(age < 12):
    print("child")
elif(age < 19):
    print("Teenager")
elif(age < 49):
    print("Adult")
else:
    print("Senior")

#Q3

a=int(input("Enter your first number"))
b=int(input("Enter your secound number"))
c=int(input("Enter your third number"))

if(a > b):
    print(a,"is greater")
elif(b > c):
    print(b,"is greater")
elif(c > a):
    print(c,"is greater")
else:
    print("All are equal")


#Q4

number=int(input("Enter a number:"))

if(number > 0):
    print("Number is positive")
elif(number < 0 ):
    print("Number is negative")
else:
    print("Number is neutral ")