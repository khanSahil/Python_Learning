import math

value = 4.45
value2 = 4.6
value3 = 4.4

print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(round(value2)) # round up
print(round(value3)) # round down

print(math.pi)
print(math.e)
print(math.inf)

print(math.log(math.e))
print(math.log(10000, 10))

print(math.cos(0))
print(math.cos(180))

import random

print(random.randint(0,10))
##print(random.seed(101)) # ensuring same random numbers are generated always.
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))




mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# sample with replcement

print(random.choices(population = mylist,k = 10))

# sample without replcement
print(random.sample(population = mylist,k = 10))

# shuffle a list
random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0, b=100))
