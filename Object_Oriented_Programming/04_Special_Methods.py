my_list = [1, 2, 3]
# print(len(my_list))


class Sample():
    pass
    
my_sample = Sample()
# Since len method won't work for the objects for user built classes so we have to use (special methods)/(dunder methods) 
# Always remember __init__ is also a special/dunder mehtod 
# print(len(my_sample))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def  __str__(self):
        return f"{self.title} by {self.author} with {self.pages}"
    def __len__(self):
        return self.pages

b = Book('Python rocks', 'Jose', 200)
# When we call without defining the dunder method str it returns 
# <__main__.Book object at 0x00000200EE1B70E0>
# But on the other hand after defining str dunder method we get custom result returned by the dunder/magic method __str__
print(str(b))
# Same is the case with dunder method __len__
print(len(b))
del b
print(len(b))