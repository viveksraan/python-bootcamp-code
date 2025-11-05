''' 
for understaind generators iter function and next function are very important so let's look upon them with a simple example
'''

def simple_gen():
    for x in range(3):
        yield x+1

# this is the simple way of iterating generators by running a loop over them but we could also use next and iter
# for number in simple_gen():
    # print(number)

gen = simple_gen()
print(next(gen))  # This will display 1
print(next(gen))  # This will display 2
print(next(gen))  # This will display 3
# print(next(gen))  # This will display nothing but give error message becuase the last gen is 3

print(iter)

s = "hello"
# Now if you want to use next with non generator object use iter to convert non generator object to iterator object
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))