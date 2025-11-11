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