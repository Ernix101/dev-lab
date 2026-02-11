# There are various types of collections: lists, sets and tuples and dictionaries too. Let's see how they work.
#    list = [] ordered and changeable. Duplicates OK
#    Tuple = () ordered and unchangeable, Duplicates OK. Faster
#    Set = {} unordered and immutable, but Add/Remove OK. No duplicates



# fruits = ["apple", "orange", "banana", "coconut", "coconut"]
# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[1] = "pinneapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))
# print(fruits.count("pineapple"))


# print(fruits[1])
# for fruit in fruits:
#     print(fruit)
# fruits.add("pinapple")
# fruits.remove("coconut")
# fruits.pop()


# print(fruits.index("apple"))
# print(fruits.count("coconut"))
# for fruit in fruits:
#     print(fruit)


# ------------------------------------------------------------------------------------------------------
# Let's move on to dictionaries now.

capitals = { "USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("Japan"))
# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Nairobi"})
# capitals.pop("China")
# capitals.popitem() --removes the latest item
# capitals.clear()

# keys = capitals.keys()

# for key in keys:
#     print(key)
# print(keys)

# values = capitals.values()
# print(values)
# for value in values:
#     print(value)

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")

