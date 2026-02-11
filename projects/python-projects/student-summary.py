students = [
{"id": 1, "name": "Alice", "score": 85, "region": "Nairobi"},
{"id": 2, "name": "Brian", "score": 67, "region": "Kisumu"},
{"id": 3, "name": "Cynthia", "score": 45, "region": "Nairobi"},
{"id": 4, "name": "David", "score": 90, "region": "Mombasa"},
{"id": 5, "name": "Eva", "score": 72, "region": "Kisumu"},
{"id": 6, "name": "Frank", "score": 55, "region": "Nairobi"},
{"id": 7, "name": "Grace", "score": 38, "region": "Eldoret"}
]

for student in students:

    # Add a Grade
    if student["score"] >= 80:
        student["Grade"] = "A"
    elif student["score"] >= 70:
        student["Grade"] = "B"
    elif student["score"] >= 60:
        student["Grade"] = "C"
    else:
        student["Grade"] = "D"

    #Add a status
    if student["score"] >= 50:
        student["Status"] = "Pass"
    else:
        student["Status"] = "Fail"

passed = 0
failed = 0

for student in students:
    if student["Status"] == "Pass": 
        passed += 1
    else:
        failed += 1

print("Passed: ", passed)
print("Failed: ", failed)

top_student = students[0]
for student in students:
    if student["score"] > top_student["score"]:
        top_student = student

print("Top Scorer: ", top_student["name"], "(", top_student["score"], ")")

region_counts = {}
for student in students:
    region = student["region"]
    region_counts[region] = region_counts.get(region, 0) + 1

print(region_counts)



