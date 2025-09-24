# Base Class
class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an Animal")
    
    def eat(self):
        print("I am eating")


# Derived Class
class Dog(Animal):  # inhereting Animal class
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    def who_am_i(self): # function over-writing
        print("I am a Dog")
        
    def bark(self): # creating new method inside Dog.
        print("WOOF..!!")

#print(Animal())
my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

print("========================================")

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()
