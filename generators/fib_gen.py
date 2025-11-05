def gen_fibon (n):
    a, b = 1, 1
    for i in range(n):
        # yield returns the result computed in current iteration of the generator
        yield a
        a, b = b, a+b

for number in gen_fibon(10):
    print(number)

# X this is wrong generator functions don't return list but they return generator 
fib_gen = gen_fibon(10) 
print(fib_gen)
# So the correct way is converting the return type to list ex. for 6 it will be [1, 1, 2, 3, 5, 8]
fib_list = list(gen_fibon(6))

print(fib_list)
