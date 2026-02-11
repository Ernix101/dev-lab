print("This is a test")
name = input("Enter your name: ")
# print(f"Hello, {name}!")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.rfind("u")  --Its like find() but in reverse
# name = name.capitalize()
# name = name.upper()         --Makes all characters uppercase.
# name = name.lower()
# result = name.isdigit()   --Returns a boolean if an item is a number.
# result = name.isalpha()   --Returns a boolean if an item is a letter.
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")   --One of the most useful methods

# A challenge to validate user's input name for spaces, numbers and length

name.find(" ")
name.isalpha()


if len(name) > 12:
    print("your name is too long not more than 12 characters")
elif not name.find(" ") == -1:
    print("your name cant contain spaces")
elif not name.isalpha():
    print("Your username cant contain numbers")
else:
    print("Welcome" + " " +  name)
