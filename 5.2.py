#Q1
my_list=['Apple','banana','orange','grape','pineapple']
print(my_list)
my_list.append('Mango')
print(my_list)
my_list.pop(1)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

print()
#Q2

number=(1,2,3,4,5)
print(number)

print("Tuple is a list which can be not change after create")

print()

#Q3

my_list1=[1,2,3]
my_tuple=(1,2,3)

print(my_list1)
print(my_tuple)

my_list1.append(4)
print(my_list1)

print("Tuple is a list which can be not change after create")

print()

#Q4

squares=[x**2 for x in range (1,11)]
print(squares)

even_number=[x for x in range (1,21) if x % 2 == 0]
print(even_number)

list=["hello","WORLD","PyThOn"]
print(list)
lowercase=[list.lower() for list in list]

print(lowercase)
