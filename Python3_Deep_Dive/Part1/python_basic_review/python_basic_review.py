

a = [1, 2, 3]

b = [1, 2,
     3, 4
     ]

c = [1 # number 1
     ,2,3,4,5]

d = (1,
     2,
     3)

e = {"key1":1 # value for key1
     ,"Key2":2,
     "Key3":3 # value for key1
     }

def my_func_one(a, b, c):
    pass

def my_func_two(a, 
            b,
            c):
    pass

print(a)
print(b)
print(c)
print(d)
print(e)

a = 10
b = 20
c = 30

if a > 5 and b > 6 and c > 8:
    print('Yes')
    

if a > 5 \
    and b > 6 \
    and c > 8:
    print('Yes')
    
a = '''this is a string'''
print(a)

b = '''this
is a string'''
print(b)

b = '''this
    is a string
    '''
print(b)

def my_func_three():
    a = '''this is multi-line
string that is indented'''
    return a
print(my_func_three())

#Variable Name Identifiers
_var = 10
var_1 = 20
varOne = 30
__var = 1
__var__ = 2 
_my_var = 3

print(_var)
print(var_1)
print(varOne)
print(__var)
print(__var__)
print(_my_var)

# _variable_name    Internal use, or private ojects. They can't be iported from other modules.
#__variable_name    Mangled to avoid name conflicts in subclasses. useful in inheritance chains.
#__variable_name__   Used for system defined names, that have special meaning to the Python interpreter.
#                   example __init__, __call__, __str__, __repr__
# https://peps.python.org/pep-0008/

#Packages =  short all lower cases, preferably no underscores.
#Modules = short all lower cases, underscores if it improves readability.
#Classes = CapitalizedWords (PascalCase or CamelCase)
#Function = lower_case_with_underscores (snake_case)
#Variables = lower_case_with_underscores (snake_case)
#Constants = ALL_UPPERCASE_WITH_UNDERSCORES
#Global Variable = lower_case_with_underscores (snake_case) with a leading underscore.

#Ternary Operators
# a if condition else b

a = 10
result = a if a > 5 else 0
print(result)

# Functions

#Annotations
# Basically saying I am going to pass \
# an integer and a string and return a string explicitly.
def my_func(a:int, b:str) -> str:
    return str(a) + b

print(my_func(10, 'hello'))
print(my_func.__annotations__)

# lambda functions

print(type(my_func))
x = 10
print((lambda x: x ** 2)(x))
fn1 = lambda x: x ** 2
print(fn1(10))
print(type(fn1))

#CLASSES

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'   
    
    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

r1 = Rectangle(10, 20)
print(r1)
print(repr(r1))
print(r1.area())
print(r1.perimeter())
print(str(r1))
r2 = Rectangle(10, 20)

print(r1 == r2)  # False, because they are different objects in memory
print(r1 is r2)  # False, because they are different objects in memory
r3 = r1
print(r1 is r3)  # True, because they reference the same object in memory
print(r1 == 100)  # False, because they are different types
print(r1 < Rectangle(15, 15))  # True, because 200 < 225
print(r1 < Rectangle(10, 10))  # True, because 200 < 225
#print(r1 < 210)


# Private Variables
# we always right getters and setters in python to access private variables
# However, in python we can do backward compatibility and access private variables directly.
class Square:
    def __init__(self, side_length):
        self._width = side_length
        self._height = side_length
    
    @property                   # this will make sure we have backward compatibility
    def width(self):
        print("Getting width")
        return self._width
    
    @property                   # this will make sure we have backward compatibility
    def height(self):
        return self._height
    
    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
            self._height = width
        else:
            raise ValueError("Width must be positive")
    
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width > 0:
            self._width = width
            self._height = width
        else:
            raise ValueError("Width must be positive")
    
    def area(self):
        return self._width * self._height
   
s1 = Square(10)
print(s1._width)
print(s1.width)
s1.width = 20
print(s1.width)
s1.width = -10



# Variables and Memory Referencing
# In python we can find out the memory address
#   of a variable using the id() function.
#   This will return a base-10 number. We can 
#  convert it to hex using the hex() function.

import sys

# reference counting
my_var = 10;
print(my_var)
print(hex(id(my_var)))

greeting = "Hello, World!"
print(greeting)
print(hex(id(greeting)))

your_var = my_var # pointing to the same memory location as my_var
print(hex(id(your_var)))
import sys, ctypes
ref_var = 20;
print(sys.getrefcount(ref_var)) # this shows the ref count as 11
print(ctypes.c_long.from_address(id(ref_var)).value) # this shows the rfernce count as 10. already my_var is being cached
# somewhere in the memroy.

x = object()  # brand new, not cached
print(sys.getrefcount(x))  # usually 2 (your binding + the temp in getrefcount)
print(ctypes.c_ssize_t.from_address(id(x)).value)  # usually 1
x = None
print(sys.getrefcount(x))  #it could be any value, or a junk value
print(ctypes.c_ssize_t.from_address(id(x)).value)  # it could be any value, or a junk value

#Garbage Collection
# Python uses reference counting and a cyclic garbage collector to manage memory.

# Circular References might lead to memory leaks.
# GC will be able to identity this and clean memory.
# GC runs periodically to clean up circular references.
# GC can be turned ON or OFF using the gc module.
# you can also manually trigger garbage collection using gc.collect().
# GC doen't work well with Python < v3.4
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object found"
    return "object not found"

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A created" with ref count {hex(id(self))} {hex(id(self.b))}')
        
class B:
    def __init__(self, a):
        self.a = a
        print(f'B created" with ref count {hex(id(self))} {hex(id(self.a))}')
    
gc.disable()  # disable automatic garbage collection
my_var = A()
print(hex(id(my_var)))

a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))  # reference count for instance of A
print(ref_count(b_id))  # reference count for instance of B

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(ref_count(a_id))  # reference count for instance of A
print(ref_count(b_id))  # reference count for instance of B

print(object_by_id(a_id))
print(object_by_id(b_id))

gc.collect()  # manually trigger garbage collection

print(ref_count(a_id))  # reference count for instance of A
print(ref_count(b_id))  # reference count for instance of B
print(object_by_id(a_id))
print(object_by_id(b_id))


# Dynamic Typing vs Static Typing
# Python is a dynamically typed language.
# This means that the type of a variable is determined at runtime and can change as the program executes.

# The value inside the int objects, can never be changed. The variable just points to a different int object
# whenever the value is changed.
a = 10
print(a)
print(hex(id(a)))
a = 20
print(a)
print(hex(id(a)))
a = "Hello"
print(a)
print(hex(id(a)))

a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

# Object Mutability
# Mutable objects can be changed after they are created.
# Immutable objects cannot be changed after they are created.

# Immutable objects: int, float, str, tuple, frozenset, boolean, User defined classes
# Mutable objects: list, dict, set, bytearray, User defined classes.

t = (1, 2, 3) # this is immutable 100%

a = [1, 2]
b = [3, 4]

t = (a,b)   # tuple mutable, but the contents of the tuple are mutable
print(t)
a.append(5)
b.append(6)
print(t)

# since the list is mutable, we can change the contents of the list inside the tuple,
# however, if we try to change the tuple itself, we will get an error.

# shared references

# The term shared references means that multiple variables point to the same object in memory.
# i.e. having the same memory address.

a = 10
b = 10 # both a and b point to the same int object in memory
# Python manager decides to automatically re-use the memory references
print(hex(id(a)))
print(hex(id(b)))

# With mutable object, the python memoery manager will not re-use the memory references

# Variable Equality

# Memory address uses "is or is not"  operator and we use => var_1 is var_2
# Object state (data) "== or !=" equality operator and we use => var_1 == var_2

a = 10
b = a

print(a == b)
print(a is b)

b = 10

print(a == b)
print(a is b)

a = "hello"
b = "hello"

print(a == b)
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

a = 10
b = 10.0

print(a == b)
print(a is b)

# None Object
# The Node object can be assigned to variables to indicate that they are not set
# (in the way we would expect them to be), i.e. an "empty" value (or null pointer)
# But the None object is a real object managed by Python memory manager.
# Furthermore, the memory manager will always use a shared reference when assigning 
# a variable to None.

a = None
b = None

print(a == b)
print(a is b)
print(a is None)



# Everything in Python is an Object
#   Data Types
#   Integers
#   Booleans
#   Floats
#   Strings
#   Lists
#   Tuples
#   Sets
#   Dictionaries
#   None

# Constructs"
#   Operators (+,-,*,/,//,%,**,=,==,!=,>,<,>=,<=,is,is not,in,not in)
#   Functions
#   Classes

# But one thing is common with all these things, is that they all
# are objects (instances of classes).
# This means they all have a memory address and a type.
# We can use id to check the address of these objects.
#   Any object can be assigned to any variable including functions.
#   Any object can be assigned to a function, including functions.
#   Any object can be returned from function, including functions

# my_func = name of the function.
# my_func() = this means you are invoking the function.


a = 10
print(type(a))
b = int(a)
print(type(b))
#print(help(int))

def square(x):
    return x ** 2

print(type(square))

f = square
print(hex(id(f)))
print(hex(id(square)))
print(square(2))

def cube(x):
    return x**3
def select_function(fn_name):
    if fn_name ==1:
        return square
    else:
        return cube
    
print(f(1) == f(1))
print(select_function(2)(3)) # printing cube of 3
print(select_function(1)(3)) # printing square of 3

def exec_function(fn, n):
    return fn(n)

print(exec_function(cube, 5))
print(exec_function(square, 5))



# Python Optimizations: Interning.
# Python memory manager optimizes the memory usage by re-using the memory references
# for immutable objects. This is called interning.

a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

a = 1000
b = 1000
print(hex(id(a)))   
print(hex(id(b)))   # different answer that that of a.

# So what is happening?
#   Interning: reusing object on demand.
#   At startup Python (CPython), pre-loads (caches) a global list of integers in the range [-5 , 256]
#   Any time, an integer is referenced in that range, Python will use the cached version of that object.
#       Singletons: Optimization strategy - small integers show up often


# Python Optimizations: String Interning.
# Some strings are also automatically interned by Python, but not all.
# Some string literals are also automatically interned, but not all.

# Why do this?
# Its all about performance and memory optimization.(speed and memory)
# Python, both internally, and in the code you write, deals with lots of
# dictionary type lookups, on string keys, which means a lot of string comparisons.

# Lets say we want to see if two strings are equal:
#    a = 'some_long_string', b = 'some_long_string'
# Using a == b, we need to compare each character in the string.

# But if we know that both a and b are interned strings,
# then we can just compare their memory addresses using a is b, which is much faster.

# We can force string interning using the sys.intern() function.
import sys
a = sys.intern('some_long_string')
b = sys.intern('some_long_string')
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)


# Python Optimizations: Peephole Optimizations
# Peephole optimizations are small optimizations that the Python compiler
# makes to the bytecode it generates. These optimizations are done to improve
# the performance of the code.

# This is another optimization method happens at compile time.

# Constant Expressions
    # a) numeric calculation 24 * 60
    # b) string concatenation "Hello" + " " + "World"
    # c) list comprehension [x * 2 for x in range(10)]  # length is less than 20
    # d) 'the quick brown fox' * 10, won't get optimized, because the length is more than 20
# Membership Tests such as below:
#   if e in [1, 2, 3]   # list of length less than 20

# lists -> tuple when membership test happens
# sets -> frozenset when membership test happens

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' *5
    f = ['a', 'b'] * 3
    
my_func()

print(my_func.__code__.co_consts)