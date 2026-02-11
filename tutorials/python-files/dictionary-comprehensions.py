# A dictionary comprehension - is similar to a list comprehension, except for the order in
#               which keys and values are arranged.

# For example, if we wanted to method chain a dictionary-validation to follow a sorted and alphabetical order

names_dict = {}
names_dict = {name: age for name, age in 
              (line.strip().split(',') for line in names_dict)}
