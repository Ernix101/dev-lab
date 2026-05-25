txt_path = "C:/Users/ERNEST/Desktop/practice-data/patients.txt"

with open(txt_path) as f:
    lines = f.readlines()

    if "Name" in lines[0]:
            lines = lines[1:]       # Skip the header row

    print(f"Total lines: {len(lines)}")

    senior_count = 0
    age_threshold = 60

    max_age = 0
    oldest_patient = ""

    min_age = 999
    youngest_patient = ""

    for line in lines:
        line = line.strip()

        if not line.strip():
            continue
        parts = line.split(',')

        try:
            age = int(parts[1].strip())     # Age is an integer to be used in math operations
            
        except ValueError:
             print(f"Bad age in {line}")
             continue
        
        if age > max_age:
                 max_age = age
                 oldest_patient = parts[0]

        if age < min_age:
             min_age = age
             youngest_patient = parts[0]

        # if age > age_threshold:                            # Check above 60 now
        #     senior_count += 1
        #     print(f"{parts[0]} - {parts[1]} - {parts[4]}")      # Show name, age and condition
        print(f"{parts[0]} - {parts[1]} - {parts[4]}")
    # print(f"\nFound {senior_count} patients over 60")   # After the loop
    print()
    print(f"Oldest: {oldest_patient}, age: {max_age}")
    print(f"Youngest: {youngest_patient}, age: {min_age}")
        




