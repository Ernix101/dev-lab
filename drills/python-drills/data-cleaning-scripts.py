
#------------Patient Registration---------------------------------------------------------------------------------
import csv


# patients = [["name","age","phone","diagnosis"],
#             ["John Kamau",45,0o0712345678,"Hypertension"],
#             ["Mary Wanjiku","",0o0723456789,"Diabetes"],
#             ["",32,0o0734567890,"Malaria"],
#             ["David Omondi",28,"","Flu"],
#             ["Grace Muthoni",67,0o0745678901],
#             ["Peter Njoroge","invalid",0o0756789012,"Asthma"]]


file_path = r"C:/Users/Administrator/Desktop/patients.csv"
output_path = r"C:/Users/Administrator/Desktop/patients_cleaned.csv"

with open(file_path, "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)        # Get the header row

    with open(output_path, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header first

        for row in reader:
            if len(row) != 4:   # Skip malformed rows
                continue

            name, age, phone, diagnosis = row

            # Clean each field
            name = name.strip() if name.strip() else "Unknown Patient"

            # Handle age
            age = age.strip()
            if not age.isdigit():
                age = "0"

            # Handle phone
            phone = phone.strip() if phone.strip() else "No phone"

            # Handle diagnosis
            diagnosis = diagnosis.strip() if diagnosis.strip() else "Not diagnosed"

            # Write cleaned row 
            writer.writerow([name, age, phone, diagnosis])

print(f"Cleaned file created at {output_path}")



#-------Medication Inventory---------------------------------------------------------------------------------------

file_path2 = r"C:/Users/Administrator/Desktop/inventory.csv"
output_path2 = r"C:/Users/Administrator/Desktop/inventory_cleaned.csv"

# Dictionary to store medications : {name: [total_quantity, latest_expiry]}
medications = {}


with open(file_path2, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    for row in reader:
        if len(row) != 3:
            continue

        medication, quantity, expiry_date = row

        # Standardize name to Title Case
        medication = medication.strip().title()

        # Convert quantity to integer
        quantity = int(quantity.strip()) if quantity.strip().isdigit() else 0

        # Handle expiry date
        expiry_date = expiry_date.strip()

        # If medication already exists in the dictionary, update it
        if medication in medications:
            # Add quantities
            medications[medication][0] += quantity

            # Keep the latest expiry date
            # Compare dates and keep the later one
            existing_date = medications[medication][1]
            if expiry_date > existing_date:  # String comparison for YYYY-MM-DD
                medications[medication][1] = expiry_date
        else:
            # First time seeing this medication
            medications[medication] = [quantity, expiry_date]

    # Now write the deduplicated data
    with open(output_path2, 'w', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)

        for med_name, data in medications.items():
            total_qty, latest_expiry = data
            writer.writerow([med_name, total_qty, latest_expiry])
        

print(f"Deduplicated inventory saved to {output_path2}")




#----------Facility Visit Records -------------------------------------------------------------------------

file_path3 = r"C:/Users/Administrator/Desktop/visits.csv"
output_path3 = "C:/Users/Administrator/Desktop/visits_cleaned.csv"

def standardize_date(date_string):
    date_string = date_string.strip()

    # If it has slashes, split by slash
    if '/' in date_string:
        parts = date_string.split('/')
    else:
        parts = date_string.split('-')

    # Find which part is the year (4 digits)
    year = None
    remaining = []

    for part in parts:
        if len(part) == 4:
            year = part
        else:
            remaining.append(part)

    # remaining has [month, day] or [day, month]
    # Assume first is day, second is month (European format)
    # OR first is month, second is day (US format)

    # Simple assumption: if year is first --> year/month/day
    if parts[0] == year:
        return f"{year}-{remaining[0].zfill(2)}-{remaining[1].zfill(0)}"
    
    # If year is last --> day/month/year OR month/day/year
    else:
        # Check if first number > 12 (must be day)
        if int(remaining[0]) > 12:
            day = remaining[0]
            month = remaining[1]

        # Check if second number is > 12 (must be day)
        elif int(remaining[1]) > 12:
            month = remaining[0]
            day = remaining[1]
        # Both <= 12, assume day/month  (European)
        else:
            day = remaining[0]
            month = remaining[1]

        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    


def validate_blood_pressure(bp_string):
    bp_string = bp_string.strip()

    if '/' not in bp_string:
        return "Invalid"
    
    parts = bp_string.split('/')

    if len(parts) != 2:
        return "Invalid"
    
    systolic, diastolic = parts

    if systolic.isdigit() and diastolic.isdigit():
        return bp_string  # Valid
    else:
        return "Invalid"
    

def validate_temperature(temp_string):
    temp_string = temp_string.strip()

    try:
        temp = float(temp_string)
        if 30 <= temp <= 45:
            return temp_string
        else:
            return "Invalid"
    except ValueError:
        return "Invalid"





with open(file_path3, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    with open(file_path3, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)

        for row in header:
            if len(row) != 4:
                continue

            patient_id, visit_date, temperature, blood_pressure = row

            # Clean each field
            visit_date = standardize_date(visit_date)
            temperature = validate_temperature(temperature)
            blood_pressure = validate_blood_pressure(blood_pressure)

            writer.writerow([patient_id, visit_date, temperature, blood_pressure])

print(f"Cleaned visits saved to {output_path3}")