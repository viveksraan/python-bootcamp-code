'''
-> In timeit.timeit method we have three parameters (statements, setup(if anything needs to be setup before running the set of statements), number of times you want to test it) 
-> statements and setup are passed as a string
-> It runs the code again and again to figure out how efficient it is
'''
from timeit import timeit

stmt = '''
list_n_1(100)
'''
setup = '''
def list_n_1(n):
    return [str(num) for num in range(n)]
'''

print(timeit(stmt, setup, number=1000000))

stmt = '''
list_n_2(100)
'''
setup = '''
def list_n_2(n):
    return list(map(str, range(n)))
'''

print(timeit(stmt, setup, number=1000000))