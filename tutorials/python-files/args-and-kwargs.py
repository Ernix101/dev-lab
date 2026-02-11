# *args   = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple key-word arguments
#           * unpacking operator
#           1.positional  2.default  3.keyword  4. ARBITRARY

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr","Spongebob"," Harold", "Squarepants")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Fake Street",
#               apt= "100",
#                city="Detroit",
#                 state="MI",
#                  zip="54321")


def shipping_label(*args, **kwargs):   # Make sure the *args in the parameters come before the **kwargs
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
      print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "poBOX" in kwargs:
      print(f"{kwargs.get('street')}")
      print(f"{kwargs.get('poBOX')}")

    else:
      print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr", "Spongebob", "Squarepants", 
               street= "123 Fake Street",
               poBOX= "PO Box #1000",
               city= "Detroit",
               state="MI",
               zip="54321")