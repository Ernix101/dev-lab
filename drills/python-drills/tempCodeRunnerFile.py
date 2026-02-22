

        if not line.strip():
            continue
        parts = line.split(',')
        print(f"{parts[0]} - int({parts[1]}) - {parts[4]}")      # Show name, age and condition
        

        