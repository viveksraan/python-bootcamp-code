import pdb

x = [1,2,3]
y, z = 2, 3
result_1 = y+z
# when you will run this code interpreter will yell at you that there's an error in this ine of code 
'''
- now we can use debugger here and as your code will reach here you can analyze what's the value of x, y, x what's the value of result1 which is already computed when you have reacher here, which will help you figure out the reason of error
- It's specially very useful when you are taking too much inputs and doing a lot of computation because you don't know what user has given as input or there's too much of reassignment and you are not sure what variable is holding what type of data
- There are other debugging commands as well in pdb module which could be really useful  
'''
pdb.set_trace()

result_2 = y+x
