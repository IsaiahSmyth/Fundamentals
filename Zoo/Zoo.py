# Imagine a game where you can create a zoo and start raising different types of animals. Say that for each zoo you create can have several different animals. Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal. (Maybe lions and tigers and bears, oh my!) Each animal should at least have a name, an age, a health level, and happiness level. The Animal class should have a display_info method that shows the animal's name, health, and happiness. It should also have a feed method that increases health and happiness by 10.

# In at least one of the Animal child classes you've created, add at least one unique attribute. Give each animal different default levels of health and happiness. The animals should also respond to the feed method with varying levels of changes to health and happiness.

# Once you've tested out your different animals and feel more comfortable with inheritance, create a Zoo class to help manage all your animals.


class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(
            f"{self.name} is {self.age} years old and has a health level of {self.health}")

    def lions(self):
        self.name = 'Lion'
        self.age = 5
        self.health = 100
        self.hapiness = 100

    def tigers(self):
        self.name = "Tiger"
        self.age = 5
        self.health = 100
        self.hapiness = 100

    def bears(self):
        self.name = "Bear"
        self.age = 5
        self.health = 100
        self.hapiness = 100
