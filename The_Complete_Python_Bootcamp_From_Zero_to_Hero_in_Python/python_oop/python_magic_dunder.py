
mylist = [1,2,3]
print(len(mylist))


class Sample():
    pass

mysample = Sample()
#print(mysample)
#print(mylist)
#print(len(mysample))


# So the question is how to use python defined standard fuctions like print or len in our
# user defined Classes. This is where those special methods comes into picture.


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author} containing {self.pages} pages"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
        
b = Book("Python Learning", "Sahil", 200)
print(b) # Outputs <__main__.Book object at 0x774eea5d1fc0
print(len(b)) # Outputs <__main__.Book object at 0x774eea5d1fc0

del b # A book object has been deleted
print(b) # NameError: name 'b' is not defined