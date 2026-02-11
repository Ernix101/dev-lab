# SET A ------------------------------------

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        print(f"{self.title} was made by {self.author} in {self.year}")


Book1 = Book("Harry Potter", "J.k Tolkien", 2011)
Book2 = Book("Tarzan", "William D", 2006)

# Book1.description()
# Book2.description()


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)
    

Student1 = Student("Alice")

Student1.add_grades(70)
Student1.add_grades(80)
Student1.add_grades(50)
print(Student1.grades)

# print(Student1.average())

# SET B -----------------------------------------------------

class Course:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.student_obj = Student(name)

    def add_student(self, student_obj):
        self.students.append(student_obj)
        
    

course1 = Course("Health Services Management")
course1.add_student("Alice")

# print(course1.student_obj.name)

# SET C --------------------------------------------------

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak():
        return "This Animal has spoken!"
    

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"
    
dog1 = Dog("Bruno")
# print(dog1.speak())

class Spaniel(Dog):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


# SET D ---------------------------------------------

class Employee:

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def info(self):
        return f"This {self.name} works in {self.department}"
    
class Doctor(Employee):

    def __init__(self, name, id, department, specialty):
        super().__init__(name, id, department)
        self.specialty = specialty

    def info(self):
        return f"This Doctor specializes in {self.specialty}"
    
class Nurse(Employee):

    def __init__(self, name, id, department, shift):
        super().__init__(name, id, department)
        self.shift = shift

    def info(self):
        return f"This Nurse works in {self.shift} shift"
    

doctor1 = Doctor("James", 331, "Cardiology", "consulting")
nurse1 = Nurse("Wendy", 221, "Pediatrics", "Rotation-call")

# print(doctor1.info())
# print(nurse1.info())


class Medication:

    def __init__(self, name, category, stock):
        self.name = name
        self.category = category
        self.stock = stock

    def restock(self, amount):
        self.stock += amount
    
    def use(self, amount):
        if amount <= self.stock:
            self.stock -= amount
        else:
            print("Not enough Stock!")


class Pharmacy:
    def __init__(self):
        self.medications = {}

    def add_med(self, med):
        self.medications[med.name] = med    # med.name is the key and the value is the medicine object

    def use_med(self, name, amount):
        if name in self.medications:
            self.medications[name].use(amount)
        else:
            print("Medication not found!")

    def report(self):
        for med in self.medications.values():    # in order to access the object, we use values()
            print(f"{med.name}: {med.stock}")



med1 = Medication("Amoxilin", "Antibiotic", 30)
med2 = Medication("Ibuprofen", "Pain Killer", 20)
med3 = Medication("Cetrizine", "Anti-allergies", 10)


lab1 = Pharmacy()
# Let's add some medicine 
lab1.add_med(med1)  # should be 30
lab1.add_med(med2)  # should be 20
lab1.add_med(med3)  # should be 10
# Let's use them 
lab1.use_med("Amoxilin", 10)  # now it's 20
lab1.use_med("Ibuprofen", 5)  # now it's 15
lab1.use_med("Cetrizine", 2)  # now it's 8
# let's restock
med1.restock(10)
med2.restock(5)
med3.restock(2)


lab1.report()