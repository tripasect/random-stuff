import random

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

    def bark(self):
        print("HAP! HAP!")


# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    def meow(self):
        print("MEOW! MEOW!")


# Person is-a object
class Person(object):

    def __init__(self, name, facts):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None
        self.facts = ["I am a human-being.", "I have two legs."]

    def fact(self):
        print(self.facts.pop())


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super().__init__(name, facts)
        # Employee has-a salary
        self.salary = salary
        super().__init__(name, facts)

# Fish is-a Object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Hailbut is-a Fish
class Hailbut(Fish):
    pass
