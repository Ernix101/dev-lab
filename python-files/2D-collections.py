fruits =      ["apple", "orange", "banana", "coconut"]
vegetables =  ["celery", "carrots", "potatoes"]    #These are one dimensional lists
meats =       ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats] -- #This has become 2 dimensional

groceries = [{"apple", "orange", "banana", "coconut"}, 
            {"celery", "carrots", "potatoes"},  # -- This is also another way of creating them.
            {"chicken", "fish", "turkey"}]  


# print(groceries[2][0])  To display each list and also its item by their indices respectively.

# for collection in groceries:
#     print(collection)  # -- This displays the collection as is.

# for collection in groceries:
#     for food in collection:
#         print(food)     # -- This displays each of the foods in each of the list separately.

for collection in groceries:
     for food in collection:
        print(food, end=" ") 
     print()


# I made a nmber pad using a 2d tuple of tuples.
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
