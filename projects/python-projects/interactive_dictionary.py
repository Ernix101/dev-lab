patients = {}

# --------------Adding records----------
while True:
    name = input("Enter patient name (or 'done' to stop): ").strip()
    if name.lower() == "done":
        break

    age = input("Enter patient age: ").strip()
    if not age.isdigit():
        print("❌ Please enter a valid number.")
        continue

    gender = input("Enter gender (M/F): ").strip().upper()
    if gender not in ("M", "F"):
        print("❌ Please enter M or F")
        continue

    # save record in dictionary
    patients[name] = {"age": int(age), "gender": gender}
    print(f"✅ Added {name} successfully")




# ------------searching for records-------------
print("\nNow you can search for a patient")
while True:
    search = input("Search by name (or 'done' to exit): ").strip()
    if search.lower() == "done":
        break

    if search in patients:
        info = patients[search]
        print(f"🔹 {search}: {info['age']} years old, Gender: {info['gender']}")
    else:
        print("⚠️ No record found.")




# -----------------Sorted tuple of names---------------------
names_tuple = tuple(sorted(patients.keys()))
print("\nAlphabetically sorted names (tuple):")
print(names_tuple)