class MedicalRecord:

    def __init__(self, diagnosis, date):
        self.diagnosis = diagnosis
        self.date = date


    # Optional:
    def __str__(self):
        return f"Diagnosis: {self.diagnosis} on {self.date}"


# --------------Start from here⬇️--------------composition had to come first-----------
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        print(f"{self.name} has been deactivated")

    def introduce_self(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

    def update_age(self, new_age):
        self.name = new_age
        print(f"I am now {self.age} years old")


class Patient(Person):

    def __init__(self, name, age, diagnosis, date):
        super().__init__(name, age)
        self.diagnosis = diagnosis
        self.date = date

        self.record = MedicalRecord(diagnosis, date)

    def report_symptoms(self):
        print(f"{self.name} is reporting fever")

    def show_record(self):
        print(f"{self.name}'s medical record: {self.record}")

    def display_details(self):
        return f"{self.name} aged {self.age} has been diagnosed with {self.diagnosis} on {self.date}"
    
    def introduce_self(self):
        print(f"My name is {self.name} and I'm currently receiving treatment.")

    def get_summary(self):
        return f"Patient {self.name} ({self.age} years) - {self.record.diagnosis} since {self.record.date}"
    

Alice = Patient("Alice", 30, "Cold", "20/1/2026")
print(Alice.introduce_self())


        
class Doctor(Person):

    def prescribe_medication(self):
        print(f"{self.name} prescribes antibiotics")


# # Test (Inheritance) :
# Alice = Patient("Alice", 30)
# Alice.introduce_self()
# # patientA.update_age(32)
# Alice.report_symptoms()

# doctorA = Doctor("Mike", 35)
# doctorA.prescribe_medication()

# print(Alice.is_active)
# print(doctorA.is_active)

# patientB = Patient('John', 23)
# patientB.deactivate()
# print(patientB.is_active)


#--------------------Hospital exercises (aggregation) ---------------------------

kenny = Patient("Kenny", 30, "Fever", "2026-01-09")
lisa = Patient("Lisa", 28, "Fever", "2026-01-09")
Gerald = Patient("Gerald", 50, "Influenza A", "2026-01-10")

class Hospital:

    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, new_patient):
        self.patients.append(new_patient)

    def display_patients(self):
        if not self.patients:
            print("No patients registered yet")

            return
        print(f"Patients at {self.name}:")
        for patient in self.patients:
            print(f" - {patient.name}, Age: {patient.age}")


Aga_Khan = Hospital("Aga Khan Hospital")
Aga_Khan.add_patient(kenny)
Aga_Khan.add_patient(lisa)
Aga_Khan.add_patient(Gerald)
Aga_Khan.display_patients()



#---------------------------Composition section ----------------------------
# It's up there, let's test it 
# Gerald.show_record()
# kenny.show_record()
# lisa.show_record()


class InventoryItem:
    def __init__(self, item_name, quantity):
        self.name = item_name
        self.quantity = quantity

class SupplyRoom:
    def __init__(self, base_quantity):
        self.items = [InventoryItem(name, base_quantity) for name in ["Syringes", "Bandages", "Masks"] ]

    def get_summary(self):
        total_items = len(self.items)
        total_qty = sum(item.quantity for item in self.items)   # Sum up all quantities

        return f" Supply Room has {total_items} item types with total quantity {total_qty} "
        

room = SupplyRoom(100)
print(room.items[0].quantity)


def process_health_data(items):
    print("Processing health data summary:")
    for item in items:
        print("➡️" + " " + item.get_summary())


# Mixed list of all stuff
mixed_things = [Alice, room, kenny]

# Process with the function
process_health_data(mixed_things)

