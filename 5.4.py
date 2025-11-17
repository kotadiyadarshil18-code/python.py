students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

# Q1 
for s in students:
    print(s["name"])

# Q2 
count = 0
for _ in students:
    count += 1

avg_score = sum(s["score"] for s in students) / count
print("Average =", avg_score)

# Q3
students.append({"id": 104, "name": "David", "score": 88})

# Q4
for s in students:
    if s["id"] == 102:
        s["score"] = 88

# Q5 - 
students = [s for s in students if s["id"] != 103]

print(students)

# Q6 
for s in students:
    if s["score"] > 80:
        print(s["name"])

# Q7
def get_score(student):
    return student["score"]

sorted_students = sorted(students, key=get_score, reverse=True)

for s in sorted_students:
    print(s["name"], s["score"])

# Q8 
top_student = sorted_students[0]
print("Top student:", top_student)

# Q9 
score = top_student["score"]

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
