# map(function, collection) = Applies a given function to all items in a collection
# If you prefer, you could also use a lambda function

# def c_to_f(temp):
#     return(temp * 9/5) + 32

celcius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

# farenheit_temps = list(map(c_to_f, celcius_temps))
farenheit_temps = list(map(lambda temp: (temp * 9/5) + 32, celcius_temps))

# for temp in farenheit_temps:
#     print(temp)
print(farenheit_temps)