def add(n1, n2):
    print(n1+n2)

result = 0
try:
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly")
else:   # either except block runs or else block runs
    print("Add went well")
print(result)



try:
    fp = open("testfile", 'r')
    fp.write("Write a test line")
except TypeError:
    print("There is a type error!")
except OSError:
    print("Hey you have an OS error!")
finally:    # both finally and except block runs in this case
    print("I always run")
    
try:
    fp = open("testfile", 'r')
    fp.write("Write a test line")
except TypeError:
    print("There is a type error!")
except: # catching any type of error in try section
    print("All other exceptions")
finally:    # both finally and except block runs in this case
    print("I always run")
    

def ask_for_input():
    while True:
        try:
            result = int(input("Please input a number:"))
        except:
            print("Opps..! that is not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except block")
            print("I qill always run at the end")
    
ask_for_input()