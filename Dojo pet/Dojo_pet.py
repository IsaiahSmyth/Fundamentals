# Ninja Class
# Attributes

# first_name
# last_name
# pet
# treats
# pet_food
# Methods

# walk()
# feed()
# bathe()

# Pet Class
# Attributes

# name
# type
# tricks
# health
# energy
# Methods

# sleep()
# eat()
# play()
# noise()

# Create a Ninja class with the ninja attributes listed above.
class Ninja:
    def __init__ (self, first_name, last_name, pet, treat, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food

# Create a Pet class with the pet attributes listed above.
class Pet:
    def __init__ (self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

# Implement walk(), feed(), bathe() on the ninja class.
    def walk(self, play):
        self.energy = self.energy - 1
    def feed(self, eat):
        self.health = self.health + 1
    def bathe(self, bathe):
        self.health = self.health + 1

# Implement sleep(), eat(), play(), noise() methods on the pet class.
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print(self.name + " says woof woof!")

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
ninja1 = Ninja(Pet)

# Have the Ninja feed, walk , and bathe their pet.
ninja1.feed()
ninja1.walk()
ninja1.bathe()

# NINJA BONUS: Use modules to separate out the classes into different files.
from user import Ninja
from pet import Pet


# SENSEI BONUS: Use Inheritance to create sub classes of pets.
class dog(Pet):
    pass
# Compress or zip up assignment and upload it.