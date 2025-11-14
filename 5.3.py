my_set={1,2,3,4,5}
print(my_set)
my_set.add(6)
my_set.remove(3)
print(2 in my_set)
print(my_set)

print()
#Q2

set_a={1,2,3,4}
set_b={3,4,5,6}

result=set_a.union(set_b)
print(result)

result1=set_a.intersection(set_b)
print(result1)

result2=set_a.difference(set_b)
print(result2)

#Q3

student={"name":"Darshil","Age":20,"grade":"A"}
print(student.keys())
print(student.values())

student1={"city":"Delhi"}

student.update(student1)


student["Age"]=26

del student["grade"]

print(student)

#Q4

keys=['id','name','email']
value=[101,'Bob','bob@example.com']
dict_name=(keys,value)
print(dict_name)

#Q5

num =int('123')
print(num)

tuple_valu=tuple([1,2,3])
print(tuple_valu)
list_val=list((1,2,3))
print(list_val)
dict_val=dict([(1,'A'),(2,'B')])
print(dict_val)

#Q6

numbers = [10, 20, 30, 40, 50]

del numbers[2]

print(numbers)