# filter(function, collection) = return all elements that pass a condition
# If you prefer, you could also use a lambda function if you can't think of a function name

# def is_passing(grade):
#     return grade >= 60

grades = [91, 32, 83, 44, 75, 56, 67]

#Now to filter any grades above 60
passing_grades = list(filter(lambda grade: grade >= 60, grades))

# for grade in passing_grades:
#     print(grade)
print(passing_grades)