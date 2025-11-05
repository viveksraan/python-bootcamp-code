'''
- Generators are functions which can return back a value and then later resume to pick up where it left off
- This way generators allow us to generate a sequence of values over time 
- The main difference in syntax will be the use of a yield keyword statement  
- When a generator function is compiled they become an object that supports an iterator protocol
- That means when they are called in your code they don't actually return a value and then exit unless they suspend and resume their execution and state around the last point of value generation
- Main advantage is that instead of having to compute an entire series of values up front, the generator computes one value waits until the next value is called for
- If a user did need the list, they have to transform the generator to a list with list(range(0, 10)), range is also a generator in itself
'''

def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3

for x in list(create_cubes(4)):
    print(x)

print(list(create_cubes(4)))