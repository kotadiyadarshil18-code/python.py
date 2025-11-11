# Q1
for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)
print()  


# Q2
num = 1  
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1
print()


# Q3
text = "PYTHON"
for ch in text:
    if ch in "AEIOU":  
        continue
    print(ch)
print()


# Q4
n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() 
print()


# Q5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

print()


# Q6
for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()
print()


# Q7
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    print()
