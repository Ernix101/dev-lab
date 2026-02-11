greeting = "Hello"
name = "ernest"
# print(greeting + " " + name)

students = [
{"id": 1, "name": "Alice", "score": 85, "region": "Nairobi"},
{"id": 2, "name": "Brian", "score": 67, "region": "Kisumu"},
{"id": 3, "name": "Cynthia", "score": 45, "region": "Nairobi"},
{"id": 4, "name": "David", "score": 90, "region": "Mombasa"},
{"id": 5, "name": "Eva", "score": 72, "region": "Kisumu"},
{"id": 6, "name": "Frank", "score": 55, "region": "Nairobi"},
{"id": 7, "name": "Grace", "score": 38, "region": "Eldoret"}
]

scores = [85, 67, 45, 90, 72, 55, 38]
names = ["Alice", "Brian", "Cynthia", "David", "Eva", "Frank", "Grace"]

studentsOne = []
for i in range(len(names)):
    studentsOne.append({
        "id": i + 1,
        "name": names[i],
        "score": scores[i]
    })
# print(studentsOne)
# print()


# subScores = scores[1:3]
# print(subScores)



def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D" 

# print(grade(85)) # "A"

# for number in [1, 2, 3, 4, 5]:
#     print("number is:", number)

# x = 1

# while x <= 5:
#     print("x is:", x)
#     x += 1

# for score in  scores:
#     if score >= 50:
#         print("PASS")
#     else:
#         print("FAIL")

student = {"id": 1, "name": "Alice", "score": 85, "region": "Nairobi"}
# print(student["name"]) # Alice
student["grade"] = "A" # add new key

# loop key / values
# for k, v in student.items():
#     print(k, v)

class Student:

    school_name = "Kenyatta University"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def displayDetails(self):
        return f"{self.name} has scored {self.grade}"

    def update_grade(self, new_grade):
        self.grade = new_grade
        return new_grade

    def is_pass(self):
        if self.grade >= 50:
            return "Pass"
        else:
            return "Fail"
        
    def add_ten(self):
        grade = (self.grade + 10)
        return grade


studentsTwo = [
    Student("Alice", 85),
    Student("Bob", 45),
    Student("Charlie", 72),
    Student("Frank", 55)
]

for s in studentsTwo:
    print(f"{s.name}: {s.is_pass()}")

# for s in studentsTwo:
#     print(f"{s.name} has scored {s.grade} at ", Student.school_name)

# studentsTwo[1].update_grade(70)
# print(f"{studentsTwo[1].name} has new grade {studentsTwo[1].grade}")

# for s in studentsTwo:
#     added = s.add_ten() 
#     print(f"{s.name} has now score{added}")

class Patient:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self._weight = weight
     
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, new_weight):
        if 0<= new_weight <= 100:
            self._weight = new_weight
        else:
            print("Invalid weight")

patients = [
    Patient("Ernest", 20, 55),
    Patient("Brian", 25, 60),
    Patient("James", 30, 70),
    Patient("David", 35, 75)
]

patients[2].weight = 500
# print(patients[2].weight)   shows invalid weight
# for patient in patients:
#     print(f"Patient: {patient.name}, Age: {patient.age}, Weight: {patient._weight}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"My name is {self.name} and I am {self.age} years old")


class Person_one(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        


class Person_two(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Person_three(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    