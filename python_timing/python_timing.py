# We will focus on three ways:
# a) Simple tracking time lapse
# b) Using the timeit module
# c) Special %%timeit "magic"


 # USING SIMPLE TIME LAPSE TRACKING
def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

import time
start_time = time.time()
func_one(100000000)
end_time = time.time()
print(f"Function One took {end_time - start_time} seconds")

start_time = time.time()
func_two(100000000)
end_time = time.time()
print(f"Function Two took {end_time - start_time} seconds")


# USING THE TIMEIT MODULE
import timeit
stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]

'''

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))

'''
print(timeit.timeit(stmt, setup, number=1000000))
print(timeit.timeit(stmt2, setup2, number=1000000))
