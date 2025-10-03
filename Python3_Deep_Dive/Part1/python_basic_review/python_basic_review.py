
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
    c = 'abc ' * 3
    d = 'ab ' * 11
    e = 'the quick brown fox ' *5
    f = ['a', 'b'] * 3
    
my_func()

print(my_func.__code__.co_consts)


# In Python we have 5 main types of numbers:
    # boolean
    # int
    # Rational
    # Real
    # Complex

# Python works slightly differently. Depending upon the int value, 
# it can use different number of bits, to store the value.
# Which means, it could use, 4, 8, 12 and so on depending upon the
# value it has to store.

# Since integers are objects, there are fixed overhead per integer.
# Theoretically only limited by the amount of memory available.


import sys

print(type(100))
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(9))
print(sys.getsizeof(2**1000))
print(2**1000)

import time
def calc(a):
    for i in range(10000000):
        a * 2
    
start = time.perf_counter()
calc(2**1000000)
end = time.perf_counter()
print(end - start)


# Integer Operations

# int + int -> int
# int - int -> int
# int * int -> int
# int ** int -> int
# int / int -> float # will always return float
print(5/2)
print(10/2) # print out 5.0 instead of 5


# int // int = int # floor division => floor(int / int)
# int % int = int # modulo 
print(5//2)
print(5%2)

import math
print(math.floor(4.9))
print(math.floor(4.1))
print(math.floor(-3.1))
print(math.floor(-3.9))


# Integers Constructors and Numberical Bases
# Int provides multiple constructors
# 1) Only one parameter, like int(10), int(10.5), int(-5), int(True), int("10") etc
# 2) With additional parameters called as base (default 10)
#   int("1010",2) => 10, or int("1010", base=2) => 10
#   int("A12F", base=16) => 41263 or int("a12f", base=16) => 41263
#   int("534", base=8) => 348

print(int(10))
print(int(True))
print(int("10"))
print(int("1010", base=2))
print(int("A12F", base=16))
print(int("534", base=8))
print(int("0xA", base=16))

# Reverse process: Changing an integer from base 10 to another base
# Built-in functions: for example: bin(), bin(10) => '0b1010'
print(bin(10))
print(oct(10))
print(hex(10))

a = 0b1010
print(f"Value of a is {a}")
b = 0o12
print(f"Value of b is {b}")

# What about other bases?
# We need to write our own custome code for other bases.



# The Fractional Class
# Rational numbers can be represented in Python
# using the Fraction classin the fractions module.

from fractions import Fraction
x = Fraction(3,4)
y = Fraction(22,7)
z = Fraction(6,10)  # Fractions are automatically reduced to 3/5
print(x)
print(y)
print(z)

# Below are the Fraction() constructors
#   Fraction(numerator = 0, denominator = 1)
#   Fraction(other_fraction)
#   Fraction(float)
#   Fraction(deciman)
#   Fraction(string)

# Standard arithmetic operations are supported.
# +,-,*,/ and result will be in Fraction objects as well.

x = Fraction(22,7)
print(f'Numerator is: {x.numerator}')
print(f'Denominator is: {x.denominator}')

# Float objects have finite precision on any operating system
# which means any float can be written as a fraction.

import math
x = Fraction(math.pi)
print(x)
x = Fraction(math.sqrt(2))
print(x)

# Constraining the denominator
# Given a fraction object, we can find an approximate equivalent fraction
# with a constrained denominator using limit_denominator(max_denominator = 1000000)
# instance method to find the closest rational (which could be precisely equal), wtth
# the denominator that doesn't exceed max_denominator.

x = Fraction(math.pi)
print(x)

print(x.limit_denominator(10))
print(x.limit_denominator(100))
print(x.limit_denominator(1000))
print(x.limit_denominator(10000))



# The Float Class
# The float class is Python's default implementation of
# representing real numbers.

# Floats uses fixed number of bytes (fixed width)
#   8 bytes -> 64 Bits
#   but Python objects have some overhead too -> 24 bytes

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x==y)

# Using rounding won't fix the issue either.
# But we can use to round the entirety of both sides of the
# equality comprison

print(round(x,5) == round(y,5))

# math module has that solution for us
# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
# If you don't specify abs_tol, then it defaults to 0
# instead of 0.0 and you will face problem.

# Coercing a float to an Integer
# THis means we will be loosing data.
# Different ways to configure this data loss

# truncation
# floor
# ceiling 
# rounding

# Data loss will happen in all of the above 4 methods

# TRUNCATION:
# Truncating a float simply return the integer portion of the float.
# Basically it ignores everything after the decimal point

import math
print(math.trunc(10.4))
print(math.trunc(-19.5))

print(int(10.4)) # is same as saying trunc(10.4) in case don't want to use math.trunc()

# FLOOR
# The floor of a number is the largest integer less than (or equal to) the number.

x = 10.7
print(math.floor(x))
x = 9.9
print(math.floor(x))
x = 9.1
print(math.floor(x))

x = -10.7
print(math.floor(x))
x = -9.9
print(math.floor(x))
x = -9.1
print(math.floor(x))

# CEILING
# The floor of a number is the smalles integer greater than (or equal to) the number.


x = 10.7
print(math.ceil(x))
x = 9.9
print(math.ceil(x))
x = 9.1
print(math.ceil(x))

x = -10.7
print(math.ceil(x))
x = -9.9
print(math.ceil(x))
x = -9.1
print(math.ceil(x))

# ROUNDING
# Python has built in function round(x, n=0)
# This will round the x to closes multiple of pow(10, -n)
# this would work for positive n, but n, in fact could be negative as well
# if n is not specified, then it defaults to zero, and round (x) will
# therefor return an int

# round(x) => int
# round(x, n) => same type as x
# round(x,0) => same as type x

print(round(1.9))
print(round(1.1))

print(round(1.97492,10))
print(round(1.108049,10))

print(round(-1.9589348,-10))
print(round(-1.18483, -10))

# TIES
print(round(1.25, 1))
print(round(2.35, 1))
print(round(3.5, 1))
print(round(4.5, 1))
print(round(5.5, 1))


# THE COMPLEX NUMBERS

#Constructor will have x component and y component
#complex(x,y) x -> real part, y -> imaginary part (x + yj)

#Example a = complex(1, 2)
#        b = 1 + 2j
#       
#        here a == b => True
# x and y are actually stored as floats. So we need to be carefull
# with the equality testing.

# Some instance properties and methods
# .real           => returns the real part
# .imag           => returns the imaginary part
# .conjugate()    => returns the complex conjugate

# d = 2-3j
# d.real => 2
# d.imag => -3
# d.conjugate = 2+3j

# The standard Arithmetic operators (+, -, / , * , **) works as expcted
# with complex numbers.

# Example: (1 + 2j) + (3 + 4j) = 4 +6j

# Real and complex numbers can be mixed as well.
# Example: (1+2j) + 5 = 6 + 2j
# Example: (1+2j) * 4 = 4 + 8j

# == and != are supported, but we have the same problem as that with float.
# We use cmath module for complex math operations on complex numbers.


## // AND % OPERATORS ARE NOT SUPPORTED
## <, >, <=, >= ARE ALSO NOT SUPPORTED
## functions in math module ALSO NOT SUPPORTED.

#Rectangular to Polar

import cmath
x = 1+1j
print(cmath.phase(x))   # returns the argument phase of the complex number x
print(abs(x))

# Polar to Rectangular
y = cmath.rect(abs(x),cmath.phase(x))
print(y) # this gives (1.0000000000000002+1j)

# BOOLEANS
# Python has concrete bool class that is used to represent Boolean values.
# However, the bool class is a subclass of the int class.
# This means, it posses all the properties and methods of integers, and add
# some specialized one such as and, or etc

print(issubclass(bool, int))
print(issubclass(int, bool))

# Two constants are defined in Python, True and False
print(isinstance(True, bool))
print(isinstance(False, bool))
print(isinstance(True, int))

# Booleans True and False are singleton objects of type bool.
# is and ==, since True and False are singleton objects, hence
# they will always retain their memory address throughout the 
# lifetime of your application.

# So, comparisons of any Boolean expression to True or False can be
# performed either the is(identity) operator, or == (equality) operator.

# a == True and a is True, both will work.

# Since bool objects are also int objects, hence they can be interpreted as
# the integers 1 and 0.
print(int(True))
print(int(False))

# However, True and 1 are not the same objects.
print(id(True) != id(1))

# Booleans as Integers
# This can lead to strange, behavior you may not expected.
# True > False
print(True > False)
print((1==2) == False)
print((1==2) == 0)

# Any interger arithmetic operations will also work with booleans
print(True+True+True)
print(-True)
print(100 * -True)
print(-True * -1)
print(-True == -1)
print(-False * 100)

# The Boolean constructor
# The boolean constructor bool(x), will return True, when x is True
# and False, when x is False

# What really happens is that many classes contain a definition of 
# how to cast instances of themselves to a Boolean
# Every class in python defines its truth value, that means a class will
# say if I am in this state, I am in Truth state else not. This is sometimes
# called as a truth value or truthyness of an object.

# Integers have a truth value defined according to this rule:
#     bool(0) -> False
#     bool(x) -> True, for any int x != 0

print(bool(1))
print(bool(0))
print(bool(-1))

# Objects have Truth Values
# All objects in Python has an associated truth value.
# We saw this with integers above.
# But this works the same for any objects.

# Rules are straightforward:
#    Every object by default has a True truth value, except:
#         None
#         False
#         0 in any numberic type(0, 0.0, 0+0j)
#         empty sequence (list, tuples, strings, ..)
#         empty mapping types
#         custome classes that implements __bool__ , __len__ methods that return False   

# under the hood

# Classes define their truth value by defining a special instance method:
#     __bool__(self) or __len__
#     
#     then when we call bool(x), where x is an instance of any class, python
#     will execute x.__bool__() method, or __len__, if __bool__ is not defined.
#     If __len__or __bool__ also not defined, then it return by default True.

#Example: Integers:
#    def __boo__(self):
#        return self != 0
    
# bool(100), python actually executes, 100.__bool__() and therefor returns
# the result of 100 != 0

print(bool([1,2,3]))
print(bool([]))
print(bool(None))

#     if my_list:
#         # code block
#     
#     if my_list is not None and len(my_list) > 0:
#         code block

print(bool('abc'))
print(bool(''))



# BOOLEANS OPERATORS, PRECEDENCE and SHORT-CIRCUIT EVLUATION
# not, and or

# Top to bottom, order of precedence
# ()
# < > <= >= != == in is
# not
# and
# or

# Boolean Operators and Truth Values

# Every object in Python has a truth value (truthiness)
# So for any object, X and Y, we can also write.
# bool(X) and bool(Y)
# bool(X) or bool(Y)

# In fact we can write as below:
# X or Y
# X and Y

# But what will it return in python, A boolean? No

# X or Y => If X is truthy, returns X, else return Y

# If X is truthy, return X, otherwise, evaluate Y, and returns it.

# Similarly for and operation
# If X is false, return X, otherwise, evaluate Y, and returns it.

print(bool(None))


# FUNCTION PARAMETERS
#   Arguments vs Parameters
#   Positional vs Keyword-Only Arguments
#   Optional Arguments via Defaults
#   Unpacking Iterables and Function Arguments
#   Extended Unpacking
#   Variable Number of Positional and Keyword-Only Arguments

def my_func(a, b): # a and b a parameters of my_func and local to my_func
    print(a*b)
    
x = 10
y = 'ab'
my_func(x, y)   # here x and y are the arguments of my_func.
                # Also note that x and y are passed as a reference.
                # Which means the memory addresses of x and y are passed.

# Module Scope:
#     a and x points to same memory reference.
#     b and y points to same memory reference.

# positional and Key word arguments

# Most common way of assigning arguments to parameters:
#   via the order in which they are passed. i.e. their postion.

def my_func(a, b):
    pass

# A positional arguments can be made optional by specifying a degault value for the
# corresponding parameter.

def my_func(a, b=10):
    pass

# we can certainly call this function as my_func(10, 20) or my_func(5)
# now suppose we have three agruments and want to make one of them as optional.

# def my_func(a, b = 100, c):
#     pass

# How can we call this function without specifying the second parameter?
# Even the definition of above funtion is incorrect.

# The correct way of doing this is below:
    # If a positional parameter is defined with a default value, every positional
    # parameter after it must also be given a default value. So the correct way is
    # below

def my_func(a, b = 5, c = 10):
    pass

# we can call above function as my_func(1), my_func(1,2), my_func(1,2,3)
# Not if we don't want tp provide the value to second argument, then how?
# So we need to specify only a and c. Below is the way:

# Keyword Argument is the way of doing it.
# my_func(a = 1, c = 2)
# my_func(1, c = 2)
# This works even if the arguments doesn't have the default value.

def my_func(a, b, c):
    print(a, b, c)

my_func(a = 1, b = 2, c = 3)
my_func(1, 2, c = 3)
my_func(1,2,3)
my_func(b = 1, a = 3, c = 2)

# If you have a name argument, all arguments thereafter must be a named too.
# my_func(c = 1, 2, 4) # won't work
# my_func(2, b = 2, 4) # won't work

# my_func(1, b = 2, c = 4) # will work
# my_func(1, c = 4, b = 2) # will work



# UNPACKING ITERABLES
#A side note on tuple, 

#(1,2,3) is a tuple, but what defines a tuple in python?
#is it (), no, its 1,2,3. Which means

#1, 2, 3 is also a tuple. In fact () is just to make tuple clearer.

#(1) is not a tuple, its just an integer
# (1,) or 1, is a tuple
# The only exception is when creating an empty tuple. () or tuple()

# Packed Values
# Packed values refers to values that are packed together in some way.
# Tuples list, string, set and dict are obviuos. (1,2,3) or [1, 2, 4], 'hello' etc

# So any iterable is considered as a packed value.

# Unpacking packed values
# Unpacking is an act of splitting packed valuess into individualvariables
# contained in a list or tuple.

a, b, c = [1, 2, 3] # need three variables to unpack
print(a, b, c)
# This unpacking is based on the relative position of each element.

a,b,c = 10,20,'hello'
print(a, b, c)

a,b,c = 'XYZ'
print(a, b, c)

# We can use both shown below in Pytho:
a = 10
b = 20
print(a, b)

a , b = 11, 12
print(a, b)  

# Unpacking works with any iterable type:

for e in 15, 25, 'hello':
    print(e)

a, b = b, a # swapping values
print(a,b)

d = {"key1":1, "Key2":2, "Key3":3}
for k,v in d.items():
    print (k, v)

# EXTENDED UNPACKING (This use case for *)
# We don't always want to unpack every single item in an iterable
# We may, for example, want to unpack the first value, and then 
# unpack the remaining values into another variable

l = [1,2,3, 4]

#we can achieve this using slicing
a = l[0]
b = l[1:]
print(a,b)

#or simple unpacking
a, b = l[0], l[1:]
print(a,b)

#or we can use * operator
a, *b = l
print(a,b)

# another * example
a,b,*c = l
print(a,b,c)

a,*b, c = l
print(a,b,c)

a,*b, c, d = 'python'
print(a,b,c,d)

#a, *b, *c = 'python' # this won't work.

# Till now we have seen, the * operator being used in the LSH
# however, we can use the * operator in RHS as well, like below:

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [*l1,*l2]
print(l3)

l1 = [1,2,3]
l2 = 'hello'
l3 = [*l1,*l2]
print(l3)

# SETS and DICTIONARIES have no ordering, so above is not the way to
# unpack data for sets or dict.

# Usage with unordered types in a situation where you might want to create single collection
# containing all the items of multiple sets, or all the keys of multiple dictionaries

d1 = {'p':1,'y':2}
d2 = {'t':3,'h':4}
d3 = {'h':5, 'o':6,'n':7}

l = [*d1, *d2, *d3]
print(l)
l = {*d1, *d2, *d3}
print(l)

## ** Unpacking operator

# When working with dictionaries we saw that * essentially iterated the keys
# We might ask the question:  can we unpack the key-value pairs of the dictionary?
# The answer is YES

d1 = {'p':1,'y':2}
d2 = {'t':3,'h':4}
d3 = {'h':5, 'o':6,'n':7}
d = {**d1, **d2, **d3}
print(d)

d1 = {'a':1,'b':2}
t = {'a':10, 'c':3, **d1}
print(t)
t = {**d1,'a':10, 'c':3}
print(t)

# NESTED UNPACKING
l = [1, 2, [3, 4]]  # here third element is list itself
# we can certainly unpack it in this way: a, b, c = l

a,b,c=l
d,e = c
print(a,b,d,e)

a,b,(c,d) = l
print(a,b,c,d)

a,*b,(c,d,e) = [1,2,3,'XYZ']
print(a,b,c,d,e)

# Earlier we said * operator can only be used once in the lHS of an
# unpacking assignment.

a,*b,(c,*d) = [1,2,3,'python']
print(a,b,c,d)



#*ARGS
#With using *args we can pass on any number of arguments.

def func1(a, b , *c):
    d,e,f = c
    print(a, b, d, e, f)

func1(1,3, 'a','b','c')

# The * parameter name is arbitrary - you can make it whatever you want.
# It is customary but not required to name it as *args.

def func1(a, b , *args):
    d,e,f = args
    print(a, b, d, e, f)

func1(1,3, 'x','y','z')

# *args exhaust the positional argument. You cannot add more positional arguments
# after *args

def func2(a,b,*args,d): # this is ok if we write function in this way
    pass

# this will throw error TypeError: func2() missing 1 required keyword-only argument: 'd'
#func2(10,20,'a','b',100)  # func5() is the solution of this

# Unpacking arguments
def func3(a,b,c):
    print(a,b,c)

l = [10,20,30] # if we pass this list in the func3(), it will error out as it expects three
# arguments. However, if we unpack it into three values, then it will work.

# func3(l) # error out
func3(*l) # will work

# KEYWORD ARGUMENT

# Recall that positional parameters can, optionally be passed as named (keyword) arguments.
def func4(a,b,c):
    pass

func4(1,2,3)
func4(a=1,b=2,c=3)

# Mandatory Keyword Arguments
# We can make keyword arguments mandatory
# To do so, we create parameters after the positional parameters have been exhausted.

def func5(a, b, *args, d):
    print(a,b,args,d)

func5(1,2,'a','b','c', d = 10.5)

# We can omit any mandatory positional arguments as well.
def func6(*args, d):
    print(args,d)

func6(d = 10)
func6(1,2,3,d = 100)

# In fact we can even enforce no positional arguments at all
def func7(*,d): #* indicates end of positional argument
    print(d)

# func7(1,2,3, d = 5) # Error : func7() takes 0 positional arguments but 3 positional arguments 
# (and 1 keyword-only argument) were given

func7(d = 100)


# *KWARGS (Keyword Arguments)

# *args - is used to scoop up the remaining variable amount of POSITIONAL arguments 
# The variable name args is arbitrary, * is the real performer here
# The values are stored in tuple.

# **kwargs - is used to scoop up a variable amount of remaining KEYWORD arguments
# The variable name kwargs is arbitrary, ** is the real performer here
# the values are stored in dictionary
# No parameters comes after **kwargs

def func1(*, d, **kwargs):
    print(d, kwargs)

func1(d = 1, a = 2, b = 4)
func1(d = 10)
    
def func2(**kwargs):
    print(kwargs)

func2(a = 1, b = 2, C = 4)

def func3(*args, **kwargs):
    print(args, kwargs)

func3(1, 2, a = 10, b = 20)

func3()
