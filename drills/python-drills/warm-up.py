hospital_departments = ("lab", "clinic", "IT", "Admin Management")
print(hospital_departments[2], "and" ,hospital_departments[3])

list = ["lab", "clinic", "pharmacy", "reception"]
converted_list = set(list)

print(converted_list)
print(len(converted_list))

staff = { "name": "Linda", "role": "Nurse", "years of experience": 7 }

for key, value in staff.items():
    print(key, " : ",value)

patients = {"Alice": 25, "Brian": 32, "Cynthia": 19, "David": 40}

new_patients = {key: value + 1 for key, value in patients.items() if value >= 30}
print(new_patients)


meds = ["panadol", "Amoxicilin", "Aspirin"]
stock = [50, 30, 20]

meds_and_stocks = dict(zip(meds, stock))

print(meds_and_stocks)

data = {"lab": [23, 18], "clinic": [12, 9], "pharmacy": [5, 11]}

visits_per_department = {key: value[0] + value[1] for key, value in data.items()}
print(visits_per_department)

patient_list = {}

while True:
    name = input("Enter patient name (or 'done' to stop): ")
    if name.lower() == 'done':
        break
    age = input("Enter patient age: ")
    if not age.isdigit():
        print("Please enter a valid number.")
        continue
    patient_list[name] = int(age)

print("\nFinal patient dictionary")
# print(patient_list) 

tags = {f"{num}-even" if num % 2 == 0 else f"{num}-odd" for num in range(1, 16)}
print(tags)


# How to ensure the data you get is cleaned and stored

# Start with the sample list (you can also use input to gather)
names_one = ["Alice", "Brian", "Cynthia", "alice", "David", "BRIAN"]

# step 1 : convert everything to lowercase for consistency
names_lower = [name.lower() for name in names_one]

# step 2 : Remove duplicates by coverting it to a set 
unique_names = set(names_lower)

# step 3 : Sort alphabetically by turning it back into a list
sorted_names = sorted(unique_names)

# step 4 : Convert to a tuple
final_tuple = tuple(sorted_names)

# print(final_tuple)

# Make it more interactive

names = input("Enter names separated by commas: ").split(",")

names_lower = [name.strip().lower() for name in names]
unique_names = set(names_lower)
final_tuple = tuple(sorted(unique_names))

print("\nFinal tuple of names: ")
print(final_tuple)





