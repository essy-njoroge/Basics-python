# Parent class / Super class / Base class

class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")


# Child class / Sub-class / Derived class - borrows attributes/behaviors

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")


class Donkey(Animal):
    hasTail = True

    def move(self):
        print("Donkey is moving")


c = Cat()      # create object
c.speak()      # call inherited method
c.meow()       # call Cat method
print()
d= Donkey()     # create Donkey object
d.speak()        # inherited from Animal
d.move()         # Donkey's own method

