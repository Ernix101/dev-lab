scores = [85, 67, 45, 90, 72, 55, 38]
names = ["Alice","Brian","Cynthia","David","Eva","Frank","Grace"]

# for score in scores:
#     if score >= 50:
#         print("Pass")
#     else:
#         print("Fail")
# for score in scores:
#     if score >= 80:
#         print("A")
#     elif score >= 70:
#         print("B")
#     elif score >= 60:
#         print("C")
#     else:
#         print("D")

# count = 0

# for score in scores:
#     if score <= 50:
#         count += 1
# print(f"The number of students below 50 are {count}")

# number = 0

# while number < 10:
#     if not number == 7:
#         number += 1
#         print(f"number is {number}")
#     else:
#         break

failed_students = []

# for i in range(len(scores)):
#     if scores[i] < 50:
#         failed_students.append(names[i])

# print(failed_students)

# for name, score in zip(names, scores):
#     if score < 50:
#         failed_students.append(name)

# print(failed_students)

students = [
    {"name": "Alice", "score": 85,"region": "Nairobi"},
    {"name": "Brian", "score": 67, "region": "Kisumu"},
    {"name": "Cynthia", "score": 45, "region": "Nairobi"}  
]



# print(student)

# for student in students:
#     for key, value in student.items():
#         print(key, "-->" ,value)

# for student in students:
#     if student["score"] >= 50:
#         print(student["name"])
# print()

# for student in students:
#     if student["score"] <= 50:
#         print(student["name"])
# print()


for student in students:
    student["Grade"] = ""
    if student["score"] >= 80:
        student["Grade"] = "A"
    elif student["score"] >= 70:
        student["Grade"] = "B"
    elif student["score"] >= 60:
        student["Grade"] = "C"
    else:
        student["Grade"] = "D"
        
for student in students:  
    print(student["name"], "-->", student["Grade"])


    