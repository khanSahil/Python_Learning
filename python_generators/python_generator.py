# Generator function is used to send a value
# and then later resume to pick up where it left off

# This type of function is called as Generator allowing
# us to generate a sequence of values over time.

# The main difference between the syntax will be the use
# of yield keyword statement

# When generator function is compiled they become an object
# that supports an iteration protocol.

# That mean when they are called i hour code, the don't 
# actually return return a value and then exit

# Instead genertor function will automatically suspend and resume
# their execution and state around the last point of value generation.

# The advantage is that instead of hacing to compute and entire series
# of values up front, the generator computes ne value waits until the 
# next value is called for.

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result 

print(create_cubes(10))

def create_cube_generator(n):
    
    for x in range(n):
        yield x**3

for x in create_cube_generator(5):
    print(x)

print(list(create_cube_generator(10)))

# Let's create another example - Fibonacci Series

def gen_fibon(n):
    a = 1
    b = 1
    
    for num in range(n):
        yield a
        a,b = b, a + b

for number in gen_fibon(10):
    print(number)


















