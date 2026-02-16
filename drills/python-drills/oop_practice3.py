txt_path = "C:/Users/ERNEST/Desktop/practice-data/patients.txt"

with open(txt_path) as f:
    lines = f.readlines()

    print(f"Total lines: {len(lines)}")

    for line in lines:
        line = line.strip()

        if not line:
            continue
        parts = line.split(',')

        