# Lambda function = A small anonymous function for a one-time use (then we throw them away)
#                   They take any number of arguments but only have 1 expression
#                   Helps keeps the namespace clean and is useful with higher order functions
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                   It looks like:  lambda parameters: expression

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: x % 2 == 0
adult_check = lambda age: True if age >= 18 else False






print(adult_check(12))
# print(is_even(3))
# print(full_name("spongebob", "squarepants"))