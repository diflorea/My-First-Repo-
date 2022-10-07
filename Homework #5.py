class Person:

    def __init__(self, name):
        self.name = name


    def first_person(self):
        print('Hello, my name is', self.name)

    def second_person(self):
        print('Hello, my name is', self.name)

p = Person('Diana')
p.first_person()
s = Person('Ludmila')
s.second_person()



### Ex #2

class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
#print("\nAccessing class variable using class name")
print(Dog.animal)