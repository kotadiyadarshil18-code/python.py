print("Welcome to the intrective personal data collecter!")
print()
name=str(input("Enter Your name:"))
age=int(input("Enter Your age:"))
height=float(input("enter your height:"))
number=int(input("enter your number:"))

print("Thank you! Here is the information we collected")


print("enter your age:",(age),type(age))
print("enter your height:",(height),type(height))

print("name:",(name),type(name),"memory adress:",id(name))
print("age:",(age),type(age),"memory adress:",id(age))
print("height",(height),type(height),"memory adress:",id(height))
print("number:",(number),type(number),"memory adress:",id(number))


current_your=2025
birth_your=(current_your-age)
print("birth_your",(birth_your))
