def hello(name = "Sahil"):
    print("The hello() function has been executed")
    
    def greet():
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is the welcome() function inside hello!'

    print("I am going to return a function")
    if name == "Sahil":
        return greet
    else:
        return welcome
    
ret_function = hello("Sahil")
print(ret_function())


def cool():
    
    def super_cool():
        return "I am very cool"
    
    return super_cool

new_func = cool()
print(new_func())



def hello():
    return "Hi Sahil..!"

def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())
    
other(hello)


## Now decorator begins


def new_decorator(original_func):
    
    def wrap_func():
        print("Some extr code, before the original function")
        original_func()
        print("Some extr code, after the original function")
    
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated..!!")
    
#decorated_func = new_decorator(func_needs_decorator)
#decorated_func()


# using @ operator now

@new_decorator
def func_needs_decorator():
    print("I want to be decorated..!!")
    
func_needs_decorator()


# Decorator Class

class decorator_class(object):
    
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('Call Method being executed')
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display():
    print("Display function ran")
    
@decorator_class
def display_info(name, age):
    print(f'Display info ran with arguments {name} {age}')
    
display_info("Sahil", "35")
display()