# Python writing files (.txt, .json, .csv)

# txt_data = "I like pizza!"

# employees = ["Eugene, Squidward, Spongebob, Patrick"]
# import json
import csv
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

employees = [["Name", "Age", "Job"], 
             ["Spongebob", 30, "cook"], 
             ["Patrick", 37, "unemployed"], 
             ["Sandy", 27, "Scientist"]]

file_path = "C:/Users/Administrator/Desktop/output.csv"
try:
    with open(file=file_path, mode='w', newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
except PermissionError:
    print("❌File is open in another program! Close it first.")

# We can also set an absolute file path or relative