# Aggregation = represents a relationship where one object (the whole) contains references
#               to one or more INDEPENDENT objects (the parts)

class Zoo:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        
    def list_animals(self):
        return [f"{animal.name}" for animal in self.animals]


class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self, sound):
        f" The {self.name} will make {sound}"


zoo1 = Zoo("Nairobi Zoo", "1200ac")

animal1 = Animal("Lion", "Roars")
animal2 = Animal("Buffalo", "Grunts")
animal3 = Animal("Hyena", "Laughs")

zoo1.add_animal(animal1)
zoo1.add_animal(animal2)
zoo1.add_animal(animal3)

print(zoo1.name)
for animal in zoo1.list_animals():
    print(animal)

# print(animal1.speak())