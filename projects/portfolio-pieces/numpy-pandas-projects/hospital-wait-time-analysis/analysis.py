import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

patient_ids = np.array([f'P{i:03d}' for i in range(1, 501)])
departments = np.array(['Emergency', 'Outpatient', 'Internal', 'Surgery', 'Gynaecology', 'Pediatrics', 'Psychiatry'])

#! Generates random dates
start = pd.Timestamp('2025-05-01')
end = pd.Timestamp('2025-05-31')


total_minutes = int((end - start).total_seconds() / 60)
random_minutes = np.random.randint(0, total_minutes, size=500)
arrival_times = [start + pd.Timedelta(minutes=int(m)) for m in random_minutes]

triage_times = [a + pd.Timedelta(minutes=int(m)) for a, m in zip(arrival_times, np.random.randint(5, 30, size=500))]
doctor_times = [t + pd.Timedelta(minutes=int(m)) for t, m in zip(triage_times, np.random.randint(20, 120, size=500))]

df = pd.DataFrame({
    'patient_id': patient_ids,
    'department': np.random.choice(departments, size=500),
    'arrival_time': arrival_times,
    'triage_time': triage_times,
    'doctor_time': doctor_times,
})

# print(df.head())
# df.to_csv('data/data.csv', index=False)

df['arrival_to_triage'] = (df['triage_time'] - df['arrival_time']).dt.total_seconds() / 60
df['triage_to_doctor'] = (df['doctor_time'] - df['triage_time']).dt.total_seconds() / 60
df['total_wait'] = (df['doctor_time'] - df['arrival_time']).dt.total_seconds() / 60

# print(df[['department', 'arrival_to_triage', 'triage_to_doctor', 'total_wait']].head(10))

summary = df.groupby('department')[['arrival_to_triage', 'triage_to_doctor', 'total_wait']].agg(
    ['mean', 'median', lambda x: x.quantile(0.9)]
).rename(columns={'<lambda_0>': 'p90'})

# print(summary)

# summary.to_csv('reports/wait-time-summary.csv')


# Time to visualize!
dept_means = df.groupby('department')['total_wait'].mean()
dept_means.plot(kind='bar', figsize=(10, 6), color='steelblue')
plt.title('Mean Total Wait Time by Department')
