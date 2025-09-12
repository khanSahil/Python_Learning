class Dog():
    
    # Class object attributes.
    # These are same for any instance of class.
    species = 'mammal'
    
    def __init__(self, breed,name):
        self.breed = breed  # string
        self.name = name    # string
        
    # Operation/Actions --> Formally known as Methods.
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")

class Circle():
    #Class object attribute
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi
        # self.area = radius * radius * Circle.pi # we can use self or name of the class to refer to attributes
        
    #method
    def get_circumference(self):
        return 2 * self.pi * self.radius
        

my_dog = Dog('Lab','Chiku')
print(my_dog.breed,my_dog.name,my_dog.species)
my_dog.bark(100)

my_circle = Circle(30)
print(f"Circumference of the Circle: {my_circle.get_circumference()}")
print(f"Area of the Circle: {my_circle.area}")