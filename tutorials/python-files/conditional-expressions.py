# conditional expression = a one-line shortcut for an if else statement (ternary operator)
#                           print or assign one or two values based on a condition
#                               x if (condition) else y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"

max_num = a if a > b else b

min_num = a if a < b else b

status = "Adult" if age >= 18 else "Child"

weather = "Hot" if temperature > 20 else "Cold"

access_level = "Full Access" if user_role == "Admin" else "Limited Access"


print(access_level)