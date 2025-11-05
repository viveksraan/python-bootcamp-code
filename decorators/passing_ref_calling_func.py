# Functions are objects that could be pased to other objects such as here hello object is referencing to the function object which returns "Hello!"
def hello():
    return "Hello!"

# Now we are passing the same function object to another object called greet"
greet = hello

# now we can use the same return "Hello!" functionality by calling greet() object also
print(f"{greet()} Simon")

# we've deleted the hello reference object which was referencing to the function 
del hello

# But still we are able to access function by calling greet object so that means hello was just another reference to the function and while you have deleted the reference function is still intact
print(greet())

# And this is why when you print simply the reference object instead of calling the function using it you are returned the memory address simply
# <function hello at 0x000001F4771A1440>
print(greet)
