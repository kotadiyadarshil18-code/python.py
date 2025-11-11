#Q6
sum = 0
a = 1
while a <= 10:
    sum += a
    a += 1
print("sum of num from 1 to 10:", sum)

# answer 55
#Q7
sum = 0
a = 1

while a <= 10:
    if a % 2 == 0:  
        sum += a
    a += 1 

print("sum of even num from 1 to 10 :", sum)

#Q8
sum = 0
a = 1
while a <= 10:
    if a % 2 != 0:
        sum += a
    a += 1
print("sum of odd num from 1 to 10 :", sum)

#Q9
print("Table of 5")

for i in range(1, 11):
    result = 5 * i
    print("5 x", i, "=", result)

#Q10

num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: ", count)

#Q11

n=23546
lastdigit = n%10

print("last digit :",lastdigit)

while(n>=10):
    n = n/10
n=int(n)
print("first digit :",n)

#Q12

n = 2345

last = n % 10

first = n
while first >= 10:
    first //= 10  

digit = first

result = digit + last  
print(result)