import numpy as np

# TODO Build notes website + health data pipeline concepts

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# * NOTE: array[start:end:step]
# print(array[:, 2])      # Returns [3, 7, 11, 15] cause ':' selects all rows then ',' separates to the columns
# print(array[:, 1:4])    # Returns columns 1 to 4 with all the rows 
# print(array[0:2, 0:2])  # Returned the first 2 rows [1, 2] and the [5, 6] as like a quadrant




# *1. 1D array of 20 patients of ages between 18 and 80
np.random.seed(1)
patient_ages = np.random.randint(18, 80, 20)

# print(patient_ages)
# Calculate the mean, median and min/maximum ages

mean = np.mean(patient_ages)
median = np.median(patient_ages)
min = np.min(patient_ages)
max = np.max(patient_ages)

# print(f"Summary of ages-> Mean: {mean}, Median: {median}, min: {min}, max: {max}")


# *2. Daily patient visits per day for 4 weeks
record = np.random.randint(10, 60, size=(4, 7))
busiest_day_count = np.max(record)
day_number = np.argmax(record)

# *3 Now from this, find the average above 35 visits
average_visits_per_week = np.mean(record, axis=1)
# print(f"The busiest day was DAY NO: {day_number} with a total of {busiest_day_count} visits")

# print(average_visits_per_week.round(2))

high_weeks = record[average_visits_per_week > 35]
# print(high_weeks)

# *4 With blood pressure readings for 10 patients (systolic & diastolic) Identify whose systolic exceeds 140

systolic = np.array([115, 122, 118, 130, 135, 142, 110, 128, 145, 119])
diastolic = np.array([75, 78, 82, 84, 88, 92, 70, 80, 95, 79])

bp_readings = np.array([systolic, diastolic])
high_systole = systolic[systolic > 140]
print()
# print(bp_readings)

hypertensive_threshold = np.where(systolic > 140, systolic, 'stable')
# print()
# print(hypertensive_threshold)
# print(high_systole)

patient_six_pressure = bp_readings[:, 5]
# print(patient_six_pressure)

#* 5. health facility malaria cases for 3 years each month, find which month had the highest cases consistently
malaria_cases = np.array([[120, 135, 210, 450, 680, 590, 350, 200, 150, 250, 380, 220], 
                          [155, 120, 220, 450, 580, 420, 310, 390, 280, 190, 165, 140,], 
                          [185, 142, 212, 444, 600, 520, 320, 195, 160, 225, 340, 290],])

max_per_month = np.max(malaria_cases, axis=0)
month_with_most_cases = np.argmax(max_per_month)
# print(max_per_month)
# print(month_with_most_cases)


months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# print(months[month_with_most_cases])


#* 6. 50 patients' BMI values. Flag anyone below 18.5(underweight) or above 30(obese)

bmis = np.random.randint(16, 35, 50)

underweight = bmis[bmis < 18.5]
obese = bmis[bmis > 30]
normal = bmis[(bmis > 18.5) & (bmis < 30)]

# print(f'underweight: {underweight}')
# print(f'obese: {obese}')
# print(f'normal: {normal}')


#* 7. Comparison of expected versus actual vaccine doses across 10 facilities

expected = np.random.randint(100, 500, 10)
actual = np.random.randint(100, 500, 10)

difference = expected - actual


labels = np.where(difference < 0, 'shortage', 'surplus')

# print(difference)
# print(labels)



#* 8. Normalize a set of hemoglobin levels among 30 patients from 0-1

levels = np.random.randint(8, 16, 30)
# normalizing based on the randint's max and min values :
#          normalized = (value - min)/ (max - min)

# print(levels)
print()
normalized = (levels - np.min(levels)) / (np.max(levels) - np.min(levels))
# print(normalized)


#* 9. DHIS-like monthly facility reporting rates across Jan-Jun. Find less than 80%
facilities = np.array(['HF_01','HF_02','HF_03','HF_04','HF_05','HF_06','HF_07','HF_08','HF_09','HF_10','HF_11','HF_12',])
reporting_rates = np.random.randint(30, 100, size=(12, 6))

always_above = np.all(reporting_rates >= 80, axis=1)
# print(facilities[always_above])
# print(reporting_rates[reporting_rates >= 80])

# print(np.sum(always_above))

ids = np.array(['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10'])
ages = np.array([27, 22, 30, 45, 21, 55, 33, 38, 77, 80])
severity_scores = np.array([5, 7, 8, 2, 8, 4, 3, 5, 6, 9])

# info = np.array([ids, ages, severity_scores])  # combining is Not was is required
sorted_indices = np.argsort(-severity_scores)
top5 = sorted_indices[:5]

print(ids[top5])
print(ages[top5])
print(severity_scores[top5])
