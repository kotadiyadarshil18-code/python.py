#Q1

while True:
    num=int(input("Enter 0 to stop:"))
    if num == 0:
        break

print()
#Q2

for i in range (1,11):
    print("square of " ,{i} ,{i ** 2})


print()
#Q3

for i in range (1,51):
    if i % 2 == 0:
        print(i)

print()
#Q4

for i in range (1,21):
    if i % 2 != 0:
        print(i)


print()
#Q5

for i in range (1,51,5):
    print(i)

print()

#Q6

for i in range(10,0,-1):
    print(i)

print()

#Q7

for i in range(1,51):
    if i % 2 == 0 and i % 3 == 0:
        print("Divisible by 2 and 3 both",{i})
    elif i % 2 == 0:
        print("Divisible by 2",{i})
    elif i % 3 == 0:
        print("Divisible by 3",{i})
    else:
        print(i)