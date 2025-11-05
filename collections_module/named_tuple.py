'''
- Similar to defaultdict namedtuple tries to improve the standard tuple by implementing names
- It's a subclass of tuples
- Sometimes you might be having a huge tuple where you might not be able to recall that the value you are trying to access is at exact which index so in those cases namedtuple will be very useful
- It provide named attributes(similar to attributes associated with any general object) also other than the index keys which are also available with the normal tuples
'''

from collections import namedtuple

# there ar two imp. parameters of the namedtupe class' __init__ method type_name, field_names. We have passed the arguments to the namedtuple class now our named tuple object is created for the Dog class and have three attributes age, breed and name 
# Now any object of Dog class will have these three attributes for the three values associated with that namedtuple in exact same order 
Dog = namedtuple('Dog', ['age', 'name', 'breed'])

# So now we are creating a Dog object as a namedtuple with exact same three attributes which we passed, be careful you have to use the exact same order because in whatever order you passed the attributes to the namedtuple class the indexing will be followed according to that so don't change the order here other wise you will mess up
sammy = Dog(age=5, name='Sam', breed='Husky')
type(sammy)

# Now we can use both indexing as well as attributes to access pretty comfortably
print(sammy.breed)
print(sammy[2])
print(sammy.age)
print(sammy[0])
print(sammy.name)
print(sammy[1])